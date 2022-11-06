def Password(str_1,d,temp):
    if 8<=len(str_1)<=12:
        if str_1.lower() == str_1:
            d.update({'error_1': 'Отсутствуют заглавные буквы'})
        if str_1.upper() == str_1:
            d.update({'error_2': 'Отсутствуют маленькие буквы'})
        for el in str_1:
            if el.isdigit():
                temp+=el
            if el.isalnum()==0 and el not in "*-#":
                d.update({'error_3':'Неправильный символ'})
        if '*' not in str_1 and  '-' not in str_1 and '#' not in str_1:
            d.update({'error_4':'Отсутствие символа'})
        if len(temp)<1:
            d.update({'error_5': 'Отсутствуют цифры'})
        if len(d)>0:
            return d
        else:
            return 'Пароль идеален'
    return "Измените длину пароля!"
print(Password(input("Input password:"),{},''))