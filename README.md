# Rent_Calculator

This is a simple Python project I created while learning the basics of Python programming. The program helps calculate the individual rent share for people living in a shared space, based on total rent, food expenses, and electricity consumption. 

## Features:
- Takes user inputs for rent, food expenses, electricity usage, and charge per unit of electricity.
- Divides the total costs among the number of people sharing the living space.
- Outputs the amount each person has to pay.

## Project Breakdown:
### Inputs:
1. **Total Rent**: The overall rent amount for the hostel or flat.
2. **Total Food Ordered**: The cost of snacks or meals ordered.
3. **Electricity Usage**: Total units of electricity consumed.
4. **Charge Per Unit**: The cost per unit of electricity.
5. **Number of People**: The total number of people living in the room or flat.

### Outputs:
- **Amount Each Person Pays**: The program divides the sum of the rent, food expenses, and electricity bill by the number of people living in the room or flat.

### Code:

```python
# Input from the user
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend (in units) = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the room/flat = "))

# Calculate total electricity bill
total_bill = electricity_spend * charge_per_unit

# Calculate the amount each person has to pay
output = (food + rent + total_bill) // persons

# Output the result
print("Each person will pay = ", output)
```

## How It Works:
1. The program first takes input for the rent, food expenses, electricity usage, and the number of people sharing the flat/room.
2. It calculates the electricity bill by multiplying the total units consumed with the charge per unit.
3. The total expenses (rent, food, electricity) are divided equally among the individuals.
4. The output is the amount each person is required to pay.

