#!/usr/bin/env python

import yaml
import xmltodict
from lxml import etree
from pymongo import MongoClient
from datetime import datetime


# Config file
with open("core/data_ingestion_products_cfg.yaml", "r") as cfg:
    config = yaml.safe_load(cfg)

# XML and XSL for transformation
folder_xml = config["queue"]["folder_xml"]
xml_file = config["queue"]["xml"]
folder_xsl = config["queue"]["folder_xsl"]
xsl_file = config["queue"]["xsl"]

xml = etree.parse(f'.././app/{folder_xml}/{xml_file}')
xsl = etree.parse(f'.././app/{folder_xsl}/{xsl_file}')

# Conversion XML to JSON
transformer = etree.XSLT(xsl)
transformation = transformer(xml)
data_dict = xmltodict.parse(transformation)
root = data_dict.items()

# MongoDB serialization
mdb_connection = config["mongodb"]["connection"]
mdb_database = config["mongodb"]["database"]
mdb_collection = config["mongodb"]["collection"]

client = MongoClient(mdb_connection)
database = client[mdb_database]
collection = database[mdb_collection]

for key in data_dict:
    for key2 in data_dict[key]:
        for doc in (data_dict[key][key2]):
            doc["price"] = float(doc["price"])
            doc["stock"] = int(doc["stock"])
            doc["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            doc["productUpdatedAt"] = None
            doc["admissionResult"] = None
            collection.insert_one(doc)

client.close()
