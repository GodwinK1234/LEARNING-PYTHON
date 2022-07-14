Name = input("Enter your name  ")

Age = int(input ("Enter your age  "))

Year = 2020

def get_year() :
    return Year - Age

print("Hello,  " + Name + " you were born in  ", get_year())
