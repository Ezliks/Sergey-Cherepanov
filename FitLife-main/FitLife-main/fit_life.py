
print("Здравствуйте! Добро пожаловать в помощника по здоровому образу жизни.")

user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? ")) 

print(f"Приятно познакомиться, {user_name} ({user_age} лет.)")

user_weight = float(input("Введите вес (в кг): "))
user_height = float(input("Введите рост (в метрах): "))

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

water_per_kg=30
water_m1=user_weight*water_per_kg
water_1=water_m1/1000

print(f"Индекс массы тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_1:.1f} л. в день")

print ("Расчёт окончен. Будьте здоровы!")