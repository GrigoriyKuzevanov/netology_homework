import json
from bson import ObjectId, json_util
import pymongo
from cachetools import cached
from celery import Celery
from celery.result import AsyncResult
from gridfs import GridFS

from config import REDIS_DSN, PG_DSN, MONGO_DSN
from upscale_cls import upscale_image

# celery_app = Celery(
#                         'app',
#                         backend='db+postgresql://test_user:test_password@127.0.0.1:5431/test_db',
#                         broker='redis://127.0.0.1:6379/1'
#                     )

celery_app = Celery('app', backend=f'db+{PG_DSN}', broker=REDIS_DSN)

# mongo = pymongo.MongoClient('mongodb://test_user_mongo:test_password_mongo@127.0.0.1:27017/files?authSource=admin')

def get_task(task_id):
    return AsyncResult(task_id, app=celery_app)


@cached({})
def get_fs():
    mongo = pymongo.MongoClient(MONGO_DSN)
    return GridFS(mongo['files'])

def parse_json(data):
    return json.loads(json_util.dumps(data))

@celery_app.task
def upscale_user_image(image_id):
    fs = get_fs()
    file_to_upscale = fs.get(ObjectId(image_id))
    b = upscale_image(file_to_upscale)
    obj_id = fs.put(b, filename='result.png')
    result_id = parse_json(obj_id)['$oid']
    return result_id
