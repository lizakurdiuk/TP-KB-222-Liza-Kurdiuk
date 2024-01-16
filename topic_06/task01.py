import logging
from calculator_library import validate_operator, genFloatValue, safe_operation

def main():
    logging.basicConfig(filename='calculator.log', level=logging.INFO)  # Ініціалізуємо логування

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

        logging.info(f"Selected operator: {choice}")

        if choice == '7':
            print("Exiting the calculator.")
            break

        if not validate_operator(choice):
            print("Invalid operator. Please choose a valid operator.")
            continue

        try:
            n1 = genFloatValue("First number: ")
            result = None

            if choice in {'+', '-', '*', '/', '**'}:
                n2 = genFloatValue("Second number: ")
                result = safe_operation(choice, n1, n2)
            elif choice == 'sqrt':
                result = safe_operation(choice, n1)

            print("Result:", result)

            logging.info(f"Entered first number: {n1}")
            if choice in {'+', '-', '*', '/'}:
                logging.info(f"Entered second number: {n2}")
            logging.info(f"Result: {result}")

            # Логуємо після успішної операції
            logging.info("Successful operation")

        except ValueError as e:
            print("Error:", e)
            logging.error(f"ValueError: {e}")
        except Exception as e:
            print("An error occurred:", e)
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

