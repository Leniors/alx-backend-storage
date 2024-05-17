#!/usr/bin/env python3
""" nginx statitic """

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
logs = client.logs
nginx = logs.nginx

print(f"{nginx.count_documents()} logs")
print("Methods:")
print(f"\\tmethod GET: {nginx.count_documents({"method": "GET"})}")
print(f"\\tmethod POST: {nginx.count_documents({"method": "POST"})}")
print(f"\\tmethod PUT: {nginx.count_documents({"method": "PUT"})}")
print(f"\\tmethod PATCH: {nginx.count_documents({"method": "PATCH"})}")
print(f"\\tmethod DELETE: {nginx.count_documents({"method": "DELETE"})}")
print(f"{nginx.count_documents({"method": "GET", "path": "/status"})} statu check")