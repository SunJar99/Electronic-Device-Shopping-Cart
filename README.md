Electronic Device Shopping Cart System
Description

This project is a Python program that simulates an electronic device store.
It uses Object-Oriented Programming (OOP) concepts such as inheritance and classes.

Customers can:

View available devices

Add devices to a shopping cart

View cart items

Checkout and reduce stock

Classes
Device (Base Class)

Attributes:

name

price

stock

warranty_period

Methods:

display_info()

apply_discount()

is_available()

reduce_stock()

Smartphone (inherits Device)

Extra attributes:

screen_size

battery_life

Laptop (inherits Device)

Extra attributes:

ram_size

processor_speed

Tablet (inherits Device)

Extra attributes:

screen_resolution

weight

Cart

Manages:

Adding devices

Removing devices

Calculating total price

Checkout
