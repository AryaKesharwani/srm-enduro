"""Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included """


def listToString(s):     
    str1 = " \n"   
    return (str1.join(s))
        


if __name__ == "__main__":
    numbers = []
    for x in range(1500, 2701):
        if (x % 7 == 0) and (x % 5 == 0):
            numbers.append(str(x))
    print(listToString(numbers))