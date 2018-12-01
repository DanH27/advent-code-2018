#Function for first part of question.
def get_frequency():
    #Open text file in read mode
    with open("day1-input.txt", "r") as f:
        #Initiate frequency to 0
        current_frequency = 0
        #For each number in the file
        for num in f:
            #Sum up the current frequency
            current_frequency += int(num)
        #Print current frequency after loop terminates
        print(current_frequency)

#Call the first function
get_frequency()



#Store all numbers from file in an array, and return the array
def get_input_arr():
    with open("day1-input.txt", "r") as f:
        num_arr = []
        for num in f:
            num_arr.append(int(num))
        return num_arr



#Get the first duplicate frequency
def firstDup():
    #Current frequency
    frequency = 0
    #Set counter to 0
    counter = 0
    #set not_found to True
    not_found = True
    #Get array of numbers from file using previous function
    num_arr = get_input_arr()
    #Initialize dictionary of the frequency of each frequency
    freq_dict = {}

    #While not found is stll True, iterate through the array and get a running total
    while not_found:
        for i in num_arr:
            frequency += i
            #If frequency is in the array add 1 to it
            if str(frequency) in freq_dict:
                freq_dict[str(frequency)] += 1
                #Print if  match is found, set not_found to False to exit loop and break from 'for' loop
                print("Match Found: %s" % frequency)
                not_found = False
                break
            else:
                #Else if not in dictionary initialzie frequency to 1
                freq_dict[str(frequency)] = 1
            #Always add 1 to the counter after every number is added
            counter += 1

#Call firstDup function
firstDup()
