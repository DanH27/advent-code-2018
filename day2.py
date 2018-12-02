letter_count = {'two': 0, 'three': 0}


def checkTwice(dict):
    #twoletters = 0
    #threeletters = 0
    for letter in dict:
        if dict[letter] == 2:
            letter_count['two'] += 1
            break;
        if dict[letter] == 3:
            letter_count['three']+= 1
            break;
    #if twoletters != 0:
    #    print("Two letters" + str(twoletters))
    #if threeletters != 0:
    #    print("three letters" + str(threeletters))


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
        print(twosFound, threesFound)


######PART 2########
with open("day2-input.txt", "r") as f:
    box_size = 25
    current_word = []
    letters_differnt = 0
    for word in f:
        current_word = list(word)
        break
    for word in f:
        listed_word = list(word)
        for i in range(box_size):
            if listed_word[i] != current_word[i]:
                letters_differnt += 25
                break;
    current_word = []

    print(letters_differnt)
