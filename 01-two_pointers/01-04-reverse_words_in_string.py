import re

def reverse_words(sentence):
   sentence = re.sub(' +',' ',sentence.strip())

   sentence = list(sentence)
   str_len = len(sentence)

   str_rev(sentence, 0, str_len - 1)

   start = 0
   end = 0

   while (start < str_len):
    while end < str_len and sentence[end] != ' ':
        end += 1
    str_rev(sentence, start, end - 1)
    start = end + 1;
    end += 1

   return ''.join(sentence)


# A function that reverses a whole sentence character by character
def str_rev(_str, start_rev, end_rev):
   while start_rev < end_rev:
       temp = _str[start_rev]
       _str[start_rev] = _str[end_rev]
       _str[end_rev] = temp

       start_rev += 1
       end_rev -= 1

# Driver code
def main():
    string_to_reverse = ["Hello Friend", "    We love Python",
                         "The quick brown fox jumped over the lazy dog   ",
                         "Hey", "To be or not to be",
                         "AAAAA","Hello     World"]

    for i in range(len(string_to_reverse)):
        print(i+1, ".\t Actual string:\t\t" +
              "".join(string_to_reverse[i]), sep='')
        Result = reverse_words(string_to_reverse[i])
        print("\t Reversed string:\t" +
              "".join(Result), sep='')
        print("-"*100)


if __name__ == '__main__':
    main()