from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    #today = date(year=2023, month=12, day=30)
    today = date.today()

    start_of_week = today + timedelta(days=-2) if today.weekday() == 0 else today
    end_of_week = start_of_week + timedelta(days=6)

    weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    result_dict = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    for user in users:
        if today.day == 1 and today.month == 1 and today.weekday() == 0:
            birthday_year = today.year - 1 if user['birthday'].month == 12 else today.year
        else:
            birthday_year = today.year if user['birthday'].month > 1 or (user['birthday'].month == 1 and user['birthday'].day >= today.day) else today.year + 1
        birthday_this_year = user['birthday'].replace(year=birthday_year)

        if start_of_week <= birthday_this_year <= end_of_week:
            weekday_index = birthday_this_year.weekday()
            weekday = 'Monday' if weekday_index >= 5 else weekday_list[weekday_index]
            result_dict[weekday].append(user['name'])

    result_dict_2 = {}
    for key, value in result_dict.items():
        if result_dict[key] != []:
            result_dict_2[key] = value

    return result_dict_2



if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")




