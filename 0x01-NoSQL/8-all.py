#!/usr/bin/env python3
""" list document in a collection """

def list_all(mongo_collection):
    """ list_all """
    my_list = []
    my_list.extend(mongo_collection.find())
    return my_list
