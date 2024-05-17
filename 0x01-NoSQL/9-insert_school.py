#!/usr/bin/env python3
""" add document to a collection """

def insert_school(mongo_collection, **kwargs):
    """ insert_school """
    return mongo_collection.insert_one(kwargs).inserted_id
