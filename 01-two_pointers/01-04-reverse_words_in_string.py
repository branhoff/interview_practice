
def reverse_words(sentence):
    reversed_sentence = sentence[::-1]
    output = ""

    head = 0

    for i in range(len(reversed_sentence)):
        if reversed_sentence[i] == " " or i == len(reversed_sentence) - 1:
            if i == len(reversed_sentence) - 1:
                output += reversed_sentence[i:head-1:-1]
            else:
                output += reversed_sentence[i:head:-1] + " "

            head = i + 1

    return output.strip()

def main():
    print(reverse_words("We love Java "))

if __name__ == "__main__":
    main()
