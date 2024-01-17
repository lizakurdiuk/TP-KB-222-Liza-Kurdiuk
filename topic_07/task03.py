import math
import logging

logging.basicConfig(filename='calc.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return x / y

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            raise ValueError("Square root of a negative number is not allowed")
        return math.sqrt(x)

    def validate_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '**', 'sqrt']
        return operator in valid_operators

    def safe_operation(self, operator, x, y=None):
        try:
            if operator == 'sqrt':
                if x < 0:
                    raise ValueError("Square root of a negative number is not allowed")
                result = self.square_root(x)
            elif operator in {'+', '-', '*', '/', '**'}:
                result = eval(f"{x}{operator}{y}")
            else:
                raise ValueError("Invalid operator")
            logging.info(f"Operation: {x} {operator} {y if y is not None else ''} = {result}")
            return result
        except Exception as e:
            logging.error(f"Error: {e}")

    def genFloatValue(self, prompt: str):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def main(self):
        while True:
            print("Make a feature selection:")
            print("1. +")
            print("2. -")
            print("3. *")
            print("4. /")
            print("5. **")
            print("6. Square root extraction")
            print("7. Exit")

            choice = input("Enter the operator of the function to perform (+/-/*/...): ")

            if choice == '7':
                print("Exiting the calculator.")
                break

            if not self.validate_operator(choice):
                print("Invalid operator. Please choose a valid operator.")
                continue

            try:
                n1 = self.genFloatValue("First number: ")
                result = None

                if choice in {'+', '-', '*', '/', '**'}:
                    n2 = self.genFloatValue("Second number: ")
                    result = self.safe_operation(choice, n1, n2)
                elif choice == 'sqrt':
                    result = self.safe_operation(choice, n1)

                print("Result:", result)

            except ValueError as e:
                print("Error:", e)
            except Exception as e:
                print("An error occurred:", e)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.main()-