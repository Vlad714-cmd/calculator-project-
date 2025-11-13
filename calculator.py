def add(a, b):
    """Додавання двох чисел"""
    return a + b

def subtract(a, b):
    """Віднімання двох чисел"""
    return a - b

def multiply(a, b):
    """Множення двох чисел"""
    return a * b

def divide(a, b):
    """Ділення двох чисел"""
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"

def power(a, b):
    """Піднесення числа a до степеня b"""
    return a ** b

def modulo(a, b):
    """Остача від ділення (ділення по модулю)"""
    if b != 0:
        return a % b
    else:
        return "Помилка: ділення на нуль!"

print("=== Простий калькулятор ===")
# Оновлено список доступних операцій
AVAILABLE_OPERATIONS = ['+', '-', '*', '/', '**', '%']
print(f"Операції: {', '.join(AVAILABLE_OPERATIONS)}")
print("Для виходу введіть 'exit'")

while True:
    # Запит на введення операції. Включено всі 6 операцій.
    operation = input(f"\nВведіть операцію ({', '.join(AVAILABLE_OPERATIONS)}) або 'exit': ")

    if operation.lower() == 'exit':
        print("До побачення!")
        break # Вихід з циклу

    # Перевірка на коректність операції
    if operation not in AVAILABLE_OPERATIONS:
        print("Невірна операція! Спробуйте ще раз.")
        continue # Повернення на початок циклу

    # Блок обробки вводу чисел та виконання операції
    try:
        # Введення чисел відбувається тільки після перевірки коректності операції
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '**':
            result = power(num1, num2)
        elif operation == '%': # Додана обробка для операції modulo
            result = modulo(num1, num2)
            
        print(f"Результат: {result}")

    except ValueError:
        # Обробка помилки, якщо користувач ввів не число
        print("Помилка: введіть коректні числа!")
    # Після виконання операції або обробки помилки цикл продовжується