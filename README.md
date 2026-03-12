# Medium Level Python Exercises

This repository contains a collection of **20 medium-level programming exercises** implemented in **Python**.
The goal of this project is to strengthen **programming logic, control flow, and modular code organization**.

Each exercise simulates a small real-world system such as a gym, parking lot, cinema, cafeteria, or pet shop.

---

# Project Structure

The project is organized so that **each exercise lives in its own file**, while a central program (`main.py`) allows the user to run them from a menu.

Example structure:

```
medium_level_exercises/

├── main.py
├── utils.py
├── .gitignore
├── README.md
│
├── gym_access.py
├── ice_cream_shop.py
├── magic_cafeteria.py
├── cinema_ticket_system.py
├── pet_shop_recommendation.py
├── parking_lot_system.py
├── hair_salon_agenda.py
├── sport_shop.py
├── spa_service_system.py
├── dance_academy.py
│
├── cafeteria_sales_system.py
├── cinema_room_control.py
├── parking_control_system.py
├── petshop_sales_control.py
├── language_center_evaluation.py
├── sport_store_inventory.py
├── club_membership.py
```

Each file contains a **function that runs the corresponding exercise**.

---

# main.py

The `main.py` file is the **entry point of the project**.

It provides a **menu system that allows the user to execute any of the 20 exercises**.

Main responsibilities of `main.py`:

• Display the main menu
• Allow the user to select an exercise
• Import and execute the corresponding function
• Control program execution using a loop

Example menu:

```
MAIN MENU
----------------------------------------
1. Ice Cream Shop
2. Gym Age Validation
3. Magic Cafeteria
4. Cinema Ticket System
5. Pet Shop Recommendation
...
20. Club Membership
```

When the user selects an option, the program calls the function from the corresponding module.

Example import:

```python
from gym_access import run_gym_access
```

Example execution:

```python
run_gym_access()
```

This design follows a **modular structure**, where each feature is isolated in its own file.

---

# utils.py

The `utils.py` module contains **helper functions used by multiple exercises**, such as:

• clearing the terminal
• creating pauses in the program
• small utilities used across the project

This prevents **code duplication** and keeps the other files cleaner.

---

# Programming Concepts Practiced

This project focuses on reinforcing core programming logic:

### Conditionals

```
if
elif
else
```

### Loops

```
while
for
```

### Counters

```
counter += 1
```

### Accumulators

```
total += value
```

### Maximum value detection

```
if value > max_value
```

### Input validation

```
try:
    value = int(input())
except ValueError:
    print("Invalid input")
```

---

# How to Run the Project

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/medium_level_exercises.git
```

2️⃣ Enter the folder

```
cd medium_level_exercises
```

3️⃣ Run the main program

```
python main.py
```

4️⃣ Select the exercise from the menu.

---

# Purpose of the Project

The main goal of this project is to **practice programming logic and build a solid foundation in Python**.

The exercises simulate small systems such as:

• cafeterias
• gyms
• cinemas
• pet shops
• parking systems
• language centers
• stores and inventories

---

# Future Improvements

Possible future improvements include:

• using lists and dictionaries to simplify logic
• storing data in files
• improving the menu system
• adding automated tests
• converting the project into a CLI application

---

# Author

Programming practice project focused on strengthening **problem solving and Python fundamentals**.
