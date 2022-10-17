from flask import Flask, request, jsonify
from qdrant import Qdrant
from embeddings import Embeddings

app = Flask(__name__)

host = "localhost"
port = 6333
COLLECTION_NAME = "images"

embeddings = Embeddings()
collection = Qdrant(host, port, embeddings)

@app.route('/')
def hello_world():   
    vector_count = collection.get_collection_count(COLLECTION_NAME)
    return f"count of vectors in {COLLECTION_NAME}: {vector_count}"


if __name__=="__main__":
    app.run(debug=True)