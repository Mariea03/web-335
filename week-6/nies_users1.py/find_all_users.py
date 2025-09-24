"""
Title: web335_mongo_queries.py
Author: Mariea Nies
Date: 9/23/2025
Description: Display all users in the connection
"""

from pymongo import MongoClient
client = MongoClient(
    "mongodb+srv://marieanies:MongoDB@bellevueuniversity.r1etkka.mongodb.net/web335DB?retryWrites=true&w=majority" 
)

# Access the web335DB
db = client["web335db"]

# Find all documents in users colletion
print("\nAll users in the collection:")
for user in db.users.find({}):
    print(user)