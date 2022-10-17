from flask import Flask, request, jsonify
from qdrant import Qdrant
from embeddings import Embeddings

app = Flask(__name__)

host = "localhost"
port = 6333
COLLECTION_NAME = "images"
DATA_DIR = "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/"

embeddings = Embeddings()
collection = Qdrant(host, port, embeddings)

@app.route('/count')
def count():   
    vector_count = collection.get_collection_count(COLLECTION_NAME)
    return f"count of vectors in {COLLECTION_NAME}: {vector_count}"

@app.route("/search/<search_img_path>")
def search(search_img_path):   
    search_img_path = DATA_DIR+f"{search_img_path}"
    results = collection.search(
        search_img_path, COLLECTION_NAME, limit=10, offset=0, threshold=0
    )
    return f"{results}"
    return results


if __name__=="__main__":
    app.run(debug=True)