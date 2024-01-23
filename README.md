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

$ git clone https://github.com/andrebianco-net/create-data-ingestion-python-mongodb.git


$ docker build -t data-ingestion-container .
$ docker run -it data-ingestion-container

$ docker tag data-ingestion-container dataingestioncontainer.azurecr.io/data-ingestion-container
$ docker push dataingestioncontainer.azurecr.io/data-ingestion-container
$ docker login dataingestioncontainer.azurecr.io



#### 2. Update file data_ingestion_products_cfg.yaml if it is necessary for you:

queue:</br>
  folder_xml: "product_reception_queue/xml"</br>
  folder_xsl: "product_reception_queue/xsl"</br>
  xml: "product_collection.xml"</br>
  xsl: "product.xsl"</br>
mongodb:</br>
  connection: "mongodb://localhost:27017"</br>
  database: "DocDB"</br>
  collection: "Products"</br>

#### 3. Create the virtual environment:

$ python -m venv .venv

#### 4. Activate the virtual environment:

$ source .venv/bin/activate

#### 5. Install dependencies:

$ pip install -r requirements.txt

dnspython==2.5.0
lxml==5.1.0
pymongo==4.6.1
PyYAML==6.0.1
xmltodict==0.13.0

#### 6. Run project:

$ python data_ingestion_products.py

#### 7. Configure it on the linux, maybe it makes sense for you:

Create a systemctl .service file and attached it into crontab.

#### 8. Json used on MongoDB as example (after running the program):

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
