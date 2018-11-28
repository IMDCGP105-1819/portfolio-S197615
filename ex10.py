low_number = input("Enter a number: ")
high_number = input("Enter a number greater than " + low_number + ": ")
new_number = low_number

while int(new_number) <= int(high_number):
    if int(new_number) % 3 == 0 and int(new_number) % 5 == 0:
        print(str(new_number) + "FizzBuzz")
        new_number = int(new_number) + 1
    elif int(new_number) % 3 == 0:
        print(str(new_number) + "Fizz")
        new_number = int(new_number) + 1
    elif int(new_number) % 5 == 0:
        print(str(new_number) + "Buzz")
        new_number = int(new_number) + 1
    else:
        new_number = int(new_number) + 1
