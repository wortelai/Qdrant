import os
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from models.vgg16_model import FeatureExtractor

class Embeddings:
    def __init__(self):
        self.normalize = transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        )

        self.tr = transforms.Compose(
            [transforms.Resize(256), transforms.ToTensor(), self.normalize,]
        )

        self.model = FeatureExtractor()

    def get_embedding(self, path_to_img=None, image=None):
        if path_to_img:
            PIL_image = Image.open(path_to_img).convert(
                "RGB"
            )  # Converting to RGB, as some images in dataset are greyscale
        if image:
            PIL_image = image
        img_tensor = self.tr(PIL_image)
        img_expanded = torch.unsqueeze(img_tensor, dim=0)
        self.model.eval()
        out = np.squeeze(self.model(img_expanded).detach().cpu()).tolist()
        return out

    def get_embeddings_across_imgs(self, images_path):
        imgs_path = self.get_img_paths(images_path)
        embeddings = []
        for img in imgs_path:
            embedding_img = self.get_embedding(img)
            embeddings.append(embedding_img)
        return embeddings

    def get_img_paths(self, imgs_path):
        imgs_paths = []
        if ".jpg" in imgs_path:
            imgs_paths.append(imgs_path)
        else:
            for file in os.listdir(imgs_path):
                if ".jpg" in file:
                    img_path = os.path.join(imgs_path, file)
                    imgs_paths.append(img_path)
        return imgs_paths


# images_path = "/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images"
# embeddings = Embeddings()
# embeddings.get_embedding("/home/ahmad/Downloads/Qdrant_images/coin_data/coin_images/1943929.jpg")
# points_list = embeddings.get_embeddings_across_imgs(images_path)