import base64
from io import BytesIO
from PIL import Image
search_img_path = (
    "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
)
f= open(search_img_path, "rb")
im_b64 = base64.b64encode(f.read())
im_b64 = bytes(im_b64, 'utf-8')
im_bytes = base64.b64decode(im_b64)   # im_bytes is a binary image
im_file = BytesIO(im_bytes)  # convert image to file-like object
img = Image.open(im_file)   # img is now PIL Image object
print(type(img))
f.close()

