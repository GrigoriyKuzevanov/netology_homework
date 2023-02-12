import os
from celery_app import upscale_photo

BASE_PATH = os.path.dirname(__file__)

def main():
    async_result = upscale_photo.delay(
        os.path.join(BASE_PATH, 'example', 'lama_300px.png'),
        os.path.join(BASE_PATH, 'example', 'lama_600px.png'),
        os.path.join(BASE_PATH, 'models', 'EDSR_x2.pb'),
    )
    print(async_result.get())

if __name__ == '__main__':
    main()
    