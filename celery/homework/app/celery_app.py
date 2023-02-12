import celery
from config import PG_DSN, REDIS_DSN
from upscale import upscale


app = celery.Celery('tasks',
                    # backend='postgresql://test_user:test_password@localhost:5431/test_db',
                    backend='redis://localhost:6379/2',
                    broker='redis://localhost:6379/1'
                    )


@app.task
def upscale_photo(input_path, output_path, model_path):
    upscale(input_path, output_path, model_path)
    return 'mission complete! check example/'
