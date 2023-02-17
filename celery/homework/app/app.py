import nanoid
from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_pymongo import PyMongo
from config import MONGO_DSN
from celery_app import celery_app, get_task, upscale_user_image
from upscale_cls import upscale_image
from bson import ObjectId, json_util
from gridfs import GridFS
from pymongo import MongoClient
from pymongo_fix import PyMongoFixed


app = Flask('app')

mongo = PyMongoFixed(app, uri='mongodb://test_user_mongo:test_password_mongo@127.0.0.1:27017/files?authSource=admin')
# mongo = PyMongo(app, uri='mongodb://test_user_mongo:test_password_mongo@127.0.0.1:27017/files?authSource=admin')
# mongo = PyMongo(app, uri=MONGO_DSN)
mongo_cl = MongoClient('mongodb://test_user_mongo:test_password_mongo@127.0.0.1:27017/files?authSource=admin')

celery_app.conf.update(app.config)

class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)
        

celery_app.Task = ContextTask


class Upscale(MethodView):
    def get(self, task_id):
        task = get_task(task_id)
        # return jsonify({'status': task.status, 'result': task.result})
        return json_util.dumps({'status': task.status, 'result': task.result})

    def post(self):
        image_id = self.save_image('user_image')
        task = upscale_user_image.delay(image_id)
        return jsonify({'task_id': task.id, 'file_id': image_id})

    def save_image(self, field):
        image = request.files.get(field)
        file_id = mongo.save_file(f'{nanoid.generate()}{image.filename}', image)
        return str(file_id)


@app.route('/processed/<file_id>')
def get_processed_file(file_id):
    # fs = GridFS(mongo_cl['files'])
    # file = fs.get(ObjectId(file_id))
    # return file.filename
    # file = mongo.db.files.find_one({'_id': ObjectId(file_id)})
    return mongo.send_file(filename=file_id)
    # return file_id

upscale_view = Upscale.as_view('upscale')

app.add_url_rule('/upscale/<string:task_id>', view_func=upscale_view, methods=['GET'])
app.add_url_rule('/upscale/', view_func=upscale_view, methods=['POST'])

app.run()
        
