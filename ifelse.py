# coding: UTF-8
# ↑日本語でコメントを書く時に追加

# variable ageが20歳以上なら、adult.
# 20歳未満ならchild.

age = 16

if age >= 20:
    print("adult")
else:
    print("child")


yourAge = 0

if yourAge >= 20:
    print("adult")
elif yourAge == 0:
    print("baby")
else:
    print("child")

hour = 10

if hour <= 6:
    print('so sleepy')
elif 10 <= hour <= 12:
    print('good morning')
elif hour <= 12 and day_of_week == "sunday" or hour > 20:
    print('Good afternoon')
else:
    print('Hi')
