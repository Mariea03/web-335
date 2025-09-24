"""
Title: web335_mongo_queries.py
Author: Mariea Nies
Date: 9/23/2025
Description: Display the user document where lastName is Mozart. 
"""

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://marieanies:MongoDB@bellevueuniversity.r1etkka.mongodb.net/web335DB?retryWrites=true&w=majority" 
)


# Access the web335DB
db = client["web335DB"]

# Find the document where lastName = Mozart
print("\nUser with lastName = Mozart")
print(db.users.find_one({"lastName": "Mozart"}))