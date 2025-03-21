"""
This code is borrowed and modified based on the source code from the 'MedCalc-Bench' repository.
Original repository: https://github.com/ncbi-nlp/MedCalc-Bench

Modifications include:
- None

Date: March 2025
"""

from utils.rounding import round_number


def mean_arterial_pressure_explanation(input_variables):
    """
    Calculates the patient's mean arterial pressure and generates a detailed explanatory text.

    Parameters:
        input_variables (dict): A dictionary containing the following key-value pairs:
            - "sys_bp" (array): The patient's systolic blood pressure (value, unit).
                - Value (float): Systolic blood pressure.
                - Unit (str): The unit of systolic blood pressure, which can be 'mm hg'.
            - "dia_bp" (array): The patient's diastolic blood pressure (value, unit).
                - Value (float): Diastolic blood pressure.
                - Unit (str): The unit of diastolic blood pressure, which can be 'mm hg'.

    Returns:
        dict: Contains two key-value pairs:
            - "Explanation" (str): A detailed description of the calculation process.
            - "Answer" (float): The patient's mean arterial pressure.

    Notes:
        - None

    Example:
        bmi_calculator_explanation({"sys_bp": [120.0, 'mm hg'], "dia_bp": [80.0, 'mm hg']})
        output: "{'Explanation': "The mean average pressure is computed by the formula 2/3 * (diastolic blood pressure) + 1/3 * (systolic blood pressure). Plugging in the values, we get 2/3 * 80.0 mm Hg + 1/3 * 120.0 mm Hg = 93.333 mm Hg.\nHence, the patient's mean arterial pressure is 93.333 mm Hg.\n", 'Answer': 93.333}"
    """

    sys_bp = input_variables['sys_bp']
    dia_bp = input_variables['dia_bp']
    
    output = ""

    value = round_number(2*dia_bp[0]/3 + sys_bp[0]/3)

    output += f"The mean average pressure is computed by the formula 2/3 * (diastolic blood pressure) + 1/3 * (systolic blood pressure). Plugging in the values, we get 2/3 * {dia_bp[0]} mm Hg + 1/3 * {sys_bp[0]} mm Hg = {value} mm Hg.\n"
    output += f"Hence, the patient's mean arterial pressure is {value} mm Hg.\n"

    return {"Explanation": output, "Answer": value}


if __name__ == "__main__":
    # Defining test cases
    test_cases = [
        {
            "sys_bp": [120.0, 'mm hg'],  # Systolic Blood Pressure
            "dia_bp": [80.0, 'mm hg'],  # Diastolic Blood Pressure
        }
    ]

    # Iterate the test cases and print the results
    for i, input_variables in enumerate(test_cases, 1):
        print(f"Test Case {i}: Input = {input_variables}")
        result = mean_arterial_pressure_explanation(input_variables)
        print(result)
        print("-" * 50)
