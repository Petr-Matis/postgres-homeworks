"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os


def read_file(filename):
    """Функция чтения данных из файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = []
        for line in file.readlines():
            if filename.endswith('orders_data.csv'):
                data.append(line[:-1].replace('"', '').split(','))
            else:
                data.append(line[:-1].replace('"', '').replace(', ', ' ').split(','))
        return data


def main():
    """Функция коннектор-курсор"""
    with psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password=input("Введите пароль для подключение к БД: "),
    ) as connector:

        with connector.cursor() as cursor:
            url = os.path.join("north_data", 'customers_data.csv')
            file = read_file(url)
            for number in range(1, len(file)):
                print(tuple(file[number]))
                cursor.execute('INSERT INTO customers VALUES (%s, %s, %s)', tuple(file[number]))

            url = os.path.join("north_data", 'employees_data.csv')
            file = read_file(url)
            for number in range(1, len(file)):
                print(tuple(file[number]))
                cursor.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (number,) + tuple(file[number]))

            url = os.path.join("north_data", 'orders_data.csv')
            file = read_file(url)
            for number in range(1, len(file)):
                print(tuple(file[number]))
                cursor.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', tuple(file[number]))

    connector.close()


if __name__ == "__main__":
    main()
