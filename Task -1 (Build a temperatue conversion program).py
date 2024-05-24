def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return f"{value}°C is {fahrenheit}°F and {kelvin}K"
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return f"{value}°F is {celsius}°C and {kelvin}K"
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return f"{value}K is {celsius}°C and {fahrenheit}°F"
    else:
        return "Invalid unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin."

def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
        result = convert_temperature(value, unit)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")

if __name__ == "__main__":
    main()
