temp = int(input("Какая температура за окном? "))

if temp <= 0: 
    print(f"Одевайся теплее, мороз!")

elif temp >= 0 and temp <= 20: #альтернатива: elif 0 < temp <= 20:
    print(f"Возьми куртку")

else:
    print(f"Можно в футболке")