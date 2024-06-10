import calendar


def find_day(date):
    # Gün, ay ve yılı almak için tarih
    day, month, year = map(int, date.split('.'))

    # Haftanın gününü almak için calendar.weekday işlevini kullan
    day_of_week = calendar.weekday(year, month, day)

    # Haftanın gününü tamsayı olarak ilgili gün adıyla eşle
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    return days[day_of_week]


# Input date in DD.MM.YYYY format
date_input = input("Enter the date in DD.MM.YYYY format: ")

# Find and print the day of the week
print(find_day(date_input))
