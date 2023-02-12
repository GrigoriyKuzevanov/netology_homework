import cv2
import os
from cv2 import dnn_superres


BASE_PATH = os.path.dirname(__file__)


def upscale(input_path: str, output_path: str, model_path: str) -> None:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path:  путь к выходному файлу
    :param model_path: путь к ИИ модели
    :return:
    """

    scaler = dnn_superres.DnnSuperResImpl_create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)
    image = cv2.imread(input_path)
    result = scaler.upsample(image)
    cv2.imwrite(output_path, result)
 

# def example():
#     upscale(
#         os.path.join(BASE_PATH, 'example', 'lama_300px.png'),
#         os.path.join(BASE_PATH, 'example', 'lama_600px.png'),
#         os.path.join(BASE_PATH, 'models', 'EDSR_x2.pb'),
#     )

# if __name__ == '__main__':
#     example()
