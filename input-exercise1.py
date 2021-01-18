#Create a program that asks user for age and name. Print out a message that tells them the year that they will turn 100 years old.

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
current_year = int(2021)
years_to_hundred = 100 - age
year_to_turn_hundred = current_year + years_to_hundred
copy_of_print = int(input("How many copy of print would you like: "))

print(f"You will turn 100 years old in year {year_to_turn_hundred}")

#or you can use ;
# year = str((2021-age)+100)
