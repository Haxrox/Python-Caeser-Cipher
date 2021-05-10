import Characters
import pyperclip
Translated = ''
mode = 'decrypt'
print('What is the message you want to decrypt')
message=input()
print('What is the key you want to decrypt your message in?')
Key = input()
B = int(Key)
for symbol in message:

    if symbol in Characters.LETTERS:
        num = Characters.LETTERS.find(symbol)

        if mode == 'decrypt':
            num = num - B

        if num >= len(Characters.LETTERS):
            num = num - len(Characters.LETTERS)

        elif num < 0:
            num = num + len(Characters.LETTERS)
        Translated = Translated + Characters.LETTERS[num]

    else:
        Translated = Translated + symbol
input('Your decrypted message is: \n' + Translated + '\nPress enter to exit')
pyperclip.copy(Translated)
