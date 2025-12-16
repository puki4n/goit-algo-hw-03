from random import randint
def get_numbers_ticket(min, max, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотереї

    :param min: Мінімальне можливе число
    :param max: Максимальне можливе число
    :param quantity: Кількість чисел, які потрібно вибрати

    :return:Відсортований список унікальних чисел або пустий список,
          якщо параметри некоректні
    """
    if min < 1 or max > 1000 or quantity >(max-min + 1)or quantity <1:
        return []

    result_array = set()
    while len(result_array) < quantity:
        result_array.add(randint(min, max))
    return sorted(result_array)
my_ticket = get_numbers_ticket(1, 49, 6)

print("Твій Білет: ", my_ticket)





