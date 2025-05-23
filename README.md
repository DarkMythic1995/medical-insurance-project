# Medical Insurance Project

This Python script was made to calculate medical insurance costs based on user inputs like age, sex, BMI, number of children, and smoking status. I built this project as part of my learning journey to practice Python programming, function design, and data processing. Both parts of this project function with Jupyter notebook.

## Project Overview

The Medical Insurance Project consists of two modular scripts:
- **`medical_insurance_part1.py`**: Calculates estimated insurance costs for individuals using a linear formula and performs list-based analysis on a dataset of names and insurance costs, including sorting, slicing, and duplicate detection.
- **`medical_insurance_part2.py`**: Analyzes a dataset of estimated and actual insurance costs, calculating averages, comparing costs to the average, and updating estimates using list comprehension.

The project demonstrates handling structured data, processing multiple inputs, and generating insights, making it a practical example of data analysis in Python.

## Skills Demonstrated

- **Python Programming**: Designed reusable functions for cost calculations and data analysis.
- **Data Processing**: Processed diverse inputs (age, sex, BMI, names, costs) to generate meaningful outputs.
- **List Manipulation**: Performed operations like appending, zipping, sorting, slicing, counting, and list comprehension on datasets.
- **Control Flow**: Used `if/else` for smoker analysis and cost comparisons, and `while` loops for iterative calculations.
- **Problem-Solving**: Refactored code for modularity, splitting into two files to improve organization and maintainability.
- **Documentation**: Created clear, detailed instructions for accessibility and reproducibility.

## Implementation Details
### Part 1: Function-Based Calculations and List Analysis (`medical_insurance_part1.py`)

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

Additional functions:
- `calculate_cost_difference()`: Computes the absolute difference between two costs.
- `analyze_smoker()`: Provides smoking status advice.
- `estimate_insurance_cost()`: Alternative cost formula for validation.

The script calculates costs for individuals (Maria, Omar, Keanu) and analyzes a dataset:
- **Dataset**: `names = ["Mohamed", "Sara", ..., "Priscilla"]` (11 entries), `insurance_costs` (costs like 13262.0).
- **Tasks**:
  - Append new data ("Priscilla", 8320.0).
  - Combine lists into `medical_records` using `zip()`.
  - Sort by cost, slice cheapest/priciest three records, count duplicates (e.g., "Paul" appears twice).
  - Extensions: Sort alphabetically, select middle five records.

### Part 2: Estimated vs. Actual Costs Analysis (`medical_insurance_part2.py`)

Analyzes a new dataset:
- **Dataset**: `names = ["Judith", "Abel", ..., "Anabel"]` (7 entries), `estimated_insurance_costs` (e.g., 1000.0), `actual_insurance_costs` (e.g., 1100.0).
- **Tasks**:
  - Calculate average actual cost using a `while` loop.
  - Compare actual and estimated costs to the average, printing above/below/equal status.
  - Update estimated costs by scaling by 11/10 using list comprehension.

## Challenges and Solutions

- **Challenge**: Initial script repeated code for each individual, reducing efficiency.
  - **Solution**: Created `calculate_insurance_cost()` for modularity, reused across individuals.
- **Challenge**: Generic output lacked personalization.
  - **Solution**: Added `name` parameter for personalized messages (e.g., “The estimated insurance cost for Maria is…”).
- **Challenge**: Managing two datasets with different structures in a single script.
  - **Solution**: Split into `medical_insurance_part1.py` and `medical_insurance_part2.py` for modularity, improving organization. <!-- Updated -->
- **Challenge**: Comparing estimated vs. actual costs required efficient iteration.
  - **Solution**: Used a `while` loop for summation and list comprehension for updates, enhancing performance. <!-- New -->

## New Features

- **Smoking Analysis**: `analyze_smoker()` advises smokers to quit, saving $10,000, and confirms non-smoker status.
- **List-Based Analysis** (Part 1): Sorting, slicing, and duplicate detection provide insights into cost distributions and data quality. <!-- New -->
- **Cost Comparison** (Part 2): Compares estimated and actual costs to the average, highlighting discrepancies for analysis. <!-- New -->
- **Modular Design**: Split project into two files for better maintainability and clarity. <!-- New -->
