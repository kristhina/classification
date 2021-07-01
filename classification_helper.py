import pandas as pd

df = pd.read_excel('nieruchomosci.xlsx', engine='openpyxl')

list_okna = ["okna", "plastikowe", "PCV", "Okna", "aluminiowe", "drewniane"]
list_klimatyzacja = ["klimatyzowany", "klimatyzacja", "klimatyzowane", "klimatyzacją", "klimatyzację", "klimatyzowana", "Klimatyzacja", "klimatyzacji", "klimatyzacje"]
list_kuchnia = ["kuchnia", "aneks", "kuchenny", "aneksem", "otwarta", "kuchni", "kuchnią", "Kuchnia", "Aneks", "odrębna", "Kuchni"]


def bold_word(text: str, list_of_words: list, color: str) -> str:
    "changes the words selected in the list_of_words into bolded and coloured ones"
    new_text = text
    for word in list_of_words:
        if word in new_text:
            new_text = new_text.replace(word, '<strong> <span style="color:{};">'.format(color) + word + '</span> </strong>')
    return new_text

