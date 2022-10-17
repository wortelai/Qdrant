import numpy as np
import os

# Import client library
import qdrant_client.models as models
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams

from embeddings import Embeddings
from qdrant import QdrantCollections

class Points(QdrantCollections):
    def __init__(self, client, collection_name):
        super().__init__(client, collection_name)
    
    def add_points(self, imgs_path):
        vectors = self.embeddings.get_embeddings_across_imgs(imgs_path)
        payloads = super().get_payload(imgs_path)
        self.client.upsert(
            collection_name=self.collection_name,
            points=models.Batch(
                ids=[1005],
                payloads=payloads,
                vectors=vectors
            ),
        )

    def retrieve_points(self, ids):
        return self.client.retrieve(
    collection_name=self.collection_name,
    ids=ids,
        )
    
    def delete_points(self, points):
        self.client.delete(
    collection_name="{collection_name}",
    points_selector=models.PointIdsList(
        points=[0, 2],
    ),
)

# imgs_path = '/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg'
# point = Points(client=QdrantClient(host="localhost", port=6333), collection_name="images") 
# point.add_points(imgs_path)
# print(point.retrieve_points([1001]))