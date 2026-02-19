Electronic Device Shopping Cart System
Project Description

This project implements an Electronic Device Store using Object-Oriented Programming (OOP) concepts in Python.

The system allows customers to:

View available electronic devices

Add devices to a shopping cart

Remove devices from the cart

Checkout and generate a receipt

Automatically update stock after purchase

The project demonstrates the use of:

Inheritance

Encapsulation

Polymorphism

Class relationships

Unit testing with Python’s unittest module

System Design
Class Overview
1. Device (Base Class)

The Device class serves as the parent class for all electronic devices.

Attributes:

name (str)

price (float)

stock (int)

warranty_period (int)

Methods:

__init__(self, name, price, stock, warranty_period)

display_info(self)

__str__(self)

apply_discount(self, discount_percentage)

is_available(self, amount)

reduce_stock(self, amount)

2. Smartphone (Inherits from Device)

Additional Attributes:

screen_size (float)

battery_life (int)

Additional Methods:

make_call(self)

install_app(self)

__str__(self)

3. Laptop (Inherits from Device)

Additional Attributes:

ram_size (int)

processor_speed (float)

Additional Methods:

run_program(self)

use_keyboard(self)

__str__(self)

4. Tablet (Inherits from Device)

Additional Attributes:

screen_resolution (str)

weight (float)

Additional Methods:

browse_internet(self)

use_touchscreen(self)

__str__(self)

5. Cart

The Cart class manages customer purchases.

Attributes:

items (list of tuples containing device and quantity)

total_price (float)

Methods:

add_device(self, device, amount)

remove_device(self, device, amount)

get_total_price(self)

print_items(self)

checkout(self)
