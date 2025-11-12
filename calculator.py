def add(a, b):
    """Повертає суму двох чисел."""
    return a + b

def subtract(a, b):
    """Повертає різницю двох чисел."""
    return a - b

def multiply(a, b):
    """Повертає добуток двох чисел."""
    return a * b

def divide(a, b):
    """Повертає частку двох чисел. Обробляє ділення на нуль."""
    if b != 0:
        return a / b
    else:
        # Повертаємо повідомлення про помилку замість виконання операції
        return "Помилка: Ділення на нуль!"

def calculator_app():
    """Основна функція, яка запускає інтерфейс калькулятора."""
    print("=== Простий Калькулятор ===")
    print("Доступні операції: +, -, *, /")
    print("Щоб вийти, введіть 'exit'")

    while True:
        # Запит операції
        operation = input("\nВведіть операцію (+, -, *, /) або 'exit': ")

        # 1. Обробка команди 'exit'
        if operation.lower() == 'exit':
            print("Дякую за використання!")
            break

        # 2. Перевірка на коректність операції
        if operation not in ['+', '-', '*', '/']:
            print("Невідома операція! Спробуйте ще раз.")
            continue

        try:
            # 3. Запит чисел
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))

            # 4. Виконання операції
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                # Функція divide сама обробляє ділення на нуль
                result = divide(num1, num2)

            # 5. Виведення результату
            print(f"Результат: {result}")

        except ValueError:
            # Обробка випадку, коли користувач ввів нечислові дані
            print("Помилка: Введіть коректне число!")
        except Exception as e:
            # Обробка інших неочікуваних помилок
            print(f"Неочікувана помилка: {e}")

# Виконання коду, якщо файл запускається безпосередньо
if __name__ == "__main__":
    calculator_app()
