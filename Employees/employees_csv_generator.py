import csv
from faker import Faker
import random

# Ініціалізуємо Faker з українською локалізацією
fake = Faker('uk_UA')

# Словники для по батькові
male_patronymics = [
    'Олександрович', 'Іванович', 'Сергійович', 'Андрійович', 'Дмитрович',
    'Вікторович', 'Юрійович', 'Миколайович', 'Олегович', 'Павлович',
    'Геннадійович', 'Петрович', 'Леонідович', 'Михайлович', 'Васильович',
    'Артемович', 'Максимович', 'Федорович', 'Ігоревич', 'Романович'
]

female_patronymics = [
    'Олександрівна', 'Іванівна', 'Сергіївна', 'Андріївна', 'Дмитрівна',
    'Вікторівна', 'Юріївна', 'Миколаївна', 'Олегівна', 'Павлівна',
    'Геннадіївна', 'Петрівна', 'Леонідівна', 'Михайлівна', 'Василівна',
    'Артемівна', 'Максимівна', 'Федорівна', 'Ігорівна', 'Романівна'
]

# Створюємо CSV файл та записуємо заголовки
with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

    # Генеруємо 2000 записів, 60% чоловічої і 40% жіночої статі
    for _ in range(2000):
        gender = random.choices(['чоловіча', 'жіноча'], weights=[60, 40])[0]
        
        if gender == 'чоловіча':
            first_name = fake.first_name_male()
            patronymic = random.choice(male_patronymics)
        else:
            first_name = fake.first_name_female()
            patronymic = random.choice(female_patronymics)

        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)  # Дата народження від 1938 до 2008 року
        position = fake.job()
        city = fake.city()
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()

        # Записуємо кожен рядок у файл
        writer.writerow([last_name, first_name, patronymic, gender, birth_date, position, city, address, phone, email])

print("CSV файл з записами успішно створено!")


