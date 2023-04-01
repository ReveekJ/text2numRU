from fuzzywuzzy import fuzz

units = (
    u'ноль', u'один', u'два',
    u'три', u'четыре', u'пять',
    u'шесть', u'семь', u'восемь', u'девять'
)
teens = (
    u'десять', u'одиннадцать',
    u'двенадцать', u'тринадцать',
    u'четырнадцать', u'пятнадцать',
    u'шестнадцать', u'семнадцать',
    u'восемнадцать', u'девятнадцать'
)

tens = (
    u'двадцать', u'тридцать',
    u'сорок', u'пятьдесят',
    u'шестьдесят', u'семьдесят',
    u'восемьдесят', u'девяносто'
)

hundreds = (
    u'сто', u'двести',
    u'триста', u'четыреста',
    u'пятьсот', u'шестьсот',
    u'семьсот', u'восемьсот',
    u'девятьсот'
)
everybody = (units, teens, tens, hundreds)

units_num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
teens_num = ('10', '11', '12', '13', '14', '15', '16', '17', '18', '19')
tens_num = ('20', '30', '40', '50', '60', '70', '80', '90')
hundreds_num = ('100', '200', '300', '400', '500', '600', '700', '800', '900')
everybody_num = (units_num, teens_num, tens_num, hundreds_num)


def text2num(text: str):
    text = text.lower()
    # список содержащий кортежи с данными
    p = []
    for k in text.split():
        # наилучший процент совпадения
        best_num = 70
        # индекс кортежа
        path_big = 0
        # индекс элемента кортежа
        path_small = 0
        for elem in everybody:
            for i in elem:
                if fuzz.ratio(k, i) > best_num:
                    best_num = fuzz.ratio(k, i)
                    path_big = everybody.index(elem)
                    path_small = elem.index(i)
                    # TODO: сделать оптимизацию
                    # if best_num == 100:
                    #     f = True
                    #     break
        # if f:
        #     p.append((path_big, path_small))
        #     break
        p.append((path_big, path_small))
    res = []

    for i in p:
        res.append(int(everybody_num[i[0]][i[1]]))

    return sum(res)

# print(text2num('девятьсот девяносто девять'))
# вывод: 999
