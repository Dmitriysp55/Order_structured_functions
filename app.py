from db import load
from restaurant import *

food = load('food')
order = {
    "items": [],
    "total": {
            "amount": 0,
            "currency" : "MDL"
        },
    "client": {
        "fullname": "Enter your name",
        "address": {
             "city": "Enter your City",
             "street": "Enter your street",
             "appartment": "Enter number of apartment"
            },
        "delivery": "Do you want delivery?(Y/N)"
        }
    }
# printItems(food, 'Today\'s Menu')


while True:
    action = printActionsMenu([
        'Show food',
        'Order Food',
        'Show Order',
        'Check out',
        'Print bill',
        'Exit'
          ]
          , 'Main Menu')
    if action == "1":
        printItems(food, 'Today\'s Menu')
    if action == "2":
        item_i = int(input("Which item?")) - 1
        item_q = int(input(f"How many {food[item_i]['name']} item?"))
        confirm_order = input(f"You ordered {item_q} of {food[item_i]['name']}. Confirm (Y/N)")
        
        if item_q <= food[item_i]["avail"] and confirm_order == "Y":
            order["items"].append(createOrderItem(food, item_i, item_q))
            order["total"]["amount"] += calcTotal(food, item_i, item_q)
        elif confirm_order != "Y":
            continue
        else:
            print(f"We do not have {item_q} of {food[item_i]['name']} available")
    if action == "3":
        # print(order)
        printItems(order["items"], "Your order", True)

    if action == "4":
        for key in order['client']:
            if key == 'address':
                for key in order['client']['adress']:
                    order['client']['adress'][key] = input(order['client']['adress'][key])
            else:
                order['client'][key] = input(order['client'][key])
        order['client']['delivery'] = True if order['client']['delivery'] == 'Y' else False
        if order['client']['delivery']:
            if order['total']['amount'] < 200:
                order['delivery']['amount'] = 100
        else:
            pass
    if action == "5":
        printBill(order)
    if action == "6":
        break