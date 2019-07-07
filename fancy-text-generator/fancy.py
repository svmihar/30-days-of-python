#! .venv/bin/python
import string
import os
import argparse

p = argparse.ArgumentParser()
p.add_argument('-a', action='store', nargs='+')

fancy = '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ'

fancy_dict = {}
for i, char in enumerate(fancy):
    fancy_dict[i] = char

normal_dict = {}
for i, char in enumerate(string.ascii_letters):
    normal_dict[char] = i


def fancy_generator(text):
    uhuy = []
    if type(text) is list:
        for word in text:
            hasil_word = []
            for char in list(word):
                if char.isalpha():
                    hasil_word.append(fancy_dict.get(normal_dict.get(char)))
                else:
                    print(f'{char} belum support')
                    hasil_word.append(char)
                    continue
            uhuy.append(''.join(hasil_word))
    else:
        for word in text.split():
            hasil_word = []
            for char in list(word):
                if char.isalpha():
                    hasil_word.append(fancy_dict.get(normal_dict.get(char)))
                else:
                    print(f'{char} belum support')
                    continue
            uhuy.append(''.join(hasil_word))
    os.system(f"echo '{' '.join(uhuy)}' | pbcopy")
    return ' '.join(uhuy)


if __name__ == "__main__":
    args = p.parse_args()
    hasil = vars(args)['a']
    print(fancy_generator(hasil))
