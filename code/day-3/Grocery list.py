item_no = int(input("Enter no. of items:\n"))
list_items = {}
while item_no != 0:
    saveFile = open('grocery_items.txt', 'a')
    item_name = input("Enter item name:\n")
    item_qty = (input("Enter item Qty:\n"))
    list_items[item_name] = item_qty
    saveFile.write(item_name)
    item_no -= 1
    saveFile.close()

choice = input("Press 'y' to search item, else 'n'\n")
if choice == 'y':
    query = input("Enter item name to search:\n")
    if query in open('grocery_items.txt').read():
        print(list_items[query])
    else:
        print("item not found")
