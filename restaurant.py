from math import ceil

def printItems(items, title = None, showQuantity = False):
    count_items = len(items)
    current_page = 1
    per_page = 5
    page_total = ceil(count_items / per_page)
    start_index = (current_page - 1)* per_page
    end_index = start_index + per_page

    if title != None:
        print("#"*50)
        print(title)
    print("#"*50)
    for i in range(count_items):
        if i >= start_index and i <= end_index:
            print(f"{i +1:2} {items[i]['name']:15} {items[i]['quantity'] if showQuantity == True else '':5} {items[i]['price']['amount']:15} {items[i]['price']['currency']}")
    print("#"*50)
    for page in range(1, page_total+1):
        if page == current_page:
            print(f"[{page}]", end="")
        else:
            print(f"{page}", end="")
    # for i in range( len(items) ):       
    

    page_control = input("\nHit '<' for previous page OR '>' for next page \n Hit Enter to continue..")
    if page_control == '>' and current_page < page_total:
        current_page += 1
    if page_control == '<' and current_page > 0:
        current_page -= 1

def printActionsMenu(items, title = None):
    if title != None:
        print("#"*20)
        print(title)
    print("#"*20)
    for i in range( len(items) ):
        print(f"{i +1:2} {items[i]:15}")
    print("#"*20)

    option = input('>>>>>>>>>>>>')
    return option

def createOrderItem(food, item_i, item_q):
    return {
        "name": food[item_i]['name'], 
        "quantity": item_q,
        "price": 
            {
            "amount": item_q * food[item_i]['price']['amount'],
            "currency" : food[item_i]['price']['currency']
            }
    }
def calcTotal(food, item_i, item_q):
    return food[item_i]["price"]["amount"] * item_q

def printBill(order):
    file = open("bill.txt", 'w')
    file.write("#"*30 + "\n")
    file.write(" "*10 +"YOUR ORDER"+ "\n")
    for item in order['items']:
        file.write(f"{item['name']:15} x{item['quantity']} {item['price']['amount']:5} {item['price']['currency']}\n")
    file.write("#"*30 + "\n")
    file.write(f"Total: {order['total']['amount']:15} {order['total']['currency']:15}\n")
    file.write("#"*30 + "\n")
    file.close()