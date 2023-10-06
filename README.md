# create-data-ingestion-python-mongodb

## Overview:
Creating a data ingestion using XML, Python, JSON and MongoDB.

This example is an implementation where I used Python to create a program for transforms XML via XSLT to JSON and serialize it as doc into MongoDB. Read [readme file ](https://github.com/andrebianco-net/andrebianco-net#readme) in order to obtain more details about the finality of this solution.

In order to know more aboute my career check my Linkedin profile, please.

https://www.linkedin.com/in/andrebianco-net/

## General Scope:

Data Ingestion Service implementation proposes a small example of how to create a service using Python simply to solve the problem of transforming document types. Many programming languages do the same, but Python is able to do this easily. It will use a XML file with a colletion of Products, that fille will be transformed using XSLT transformation to JSON and the result will be stored into a MongoDB database that is used as a conceptual queue of documents.

The Solution will be a Worker which read a MongoDB queue (Product collection) and after validate each doc it will be stored in another base via a Web API.

## How to run this project

#### 1. Clone project:

$ git clone https://github.com/andrebianco-net/create-data-ingestion-python-mongodb.git

#### 2. Update file data_ingestion_products_cfg.yaml if it is necessary for you:

queue:
  folder_xml: "product_reception_queue/xml"
  folder_xsl: "product_reception_queue/xsl"
  xml: "product_collection.xml"
  xsl: "product.xsl"
mongodb:
  connection: "mongodb://localhost:27017"
  database: "DocDB"
  collection: "Products"

#### 3. Create the virtual environment:

$ python -m venv .venv

#### 4. Activate the virtual environment:

$ source ./.venv/bin/activate

#### 5. Run project:

$ python data_ingestion_products.py

#### 6. Configure it on the linux, maybe it makes sense for you:

Create a systemctl .service file and attached it into crontab.
