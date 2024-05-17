#!/usr/bin/env python3
""" filter by find """

def schools_by_topic(mongo_collection, topic):
    """ find schools """
    my_list = []
    my_list.extend(mongo_collection.find({"topics": topic}))
    return my_list
