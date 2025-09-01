"""
Author: Mariea Nies
Date: 8/29/2025
File Name: nies_lemonadeStand.py
Description: This file demonstrates the use of functions.
"""

# Function to calculate cost
def calculate_cost (lemon_cost, sugar_cost):
    total_cost = lemon_cost + sugar_cost #add numbers
    return total_cost

def calculate_profit (lemon_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemon_cost, sugar_cost) #reuse function
    profit = selling_price - total_cost
    return profit


# testing with sample values
lemons = 5 
sugar = 3
selling_price = 15

# calculate values
cost = calculate_cost(lemons, sugar)
profit = calculate_profit(lemons, sugar, selling_price)

# build output strings
cost_output = str(lemons) + "+" +str(sugar) + "+" + str(cost)
profit_output = "selling price(" + str(selling_price)+ ") - total cost(" + str(cost)+ ") = " +str(profit)

#print results
print("Total Cost: " + cost_output)
print("Profit: " + profit_output)