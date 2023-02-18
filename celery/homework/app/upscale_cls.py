import cv2
import os
import pymongo
from gridfs import GridFS
from bson import ObjectId
from cv2 import dnn_superres
from skimage.io import imread, imsave
from PIL import Image
mongo = pymongo.MongoClient('mongodb://test_user_mongo:test_password_mongo@127.0.0.1:27017/files?authSource=admin')

class Upscaler:

    instance = None

    def __init__(self, scaler):
        self.scaler = scaler

    @classmethod
    def get_instance(
        cls,
        model_path=os.path.join('models', 'EDSR_x2.pb')
    ):
        if not cls.instance:
            cls.instance = cls.with_files(model_path)
        return cls.instance


    @classmethod
    def with_files(
        cls,
        model_path=os.path.join('models', 'EDSR_x2.pb')
    ):
        if not cls.instance:
            scaler = dnn_superres.DnnSuperResImpl_create()
            scaler.readModel(model_path)
            scaler.setModel('edsr', 2)
            cls.instance = cls(scaler)
        return cls.instance
        
    def upscale(self, file_to_upscale):
        image = imread(file_to_upscale)
        result = self.scaler.upsample(image)
        b = result.tobytes()
        return b            


def upscale_image(image_id):
    return Upscaler.get_instance().upscale(image_id)

# def main():
#     file = upscale_image('example/lama_300px.png')
#     cv2.imwrite('example/lama_600px_2.png', file)

# main()
