# не забываем про pip install -r requirements.txt в терминал
from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date


today = date.today()

if __name__ == '__main__':
    print(f'Сегодня {today}')
    calculate_salary()
    get_employees()
