def is_leap(year):
    leap = False
    
    if year%4==0:
      if year%400 is 0:
        return leap
      if year%1000 is 0:
        return False
    return leap

year = int(input())
print(is_leap(year))