def single_root_words(root_word, *other_words):
    same_words = []  # пустой список


    root_word_lower = root_word.lower() # переводим слова к нижнему регистру для сравнения

    for word in other_words:
        word_lower = word.lower()   # приводим текущее слово к нижнему регистру
        if root_word_lower in word_lower or word_lower in root_word_lower:   # проверяем, есть ли root_word в word или наоборот
            same_words.append(word)  # обавляем слово в список, если есть
    return same_words  


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print('Результат первого списка')
print(result1)
print('Результат второго списка')
print(result2)
