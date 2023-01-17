# ImageSearch

### **Create Collection:**

**Python Code:**

The input arguments:

- ***collection_name:*** The name of the collection that you want to be created. (In this case, the **collection_name** is “test” you can change it as need it to be)
- ***vector_size:***  The collection size. In this case, the **vector_size** is 4096 you can change it as need it to be)

```python
import requests

url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/create_index"

collection_name = "test"
vector_size = 4096

data = {"collection name": collection_name, "vector size": vector_size,}

response = requests.post(url=url, data=data)
print(response.text)
```

Curl Command:

```jsx
curl -X POST -d "collection name=test&vector size=4096" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/create_index
```

### Delete Collection:

**Python Code:**

The input arguments:

- ***collection_name:*** The name of the collection that you want to be deleted. (In this case, the **collection_name** is “test” you can change it as need it to be)

```python
import requests

url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_index"

collection_name = "test"

data = {"collection name": collection_name}
response = requests.post(url=url, data=data)
print(response.text)
```

Curl Command:

```python
curl -X POST -d "collection name=test" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_index
```

### Add Image To Collection:

**Python Code:**

The input arguments:

- ***collection_name:*** The name of the collection to which you want to add an image. (In this case, the **collection_name** is “test” you can change it as need it to be)
- ***img_path:*** The path of the image you want to be added to a collection. (In this case, the **img_path** is “image.jpg” you can change it as need to be)

```python
import requests
import base64
import json

url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point"

img_path = "image.jpg"
collection_name = "test"

image_file = open(img_path, 'rb')
image_data = base64.b64encode(image_file.read()).decode('utf-8')
 
data = {
    'collection name': collection_name,
    'path': img_path,
    'image': image_data
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url=url, data=json.dumps(data), headers=headers)
print(response.text)
```

**Curl Command for Mac:**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "path": "image.jpg", "image": "'$(base64 image.jpg)'"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point
```

**Curl Command for Linux :**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "path": "image.jpg", "image": "'$(base64 -w 0 image.jpg)'"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point
```

**Curl Command for Mac/Linux:**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "path": "image.jpg", "image": "'$(base64 image.jpg | tr -d '\n')'"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/add_point
```

### Delete Image From Collection:

**Python Code:**

The input arguments:

- ***collection_name:*** The name of the collection from which you want to delete an image. (In this case, the **collection_name** is “test” you can change it as need it to be)
- ***img_path:*** The path of the image you want to be deleted from a collection. (In this case, the **img_path** is “image.jpg” you can change it as need to be)

```python
import requests
import json

url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_point"

collection_name = "test"
img_path = "image.jpg"

data = {
    'collection name': collection_name,
    'path': img_path
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url=url, data=json.dumps(data), headers=headers)
print(response.text)
```

**Curl Command:**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "path": "image.jpg"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/delete_point
```

### Search Image In A Collection:

**Python Code:**

The input arguments:

- ***collection_name:*** The name of the collection where you want to search for an image. (In this case, the ***collection_name*** is “test” you can change it as need it to be)
- ***img_path:*** The path of the image you want to search in a collection. (In this case, the **img_path** is “image.jpg” you can change it as need to be)
- ***limit:*** Parameter `limit` specifies the amount of most similar results we would like to retrieve. (In this case, the **limit** is 10 you can change it as need to be)
- ***offset:*** Search and recommendation APIs allow to skip the first results of the search and return only the result starting from some specified offset. (In this case, the **offset** is 0 you can change it as need to be)
- ***threshold:*** if you know the minimal acceptance score for your model and do not want any results which are less similar than the threshold. (In this case, the **threshold** is 0 you can change it as need to be)

```python
import requests
import base64
import json

url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search"

collection_name = "test"
img_path = "image.jpg"
limit = 10
offset = 0
threshold = 0
    
image_file = open(img_path, "rb")
image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
data = {
    "collection name": "test",
    "limit": limit,
    "offset": offset,
    "threshold": threshold,
    "image":image_data
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url=url, data=json.dumps(data), headers=headers)
print(response.text)
```

**Curl Command for Mac:**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "limit": 10, "offset": 0, "threshold": 0, "image": "'$(base64 image.jpg)'"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search
```

**Curl Command for Linux:**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "limit": 10, "offset": 0, "threshold": 0, "image": "'$(base64 -w 0 image.jpg)'"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search
```

**Curl Command for Mac/Linux:**

```python
curl -X POST -H 'Content-Type: application/json' -d '{"collection name": "test", "limit": 10, "offset": 0, "threshold": 0, "image": "'$(base64 image.jpg | tr -d '\n')'"}' https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/search
```

### Count Of Images In Collection:

**Python Code:**

The input arguments:

- ***collection_name:*** The name of the collection from which you want to retrieve the count of images. (In this case, the **collection_name** is “test” you can change it as need to be)

```python
import requests

url = "https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/count"
    
data = {
  "collection name": "test",
}

response = requests.post(url=url, data=data)
print(response.text)
```

Curl Command:

```python
curl -X POST -d "collection name=test" https://mzul3mezie.execute-api.us-west-2.amazonaws.com/Prod/count
```

### AWS services that are being used in Image Search:

- **S3:** ([https://s3.console.aws.amazon.com/s3/home?region=us-west-2](https://s3.console.aws.amazon.com/s3/home?region=us-west-2))
- **Lambda:** ([https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2](https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2))
- **API Gateway:** ([https://us-west-2.console.aws.amazon.com/apigateway/home?region=us-west-2](https://us-west-2.console.aws.amazon.com/apigateway/home?region=us-west-2))
- **CloudWatch:** ([https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2))
- **EC2:** ([https://us-west-2.console.aws.amazon.com/ec2/home?region=us-west-2](https://us-west-2.console.aws.amazon.com/ec2/home?region=us-west-2))
- **IAM:** ([https://us-west-2.console.aws.amazon.com/iam/home?region=us-west-2](https://us-west-2.console.aws.amazon.com/iam/home?region=us-west-2))
- **CloudFormation:** ([https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2))