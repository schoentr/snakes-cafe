appetizers = ['Nachos', 'Wings', 'Fries']
entrees = ['Salmon', 'Pasta', 'Cheeseburger', 'Salad']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Soda','Coffee','Water']
menu = f"""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
{drinks[0]}
{drinks[1]}
{drinks[2]} """

print(menu)
