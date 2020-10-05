import csv
import re

with open('steam_description_data.csv', encoding='utf-8') as f:
    f_reader = csv.reader(f)

    all_symbols = 0
    spaces = 0
    dots = 0
    commas = 0
    exclMarks = 0
    qMarks = 0
    dashes = 0
    colons = 0
    semicolons = 0
    slashes = 0
    left = 0
    right = 0
    words = 0

    for row in f_reader:
        line = ','.join(row)
        all_symbols += len(line)
        spaces += line.count(' ')
        dots += line.count('.')
        commas += line.count(',')
        exclMarks += line.count('!')
        qMarks += line.count('?')
        dashes += line.count('-')
        colons += line.count(':')
        semicolons += line.count(';')
        slashes += line.count('/')
        left += line.count('(')
        right += line.count(')')
        words += len(re.findall(r"(\w+'\w+)|(w+-\w+'\w+)|(w+-\w+'\w)|\w+", line))

without_spaces = all_symbols - spaces
without_punk = all_symbols - dots - commas - exclMarks - qMarks - dashes - colons - semicolons - slashes - left - right
sentences = dots + exclMarks + qMarks

print('Общее количество символов:', all_symbols)
print('Общее количество символов без пробелов:', without_spaces)
print('Количество символов без знаков препинания:', without_punk)
print('Количество слов:', words)
print('Количество предложений:', sentences)
