""" Write a Python program to convert temperatures to and from celsius, fahrenheit. """


def celsius_to_fahrenheit(degree):
    return round((9 * degree) / 5 + 32)
    

def fahrenheit_to_celsius(degree):
    return round((degree - 32) * 5 / 9)

temp = input("Input the  temperature you like to convert?  : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(celsius_to_fahrenheit(degree=degree))
  o_convention = "Fahrenheit"
  print("The temperature in", o_convention, "is", result, "degrees.")
elif i_convention.upper() == "F":
  result = int(fahrenheit_to_celsius(degree=degree))
  o_convention = "Celsius"
  print("The temperature in", o_convention, "is", result, "degrees.")
else:
  print("Input proper convention.")

