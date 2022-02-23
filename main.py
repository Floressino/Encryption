alphabet = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
           13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
           25: 'Z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K',
           37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W',
           49: 'X', 50: 'Y', 51: 'Z', 52: 'А', 53: 'Б', 54: 'В', 55: 'Г', 56: 'Д', 57: 'Е', 58: 'Ё', 59: 'Ж', 60: 'З',
           61: 'И', 62: 'Й', 63: 'К', 64: 'Л', 65: 'М', 66: 'Н', 67: 'О', 68: 'П', 69: 'Р', 70: 'С', 71: 'Т', 72: 'У',
           73: 'Ф', 74: 'Х', 75: 'Ц', 76: 'Ч', 77: 'Ш', 78: 'Щ', 79: 'Ъ', 80: 'Ы', 81: 'Ь', 82: 'Э', 83: 'Ю', 84: 'Я',
           85: 'А', 86: 'Б', 87: 'В', 88: 'Г', 89: 'Д', 90: 'Е', 91: 'Ё', 92: 'Ж', 93: 'З', 94: 'И', 95: 'Й', 96: 'К',
           97: 'Л', 98: 'М', 99: 'Н', 100: 'О', 101: 'П', 102: 'Р', 103: 'С', 104: 'Т', 105: 'У', 106: 'Ф', 107: 'Х',
           108: 'Ц', 109: 'Ч', 110: 'Ш', 111: 'Щ', 112: 'Ъ', 113: 'Ы', 114: 'Ь', 115: 'Э', 116: 'Ю', 117: 'Я', 118: ' '}

# Достаем ключ из словаря по значению
def get_key(dictionary: dict, s: str) -> int:
    for key, value in dictionary.items():
        if value == s:
            return key

# Получаем двумерный массив
def get_square_array() -> []:
    arr = []
    alph = list(alphabet.values())
    arr.append(alph)
    for i in range(1, len(alphabet)):
        alph = alph[1:] + alph[:1]
        arr.append(alph)

    return arr

def append_to_size(word: str, length: int):
    while len(word) <= length:
        word += word
    
    return word[0:length]

def ceasar(is_encode: bool) -> str:
    message = input("Введите сообщение для шифрования: ").upper()

    # Количество сдвига
    n = 1 if is_encode else -1
    encode = ""
    for char in message:
        index = get_key(alphabet, char)
        new_index = index + n

        if new_index == -1:
            new_index = len(alphabet) - 1
        elif new_index == len(alphabet):
            new_index = 0

        encode += alphabet[new_index]

    return encode

def vigenere() -> str:
    message = input("Введите сообщение для шифрования: ").upper()
    key = append_to_size(input("Введите ключ шифрования: ").upper(), len(message))
    arr = get_square_array()
    print(arr)
    new_message = ""

    for i in range(0, len(message)):
        row = get_key(alphabet, key[i])
        column = get_key(alphabet, message[i])
        new_message += arr[row][column]

    return new_message

def wanderers() -> str:
    row = int(input("Введие кол-во строк: "))
    message = input("Введите сообщение для шифрования: ").upper()
    new_message = ""
    c = 0
    j = 1

    message_length = len(message)
    count_row = message_length // row
    if message_length % row != 0:
        count_row = count_row + 1

    while c < row:
        sh = c
        while j <= count_row:
            if sh <= message_length - 1:
                new_message += message[sh]
            else: 
                new_message += " "
            sh = sh + row
            j = j + 1
        c = c + 1
        j = 1
    
    return new_message


if __name__ == '__main__':
    while True:
        print("=" * 16)
        print("Выберите шифр:\n1. Цезаря\n2. Виженера\n3. Скиталы\n4. Exit")
        while True:
            try:
                number = int(input("Номер: "))
                if number in range(1, 5):
                    break
                else:
                    print("Введите число от 1 до 4")
            except:
                print("Введите корректное число")

        if number == 1:
            question = input("1. Шифровать\n2. Расшифровать\n")
            is_encode = True if int(question) == 1 else False
            word = ceasar(is_encode)
        elif number == 2:
            word = vigenere()
        elif number == 3:
            word = wanderers()
        else:
            print("Bye bye")
            break

        print(f"Слово: {word}")
