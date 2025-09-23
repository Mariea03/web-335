// Name: Mariea Nies
// Date: 09/20/2025
// Assignment: Week 6 MongoDB Hands-On Project

// a. Display all students
db.students.find()

//b. Add a new student, then prove they were successfully added
db.students.insertOne({
    "firstName": "Severus",
    "lastName": "Snape",
    "studentId": "s1019",
    "houseId": "h1010"  // Slytherin
})
db.students.find({ "studentId": "s1019" })

// c. Update one property of the new student (e.g., lastName)
db.students.updateOne(
    { "studentId": "s1019"},
    { $set: { "lastName": "Prince"} }
)
db.students.find({ "studentId": "s1019"})

// d. Delete the student you just created, then prove they were removed.
db.students.deleteOne({ "studentId": "s1019" })
db.students.find({ "studentId": "s1019"})

// e. Display all students by house
db.houses.aggregate([
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
        $project: {
            _id: 0,
            house: "$founder",
            students: 1
        }
    }
])

// g. Display all students in the house with an Eagle mascot (ravenclaw).
db.houses.aggregate([
    { $match: { "masoct": "Eagle"} },
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
    $project: {
        _id: 0,
        house: "$founder",
        students: 1
    }
  }  
])