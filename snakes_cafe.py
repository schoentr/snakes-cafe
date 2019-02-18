appetizers = ['Nachos', 'Wings', 'Fries']
entrees = ['Salmon', 'Pasta', 'Cheeseburger', 'Salad']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Soda', 'Coffee', 'Water']
menu = f"""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
{appetizers[0]}
{appetizers[1]}
{appetizers[2]}

Entrees
-------
{entrees[0]}
{entrees[1]}
{entrees[2]}

Desserts
--------
{desserts[0]}
{desserts[1]}
{desserts[2]}

Drinks
------
{drinks[0]}
{drinks[1]}
{drinks[2]} 
"""
print(menu)
order_prompt = """
***********************************
** What would you like to order? **
***********************************
"""
item_totals = {}
for i in appetizers:
    item_totals[i.lower()] = 0
for i in entrees:
    item_totals[i.lower()] = 0
for i in desserts:
    item_totals[i.lower()] = 0
for i in drinks:
    item_totals[i.lower()] = 0

order_msg = ''
item = ''
# print(item_totals)
while item != 'quit':
    # print(item_totals.keys())
    item = input(order_prompt).lower()
    if item in item_totals.keys():
        num = item_totals[item]
        num += 1
        item_totals[item] = num
        if (item_totals[item] == 1):
            order_msg = f'**   You have 1 order of {item}.   **'
        else:
            order_msg = f'**   You have {num} orders of {item}.   **'
    else:
        order_msg = f'** Sorry we do not have {item} on our menu today.   **'
    if item != 'quit':
        print(order_msg)