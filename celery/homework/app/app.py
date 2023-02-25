import io

import nanoid
from bson import ObjectId
from flask import Flask, jsonify, request, send_file
from flask.views import MethodView
from flask_pymongo import PyMongo
from gridfs import GridFS
from pymongo import MongoClient

from celery_app import celery_app, get_task, upscale_user_image
from config import MONGO_DSN

app = Flask("app")

mongo = PyMongo(app, uri=MONGO_DSN)
mongo_cl = MongoClient(MONGO_DSN)

celery_app.conf.update(app.config)


class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery_app.Task = ContextTask


class Upscale(MethodView):
    def get(self, task_id):
        task = get_task(task_id)
        return jsonify({"status": task.status, "id_for_download": task.result})

    def post(self):
        image_id = self.save_image("user_image")
        task = upscale_user_image.delay(image_id)
        return jsonify({"task_id": task.id, "file_id": image_id})

    def save_image(self, field):
        image = request.files.get(field)
        file_id = mongo.save_file(f"{nanoid.generate()}{image.filename}", image)
        return str(file_id)


@app.route("/processed/<file_id>")
def get_processed_file(file_id):
    fs = GridFS(mongo_cl["files"])
    processed_file = fs.get(ObjectId(file_id)).read()
    buffer = io.BytesIO()
    buffer.write(processed_file)
    buffer.seek(0)
    return send_file(buffer, download_name="result.png", mimetype="png")


upscale_view = Upscale.as_view("upscale")

app.add_url_rule("/upscale/<string:task_id>", view_func=upscale_view, methods=["GET"])
app.add_url_rule("/upscale/", view_func=upscale_view, methods=["POST"])
