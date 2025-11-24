'''
Время работы алгоритма оценивается как O(m+klogk), где m — длина первого числа,
k — второго, что делает алгоритм эффективным и близким к линейному.
'''

def maximize_number(A, B):
    digits_A = list(map(int, A))  # Создаем список. Разбираем A на отдельные цифры
    digits_B = sorted([int(i) for i in B], reverse=True)  # Доступные цифры из B, отсортированы по убыванию
    used = set()  # Отмечаем использованные цифры из B

    result = []  # Результирующая строка

    for digit in digits_A:
        found = False
        # Проверяем возможные замены для текущей позиции
        for b_digit in digits_B:
            if b_digit > digit and b_digit not in used:
                # Нашли лучшую цифру из B, которую можно вставить
                result.append(str(b_digit))
                used.add(b_digit)  # Использованная цифра помечается
                found = True
                break
        if not found:
            # Нет подходящей цифры, сохраняем оригинальную
            result.append(str(digit))

    return ''.join(result) # Возвращаем результат в виде строки

# Тестирование
print(maximize_number("123456", "987"))  # Output: "987456"
print(maximize_number("111", "99"))  # Output: "991"
print(maximize_number("555", "639"))  # Output: "965"