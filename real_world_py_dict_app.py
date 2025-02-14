# Real-World Python Dictionary Applications
# Objective: The aim of this assignment is to reinforce your understanding and application 
# of Python dictionaries, nested collections, and dictionary methods.

# Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. 
# Your task is to update this menu based on given instructions

# Problem Statement: Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50}, 
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
    }

# - Add a new category called "Beverages" with at least two items.
restaurant_menu ["Beverage"] = {"Sodas": 3.50, "Juice": 2.75}
print(restaurant_menu)

# - Update the price of "Steak" to 17.99.
updated_menu = {"Steak": 17.99}
print(updated_menu)

# - Remove "Bruschetta" from "Starters". 
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50}, 
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}}

del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)
