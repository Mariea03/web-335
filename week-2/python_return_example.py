# Returning a newly created dictionary
def dictionaryOfStrings(firstName, lastName, age=None):
    #Returns a newly created Dictionary, optional age

    returnDictionary = {'firstName': firstName, 'lastName': lastName}

    if age:
        returnDictionary['age'] = age

    return returnDictionary

while True:
    print('Enter the first & last name, optional age, q to quit:')

    fName = input('First Name: ')
    if fName == "q":
        break

    lName = input("Last Name: ")
    if lName == 'q':
        break

    age = input('Age, q to quit, negative age to leave out: ')
    if age == 'q':
        break

    ageInput = int(age)

    if ageInput < 0:
        print()
        print(dictionaryOfStrings(fName, lName))
        print()
    else:
        print()
        print(dictionaryOfStrings(fName, lName, ageInput))
        print()    