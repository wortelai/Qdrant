import os
import random
import numpy as np

from qdrant import Qdrant

from embeddings import Embeddings

search_img_path = (
    "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
)
DATA_DIR = "/home/ahmad/Downloads/Qdrant_images/coin_data"
COLLECTION_NAME = "images"
vector_size = 4096
host = "localhost"
port = 6333

images_path = os.path.join(DATA_DIR, "coin_images")
vectors_path = os.path.join(DATA_DIR, "vectors.npy")

embeddings = Embeddings()

if __name__ == "__main__":
    collection = Qdrant(host, port, embeddings)
    # vector_count = collection.get_collection_count(COLLECTION_NAME)
    # print(
    #     f"vector count in collection '{COLLECTION_NAME}': {vector_count}"
    # )

    # Create a new index
    # collection.create_collection(vector_size, COLLECTION_NAME)

    # # Delete a new index
    # collection.delete_collection(COLLECTION_NAME)

    # Add new image to index
    # collection.upload_to_collection_from_file_path(vectors_path, images_path, COLLECTION_NAME)
    # collection.upload_to_collection_from_image_path(images_path, COLLECTION_NAME)
    # collection.add_points(search_img_path, COLLECTION_NAME, [random.getrandbits(64)])

    # # Delete a new image from index
    # collection.delete_filtered_points(COLLECTION_NAME, search_img_path)

    #   Retrieve image based on a search result
    results = collection.search(
        search_img_path, COLLECTION_NAME, limit=1, offset=4, threshold=9.2
    )
    for result in results:
        print(f"image path: {result[0]}")
        print(f"similarity score: {result[1]}")
        print("----------------------------")

    # print(my_collection.retrieve_points([1001]))
    # print(collection.retrieve_filtered_count(COLLECTION_NAME,"image path", search_img_path))