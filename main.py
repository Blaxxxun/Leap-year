year = ""

while year == '':
    try:
        year = int(input("Какой год проверить?\n"))
    except:
        print("Это не число или оно не целое!\n")


def proverka(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if proverka(year) is True:
    print("Год високосный!")
else:
    print("Год не високосный!")
