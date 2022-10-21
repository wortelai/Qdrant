# # Calling search API
import requests
from torch import embedding

from embeddings import Embeddings

# search_url = "http://127.0.0.1:5000/search/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
# response = requests.get(url=search_url)
# print(response.text)

# search_url = "http://127.0.0.1:5000/search"
# img_path = "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
# response = requests.post(url=search_url, json={"path":img_path})
# print(response.text)

# # Reading image from a URL
from PIL import Image
import requests
from io import BytesIO
from embeddings import Embeddings
import numpy as np

src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
embedding = Embeddings()
embedding.get_embedding(src)
    # img = Image.open(BytesIO(response.content))
# print(np.array(Embeddings().get_embedding(image=img)).shape)