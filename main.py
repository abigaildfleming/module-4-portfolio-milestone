class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    items = []
    num_items = 2
    i = 0
    total = 0
    for i in range(num_items):
        print('Item {}'.format(i + 1))
        item_name = input('Enter the item name (ex: apple, Chips): ')
        item_price = float(input('Enter the item price (ex: 1, 2.38): '))
        item_quantity = int(input('Enter the item quantity (ex: 1, 2): '))
        print('\n')
        item = ItemToPurchase(item_name, item_price, item_quantity)
        items.append(item)
        total += item.item_quantity * item.item_price


    print('\nTOTAL COST')
    for x in range(len(items)):
        items[x].print_item_cost()

    print('Total: ${:.2f}'.format(total))



