from flask_lambda import FlaskLambda
from flask import Flask, request
from PIL import Image
from io import BytesIO
from qdrant import Qdrant
from embeddings import Embeddings
import base64
import random
import numpy as np
import io
import os


app = FlaskLambda(__name__)

host = "35.78.139.182"
port = 6333

embeddings = Embeddings()
collection = Qdrant(host, port, embeddings)


@app.route("/hello")
def hello():
    return "Hello from get"

@app.route("/hi", methods=["POST"])
def hi():
    return "Hi from Post"


@app.route("/create_index", methods=["POST"])
def create_index():
    index_name = request.form.get('collection name')
    vector_size = int(request.form.get('vector size'))
    result = collection.create_collection(vector_size, index_name)
    return f'"{index_name}" has been successfully created'

                    


@app.route("/delete_index", methods=["POST"])
def delete_index():
    index_name = request.form.get('collection name')
    collection.delete_collection(index_name)
    return f'"{index_name}" has been successfully deleted'


@app.route("/add_point", methods=["POST"])
def add_point():
    id = random.getrandbits(64)
    data = request.get_json()
    index_name = data['collection name']
    img_path = data['path']
    img_path = os.path.split(img_path)[-1]
    image_data = data['image']
    # Decode the base64-encoded image data
    image_binary = base64.b64decode(image_data)
    
    # Open the binary image data with Image.open()
    img = Image.open(BytesIO(image_binary))
    try:
        collection.add_points(img_path, img, index_name, id)
        return f'"{img_path}" image has been added to "{index_name}" collection'
    except:
        return f'"{index_name}" collection does not exist or Something went wrong'
    


@app.route("/delete_point", methods=["POST"])
def delete_point():
    data = request.get_json()
    index_name = data['collection name']
    img_path = data['path']
    img_path = os.path.split(img_path)[-1]

    
    try:
        collection.delete_filtered_points(index_name, img_path)
        return f' "{img_path}" has been deleted from "{index_name}" '
    except:
        return f'"{index_name}" collection does not exist or Something went wrong'


@app.route("/search", methods=["POST"])  # Search function using post (pass the image path in requests.post)
def search():
    data = request.get_json()
    index_name = data['collection name']
    limit = int(data['limit'])
    offset = int(data['offset'])
    threshold = int(data['threshold'])
    image_data = data['image']
    # Decode the base64-encoded image data
    image_binary = base64.b64decode(image_data)
    
    # Open the binary image data with Image.open()
    img = Image.open(BytesIO(image_binary))

    results = collection.search(
        img, index_name, limit=limit, offset=offset, threshold=threshold
    )
    return f"{results}"


@app.route("/count", methods=["POST"])
def count():
    collection_name = request.form.get('collection name')
    try:
        vector_count = collection.get_collection_count(collection_name)
        return f"count of vectors in {collection_name}: {vector_count}"
    except:
        return f'"{collection_name}" collection does not exist or Something went wrong'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
