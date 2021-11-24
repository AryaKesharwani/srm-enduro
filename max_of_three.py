first = float(input("Enter the first Number :"))
second = float(input("Enter the second Number :"))
third = float(input("Enter the third Number :"))

greatest = 0

if first > second and first > third:
    greatest = first
elif second > first and second > third:
    greatest = second
else:
    greatest = third

print("The greatest number is ", greatest)
