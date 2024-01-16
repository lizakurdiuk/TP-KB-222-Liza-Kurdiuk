# calculator_library.py

def validate_operator(operator):
    # Реалізуйте функцію для перевірки правильності оператора
    pass

def genFloatValue(prompt):
    # Реалізуйте функцію для отримання дійсного числа від користувача
    pass

def safe_operation(operator, n1, n2=None):
    # Реалізуйте функції для виконання безпечних операцій
    pass

# calculator_library.py

def validate_operator(operator):
    return operator in ['+', '-', '*', '/', '**', 'sqrt']

def genFloatValue(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def safe_operation(operator, n1, n2=None):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        if n2 != 0:
            return n1 / n2
        else:
            print("Division by zero is not allowed.")
            return None
    elif operator == '**':
        return n1 ** n2
    elif operator == 'sqrt':
        if n1 >= 0:
            return n1 ** 0.5
        else:
            print("Cannot calculate square root of a negative number.")
            return None
