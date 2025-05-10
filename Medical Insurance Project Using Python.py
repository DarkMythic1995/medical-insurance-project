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
