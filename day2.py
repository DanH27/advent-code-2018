letter_count = {'two': 0, 'three': 0}


with open("day2-input.txt", "r") as f:
    twosFound = 0
    threesFound = 0
    letter_dict = {}
    for word in f:
        found_two = False
        found_three = False
        for letter in word:
            if letter in letter_dict:
                letter_dict[str(letter)] += 1
            else:
                letter_dict[str(letter)] = 1
        for lt in letter_dict:
            if letter_dict[lt] == 2 and found_two == False:
                twosFound += 1
                found_two = True
            if letter_dict[lt] == 3 and found_three == False:
                threesFound += 1
                found_three = True

        #checkTwice(letter_dict)
        letter_dict.clear()
        #Print twos found and threes found
        print(twosFound, threesFound)


######PART 2########
with open("day2-input.txt", "r") as f:
    all_words = []
    current_word = []
    words_not_matched = 0
    correct_letters = 0
    correct_letters_list = []
    for line in f:
        all_words.append(line.rstrip())

    for word in all_words:
        current_word = list(word)

        for word2 in all_words:
            matches = 0
            for i in range(25):
                if list(word2)[i] != list(word)[i]:
                    matches += 1
            if matches == 1:
                #Returns words that have only 1 difference at same index
                print(word2)
