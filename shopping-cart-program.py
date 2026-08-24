# Shppoing Cart

cart = {
    "apple": {"price": 5, "quantity": 6},
    "milk": {"price": 2.50, "quantity": 1},
    "bread": {"price": 2.50, "quantity": 2}
}

# Functions for menu items
def add_item(item_name, price, quantity):
  cart.update({item_name: {"price": price, "quantity": quantity}})

def checkout(subtotal, tax=0.3):
  print(f"{'ITEM':<10}{'QTY':>5}{'PRICE':>8}{'TOTAL':>8}")
  for name, info in cart.items():
    line_total = info['price'] * info['quantity']
    print(f"{name:<10}{info['quantity']:>5}{info['price']:>8.2f}{line_total:>8.2f}")
  
  total = subtotal * (1 + tax)
  print(f"\nSubtotal: ${subtotal:.2f}")
  print(f"Tax:      ${subtotal * tax:.2f}")
  print(f"Total:    ${total:.2f}")
  
for name, info in cart.items():
    line_total = info['price'] * info['quantity']
    print(f"{name:<10}{info['quantity']:>5}{info['price']:>8.2f}{line_total:>8.2f}")

state = False

while not state:
  # Input for Menu Item
  menu_item = input(
    '1. Add item\n'
    '2. Remove item\n'
    '3. Checkout\n'

    'Enter Here: '
 )

  # Check user menu input
  # Add Items
  if menu_item == '1':
    # get item name
    name_new_item = str(input('Enter the name of the item: ')).lower()
    # check if item is in cart before moving forward
    if name_new_item in cart:
      price_new_item = float(input('Enter price of item: '))
      quanitity_new_item = int(input('Enter quanity of items: '))
      add_item(name_new_item, price_new_item, quanitity_new_item)
    else: 
      print('\n')
      print('Item is already in cart in cart\n')

  # Remove Item
  elif menu_item == '2':
    session = False
    while not session:
     remove_item_name = str(input('Enter the name of the item: ')).lower()
     if (cart.get(remove_item_name)) is None:
       print('Item is not in the cart')
     else:
       session = True
       del cart[remove_item_name]
       print(f'{remove_item_name} has been removed\n')

  # Process checkout
  elif menu_item == '3':
    # Loop and get prices & quantity
   total = 0
   for item in cart.values():
    total += item['price'] * item['quantity']
    state = True
   checkout(total, tax=0.3)

  else:
    print('Please choose from the menu 1-3\n')

