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
    #data = request.forms
    index_name = request.form.get('collection name')
    #index_name = request.args.get('collection name')
    #img_path = request.form.get('image path')
    #index_name = request.form.get('collection name')
    #img_path = data["image path"]
    #img_bytes = bytes(img_utf, "utf-8")
    #img_decoded = base64.b64decode(img_bytes)
    #img = Image.open(BytesIO(request.files['file'].read()))
    #img = Image.open(file)
    id = random.getrandbits(64)
    #id=11334160272865621853
    file = request.files['file']
    read_file = file.read()
    img_path = file.filename
    #    print(f)
    npimg = np.fromstring(read_file,np.uint8)
    #img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
    #img = base64.b64decode(npimg)
    img = io.BytesIO(npimg)
    img=Image.open(img)
    try:
        collection.add_points(img_path, img, index_name, id)
        return f'"{img_path}" image has been added to "{index_name}" collection'
    except:
        return f'"{index_name}" collection does not exist or Something went wrong'
    


@app.route("/delete_point", methods=["POST"])
def delete_point():
    index_name = request.form.get('collection name')
    file = request.files['file']
    read_file = file.read()
    img_path = file.filename

    
    try:
        collection.delete_filtered_points(index_name, img_path)
        return f' "{img_path}" has been deleted from "{index_name}" '
    except:
        return f'"{index_name}" collection does not exist or Something went wrong'


@app.route("/search", methods=["POST"])  # Search function using post (pass the image path in requests.post)
def search():
    collection_name = request.form.get('collection name')
    limit = int(request.form.get('limit'))
    offset = int(request.form.get('offset'))
    threshold = int(request.form.get('threshold'))

    file = request.files['file']
    read_file = file.read()
    npimg = np.fromstring(read_file,np.uint8)
    img_b = io.BytesIO(npimg)
    img = Image.open(img_b)

    results = collection.search(
        img, collection_name, limit=limit, offset=offset, threshold=threshold
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
