alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def count_letters(text):
    letters = 0
    for i in range(len(text)):
        if text[i] != '!' and text[i] != '.' and text[i] != '\'' and text[i] != '?' and text[i] != ' ' and text[i] != ',':
            letters += 1
    return letters


def count_words(text):
    words = text.split()
    return len(words)


def count_sentences(text):
    sentences = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == '!':
            sentences += 1
    return sentences


text = input("Text: ")
letters = int(count_letters(text))
words = int(count_words(text))
sentences = int(count_sentences(text))

index = round((0.0588 * ((letters/words) * 100)) - (0.296 * ((sentences/words) * 100)) - 15.8)

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
