import random

Restuarants = ["Popeyes", "ChickFila", "Ininout"]
Popeyes = ["Chicken sandwich", "Cajun fries", "Dry biscuits"]
ChickFila = ["Chicken sandwich", "Waffle fries", "House lemonade"]
Ininout = ["Hamburger", "4x4", "Animal Fries"]

Restuarant = Restuarants[random.randrange(0,3)]


if Restuarant == "Popeyes":
    item = Popeyes[random.randrange(0,3)]
    print("The resuarant is popeyes")
    print("The item is " + item)

if Restuarant == "ChickFila":
    item = ChickFila[random.randrange(0,3)]
    print("The resuarant is Chickfila")
    print("The item is " + item)
    
    
if Restuarant == "Ininout":
    item = Ininout[random.randrange(0,3)]
    print("The resuarant is Ininout")
    print("The item is " + item)