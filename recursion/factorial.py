def fac(n: int):
    assert n >= 0, 'Факториал отрицательный. Не определен'  # условие ввода данных и описание ошибки
    if n == 0:
        return 1
    return fac(n - 1) * n

print(fac(5))