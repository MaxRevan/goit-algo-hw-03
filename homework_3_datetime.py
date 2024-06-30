from datetime import datetime


def get_days_from_today(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        delta_days = format_date - date_today
        return (delta_days).days
    except ValueError:
        return "Не вірний формат дати. Введіть дату у форматі 'YYYY-MM-DD."


date_str = "1985-05-09"
delta = get_days_from_today(date_str)
print(f"Різниця між {date_str} до поточної дати складає: {delta}")


#print(get_days_from_today("2021-08-09"))