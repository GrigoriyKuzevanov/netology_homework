from datetime import date


def take_cur_date():
    print(date.today().strftime('%d.%m.%Y'))
