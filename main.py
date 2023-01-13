import requests
import base64
import json

def create_collection(collection_name, vector_size):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/create_index"
    
    data = {"collection name": collection_name, "vector size": vector_size,}
    response = requests.post(url=url, data=data)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')


def delete_collection(collection_name):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_index"

    data = {"collection name": collection_name}
    response = requests.post(url=url, data=data)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')


def add_vector_points(collection_name, img_path):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point"
    
    image_file = open(img_path, 'rb')
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
    data = {
        'collection name': collection_name,
        'path': img_path,
        'image': image_data
    }
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=url, data=json.dumps(data), headers=headers)

    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')
     
        
def delete_vector_point(collection_name, img_path):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_point"

    data = {
        'collection name': collection_name,
        'path': img_path
    }
    
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')

def search_vector_point(collection_name, img_path, threshold, offset, limit):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search"
    
    image_file = open(img_path, "rb")
    image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
    data = {
        "collection name": collection_name,
        "limit": limit,
        "offset": offset,
        "threshold": threshold,
        "image":image_data
    }

    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    if response.status_code==200:
        print(response.text)
    else:
        print('Something went wrong')
        

def vectors_count(collection_name):
    url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/count"
    

    data = {
        "collection name": collection_name,
    }
    response = requests.post(url=url, data=data)
    if response.status_code==200:
        print(response.text)
    else:
        print("test collection does not exist or Something went wrong")




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
        image_path=input("Enter the path of the directory or image: ")
        add_vector_points(COLLECTION_NAME, image_path)
        

    elif(choice==4):
        COLLECTION_NAME = input("Collection Name:")
        delete_image_path=input("Enter the path of the image you want to delete: ")
        delete_vector_point(COLLECTION_NAME, delete_image_path)


    elif(choice==5):
        COLLECTION_NAME = input("Collection Name:")
        search_img_path=input("Enter the path of the image you want to search: ")
        limit = int(input("limit [default 10]: ") or 10)
        offset = int(input("offset [default 0]: ") or 0)
        threshold = int(input("threshold [default 0]: ") or 0)
        search_vector_point(COLLECTION_NAME, search_img_path,threshold,offset,limit)
        

    elif(choice==6):
        COLLECTION_NAME = input("Collection Name:")
        vectors_count(COLLECTION_NAME)
        
    else:
        print("Please retry with an correct option")
