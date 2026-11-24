def get_name():
    """Запрашивает имя пользователя."""
    while True:
        user_name = input('Введите ваше имя: ').strip()
        clean_user_name = user_name.replace('-', '').replace(" ", "")
        if not user_name:
            print('Имя не может быть пустым')
        elif not clean_user_name.isalpha():
            print('Имя может содержать только буквы')
        else:
            return user_name


def get_age():
    """Запрашивает возраст."""
    while True:
        try:
            age = int(input('Введите ваш возраст: '))
        except ValueError:
            print("Введите целое число.")
            continue
        if validate_data(age, MIN_AGE, MAX_AGE):
            return age


def get_weight():
    """Запрашивает вес."""
    while True:
        try:
            weight = float(input("Введите ваш вес" '(в кг): ')
                           .replace(',', '.'))
        except ValueError:
            print("Введите число.")
            continue
        if validate_data(weight, MIN_WEIGHT, MAX_WEIGHT):
            return weight


def get_height():
    """Запрос роста."""
    while True:
        try:
            height = float(input("Введите ваш рост"
                                 '(в метрах, например 1.75): ')
                           .replace(',', '.'))
        except ValueError:
            print("Введите число.")
        if validate_data(height, MIN_HEIGHT, MAX_HEIGHT):
            return height


def validate_data(value, min_value, max_value):
    """Проверка диапозона."""
    if value <= min_value:
        print("Значение не может быть отрицательным.")
        return False
    elif value > max_value:
        print("Введено слишком большое значение.")
        return False
    return True


def bmi_category(bmi: float) -> str:
    """Проверка категории ИМП."""
    if bmi < 16:
        return "Выраженный дефицит массы тела."
    elif bmi < 18.5:
        return "Недостаточная масса тела."
    elif bmi < 25:
        return "Норма."
    elif bmi < 30:
        return "Избыточная масса тела (предожирение)."
    elif bmi < 35:
        return "Ожирение 1-й степени."
    elif bmi < 40:
        return "Ожирение 2-й степени."
    else:
        return "Ожирение 3-й степени."


MIN_WEIGHT = 0
MAX_WEIGHT = 635

MIN_HEIGHT = 0
MAX_HEIGHT = 3

MIN_AGE = 0
MAX_AGE = 100

WATER_PER_KG = 30

print("Здраствуйте, вас приветствует FitLify-трекер.")
print("Мне нужно собрать базовую информацию о вас.")


user_name = get_name()
user_age = get_age()
user_weight = get_weight()
user_height = get_height()

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

water_ml = user_weight * WATER_PER_KG
water_l = water_ml / 1000
water_l = round(water_l, 2)

print(f"""
Пользователь: {user_name}
Возраст: {user_age}
Индекс массы тела: {bmi} — {bmi_category(bmi)}
Рекомендуемая норма воды: {water_l} л. в день""")
print("Расчёт окончен. Будьте здоровы!")
