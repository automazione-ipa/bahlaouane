def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Inserisci la temperatura in gradi Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C corrispondono a {fahrenheit:.2f}°F")