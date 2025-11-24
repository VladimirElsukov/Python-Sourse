class Humidifier:
    def __init__(self):
        self.water = 0
        self.last_time = 0

    # реализуем дозаполнение воды по времени
    def add_water(self, time, volume):
        if time > 0:
            # вычисляем время, прошедшее с последнего обновления
            elapsed_time = time - self.last_time
            self.water -= min(elapsed_time, self.water)

        # Обновляем общее количество воды
        self.water += volume
        self.last_time = time

    def final_amount(self):
        return max(0, self.water)


def solve_humidifier(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    humidifier = Humidifier()  # Создаем экземпляр увлажнителя

    for line in lines[1:n + 1]:  # Перебираем строки с данными
        t, v = map(int, line.split())  # Читаем время и объем воды
        humidifier.add_water(t, v)  # Дозаполняем водой

    return str(humidifier.final_amount())  # Возвращаем итоговое количество воды


# Тестирование
test_cases = [
    ("4\n1 3\n3 1\n4 4\n7 1", '3'),
    ("3\n1 8\n10 11\n21 5", '5'),
    ("10\n2 1\n22 10\n26 17\n29 2\n45 20\n47 32\n72 12\n75 1\n81 31\n97 7", '57')
]

for test_input, expected_output in test_cases:
    result = solve_humidifier(test_input)
    print(f'Input:\n{test_input}\nOutput: {result}')
    assert result == expected_output, f'Test failed. Expected output is {expected_output}, but got {result}'
