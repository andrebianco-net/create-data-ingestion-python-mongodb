# create-data-ingestion-python-mongodb

## Overview:
Creating a data ingestion using XML, Python, JSON and MongoDB.

This example is an implementation where I used Python to create a program for transforms XML via XSLT to JSON and serialize it as doc into MongoDB. The config file used here is a YAML file. Read the [readme file ](https://github.com/andrebianco-net/andrebianco-net#readme) in order to obtain more details about the finality of this solution.

In order to know more aboute my career check my Linkedin profile, please.

https://www.linkedin.com/in/andrebianco-net/

## General Scope:

Data Ingestion Service implementation proposes a small example of how to create a service using Python simply to solve the problem of transforming document types. Many programming languages do the same, but Python is able to do this easily. It will use a XML file with a collection of Products, that file will be transformed using XSLT transformation to JSON and the result will be stored into a MongoDB database that is used as a conceptual queue of documents.

## How to run this project

#### 1. Clone project:

```bash
$ git clone https://github.com/andrebianco-net/create-data-ingestion-python-mongodb.git
```

#### 2. Update file data_ingestion_products_cfg.yaml if it is necessary for you:

```yaml
queue:
  folder_xml: "product_reception_queue/xml"
  folder_xsl: "product_reception_queue/xsl"
  xml: "product_collection.xml"
  xsl: "product.xsl"
mongodb:
  connection: "mongodb://localhost:27017"
  database: "DocDB"
  collection: "Products"
```

#### 3. Create the virtual environment:

```bash
$ python -m venv .venv
```

#### 4. Activate the virtual environment:

```bash
$ source .venv/bin/activate
```

#### 5. Install dependencies:

```bash
$ pip install -r requirements.txt
```

dnspython==2.5.0
lxml==5.1.0
pymongo==4.6.1
PyYAML==6.0.1
xmltodict==0.13.0

#### 6. Run project:

```bash
$ python data_ingestion_products.py
```

#### 7. Configure it on the linux, maybe it makes sense for you:

Create a systemctl .service file and attached it into crontab.

#### 8. Json used on MongoDB as example (after running the program):

```json
{
  "_id": {
    "$oid": "651c5dcf0c7cdeb0129d3ed7"
  },
  "category": "Racing Wheel",
  "name": "Advant Racing",
  "description": "Advant Racing Wheels for High Performance Cars",
  "price": 100,
  "stock": 10,
  "image": "https://image.made-in-china.com/43f34j00OIeYilgMAdkR/Advant-Racing-Wheels-for-High-Performance-Cars.jpg",
  "createdAt": "2023-10-03 15:30:39",
  "productUpdatedAt": "",
  "admissionResult": ""
}
```

#### 9. From Docker to Azure Container

```bash
$ docker build -t data-ingestion-container .
```

```bash
[$ docker run -it data-ingestion-container]
```

```bash
$ docker login youruricreatedinazurecontainerregistry.azurecr.io
```

```bash
$ docker tag data-ingestion-container youruricreatedinazurecontainerregistry.azurecr.io/data-ingestion-container
```

```bash
$ docker push youruricreatedinazurecontainerregistry.azurecr.io/data-ingestion-container
```

```bash
[$ docker pull youruricreatedinazurecontainerregistry.azurecr.io/data-ingestion-container]
```

#### 10. Created in Azure Cloud Computing
###
![image](https://github.com/andrebianco-net/create-data-ingestion-python-mongodb/assets/453193/e03d1428-0ca9-4a66-909a-60241bd6d0e5)

###
![image](https://github.com/andrebianco-net/create-data-ingestion-python-mongodb/assets/453193/5e9c42a1-af71-41f1-926f-7717201f6ff4)

###
![image](https://github.com/andrebianco-net/create-csharp-worker-clean-architecture/assets/453193/d7c683b7-55aa-43ed-b3a8-f55b85365fb7)
