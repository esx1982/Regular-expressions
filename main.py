from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

pattern = r"(\+7|8)?\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s?)\(?(доб.)?\s?(\d+)?\)?"
sub = r"+7(\2)\3-\4-\5\6\7\8"
pattern2 = r"([А-Я][Ёа-яё]+)[\s\,]?([А-Я][Ёа-яё]+)[\s]?([А-ЯЁа-яё]+)?"
sub2 = r"\1 \2 \3"

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)
    # pprint(contacts_list[1])
for i in contacts_list:
    result = re.sub(pattern, sub, i[5])
    i[5] = result
    text = i[0]+' '+i[1]+' '+i[2] + ','
    result1 = re.sub(pattern2, sub2, text)
    i[0] = result1.split()[0]
    i[1] = result1.split()[1]
    i[2] = result1.split()[2].replace(',', '')
for a in contacts_list:
    for i in contacts_list:
        if a[0] == i[0] and a[1] == i[1]:
            if a[0] == i[0] and a[1] == i[1] and a[4] != i[4]:
                a[4] = i[4]
            elif a[0] == i[0] and a[1] == i[1] and a[6] != i[6]:
                a[6] = i[6]
exam = []
for i in contacts_list:
    for b in contacts_list:
        if i == b:
            if i[0] == b[0] and i[1] == b[1] and i[2] != '':
                if i[5] != '' or i[6] != '':
                    exam.append(i)

# print(contacts_list)
print(exam, len(exam))

# 1. Выполните пункты 1-3 задания.
# Ваш код

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(exam)