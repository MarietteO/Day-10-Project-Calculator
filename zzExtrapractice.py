#Find leap year

def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
if is_leap_year(2024):
     print("True")
else:
    print("False")

# ***
# Simplified:

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) #(I.e. it IS divisible by 100,
                                                                  #but also 400, therefore True. %400=0 implies %100=0 by definition.)

print(is_leap_year(2024))
