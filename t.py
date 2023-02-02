from translate import Translator
translator= Translator(to_lang="th")

try:
    with open('a.txt',mode='r') as f:
        i = f.read()
        translation = translator.translate(i)
        print(translation)
except FileNotFoundError:
    print('no such file')

print('hi')
print('testing')