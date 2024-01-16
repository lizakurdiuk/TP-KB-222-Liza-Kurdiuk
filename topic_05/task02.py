import requests

def get_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve exchange rates. Please try again later.")
        return {}
    
    data = response.json()
    result = {elem["cc"]: elem["rate"] for elem in data}
    return result

def convert_currency(amount, currency, exchange_rates):
    if currency not in exchange_rates:
        print("Currency not found in exchange rates.")
        return None
    
    convert = amount * exchange_rates[currency]
    return convert

def main():
    exchange_rates = get_exchange_rates()

    while True:
        try:
            amount = float(input("Enter the amount: "))
            currency = input("Enter the currency code for conversion (USD, EUR, PLN): ").upper()

            conversion_result = convert_currency(amount, currency, exchange_rates)
            if conversion_result is not None:
                print(f"{amount} {currency} = {conversion_result:.2f} UAH")
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")

if __name__ == "__main__":
    main()

    