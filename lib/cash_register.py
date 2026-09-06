

class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
#discount property with getter and setter methods,ensure discount is 0-100
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")


#adds items to the register, updating the total and storing the item details in the previous transactions list.

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

#applies discount to the total if there are previous transactions, otherwise prints a message indicating that there is no discount to apply.
#  It calculates the discount amount based on the current total and the discount percentage,
#  then subtracts that amount from the total. Finally, it removes the last transaction from the previous transactions list.
    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

# Calculate and subtract the percentage discount
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount

        self.previous_transactions.pop()

    # checks whether there is anything to void,
    # if so it removes the last transaction from the previous transactions list
    # and updates the total and items accordingly.
    def void_last_transaction(self):
        # Check if there are any transactions to void
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        # Remove the most recent transaction
        transaction = self.previous_transactions.pop()

        # Subtract the transaction amount from the total
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove the corresponding item
        self.items.pop()