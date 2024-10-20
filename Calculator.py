class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        """Складывает два числа."""
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        """Вычитает второе число из первого."""
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        """Умножает два числа."""
        self.result = x * y
        return self.result

    def divide(self, x, y):
        """Делит первое число на второе, 
        проверяя на деление на ноль."""
        if y == 0:
            raise ValueError
        ("Деление на ноль невозможно.")
        self.result = x / y
        return self.result

    def power(self, x, y):
        """Возводит первое число
          в степень второго."""
        if y < 0 and x == 0:
            raise ValueError
        ("Невозможно возвести 0 в отрицательную степень.")
        self.result = x**y
        return self.result

    def square(self, x):
        """Вычисляет квадрат числа."""
        self.result = x**2
        return self.result

    def square_root(self, x):
        """Вычисляет квадратный корень числа."""
        if x < 0:
            raise ValueError
        ("Невозможно вычислить квадратный корень отрицательного числа.")
        self.result = x**0.5
        return self.result

    def clear(self):
        """Очищает результат калькулятора."""
        self.result = 0
        return "Калькулятор очищен."


def main():
    calc = Calculator()

    while True:
        print("\nКалькулятор Menu:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадрат числа")
        print("7. Квадратный корень числа")
        print("8. Очистить")
        print("9. Выход")

        choice = input("Введите ваш выбор (1-9): ")

        if choice == "9":
            print("Выход...")
            break

        if choice == "8":
            print(calc.clear())
            continue

        if choice not in [str(i) for i in range(1, 10)]:
            print("Ошибка: Неверный ввод. Пожалуйста, выберите номер от 1 до 9.")
            continue

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                x = float(input("Введите первое число: "))
                y = float(input("Введите второе число: "))
            elif choice in ["6", "7"]:
                x = float(input("Введите число: "))
                y = None  # Для методов с одним параметром
            else:
                print("Ошибка: Неверный ввод. Пожалуйста, выберите номер от 1 до 9.")
                continue
        except ValueError:
            print("Ошибка: Введите правильное число.")
            continue

        try:
            if choice == "1":
                result = calc.add(x, y)
                print(f"Результат: {result}")

            elif choice == "2":
                result = calc.subtract(x, y)
                print(f"Результат: {result}")

            elif choice == "3":
                result = calc.multiply(x, y)
                print(f"Результат: {result}")

            elif choice == "4":
                result = calc.divide(x, y)
                print(f"Результат: {result}")

            elif choice == "5":
                result = calc.power(x, y)
                print(f"Результат: {result}")

            elif choice == "6":
                result = calc.square(x)
                print(f"Результат: {result}")

            elif choice == "7":
                result = calc.square_root(x)
                print(f"Результат: {result}")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
