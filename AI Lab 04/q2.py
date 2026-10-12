def convert_temperature(value, to_unit="Fahrenheit"):
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15


temp = float(input("\nEnter temperature in Celsius: "))

print(f"{temp}C in Fahrenheit (default): {convert_temperature(temp)}")
print(f"{temp}C in Kelvin: {convert_temperature(temp, 'Kelvin')}")
print(f"100C in Kelvin: {convert_temperature(value=100, to_unit='Kelvin')}")