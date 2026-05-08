cities = ["Москва","СПб","Екб","Нкс","Казань"]

print(cities[0])
print(cities[-1])

cities.append("Орел")

for i, city in enumerate(cities, start=1):
    print(f"Город: {i}. {city}")

#i = 1 
#for city in cities:
#     print(f"Город: №{i} {city}")
#     i += 1