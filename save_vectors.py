import numpy as np
from embeddings import Embeddings


# Saving the vectors in np array format
images_path = "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images"
embeddings = Embeddings()
points_list = embeddings.get_embeddings_across_imgs(images_path)

vectors = np.array(points_list)
np.save(
    "/home/ahmad/Downloads/Qdrant_images/coin_data/vectors.npy",
    vectors,
    allow_pickle=False,
)