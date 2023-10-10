year=int(input("Введіть рік"))
if year>1900 and year<1000000:

  if year%4==0 or year%400==0:
        print(year, "високосний рік")
  elif year%100==0:
        print(year, "не є високосним")
  else:
       print(year, "не є високосним")

else:
    print("Помилка. Неправильно введен діапазон.")


