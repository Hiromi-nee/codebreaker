# Vigenere Cipher (Polyalphabetic Cipher)
# http://inventwithpython.com/codebreaker (BSD Licensed)
import pyperclip, simpleSubCipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
    key = 'ASIMOV'
    mode = 'encrypt' # set to 'encrypt' or 'decrypt'

    message = message.upper()
    key = key.upper()

    print('Original text:')
    print(message)
    print()

    if mode == 'encrypt':
        translated = translateMessage(message, key, 'encrypt')
    elif mode == 'decrypt':
        translated = translateMessage(message, key, 'decrypt')

    print('%sed message:' % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('The message has been copied to the clipboard.')


def encryptMessage(message, key):
    return translateMessage(message, key, 'encrypt')


def decryptMessage(message, key):
    return translateMessage(message, key, 'decrypt')


def translateMessage(message, key, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()
    message = message.upper()

    for symbol in message: # loop through each character in message
        num = SYMBOLS.find(symbol)
        if num != -1:
            if mode == 'encrypt':
               num += SYMBOLS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
               num -= SYMBOLS.find(key[keyIndex]) # subtract if decrypting

            # handle the potential wrap around
            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num += len(SYMBOLS)

            # add the encrypted/decrypted symbol to the end of translated.
            translated.append(SYMBOLS[num])

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in SYMBOLS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)


if __name__ == '__main__':
     main()