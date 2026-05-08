attempts = 0
secret = 11

while attempts < 3:
    n = int(input(f"Введи любое число: "))
    if n < secret:
        print(f"Слишком мало.")
    elif n == secret:
        print(f"Угадал!")
    else:
        print(f"Слишком много.")
    attempts += 1
    if n == secret:
        break

if attempts == 3 and n != secret:
    print(f"Не угадал, загадано было {secret}!")