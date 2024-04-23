import pickle
import gzip
import os



user_input = input("Введіть список цілих чисел через пробіл: ")
numbers = [int(x) for x in user_input.split()]

with open("numbers.pkl", "wb") as file:
    pickle.dump(numbers, file)

new_numbers = []
with open("numbers.pkl", "rb") as file:
    new_numbers = pickle.load(file)

print("Дані з файлу:", new_numbers)
# Завдання 2


def load_data():
    try:
        with open("data.pkl", "rb") as file:
            data = pickle.load(file)
            print("Дані успішно завантажено.")
            return data
    except FileNotFoundError:
        print("Файл даних не знайдено. Створення нового порожнього списку.")
        return []
    except Exception as e:
        print(f"Помилка завантаження данних: {e}")
        return []


def save_data(data):
    try:
        with open("data.pkl", "wb") as file:
            pickle.dump(data, file)
            print("Данні успішно збережено.")
    except Exception as e:
        print(f"Помилка збереження данних: {e}")


def add_data(data):
    new_value = int(input("Введіть число для додавання: "))
    data.append(new_value)
    print(f"Число {new_value} успішно додано.")


def delete_data(data):
    if data:
        index = int(input("Введіть індекс значення, яке потрібно видалити: "))
        if 0 <= index < len(data):
            deleted_value = data.pop(index)
            print(f"Число {deleted_value} успішно видалено.")
        else:
            print(f"Недійсний індекс. Будь ласка, введіть число між 0 та {len(data) - 1}.")
    else:
        print("Список порожній. Нічого видаляти.")


def display_data(data):
    if data:
        print("\n--- Data List ---")
        for index, value in enumerate(data):
            print(f"{index + 1}. {value}")
    else:
        print("Список порожній.")


def main():
    data = load_data()

    while True:
        print("\n--- Data Management Menu ---")
        print("1. Завантажити данні")
        print("2. Зберегти данні")
        print("3. Додати данні")
        print("4. Видалити данні")
        print("5. Вивести на екран")
        print("6. Exit")

        choice = input("Введіть вибір: ")

        if choice == "1":
            data = load_data()
        elif choice == "2":
            save_data(data)
        elif choice == "3":
            add_data(data)
        elif choice == "4":
            delete_data(data)
        elif choice == "5":
            display_data(data)
        elif choice == "6:":
            print("Вихід")
            break
        else:
            print("Неправильний вибір, виберіть між 1 та 6.")


if __name__ == "__main__":
    main()
# Завдання 3

def add_user(users, login, password):
    users[login] = password
    print(f"Користувач {login} з паролем {password} доданий.")


def delete_user(users, login):
    if login in users:
        del users[login]
        print(f"Користувач {login} видалений.")
    else:
        print(f"Користувача з логіном {login} не знайдено.")


def search_user(users, login):
    if login in users:
        print(f"Пароль для користувача {login}: {users[login]}")
    else:
        print(f"Користувача з логіном {login} не знайдено.")


def edit_password(users, login, new_password):
    if login in users:
        users[login] = new_password
        print(f"Пароль для користувача {login} змінено на {new_password}.")
    else:
        print(f"Користувача з логіном {login} не знайдено.")


def save_users(users):
    with gzip.open("users.pkl.gz", "wb") as file:
        pickle.dump(users, file)
    print("Дані про користувачів збережені.")


def load_users():
    if os.path.exists("users.pkl.gz"):
        with gzip.open("users.pkl.gz", "rb") as file:
            return pickle.load(file)
    else:
        print("Файл з даними про користувачів не знайдено.")
        return {}


def display_users(users):
    print("Список користувачів:")
    for login, password in users.items():
        print(f"Логін: {login}, Пароль: {password}")


def main():
    users = load_users()

    while True:
        print("\nМеню:")
        print("1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Пошук користувача")
        print("4. Редагування пароля")
        print("5. Зберегти дані")
        print("6. Вивести список користувачів")
        print("0. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            login = input("Введіть логін нового користувача: ")
            password = input("Введіть пароль для нового користувача: ")
            add_user(users, login, password)
        elif choice == "2":
            login = input("Введіть логін користувача, якого потрібно видалити: ")
            delete_user(users, login)
        elif choice == "3":
            login = input("Введіть логін користувача для пошуку: ")
            search_user(users, login)
        elif choice == "4":
            login = input("Введіть логін користувача, для якого потрібно змінити пароль: ")
            new_password = input("Введіть новий пароль: ")
            edit_password(users, login, new_password)
        elif choice == "5":
            save_users(users)
        elif choice == "6":
            display_users(users)
        elif choice == "0":
            break
        else:
            print("Неправильний вибір опції.")


if __name__ == "__main__":
    main()
