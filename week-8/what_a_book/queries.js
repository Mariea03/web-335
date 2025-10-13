// whatabook-queries.js

db.books.find()

db.books.find({ genre: "Sci-Fi" })

db.books.find({ author: "Micaiah Johnson" })

db.books.find({ bookId: 1001 })

db.wishlistitems.aggregate([
    {
        $lookup: {
            from: "books",
            localField: "booksId",
            foreignField: "bookId",
            as: "book_info"
        }
    },
    {
          $lookup: {
            from: "customers",
            localField: "customerId",
            foreignField: "customerId",
            as: "customer_info"
        }
    },
    {
        $project:{
            _id:0,
            "customer_info.firstName": 1,
            "customer_info.lastName": 1,
            "book_info.title": 1,
            "book_info.author": 1,
            "book_info.genre": 1,
        }
    }
])