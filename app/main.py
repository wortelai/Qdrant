import os
import random
from io import BytesIO
from PIL import Image
import requests
import base64

def create_collection(COLLECTION_NAME, vector_size):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/create_index"
    
    # curl -X POST -d "collection name=test&vector size=4096" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/create_index
    
    data = {"collection name": COLLECTION_NAME, "vector size": vector_size,}
    response = requests.post(url=url, data=data)
    print(response.text)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')


def delete_collection(COLLECTION_NAME):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_index"

    # curl -X POST -d "collection name=test" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_index                 


    data = {"collection name": COLLECTION_NAME}
    response = requests.post(url=url, data=data)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')


def add_vector_points(dir_name, COLLECTION_NAME):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point"

    image_file = open(dir_name, "rb")
    
    files = {"file":  image_file}
            
    data = {
        "collection name": COLLECTION_NAME,
    }
    response = requests.post(url=url, files=files, data=data)

    if response.status_code==200:
        print(f"{dir_name} has been added to {COLLECTION_NAME} collection.")
    else:
        return 'Something went wrong'
    # curl -X POST -F "file=@/Users/zeeshan/Documents/Qdrant-App/coin_images/1695.jpg" -F "collection name=test" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point
    
        
        
def delete_vector_point(vector_path, COLLECTION_NAME):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_point"
    
    image_file = open(vector_path, "rb")

        
    files = {"file":  image_file}
    
    data = {
        "collection name": COLLECTION_NAME,
        "image path": vector_path,
    }
    
    response = requests.post(url=url,files=files, data=data)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')
    #curl -X POST -F "collection name=test" -F "file=@/Users/zeeshan/Documents/Qdrant-App/coin_images/1695.jpg" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_point

def search_vector_point(search_img_path, COLLECTION_NAME,threshold, offset,limit):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search"
    
    image_file = open(search_img_path, "rb")

    files = {"file":  image_file}
    
    data = {
        "collection name": COLLECTION_NAME,
        "limit": limit,
        "offset": offset,
        "threshold": threshold,
    }
    response = requests.post(url=url, headers=headers, files=files, params=data)
    print(response.text)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')
        
    # curl -X POST -F "file=@/Users/zeeshan/Documents/Qdrant-App/coin_images/1695.jpg" -F "collection name=test" -F "limit=10" -F "offset=0" -F "threshold=0" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search



def vectors_count(COLLECTION_NAME):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/count"
    
    # curl -X POST -d "collection name=test" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/count
    
    data = {
        "collection name": COLLECTION_NAME,
    }
    response = requests.post(url=url, data=data)
    if response.status_code==200:
        print(response.text)
    else:
        print(f'"{COLLECTION_NAME}" collection does not exist or Something went wrong')




if __name__ == "__main__":
    
    print("Which option in the following would you like to use?")
    print("1 - Create a new collection")
    print("2 - Delete a collection")
    print("3 - Add images to collection")
    print("4 - Delete image from collection")
    print("5 - Search image in the Image Search Vector")
    print("6 - Display count of images in the collection")

    choice = int(input("Choice: "))
    
    if(choice==1):
        COLLECTION_NAME = input("Collection Name:")
        vector_size = int(input("Vector Size [default 4096]: ") or 4096)
        create_collection(COLLECTION_NAME, vector_size)
 

    elif(choice==2):
        COLLECTION_NAME = input("Collection Name:")
        delete_collection(COLLECTION_NAME)
        

    elif(choice==3):
        COLLECTION_NAME = input("Collection Name:")
        dir_name=input("Enter the path of the directory or image: ")
        add_vector_points(dir_name, COLLECTION_NAME)
        

    elif(choice==4):
        COLLECTION_NAME = input("Collection Name:")
        delete_image_path=input("Enter the path of the image you want to delete: ")
        delete_vector_point(delete_image_path,COLLECTION_NAME)


    elif(choice==5):
        COLLECTION_NAME = input("Collection Name:")
        search_img_path=input("Enter the path of the image you want to search: ")
        limit = int(input("limit [default 10]: ") or 10)
        offset = int(input("offset [default 0]: ") or 0)
        threshold = int(input("threshold [default 0]: ") or 0)
        search_vector_point(search_img_path, COLLECTION_NAME,threshold,offset,limit)
        

    elif(choice==6):
        COLLECTION_NAME = input("Collection Name:")
        vectors_count(COLLECTION_NAME)
        
    else:
        print("Please retry with an correct option")
