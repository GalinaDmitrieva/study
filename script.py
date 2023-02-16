import json
from files import JSON_FILE_PATH
from csv import DictReader
from files import CSV_FILE_PATH

data = []
list_books = []

with open(JSON_FILE_PATH, 'r') as f:
    users = json.load(f)

with open(CSV_FILE_PATH, newline='') as f:
    csv_reader = DictReader(f)

    for row in csv_reader:
        list_books.append(row)

i = 0
j = 0
for user in users:
    books_internal = []
    i = j
    while i < len(list_books):
        books_internal.append({'title': list_books[i]['Title'],
                               'author': list_books[i]['Author'],
                               'pages': int(list_books[i]['Pages']),
                               'genre': list_books[i]['Genre']
                               })
        data.append({'name': users[j]['name'],
                     'gender': users[j]['gender'],
                     'address': users[j]['address'],
                     'age': users[j]['age'],
                     'books': books_internal})
        i = i + len(users)
    j = j + 1


with open('result.json', 'w') as f:
    f.write(json.dumps(data, indent=4))
