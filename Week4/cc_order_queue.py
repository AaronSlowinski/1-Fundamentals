class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, We do not have that flavor.")
            return
        if scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops \n") 
            return

        print("Order created!")
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All Pending Ice Cream Orders:")
        for order in self.orders.items:
            print(f"Customer: {order['customer']}, Flavor: {order['flavor']}, Scoops: {order['scoops']} ")

    def next_order(self):
        order = self.orders.dequeue()
        if order is not None:
            print(f"\nNext order up! \nCustomer: {order['customer']}, Flavor: {order['flavor']}, Scoops: {order['scoops']} \n")
        else:
            print("No more orders.")
        
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()