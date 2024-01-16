from calculator_library import validate_operator, genFloatValue, safe_operation


def main():
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

        if not validate_operator(choice):
            print("Invalid operator. Please choose a valid operator.")
            continue

        try:
            n1 = genFloatValue("First number: ")
            result = None

            if choice in ['+', '-', '*', '/', '**']:
                n2 = genFloatValue("Second number: ")
                result = safe_operation(choice, n1, n2)
            elif choice == 'sqrt':
                result = safe_operation(choice, n1)

            print("Result:", result)

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
