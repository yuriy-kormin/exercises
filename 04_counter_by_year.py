#!/usr/bin/env python3
from datetime import date
from collections import Counter

def name(list_users):
    list_year = []
    for element in list_users:
        list_year.append(date.fromisoformat(element['birthday']).year)
    print (list_year)
    return dict(Counter(list_year))


users = [
{'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
{'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
{'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
{'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
{'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
{'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
{'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
{'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
{'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
{'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]

print(name(users))