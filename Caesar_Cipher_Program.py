import pyperclip
def Caesar_Cipher_Program():
    print('Do you want to encrypt or decrypt a message?')
    a=input()
    if a=='Encrypt':
        import Encrypting
    elif a=='encrypt':
        import Encrypting
    elif a=='Decrypt':
        import Decrypting
    elif a=='decrypt':
        import Decrypting
    else:
        Caesar_Cipher_Program()
Caesar_Cipher_Program()
   

    
