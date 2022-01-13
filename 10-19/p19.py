#!usr/bin/env python3

# Counts how many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)
def countSundays():
    year = 1901
    day = 3 # Tuesday
    total = 0

    while year <= 2000:
        month = 1
        while month < 13:
            # Add the day
            if day == 1:
                total += 1
            # Change the month
            if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
                day += 2
            elif month == 2:
                if year % 100 == 0 and year % 400 == 0:
                    day += 1
                elif year % 4 == 0:
                    day += 1
            else:
                day += 3
            if day > 7:
                day -= 7
            month += 1
        year += 1

    return total

if __name__ == "__main__":
    print(countSundays())