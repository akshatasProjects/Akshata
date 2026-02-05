
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


encrypt_decrypt = input("Type 'encode' to Encode and 'decrypt' to Decrypt:\n ").lower()
text = input("Type your message\n").lower()
shift_num = int(input("Type the number to shift:\n"))



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for eachLtr in original_text:
        shifted = alphabet.index(eachLtr) + shift_amount
        shifted = shifted % len(alphabet)
        # print(shifted)
        cipher_text += alphabet[shifted]
        print(cipher_text)

encrypt(text, shift_num)


# % : if we try to forward 2 step ahead of z which is at position 25 it cannot go further and through index out of range error, 
# so if we divide shifted position by the len of list it will continue without giving error.