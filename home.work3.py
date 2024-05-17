while True:
    word = input("Введите слово на латинице или кириллице (для выхода введите 'exit'): ")
    if word.lower() == 'exit':
        break

    vowels = 'aeiouаеёиоуыэюя'
    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

    word_lower = word.lower()
    total_letters = len(word)
    vowel_count = sum(1 for letter in word_lower if letter in vowels)
    consonant_count = sum(1 for letter in word_lower if letter in consonants)

    print(f"Слово: {word}")
    print(f"Количество: {total_letters}")
    print(f"Согласных букв: {consonant_count}")
    print(f"Гласных букв: {vowel_count}")

    if total_letters != 0:
        vowel_percentage = (vowel_count / total_letters) * 100
        consonant_percentage = (consonant_count / total_letters) * 100
        print(f"Гласные/согласные: {vowel_percentage:.2f}% / {consonant_percentage:.2f}%")
    else:
        print("Слово не содержит букв.")