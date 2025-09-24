"""
Title: web335_mongo_queries.py
Author: Mariea Nies
Date: 9/23/2025
Description: Test connection to MongoDB
"""

# Import MongoClient
from pymongo import MongoClient

# Build a connection string to connect to MongoDB
client = MongoClient(
    "mongodb+srv://marieanies:MongoDB@bellevueuniversity.r1etkka.mongodb.net/web335DB?retryWrites=true&w=majority" 
)

# Print the client object to confirm connection
print(client)