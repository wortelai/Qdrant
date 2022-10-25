from cv2 import _INPUT_ARRAY_STD_VECTOR_MAT
from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
from qdrant import Qdrant
from embeddings import Embeddings
import base64
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

host = "localhost"
port = 6333
COLLECTION_NAME = "images"

embeddings = Embeddings()
collection = Qdrant(host, port, embeddings)

@app.route('/count')
def count():   
    vector_count = collection.get_collection_count(COLLECTION_NAME)
    return f"count of vectors in {COLLECTION_NAME}: {vector_count}"

# @app.route("/search/<path:search_img_path>")  # Search function using get (provide image path in url)
# def search(search_img_path):   
#     search_img_path = "/"+f"{search_img_path}"
#     results = collection.search(
#         f"{search_img_path}", COLLECTION_NAME, limit=10, offset=0, threshold=0
#     )
#     return f"{results}"

@app.route('/search', methods=["POST"]) # Search function using post (pass the image path in requests.post)
def search():
     img_utf = request.get_data(as_text=False)
    #  img_bytes = bytes(img_utf, 'utf-8')
    #  img_decoded = base64.b64decode(img_bytes)
     search_img_path = Image.open(BytesIO(img_utf)) 
     a = np.array(search_img_path)
     plt.imshow(a)
     plt.savefig('/home/ahmad/Downloads/Qdrant_clean/iMg.jpeg')
     results = collection.search(
        search_img_path, COLLECTION_NAME, limit=10, offset=0, threshold=0
    )
     return f"{results}"
    #  return f"{search_img_path}"

if __name__=="__main__":
    app.run(debug=True)