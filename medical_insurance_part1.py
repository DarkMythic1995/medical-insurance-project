"""
Medical Insurance Costs Project - Part 1
This script includes function-based insurance cost calculations and list-based analysis
for a dataset of names and insurance costs.
"""

# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    message = "The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."
    return (message, estimated_cost)

# Create calculate_cost_difference() function
def calculate_cost_difference(cost1, cost2):
    difference = abs(cost1 - cost2)
    print("The difference in insurance cost is " + str(difference) + " dollars.")
    return difference

# Estimate Maria's insurance cost
maria_message, maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
print(maria_message)

# Estimate Omar's insurance cost 
omar_message, omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)
print(omar_message)

# Calculate the difference between Maria's and Omar's insurance costs
maria_omar_difference = calculate_cost_difference(maria_insurance_cost, omar_insurance_cost)

# Function to analyze smoking status
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")

# Function to estimate insurance cost
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
    estimated_cost = 400 * age - 128 * sex + 425 * num_of_children + 10000 * smoker - 2500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name='Keanu', age=29, sex=1, num_of_children=3, smoker=1)

# --- List-Based Analysis ---

# Initial data for list-based tasks
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Append new data
names.append("Priscilla")
insurance_costs.append(8320.0)
print("Updated names:", names)
print("Updated insurance costs:", insurance_costs)

# Combine insurance_costs and names into medical_records
medical_records = list(zip(names, insurance_costs))
print("Medical Records:", medical_records)

# Store and print the length of medical_records
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

# ort medical_records by insurance costs and print
medical_records.sort()
print("Here are the medical records sorted by insurance cost:" + str(medical_records))

# Slice the three cheapest records
cheapest_three = medical_records[:3]
print("Three cheapest insurance costs:", cheapest_three)

# Slice the three most expensive records
priciest_three = medical_records[-3:]
print("Three most expensive insurance costs:", priciest_three)

# Calculate the average insurance cost
occurences_paul = names.count("Paul")
print("There are " + str(occurences_paul) + " individuals with the name Paul in our medical records.")

# Sort alphabetically by name
name_sorted_records = list(zip(names, insurance_costs))
name_sorted_records.sort()
print("Here are the medical records sorted by name:" + str(name_sorted_records))

# Select the middle 5 records (indices 3 to 7)
middle_five_records = medical_records[3:8]
print("Middle five records:", middle_five_records)