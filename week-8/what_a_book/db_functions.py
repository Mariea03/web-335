"""
db_functions.py
MongoDB Backend Logic for WhatABook

This module handles all database operations for the WhatABook console app.
It connects to MongoDB, retrieves data, and performs CRUD actions related
to books, customers, and wishlists.

Mariea Nies
Ben Hilarides
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

# Database Connection
def connect_to_db(uri=None, db_name="whatABook"):
    uri = uri or "mongodb+srv://marieanies_db_user:MongoDB@bellevueuniversity.r1etkka.mongodb.net/web335DB?retryWrites=true&w=majority/whatABook" 
    try:
        client = MongoClient(uri)
        db = client['whatABook']
        print("Connected to MongoDB successfully.")
        return db
    except Exception as e:
        print("Connection failed:", e)
        return None
    

# Book Functions
def get_all_books(db):
    """
    Retrieves and returns all books from the 'books' collection.
    """
    try:
        books = list(db.books.find({}, {"_id": 0, "bookId": 1, "title": 1, "author": 1, "genre": 1 }))
        return books
    except Exception as e:
        print("Error fetching books:", e)
        return []


def get_books_by_genre(db, genre):
    """
    Retrieves all books mataching a specific genre.
    """
    try:
        books = list(db.books.find({"genre": genre},{"_id": 0}))
        return books
    except Exception as e:
        print("Error fetching books by genre:", e)
        return []
    

def get_book_by_id(db, book_id):
    """
    Retrieves a single book document bu its bookId.
    """    
    try:
        book = db.books.find_one({"bookId": book_id}, {"_id: 0"})
        return book
    except Exception as e:
        print("Error fetching book by ID:", e)
        return None
    

# Wishlist Functions
def get_wishlist_by_customer(db, customer_id):
    """
    Retrieves all wishlist items for a given customerId using aggregation.
    Joins the wishlistitems collection with books to show book details. 
    """
    try:
        customer = db.customers.find_one({"customerId": customer_id})
        if customer:
            wishlist = customer.get("wishlist", [])
            return wishlist
        else:
            return []
    except Exception as e:
        print("Error fetching wishlist:", e)
        return []
    

def add_book_to_wishlist(db, customer_id, book_obj):
    """
    Adds a book to the customer's wishlist.
    """
    try:
        db.customers.update_one(
            {"cusotmerId": customer_id},
            {"$addToSet": {"wishlist": book_obj}}
        )
        print("Book added to wishlist.")
        return True
    except Exception as e:
        print("Error adding to wishlist.", e)
        return False
    

def remove_book_from_wishlist(db, customer_id, book_id):
    """
    Removes a book from the customer's wishlist.
    """    
    try:
        db.customers.update_one(
            {"customerId": customer_id},
            {"$pull": {"wishlist": {"bookId": book_id}}}
        )
    except Exception as e:
         print("Error removing book from wishlist:", e)
         return False
    

# Testing
if __name__ == "__main__":
    db = connect_to_db()

    # Quick test runs (comment out when intergrating) 
    print("\nAll Books:")
    for b in get_all_books(db):
        print(f" - {b['title']} by {b['author']}")

    print("\nWishlist for c102:")
    wishlist = get_wishlist_by_customer(db, "c102")
    for w in wishlist:
        print(f" - {w.get('title', 'Unknown')} ({w.get('genre', 'Uknown')})")       
      