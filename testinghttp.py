# # Calling search API
# import requests

# url = "http://127.0.0.1:5000/search/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
# response = requests.get(url = url)
# print(response.text)


# Reading image from a URL
from PIL import Image
import requests
from io import BytesIO
from embeddings import Embeddings
import numpy as np

src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
response = requests.get(url=src)
img = Image.open(BytesIO(response.content))
print(np.array(Embeddings().get_embedding(image=img)).shape)