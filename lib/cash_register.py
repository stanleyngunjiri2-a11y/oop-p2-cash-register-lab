class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Discount property with getter and setter methods.
    # Ensures discount is an integer between 0 and 100.
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    # Adds items to the register, updates the total,
    # and stores the item details in previous transactions.
    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    # Applies the discount to the total if there are previous transactions.
    # If there are no transactions, it prints a message.
    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        # Calculate and subtract the percentage discount.
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount

        self.previous_transactions.pop()

    # Checks whether there is anything to void.
    # If there is, it removes the last transaction and
    # updates the total and items accordingly.
    def void_last_transaction(self):
        # Check if there are any transactions to void.
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        # Remove the most recent transaction.
        transaction = self.previous_transactions.pop()

        # Subtract the transaction amount from the total.
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove the corresponding item.
        self.items.pop()

