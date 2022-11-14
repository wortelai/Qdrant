# # Calling search API
from regex import A
import requests
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
from embeddings import Embeddings
import numpy as np
import base64
search_img_path = (
    "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
)

# search_url = "http://127.0.0.1:5000/search/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
# response = requests.get(url=search_url)
# print(response.text)

search_url = "http://127.0.0.1:5000/search"
img_path = "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
# response = requests.post(url=search_url, json={"path":img_path})
# print(response.text)

# Reading image from a URL
src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
if src[:4] == 'http':
    response = requests.get(url=src)
    payload = response.content
    img = Image.open(BytesIO(payload))

# Saving image as bytes
# When using this approach, make sure to use request.get_data(as_text=True) in POST method
buffered = BytesIO()
img = Image.open(search_img_path)
img.save(buffered, format="JPEG")
temp_payload = buffered.getvalue()
payload1 = base64.b64encode(temp_payload).decode('utf-8')
payload1_bytes = bytes(payload1, 'utf-8')
payload1_decoded = base64.b64decode(payload1_bytes)
img1 = Image.open(BytesIO(payload1_decoded))

f= open(search_img_path, "rb")
im_b64_utf8 = base64.b64encode(f.read()).decode('utf-8')
im_b64_bytes = bytes(im_b64_utf8, 'utf-8')
im_bytes = base64.b64decode(im_b64_bytes)   # im_bytes is a binary image
im_file = BytesIO(im_bytes)  # convert image to file-like object
img2 = Image.open(im_file)   # img is now PIL Image object
f.close()

# When using this approach, make sure to use request.get_data(as_text=False) in POST method
buffered = BytesIO()
img = Image.open(search_img_path)
img.save(buffered, format='JPEG')
payload2 = buffered.getvalue()  # or use bufferred.read()
img3 = Image.open(BytesIO(payload2))

a = np.array(img)
b = np.array(img2)
plt.imshow(a)
plt.savefig('/home/ahmad/Downloads/Qdrant_clean/img.jpeg')
plt.imshow(b)
plt.savefig('/home/ahmad/Downloads/Qdrant_clean/img2.jpeg')

response = requests.post(url=search_url, data= payload2)
result = response.text
print(result)
