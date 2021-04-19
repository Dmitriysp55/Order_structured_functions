from db import load
from restaurant import *

food = load('food')
order = {
    "items": [] 
    }
# printItems(food, 'Today\'s Menu')


while True:
    action = printActionsMenu([
        'Show food',
        'Order Food',
        'Show Order',
        'Exit'
          ]
          , 'Main Menu')
    if action == "1":
        printItems(food, 'Today\'s Menu')
    if action == "2":
        item_i = int(input("Which item?")) - 1
        item_q = int(input(f"How many {food[item_i]['name']} item?"))
        order["items"].append(createOrderItem(food, item_i, item_q))
    if action == "3":
        # print(order)
        printItems(order["items"], "Your order")
    if action == "4":
        break