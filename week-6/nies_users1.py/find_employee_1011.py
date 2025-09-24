"""
Title: web335_mongo_queries.py
Author: Mariea Nies
Date: 9/23/2025
Description: Display the user document where employeeId is 1011
"""

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://marieanies:MongoDB@bellevueuniversity.r1etkka.mongodb.net/web335DB?retryWrites=true&w=majority" 
)

# Access the web335DB
db = client["web335DB"]

# Find the document where employeeId = 1011
print("\nUser with employeeId = 1011:")
print(db.users.find_one({"employeeId": "1011"}))