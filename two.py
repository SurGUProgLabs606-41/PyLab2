def calculate_expression():
    # Вычисляем значение выражения
    value = 216 * 6 + 216 * 4 + 36 * 6 - 6 * 14 - 24

    # Переводим значение в систему счисления с основанием 6
    def to_base_6(n):
        digits = []
        while n:
            digits.append(n % 6)
            n //= 6
        return digits[::-1]

    base_6_digits = to_base_6(value)
    # Подсчитываем количество различных цифр
    unique_digits = set(base_6_digits)
    return len(unique_digits)


print(calculate_expression())