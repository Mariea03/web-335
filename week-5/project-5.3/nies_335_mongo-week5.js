
// add a new user to the collection
db.users.insertOne({
    firstName: "Axel",
    lastName: "Rose",
    employeeId: 1985,
    email: "axel_rose@gnr.com",
    dateCreated: new Date()
})

// verify user was added
db.users.find({ email: "axel_rose@gnr.com"})

// update mozarts email
db.users.updateOne(
    { lastName: "Mozart" },
    { $set: { email: "mozart@me.com"} }
)

// verify email was updated
db.users.find({ lastName: "Mozart" })

// display all users with only firstName, lastName, and email
db.users.find({}, {firstName: 1, lastName: 1, email: 1, _id: 0 })