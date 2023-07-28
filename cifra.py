import sys
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ROT = 13

def cipher(mensagem, dir):
    m = ''
    for c in mensagem:
        if c in ALPHABET:
            c_index = ALPHABET.index(c)
            m += ALPHABET[(c_index + (dir * ROT)) % len(ALPHABET)]
        else:
            m += c
    return m

def encrypt(mensagem):
    return cipher(mensagem, 1)

def decrypt(mensagem):
    return cipher(mensagem, -1)

def main():
    command = sys.argv[1].lower()
    mensagem = sys.argv[2].lower()

    if command == 'encrypt':
        print(encrypt(mensagem))
        
    elif command == 'decrypt':
        print(decrypt(mensagem))

    else:
        print(command + ' -> command not found')

if __name__ == '__main__':
    main()