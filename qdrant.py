import os
import numpy as np
import requests


# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams
import qdrant_client.models as models
from qdrant_client.http.models.models import Filter

from embeddings import Embeddings

class Qdrant:
    def __init__(
        self,
        host="localhost", 
        port=6333,
        embeddings = Embeddings()
    ):
        self.client = QdrantClient(host=host, port=port)
        self.host = host
        self.port = port
        self.embeddings = embeddings     

    def create_collection(self, vector_size, collection_name):
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance="Cosine"),
        )

    def upload_to_collection_from_file_path(self, vectors_path, images, collection_name, batch_size=256):
        vectors = np.load(vectors_path)
        payload = self.get_payload(images)
        self.client.upload_collection(
            collection_name=collection_name,
            vectors=vectors,
            payload=payload,
            ids=None,
            batch_size=batch_size,
            parallel=2,
        )

    def upload_to_collection_from_image_path(self, images, collection_name, batch_size=256):
        points_list = self.embeddings.get_embeddings_across_imgs(images)
        vectors = np.array(points_list)
        payload = self.get_payload(images)
        self.client.upload_collection(
            collection_name=collection_name,
            vectors=vectors,
            payload=payload,
            ids=None,
            batch_size=batch_size,
            parallel=2,
        )
    
    def delete_collection(self, collection_name):
        self.client.delete_collection(collection_name=collection_name)

    def get_collection_count(self, collection_name):
        url = f"http://{self.host}:{self.port}/collections/{collection_name}"
        count = requests.get(url=url).json()['result']['vectors_count']
        return count

    def get_payload(self, imgs_path):
        imgs_paths = []
        if ".jpg" in imgs_path:
            imgs_paths.append({"image path": imgs_path})
        else:
            for file in os.listdir(imgs_path):
                if ".jpg" in file:
                    img_path = os.path.join(imgs_path, file)
                    imgs_paths.append({"image path": img_path})
        return imgs_paths


    def add_points(self, imgs_path, collection_name, ids):
        vectors = self.embeddings.get_embeddings_across_imgs(imgs_path)
        payloads = self.get_payload(imgs_path)
        self.client.upsert(
            collection_name=collection_name,
            points=models.Batch(
                ids=ids,
                payloads=payloads,
                vectors=vectors
            ),
        )

    def retrieve_points(self, collection_name, ids):
        return self.client.retrieve(
    collection_name=collection_name,
    ids=ids,
        )
    
    def delete_points(self, collection_name, points):
        self.client.delete(
    collection_name=collection_name,
    points_selector=models.PointIdsList(
        points=[0, 2],
    ),
)

    def delete_filtered_points(self, collection_name, filter_value):
        self.client.delete(
    collection_name=collection_name,
    points_selector=models.FilterSelector(
        filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="image path",
                    match=models.MatchValue(value=filter_value),
                ),
            ],
        )
    ),
)


    def retrieve_filtered_count(self, collection_name, key, value):
        result = self.client.scroll(
            collection_name=collection_name, 
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key=key, 
                        match=models.MatchValue(value=value)
                    ),
                ]
            ),
            # limit=1,
            # with_payload=True,
        )
        count = len(result[0])
        return count

    def search(self, img, collection_name, limit=5, offset=0, threshold=0, filter: dict = None):
        results = []
        # Convert image into vector
        vector = self.embeddings.get_embedding(img)

        # Use `vector` for search for closest vectors in the collection
        search_result = self.client.search(
            collection_name=collection_name,
            query_vector=vector,
            query_filter=Filter(**filter) if filter else None,
            limit=limit+offset,
            score_threshold=threshold*0.1
        )
        # return image paths and corresponding scores
        for result in search_result[offset:]:
            results.append((result.payload['image path'], result.score*10))

        return results


    def filter(self, collection_name, key, value):
        self.client.scroll(
            collection_name=collection_name, 
            scroll_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key=key, 
                        match=models.MatchValue(value=value),
                    ),
                ]
            ),
        )

#############################################################################################

# img_path = (
#     "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
# )
# my_collection = Qdrant(
#     client=QdrantClient(host="localhost", port=6333), collection_name="images"
# )
# my_collection.add_points(img_path, [1001])

# print(my_collection.retrieve_points([1001]))
# print(my_collection.search(img_path))

