Orders = []
buy_orders = []
sell_orders = []

class Order:
    def __init__(self, id: int, order: str, type: str, price: float, quantity: float):
        self.id = id
        self.order = order
        self.type = type
        self.price = price
        self.quantity = quantity

    def action(self):
        if self.type == "add":
            Orders.append((self.id, self.order, self.price, self.quantity))
            if self.order == "buy":
                buy_orders.append((self.id, self.order, self.price, self.quantity))
            elif self.order == "sell":
                sell_orders.append((self.id, self.order, self.price, self.quantity))
        elif self.type =="remove":
            Orders.remove((self.id, self.order, self.price, self.quantity))
            if self.order == "buy":
                buy_orders.remove((self.id, self.order, self.price, self.quantity))
            else:
                sell_orders.remove((self.id, self.order, self.price, self.quantity))
        print(f"List of orders: {Orders}")
        print(f"Buy orders: {buy_orders}")
        print(f"Sell orders: {sell_orders}")
        if len(buy_orders) > 0:
            sorted_buy_orders = sorted(buy_orders, key=lambda x: x[2])
            print(f"Best buy order: {sorted_buy_orders[0]}")
            print(f"Quantity of best bought shares: {sorted_buy_orders[0][3]}, price {sorted_buy_orders[0][2]}")
        if len(sell_orders) > 0:
            sorted_sell_orders = sorted(sell_orders, key=lambda x: x[2])
            print(f"Best sell order: {sorted_sell_orders[-1]}")
            print(f"Quantity of best sold shares: {sorted_sell_orders[-1][3]}, price {sorted_sell_orders[-1][2]}")
        print('')

Order_001 = Order(1, "buy", "add", 20, 100)
Order_002 = Order(2, "sell", "add", 25, 200)
Order_003 = Order(3, "buy", "add", 23, 50)
Order_004 = Order(4, "buy", "add", 23, 70)
Order_005 = Order(3, "buy", "remove", 23, 50)
Order_006 = Order(5, "sell", "add", 28, 100)

Order_001.action()
Order_002.action()
Order_003.action()
Order_004.action()
Order_005.action()
Order_006.action()
