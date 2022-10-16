print("Введите кодовое слово:")
key_word = list(input())
alphabet = list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
matrix = [[], [], [], [], [], [], [], []]
i = 0
j = 0

# changing all Ё to E
for c in key_word:
    index = key_word.index(c)
    c = c.upper()
    if c == "Ё":
        key_word[index] = "Е"
    else:
        key_word[index] = c

# deleting repeating letters from the key_word
key_word = ''.join(sorted(set(key_word), key=key_word.index))

# adding characters from key word to matrix
for c in key_word:
    c = c.upper()
    matrix[i].append(c)
    alphabet.remove(c)
    j += 1
    if j == 4:
        j = 0
        i += 1

a = 0

# adding all other characters to matrix
while alphabet:
    letter = alphabet[a].upper()
    matrix[i].append(letter)
    alphabet.remove(letter)
    j += 1
    if j == 4:
        j = 0
        i += 1


# function for searching character in matrix
def find_in_matrix(character):
    for i_fun in range(0, 8):
        for j_fun in range(0, 4):
            if matrix[i_fun][j_fun] == character:
                return [i_fun, j_fun]
            j_fun += 1
        i_fun += 1


# function for encryption
def encrypt():
    print("Введите название файла:")
    path = input()
    f = open(path, 'r')
    text = f.read()
    # deleting punctuation from text
    text = text.replace(" ", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace("\n", "")
    f.close()
    output = []
    text = list(text)
    # changing all Ё to E in text
    for c in text:
        index = text.index(c)
        c = c.upper()
        if c == "Ё":
            text[index] = "Е"
        else:
            text[index] = c

    while text:
        if len(text) == 1:
            text.append("Й")
        if text[0] == text[1]:
            text.insert(1, "Й")
        first = find_in_matrix(text[0].upper())
        first_i = first[0]
        first_j = first[1]
        second = find_in_matrix(text[1].upper())
        second_i = second[0]
        second_j = second[1]
        if first_i == second_i:
            if first_j != 3:
                output.append(matrix[first_i][first_j + 1])
            else:
                output.append(matrix[first_i][0])
            if second_j != 3:
                output.append(matrix[second_i][second_j + 1])
            else:
                output.append(matrix[second_i][0])
        elif first_j == second_j:
            if first_i != 7:
                output.append(matrix[first_i + 1][first_j])
            else:
                output.append(matrix[0][first_j])
            if second_i != 7:
                output.append(matrix[second_i + 1][second_j])
            else:
                output.append(matrix[0][second_j])
        else:
            output.append(matrix[first_i][second_j])
            output.append(matrix[second_i][first_j])
        text.pop(0)
        text.pop(0)
    f = open(path, 'w')
    f.write(''.join(output))
    f.close()


# function for decryption
def decrypt():
    print("Введите название файла:")
    path = input()
    f = open(path, 'r')
    text = f.read()
    text = text.replace(" ", "")
    output = []
    f.close()
    text = list(text)
    while text:
        first = find_in_matrix(text[0].upper())
        first_i = first[0]
        first_j = first[1]
        second = find_in_matrix(text[1].upper())
        second_i = second[0]
        second_j = second[1]
        if first_i == second_i:
            if first_j != 0:
                output.append(matrix[first_i][first_j - 1])
            else:
                output.append(matrix[first_i][3])
            if second_j != 0:
                output.append(matrix[second_i][second_j - 1])
            else:
                output.append(matrix[second_i][3])
        elif first_j == second_j:
            if first_i != 0:
                output.append(matrix[first_i - 1][first_j])
            else:
                output.append(matrix[7][first_j])
            if second_i != 0:
                output.append(matrix[second_i - 1][second_j])
            else:
                output.append(matrix[7][second_j])
        else:
            output.append(matrix[first_i][second_j])
            output.append(matrix[second_i][first_j])
        text.pop(0)
        text.pop(0)
    f = open(path, 'w')
    f.write(''.join(output))
    f.close()


print("Нажмите 1 для шифрования, 2 для дешифрования")
var = input()
if var == "1":
    encrypt()
elif var == "2":
    decrypt()
else:
    print("wrong argument")
