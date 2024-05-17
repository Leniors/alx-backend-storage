#!/usr/bin/env python3
""" nginx statitic """

from pymongo import MongoClient

def print_nginx_logs_stats():
    client = MongoClient('mongodb://localhost:27017/')
    
    db = client.logs
    collection = db.nginx
    
    total_logs = collection.count_documents({})
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_counts = {method: collection.count_documents({"method": method}) for method in methods}
    
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_counts[method]}")
    print(f"{get_status_count} status check")

if __name__ == "__main__":
    print_nginx_logs_stats()
