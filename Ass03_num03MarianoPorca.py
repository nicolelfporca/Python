while True:
    sentence = str(input("Enter a sentence: "))

    def flipEndCharacter(sentence):
        if len(sentence) < 2:
            return "Incompatible"
        elif sentence[0] == sentence[-1]:
            return "Two's a pair"
        else:
            return sentence[-1] + sentence[1:-1] + sentence[0]

    print(flipEndCharacter(sentence))