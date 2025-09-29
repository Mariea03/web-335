"""
Title: nies_usersp2.py
Author: Mariea Nies
Date: 9/28/2025
Description: Week 7 hands on project - Perform CRUD operations on MongoDB users collection
"""

# Import the MongoClient from pymongo
from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://marieanies_db_user:MongoDB@bellevueuniversity.r1etkka.mongodb.net/web335DB?retryWrites=true&w=majority"
)
db = client['web335DB'] #Access the database
print("Connected to MongoDB.\n")

# Create a new user document
new_user = {
    "firstName": "Billy",
    "lastName": "Crystal",
    "employeeId": "10987",
    "email": "princessbride@eightiesmovies.com",
    "dateCreated": datetime.datetime.now(datetime.timezone.utc)
}

user_id = db.users.insert_one(new_user).inserted_id
print(f"User created with ID: {user_id}\n")

# Prove the document was created
created_user = db.users.find_one({"employeeId": "10987"})
print("Document after creation:")
print(created_user, "\n")


# UPDATE the users email address
db.users.update_one(
    {"employeeId": "10987"},
    {"$set":{"email": "pb87@eightiesmovies.com"}}
)
print("User email updated \n")


# PROVE the document was updated
updated_user = db.users.find_one({"employeeId": "10987"})
print("Document after email update:")
print(updated_user, "\n")


# DELETE the document
delete_result = db.users.delete_one({"employeeId": "10987"})
print(f"Number of documents deleted: {delete_result.deleted_count}\n")


# PROVE the document was deleted
deleted_user = db.users.find_one({"employeeId": "10987"})
print("Document after deletion (should be None):")
print(deleted_user)