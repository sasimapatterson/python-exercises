#Write a Python program to convert temperatures to and from celsius, fahrenheit.

celsius = float(input("Please enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
fahrenheit = float(round(fahrenheit,2))

print(celsius, "C is", fahrenheit, "in Fahrenheit\n")

