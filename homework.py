text_from_file = open("text.txt", "r", encoding="UTF-8")
text_in_program = text_from_file.read()
text_from_file.close()

# 1) методами строк очистить текст от знаков препинания
punctuation_mark = ".,!?-;«»:—"
for i in punctuation_mark:
    text_in_program = text_in_program.replace(i, "")
# print(text_in_program)

# 2) сформировать list со словами (split)
text_in_program_split = text_in_program.split()
# print(text_in_program_split)

# 3.1) привести все слова к нижнему регистру (map)
text_in_program_lower = list(map(lambda x: x.lower(), text_in_program_split))
# print(text_in_program_lower)

# 3.2) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте
text_dictionary = {}

for keys in text_in_program_lower:
    text_dictionary[keys] = text_dictionary.get(keys, 0) + 1
# print(text_dictionary)

# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)
text_dictionary_list = list(text_dictionary.items())
text_dictionary_list.sort(key=lambda x: x[1], reverse=True)
# print(text_dictionary_list[:5])
# print("Количество уникальных слов:", len(set(text_in_program_lower)))

# 5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
lemmatization = []
for i in text_in_program_lower:
    lemmatization.append(morph.parse(i)[0].normal_form)
# print(lemmatization)
