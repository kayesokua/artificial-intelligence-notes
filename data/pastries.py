import datetime
import random


def generate_pastry_leftovers(size):
    pastry_choices = [
        {
            "name": "Butter Croissant",
            "inventory_date": datetime.date.today(),
            "shelf_life": 2,
            "price": 2.50,
        },
        {
            "name": "Blueberry Muffin",
            "inventory_date": datetime.date.today(),
            "shelf_life": 3,
            "price": 3.0,
        },
        {
            "name": "Banana Bread",
            "inventory_date": datetime.date.today(),
            "shelf_life": 4,
            "price": 3.5,
        },
        {
            "name": "Chocolate Chip Cookie",
            "inventory_date": datetime.date.today(),
            "shelf_life": 14,
            "price": 1.50,
        },
        {
            "name": "Bacon and Egg Bagel",
            "inventory_date": datetime.date.today(),
            "shelf_life": 1,
            "price": 5.50,
        },
        {
            "name": "Ham and Cheese Baguette",
            "inventory_date": datetime.date.today(),
            "shelf_life": 2,
            "price": 4.0,
        },
        {
            "name": "Cinnamon Swirl",
            "inventory_date": datetime.date.today(),
            "shelf_life": 3,
            "price": 3.0,
        },
        {
            "name": "Cream Cheese Bagel",
            "inventory_date": datetime.date.today(),
            "shelf_life": 3,
            "price": 4.5,
        },
        {
            "name": "Caprese Focaccia Sandwich",
            "inventory_date": datetime.date.today(),
            "shelf_life": 2,
            "price": 5.5,
        },
        {
            "name": "Flatbread Falafel",
            "inventory_date": datetime.date.today(),
            "shelf_life": 1,
            "price": 2.50,
        },
        {
            "name": "Vanilla Bean Scone:",
            "inventory_date": datetime.date.today(),
            "shelf_life": 3,
            "price": 3.50,
        },
        {
            "name": "Pretzel With Herb Cream Cheese",
            "inventory_date": datetime.date.today(),
            "shelf_life": 2,
            "price": 3.50,
        },
        {
            "name": "Double Chocolate Brownie",
            "inventory_date": datetime.date.today(),
            "shelf_life": 7,
            "price": 2.50,
        },
        {
            "name": "New York Cheesecake",
            "inventory_date": datetime.date.today(),
            "shelf_life": 7,
            "price": 4.0,
        },
        {
            "name": "Strawberry Cheesecake",
            "inventory_date": datetime.date.today(),
            "shelf_life": 5,
            "price": 4,
        }]
    
    pastry_data = []
    
    for i in range(size):
        selected_pastry = random.choice(pastry_choices)
        selected_pastry["exp_date"] = selected_pastry["inventory_date"] + datetime.timedelta(days=selected_pastry["shelf_life"])
        pastry_data.append(selected_pastry)
    
    for pastry in pastry_data:
        pastry.pop('inventory_date', None)
        
    return pastry_data
