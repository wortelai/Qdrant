import os
import random
import numpy as np
from io import BytesIO
from qdrant import Qdrant
from PIL import Image
import requests
import base64

COLLECTION_NAME = "images"
vector_size = 4096
img_path = (
    "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
)


def img_to_byte_stream(img_path):
    buffered = BytesIO()
    img = Image.open(img_path)
    img.save(buffered, format="JPEG")
    temp_payload = buffered.getvalue()
    payload = base64.b64encode(temp_payload).decode("utf-8")
    return payload


if __name__ == "__main__":

    """ ***Invoking all the Qdrant functions through Flask APIs***
    Uncomment one by one and run """

    # # 1) Creating an index
    # url = "http://127.0.0.1:5000/create_index"

    # data = {"collection name": COLLECTION_NAME, "vector size": vector_size}
    # response = requests.post(url=url, json=data)
    # print(response)

    # # 2) Delete an index
    # url = "http://127.0.0.1:5000/delete_index"

    # data = {
    #     "collection name": COLLECTION_NAME,
    # }
    # response = requests.post(url=url, json=data)
    # print(response)

    # # 3) add new image to index
    # url = "http://127.0.0.1:5000/add_point"
    # img_bytes = img_to_byte_stream(img_path)
    # data = {
    #     "collection name": COLLECTION_NAME,
    #     "image path": img_path,
    #     "img_bytes": img_bytes,
    # }
    # response = requests.post(url=url, json=data)
    # print(response)

    # # 4) delete an image from index
    # url = "http://127.0.0.1:5000/delete_point"
    # data = {
    #     "collection name": COLLECTION_NAME,
    #     "image path": img_path,
    # }
    # response = requests.post(url=url, json=data)
    # print(response)

    # # 5) Search an image in index
    # url = "http://127.0.0.1:5000/search"
    # payload = img_to_byte_stream(img_path)
    # data = {
    #     "collection name": COLLECTION_NAME,
    #     "payload": payload,
    # }
    # response = requests.post(url=url, json=data)
    # print(response.text)

    # # 6) Return count of images in index
    # url = "http://127.0.0.1:5000/count"
    # data = {
    #     "collection name": COLLECTION_NAME,
    # }
    # response = requests.post(url=url, json=data)
    # print(response.text)
