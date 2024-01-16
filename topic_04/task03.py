def example_exception_handling():
    try:
        # Ділення на нуль
        result = 10 / 0
    except ZeroDivisionError:
        print("Виняткова ситуація: Ділення на нуль")

    try:
        # Відсутній ключ у словнику
        my_dict = {"key": "value"}
        value = my_dict["nonexistent_key"]
    except KeyError:
        print("Виняткова ситуація: Відсутній ключ у словнику")

    try:
        # Перетворення рядка у число
        number = int("abc")
    except ValueError:
        print("Виняткова ситуація: Помилка при конвертації рядка у число")

    try:
        # Ділення з використанням невідомого оператора
        result = 10 / 0
    except Exception as e:
        print(f"Невідома виняткова ситуація: {e}")

# Виклик функції
example_exception_handling()
