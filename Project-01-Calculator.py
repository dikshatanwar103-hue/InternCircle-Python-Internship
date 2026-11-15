def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error!, Please enter a valid number for example '12' or '12.5' ")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error!, division by zero in not allowed.")
    else:
        return a / b

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def currency_converter(ammount, rate):
    return ammount*rate

def main():
    while True:
        print("INTERACTIVE CALCULATOR")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")
        print("5. km_to_miles")
        print("6. celsius_to_fahrenheit")
        print("7. currency_converter")
        print("8. Exit")

        choice = input("\n Enter your choice (1-8): ")

        if choice == "1":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print("Result: ", addition(a,b))

        elif choice == "2":
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            print("Result: ", subtraction(a,b))

        elif choice == "3":
                    a = get_number("Enter first number: ")
                    b = get_number("Enter second number: ")
                    print("Result: ", multiply(a,b))

        elif choice == "4":
                    a = get_number("Enter first number: ")
                    b = get_number("Enter second number: ")
                    print("Result: ", divide(a,b))

        elif choice == "5":
                    km = get_number("Enter distance in km: ")
                    print("Miles: ", round(km_to_miles(km), 2))

        elif choice == "6":
                    celsius = get_number("Enter temperature in celsius: ")
                    print("Fahrenheit: ", round(celsius_to_fahrenheit(celsius), 2))

        elif choice == "7":
                    ammount = get_number("Enter ammount: ")
                    rate = get_number("Enter exchange rate (target currency per 1 source currency): ")
                    print("Converted amount: ", round(currency_converter(ammount, rate), 2))

        elif choice == "8":
              print ("Thank you for using calculator")
              break

        else:
              print("Invalid choice!, please select between 1 and 8.")

if __name__ == "__main__":
      main()
