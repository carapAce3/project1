with open('LMAO.txt', 'r', encoding='utf-8') as f:
    f = f.read()
    print(f)
a = input('Ви хотіли б добавити новий текст?(відповісти "так" або "ні"): ')
while a != 'ні':
    b = input('Введіть, що ви хочете додати: ')
    with open('LMAO.txt', 'a', encoding='utf-8') as f:
        f.write(b)
    with open('LMAO.txt', 'r', encoding='utf-8') as f:
        f = f.read()
        print(f)
    a = input('Ви хотіли б добавити новий текст?(відповісти "так" або "ні"): ')