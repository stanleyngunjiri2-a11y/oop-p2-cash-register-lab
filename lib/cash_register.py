class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # discounts property
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    # adds an item to the cash register
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # adds the item once for each quantity
        for _ in range(quantity):
            self.items.append(item)

        # stores the transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    # applies the discount to the total
    def apply_discount(self):
        if self.discount == 0:
            return "There is no discount to apply."

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        return "After the discount, the total comes to ${}.".format(
            self.total
        )

    # voids the most recent transaction
    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()

        self.total -= transaction["price"] * transaction["quantity"]

        quantity = transaction["quantity"]
        item = transaction["item"]

        # removes the correct number of items
        for _ in range(quantity):
            self.items.remove(item)