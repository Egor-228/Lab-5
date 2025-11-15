import re
import csv

# 1 task: Все слова, начинающиеся с большой буквы; все слова, после которых стоит двоеточие.

f = open(r'lab_5\task1-en.txt', 'r')
s = f.read()
f.close()

upper_letter = re.findall(r"[A-Z]\w*", s) #Все слова, начинающиеся с большой буквы

double_dot = re.findall(r"\w+:", s) #Все слова, после которых стоит двоеточие


# task 2: Все закрывающие теги без повторений.

with open(r'lab_5\task2.html', 'r', encoding='utf-8') as f:
    s = f.read()

closing_tags = re.findall(r'</.+?>', s) # Все закрывающие теги без повторений\

# task 3

f = open(r'lab_5\task3.txt', 'r')
s = f.read()
f.close()

#id = re.findall(r' (\d+) ',s)

email = re.findall(r'\w+@\w+.\w+',s)

id = [i for i in range(1,len(email)+1)]

surname = re.findall(r'[A-Z][a-z]+',s)

date = re.findall(r'\d\d\d\d-\d\d-\d\d',s)

website = re.findall(r'\w+://.+?/',s)

data = []

for i in range(len(id)):
    data.append([id[i], website[i], date[i], surname[i], email[i]])

with open(r'lab_5\data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# task_add

f = open(r'lab_5\task_add.txt', 'r')
s = f.read()
f.close()

date = re.findall(r'\d{1,4}[-/.]\d{1,4}[-/.]\d{1,4}',s)

email = re.findall(r'\w+@\w+.(?:ru|org|com)',s)

website = re.findall(r'\w+://.+?/',s)

print(website)
