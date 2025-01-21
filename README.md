# Food Ordering System (OOPs Project)

## Overview

The **Food Ordering System** is a Python-based project developed using **Object-Oriented Programming (OOP)** principles. The system allows users to explore various restaurants, 
browse their menus, add items to a cart, and place an order. It incorporates core OOP concepts like **inheritance**, **encapsulation**, and **polymorphism** to ensure that the code is maintainable,
reusable, and easy to extend. 

This project simulates a real-world food ordering experience, making it both an excellent learning tool for OOP concepts and a practical example of implementing a food ordering system.

## Features

- **Restaurant Management**: The system manages a list of restaurants, each with its own menu.
- **Food Menu**: Displays available food items at each restaurant.
- **Cart Management**: Allows users to add or remove items from their cart.
- **Total Price Calculation**: Automatically calculates the total price based on the selected food items.
- **Payment System**: Facilitates order confirmation and payment.
- **User Details**: Allows users to manage their personal details for future orders.
- **Modular Design**: Uses OOP concepts to create reusable and modular components (like classes and objects).

## Project Structure

This project is organized into several files and modules. Below is an overview of the folder structure:

food_ordering_system/             # Main project directory
├── food/                         # Folder containing food-related files
│   ├── Abstract.py               # This file is an abstract base class for food-related operations
│   ├── Cart.py                   # Manages items that are added to the user's cart
│   ├── Fooditem.py               # Represents an individual food item, including its properties (e.g., name, price)
│   ├── Foodmanager.py            # Handles operations related to managing food items, such as adding or removing them
│   ├── Foodmenu.py               # Manages the list of available food items in a restaurant’s menu
│   ├── Payment.py                # Handles the process of payment after an order is placed
│   └── Restaurant.py             # Contains details of a restaurant, such as its name, menu, etc.
├── sample_file1.py               # An example file that may contain additional features or operations (can be a demo)
├── userdetails.py                # Manages user details and user-related information
├── userstorage.py                # Stores user-related data, typically in a mock database format
├── __pycache__/                  # Contains Python bytecode files generated during runtime (not essential to understand)
└── .vscode/                      # Contains configuration files for Visual Studio Code (IDE-specific)


### Key Classes and Their Responsibilities:

- **Restaurant**: Represents each restaurant with its name, details, and the menu of available food items. 
  - Methods include adding/removing food items, displaying the menu, etc.
  
- **FoodItem**: Represents an individual food item, including its name, price, description, and other properties.
  - Methods include displaying details of the food item and handling pricing.

- **Cart**: Manages the user's cart, which can store selected food items. 
  - Methods include adding/removing items and calculating the total price.

- **FoodMenu**: Manages the list of food items available at a particular restaurant.
  - Methods include displaying the menu and adding/removing items.

- **FoodManager**: This class acts as the interface between the user and the food-related functionalities. 
  - It manages the operations that deal with food items, such as adding food to the cart.

- **Payment**: Handles the payment process once the user has completed the ordering.
  - Methods include processing the payment and displaying the total price.


  ## Installation

### Requirements
Before running the project, make sure you have **Python 3.x** installed on your machine.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Marankrish/Food.git

Example Output:
Welcome to Food Ordering System!

Please select a restaurant:
1. Restaurant A
2. Restaurant B
3. Restaurant C

Enter the number corresponding to your choice: 1

Menu for Restaurant A:
1. Pizza - $10.99
2. Burger - $5.49
3. Pasta - $8.99

Enter the food item you want to add to your cart: 2
You added Burger to your cart.

Your cart:
- Burger - $5.49
Total: $5.49

Proceed to payment? (yes/no): yes
Payment successful! Thank you for your order.


