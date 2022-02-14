alphabet_str = 'abcdefghijklmnopqrstuvwxyz'     # список букв алфавита
punkt_str = ',.''"";:-()!?“”\n'                 # список знаков препинания
itog_dict = {}                                  # пустой словарь


def analyse_of_word(x):
    x = x.lower()                               # приведение к нижнему регистру

    for i in punkt_str:
        x = x.replace(i, '')                    # удаление всех знаков препинания из списка punkt_str

    x = x.split()                               # разбиение текста на отдельные слова

    for z in alphabet_str:
        itog_dict[z] = 0                        # создание ключей для словаря из букв алфавита с нулевыми значениями

    print(x)                                    # вывод списка слов

    for j in x:
        t = itog_dict.get(j[0], 0)              # подсчет количества слов в тексте, начинающихся на определённую букву
        itog_dict[j[0]] = t + 1                 # алфавита


    return itog_dict                            # возвращение результата


print(analyse_of_word(
    'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing'
    ' to do: once or twice she had peeped into the book her sister was reading, but it had no pictures'
    ' or conversations in it, “and what is the use of a book,” thought Alice “without pictures or'
    ' conversations?” So she was considering in her own mind (as well as she could, for the hot day '
    'made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be '
    'worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink '
    'eyes ran close by her.')
    )
