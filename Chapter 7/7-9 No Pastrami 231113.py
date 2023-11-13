sandwich_orders = ['pastrami', 'beef', 'fish', 'pastrami', 'pepperoni', 'pastrami']

print("Sorry to tell you that pastrami sandwich have been sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)