import time

import requests

from config_test import API_URL


def test_root():
    assert requests.get(API_URL).status_code == 404


def test_api():
    with open("example/lama_300px_1.png", "rb") as file:
        resp_post = requests.post(f"{API_URL}/upscale/", files={"user_image": file})
    assert resp_post.status_code == 200
    resp_data = resp_post.json()
    assert "task_id" in resp_data
    assert "file_id" in resp_data
    print("==========test post_image finished==========")

    task_id = resp_post.json()["task_id"]
    assert isinstance(task_id, str)
    resp_get = requests.get(f"{API_URL}/upscale/{task_id}")
    assert resp_get.status_code == 200
    assert "id_for_download" in resp_get.json()
    assert "status" in resp_get.json()
    print("==========test get task finished==========")

    print("==========start processing the image==========")
    while resp_get.json()["status"] == "PENDING":
        time.sleep(3)
        resp_get = requests.get(f"{API_URL}/upscale/{task_id}")
    print("==========processing is finished==========")

    assert "id_for_download" in resp_get.json()
    assert "status" in resp_get.json()
    assert resp_get.json()["status"] == "SUCCESS"
    print("==========test get task success finished==========")

    id_for_download = resp_get.json()["id_for_download"]
    resp_get_file = requests.get(f"{API_URL}/processed/{id_for_download}")
    assert resp_get_file.status_code == 200
