import Characters
import clipboard
import pyperclip
Translated = ''
mode = 'encrypt'
print('What is the message you want to encrypt?')
message=input()
print('What is the key you want to encrypt your message in?')
Key = input()
B = int(Key)

for symbol in message:

    if symbol in Characters.LETTERS:
        num = Characters.LETTERS.find(symbol)

        if mode == 'encrypt':
            num = num + B

        if num >= len(Characters.LETTERS):
            num = num - len(Characters.LETTERS)

        elif num < 0:
            num = num + len(Characters.LETTERS)
        Translated = Translated + Characters.LETTERS[num]

    else:
        Translated = Translated + symbol
input('Your encrypted message is: \n' + Translated + '\nPress enter to exit')
pyperclip.copy(Translated)
