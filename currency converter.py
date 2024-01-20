'''pip install forex-python (To convert currency using the latest exchange rates in Python,
 here i used a third-party library like forex-python to fetch the latest exchange rates from an API.)'''


from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount, to_currency
    except:
        return None, None

def main():
    print("Welcome to the Currency Converter!")

    while True:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency (e.g., INR): ").upper()
        to_currency = input("Enter the target currency (e.g., USD): ").upper()

        converted_amount, target_currency = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None and target_currency is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {target_currency}")
        else:
            print("Error: Unable to fetch exchange rate. Please check your currencies.")

        another_conversion = input("Do you want to convert another currency? (yes/no): ").lower()
        if another_conversion != 'yes':
            print("Thanks for using the Currency Converter. Sayonara!")
            break

if __name__ == "__main__":
    main()

