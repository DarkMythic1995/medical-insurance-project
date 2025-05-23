"""
Medical Insurance Costs Project - Part 2
This script analyzes a dataset of estimated and actual insurance costs,
calculating averages, comparing costs, and updating estimates.
"""

# Dataset
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Initialize total_cost
total_cost = 0

# Convert first for loop to while loop
index = 0
while index < len(actual_insurance_costs):
    total_cost += actual_insurance_costs[index]
    index += 1

# Calculate average cost
average_cost = total_cost / len(actual_insurance_costs)

# Print average cost
print(f"Average Insurance Cost: {average_cost} dollars.")

# Modify second for loop to include difference from average for estimated costs
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    estimated_cost = estimated_insurance_costs[i]
    print(f"The insurance cost for {name} is {insurance_cost} dollars.")
    if insurance_cost > average_cost:
        print(f"The insurance cost for {name} is above average.")
    elif insurance_cost < average_cost:
        print(f"The insurance cost for {name} is below average.")
    else:
        print(f"The insurance cost for {name} is equal to the average.")
    # Calculate and print difference between estimated cost and average
    difference = estimated_cost - average_cost
    if difference > 0:
        print(f"The estimated cost for {name} is {difference} dollars above average.")
    elif difference < 0:
        print(f"The estimated cost for {name} is {-difference} dollars below average.")
    else:
        print(f"The estimated cost for {name} is equal to the average.")

# Create updated_estimated_costs using list comprehension
updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

# Print updated_estimated_costs
print(updated_estimated_costs)