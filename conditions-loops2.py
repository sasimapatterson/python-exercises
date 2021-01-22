#Write a Python program to convert temperatures to and from celsius, fahrenheit.

user_temp = input("Please enter the temperature you want to convert (e.g., 72F, 24C): ").upper()
degree = int(user_temp[:-1])
to_convert = user_temp[-1]

#to_fahrenheit = (celsius * 1.8) + 32
#to_celsius = (fahrenheit - 32) * .5556

if to_convert == "C":
    result = float(round((degree * 1.8) + 32))
    temp_unit = "Fahrenheit"

elif to_convert == "F":
    
    result = float(round((degree - 32) * .5556))
    temp_unit = "Celsius"
    
else:
    print("Input invalid.")
    quit()
     
print("The temperature in", temp_unit, "is", result, "degree.")
