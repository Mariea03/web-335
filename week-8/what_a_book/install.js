// whatabook-install.js

// Drop and recreate database
db.dropDatabase()

// Create collections
db.createCollection("customers")
db.createCollection("books")
db.createCollection("wishlistitems")

// Insert books
db.books.insertMany([
    {
        bookId: 1001,
        title: "The Space Between worlds",
        author: "Micaiah Johnson",
        genre: "Sci-fi",
    },
    {
        bookId: 1002,
        title: "It Ends with us",
        author: "Colleen Hoover",
        genre: "Fiction",
    },
    {
        bookId: 1003,
        title: "Onyx Storm",
        author: "Rebecca Yarros",
        genre: "Fantasy",
    }
])


// Insert customers
db.customers.insertMany([
    {
        customerId: "c102",
        firstName: "Mark",
        lastName: "Whalberg"
    },
    {
        customerId: "c103",
        firstName: "Donny",
        lastName: "Whalberg"
    },
        {
        customerId: "c104",
        firstName: "Harry",
        lastName: "styles"
    },
    {
        customerId: "c105",
        firstName: "Michelle",
        lastName: "Pfifer"
    }
])

// Insert wishlist items
db.wishlistitems.insertMany([
    {
        wishlistId: ObjectId(),
        customerId: 101,
        bookId: 1003
    },
    {
       wishlistId: ObjectId(),
        customerId: 102,
        bookId: 1002 
    }
])


