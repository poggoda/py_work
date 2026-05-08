age = int(input(f"Введите любое число: "))
number = 1

while number: 
    print(f"{age} * {number} = {age * number}")
    number += 1
    if number == 11:
        break


# аналог
# n = int(input("Введите любое число: "))
# for i in range(1, 11):
#   print(f"{n} x {i} = {n * i}")