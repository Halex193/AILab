from numpy.random import randint


def transform(word, cipher):
    number = 0
    if cipher[word[0]] == 0:
        raise ArithmeticError("Word starts with 0")

    for letter in word:
        number *= 16
        number += cipher[letter]
    return number


def solution(cipher, words, operation):
    result = 0
    if operation == "+":
        result = 0
        for i in range(len(words) - 1):
            number = transform(words[i], cipher)
            result += number
    elif operation == "-":
        result = transform(words[0], cipher)
        for i in range(1, len(words) - 1):
            number = transform(words[i], cipher)
            result -= number
    return result == transform(words[-1], cipher)


def main():
    chances = int(input("chances: "))
    operation = input("operation: ")
    n = int(input("number of words: "))
    if n < 3:
        raise RuntimeError("there have to be more than two words")
    words = []
    for i in range(n):
        words.append(input("word: "))
    print("Computing...")
    for i in range(chances):
        cipher = {}
        for word in words:
            for letter in word:
                if letter not in cipher:
                    cipher[letter] = randint(0, 16 + 1)
        try:
            if solution(cipher, words, operation):
                print("Number of attempts: " + str(i))
                print(cipher)
                return
        except ArithmeticError:
            pass
    print("No solution found")


if __name__ == '__main__':
    main()

# SEND + MORE = MONEY {'S': 15, 'E': 3, 'N': 4, 'D': 3, 'M': 1, 'O': 0, 'R': 15, 'Y': 6}
# TAKE + A + CAKE = KATE {'T': 3, 'A': 15, 'K': 9, 'E': 1, 'C': 5}
# EAT + THAT = APPLE {'E': 16, 'A': 1, 'T': 16, 'H': 1, 'P': 1, 'L': 3}
# NEVER - DRIVE = RIDE {'N': 8, 'E': 16, 'V': 8, 'R': 16, 'D': 7, 'I': 4}
