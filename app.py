from flask import Flask, request
from PIL import Image
from io import BytesIO
from qdrant import Qdrant
from embeddings import Embeddings
import base64
import random

app = Flask(__name__)

host = "localhost"
port = 6333

embeddings = Embeddings()
collection = Qdrant(host, port, embeddings)


@app.route("/")
def hello():
    return "Hello"


@app.route("/create_index", methods=["POST"])
def create_index():
    data = request.json
    index_name = data["collection name"]
    vector_size = data["vector size"]
    collection.create_collection(vector_size, index_name)
    return data


@app.route("/delete_index", methods=["POST"])
def delete_index():
    data = request.json
    index_name = data["collection name"]
    collection.delete_collection(index_name)
    return data


@app.route("/add_point", methods=["POST"])
def add_point():
    data = request.json
    index_name = data["collection name"]
    img_path = data["image path"]
    img_utf = data["img_bytes"]
    img_bytes = bytes(img_utf, "utf-8")
    img_decoded = base64.b64decode(img_bytes)
    img = Image.open(BytesIO(img_decoded))
    id = random.getrandbits(64)
    collection.add_points(img_path, img, index_name, id)
    return index_name


@app.route("/delete_point", methods=["POST"])
def delete_point():
    data = request.json
    index_name = data["collection name"]
    img_path = data["image path"]
    collection.delete_filtered_points(index_name, img_path)
    return index_name


@app.route(
    "/search", methods=["POST"]
)  # Search function using post (pass the image path in requests.post)
def search():
    data = request.json
    collection_name = data["collection name"]
    img_utf = data["payload"]
    img_bytes = bytes(img_utf, "utf-8")
    img_decoded = base64.b64decode(img_bytes)
    search_img_path = Image.open(BytesIO(img_decoded))
    results = collection.search(
        search_img_path, collection_name, limit=10, offset=0, threshold=0
    )
    return f"{results}"


@app.route("/count", methods=["POST"])
def count():
    data = request.json
    collection_name = data["collection name"]
    vector_count = collection.get_collection_count(collection_name)
    return f"count of vectors in {collection_name}: {vector_count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
