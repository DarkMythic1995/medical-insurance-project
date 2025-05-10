# Medical Insurance Project

This Python script was made to calculate medical insurance costs based on user inputs like age, sex, BMI, number of children, and smoking status. I built this project as part of my learning journey to practice Python programming, function design, and data processing — skills I’m leveraging as an aspiring Data Analyst.

## Project Overview

The Medical Insurance Project calculates estimated insurance costs using a linear formula, taking into account key factors that influence premiums. 

The script calculates costs for multiple individuals, making it a practical example of handling and processing structured data.

## Skills Demonstrated

- **Python Programming**: Designed a reusable function to compute insurance costs.
- **Data Processing**: Processed multiple input parameters (age, sex, BMI, etc.) to generate meaningful outputs.
- **Problem-Solving**: Refactored code to eliminate redundancy and improve readability.
- **Documentation**: Created clear usage instructions for accessibility.

## Implementation Details

The core of the project is the `calculate_insurance_cost()` function, which uses the following formula:

estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500


### Parameters:

- `name`: The individual’s name (string)
- `age`: Age in years (integer)
- `sex`: 0 for female, 1 for male (integer)
- `bmi`: Body Mass Index (float)
- `num_of_children`: Number of children (integer)
- `smoker`: 0 for non-smoker, 1 for smoker (integer)

The function prints the estimated cost for each individual and returns the value for potential further use.

## Challenges and Solutions

- **Challenge**: Initially, the script repeated code for each individual, making it inefficient.
  - **Solution**: I created a reusable `calculate_insurance_cost()` function to handle all calculations, improving modularity and reducing redundancy.
- **Challenge**: The output was generic, referring to “this person” without personalization.
  - **Solution**: Added a `name` parameter to the function, allowing for personalized output (example: “The estimated insurance cost for Maria is…”).
 

## New Feature: Smoking Analysis

Added a function `analyze_smoker()` that uses control flow (`if/else`) to provide advice:
- Suggests quitting smoking to save $10,000 for smokers.
- Confirms smoking is not an issue for non-smokers.

## Future Improvements

-  Add input validation to ensure parameters like `age` and `bmi` are within realistic ranges.
-  Implement a function to compare costs between individuals, as suggested in the project’s optional challenges.
-  Visualize the cost breakdown (example: the contribution of each parameter) using a library like Matplotlib to enhance data analysis capabilities.
