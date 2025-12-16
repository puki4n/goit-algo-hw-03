from datetime import datetime
def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою і поточною датою.
    Аргументи:
    date (str): Дата у форматі 'РРРР-ММ-ДД'

    Повертає:
    int: Різниця у днях
    str: Повідомлення про помилку, якщо формат неправильний
    """
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d').date()

        current_day = datetime.today().date()

        difference = current_day - date_object

        return difference.days
    except ValueError:
        return "Неправильний формат дати"
print(get_days_from_today("2025-12-09"))

