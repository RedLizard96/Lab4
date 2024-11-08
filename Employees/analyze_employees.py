import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Функція для розрахунку віку на основі дати народження
def calculate_age(birth_date):
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Функція для зчитування даних із CSV файлу
def read_csv(file_name):
    employees = []
    try:
        with open(file_name, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаємо заголовки
            for row in reader:
                birth_date = datetime.strptime(row[4], '%Y-%m-%d')  # Дата народження у форматі 'рррр-мм-дд'
                age = calculate_age(birth_date)
                employees.append({
                    'Стать': row[3],
                    'Вік': age
                })
        print("Ok: CSV файл успішно відкрито.")
    except FileNotFoundError:
        print("Помилка: CSV файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None
    return employees

# Функція для підрахунку кількості співробітників за статтю
def count_by_gender(employees):
    male = sum(1 for emp in employees if emp['Стать'] == 'чоловіча')
    female = sum(1 for emp in employees if emp['Стать'] == 'жіноча')
    return male, female

# Функція для підрахунку кількості співробітників за віковими категоріями
def count_by_age_category(employees):
    age_categories = {
        'younger_18': 0,
        '18-45': 0,
        '45-70': 0,
        'older_70': 0
    }
    for emp in employees:
        age = emp['Вік']
        if age < 18:
            age_categories['younger_18'] += 1
        elif 18 <= age <= 45:
            age_categories['18-45'] += 1
        elif 45 <= age <= 70:
            age_categories['45-70'] += 1
        else:
            age_categories['older_70'] += 1
    return age_categories

# Функція для побудови кругової діаграми
def plot_pie_chart(labels, data, title):
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Забезпечує круглу форму діаграми
    plt.show()

# Функція для побудови стовпчастої діаграми
def plot_bar_chart(labels, data, title):
    plt.figure(figsize=(8, 6))
    plt.bar(labels, data, color=['red', 'blue', 'purple', 'green'])
    plt.title(title)
    plt.xlabel('Категорії')
    plt.ylabel('Кількість співробітників')
    plt.show()

# Основна функція
def main():
    file_name = 'employees.csv'
    employees = read_csv(file_name)

    if employees is None:
        return

    # Підрахунок кількості співробітників за статтю
    male, female = count_by_gender(employees)
    print(f"Чоловіків: {male}, Жінок: {female}")
    plot_pie_chart(['Чоловіки', 'Жінки'], [male, female], 'Розподіл за статтю')

    # Підрахунок кількості співробітників за віковими категоріями
    age_categories = count_by_age_category(employees)
    print("Розподіл співробітників за віковими категоріями:")
    for category, count in age_categories.items():
        print(f"{category}: {count}")

    plot_bar_chart(age_categories.keys(), age_categories.values(), 'Розподіл за віковими категоріями')

    # Підрахунок співробітників за віковими категоріями та статтю
    male_categories = {key: 0 for key in age_categories}
    female_categories = {key: 0 for key in age_categories}

    for emp in employees:
        age = emp['Вік']
        gender = emp['Стать']
        if age < 18:
            if gender == 'чоловіча':
                male_categories['younger_18'] += 1
            else:
                female_categories['younger_18'] += 1
        elif 18 <= age <= 45:
            if gender == 'чоловіча':
                male_categories['18-45'] += 1
            else:
                female_categories['18-45'] += 1
        elif 45 <= age <= 70:
            if gender == 'чоловіча':
                male_categories['45-70'] += 1
            else:
                female_categories['45-70'] += 1
        else:
            if gender == 'чоловіча':
                male_categories['older_70'] += 1
            else:
                female_categories['older_70'] += 1

    # Побудова діаграм для кожної вікової категорії за статтю
    plot_bar_chart(male_categories.keys(), male_categories.values(), 'Чоловіки за віковими категоріями')
    plot_bar_chart(female_categories.keys(), female_categories.values(), 'Жінки за віковими категоріями')

# Запуск основної функції
if __name__ == '__main__':
    main()
