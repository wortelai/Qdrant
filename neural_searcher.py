from qdrant_client import QdrantClient
from embeddings import Embeddings
from qdrant import Qdrant

class NeuralSearcher(Qdrant):
    def __init__(self, client, collection_name):
        super().__init__(client, collection_name)

    def search(self, img):
        # Convert image into vector
        vector = self.embeddings.get_embedding(img)

        # Use `vector` for search for closest vectors in the collection
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,
            limit=5,
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function we are interested in payload only
        payloads = [hit.payload for hit in search_result]
        return payloads


img_path = (
    "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg"
)
neural_searcher = NeuralSearcher(
    client=QdrantClient(host="localhost", port=6333), collection_name="images"
)
print(neural_searcher.search(img_path))
