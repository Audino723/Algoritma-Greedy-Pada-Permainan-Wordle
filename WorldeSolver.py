def count_similar_string(guess, result, words_list):
    similar_string = 0
    # Green n Yellow Letters Position
    green_position = []
    yellow_position = []
    for i, v in enumerate(result):
        if (v == 'G'):
            green_position.append(i)
        if (v == 'Y'):
            yellow_position.append(i)

    # Find Green n Yellow Letter Words
    for word in words_list:
        green_word = True
        yellow_word = True

        for i in green_position:
            if word[i] != guess[i]:
                green_word = False

        for i in yellow_position:
            if guess[i] not in word:
                yellow_word = False

        if (green_word and yellow_word):
            similar_string += 1

    return similar_string

def find_similar_string(guess, result, words_list):
    # Green n Yellow Letters Position
    green_position = []
    yellow_position = []
    for i, v in enumerate(result):
        if (v == 'G'):
            green_position.append(i)
        elif (v == 'Y'):
            yellow_position.append(i)

    # Find Green n Yellow Letter Words
    answer_list = []
    for word in words_list:
        green_word = True
        yellow_word = True

        for i in green_position:
            if word[i] != guess[i]:
                green_word = False

        for i in yellow_position:
            if guess[i] not in word or guess[i] == word[i]:
                yellow_word = False

        if (green_word and yellow_word):
            answer_list.append(word)

    return answer_list

def guess_checker(guess, answer):
    ans = ''

    for i in range(5):
        if (guess[i] == answer[i]):
            ans += 'G'
        elif (guess[i] in answer):
            ans += 'Y'
        else:
            ans += 'B'

    return ans

def eliminate_answers_list(list1, list2, list3):
    new_list = list(set(list1) & set(list2) & set(list3)) 

    return new_list

def first_three_guess(words_list):
    guesses = input("Guess Words : ").split(" ")
    results = input("Guess Results : ").split(" ")
    listes = []

    for i in range(3):
        guess = guesses[i]
        result = results[i]
        listes.append(find_similar_string(guess.lower(), result.upper(), words_list))

    return eliminate_answers_list(listes[0], listes[1], listes[2])

def read_file():
    with open('words2.txt') as f:
        lines = f.readlines()
    f.close()

    words_list = []
    for line in lines:
        words_list.append(line.split('\n')[0])

    return words_list

def find_best_guessed_word(answer_list):
    guess_similar_string_counter = []
    for guess in answer_list:
        max_similar_string = 0
        similar_string = 0
        for answer in answer_list:
            result = guess_checker(guess, answer)
            similar_string = count_similar_string(guess, result, answer_list)

            if max_similar_string < similar_string and len(answer_list) - similar_string > 2:
                if (guess == "blade"):
                    print(answer, len(answer_list), similar_string)
                max_similar_string = similar_string

        guess_similar_string_counter.append(max_similar_string)
        #guess_similar_string_counter.append(similar_string/len(answer_list))

    return guess_similar_string_counter

def main():
    # Read File
    answer_list = read_file()
    use_three_guesses_starter = input("Three starter guesses (Y/N) ? ")

    if (use_three_guesses_starter.upper() != 'Y'):
        guess = input("Guessed Word : ")
    
    total_attempt = 0
    while (True):
        total_attempt += 1

        # First three attempts
        if (total_attempt < 3 and use_three_guesses_starter.upper() == 'Y'):
            answer_list = first_three_guess(answer_list)
            total_attempt = 3

        # 4th and so on
        else :
            print("Guessed word", guess)
            result = input("result: ")
            if (result == "won"):
                print("Congrats!, total attempts", total_attempt)
                break
            elif (result == "exit"):
                print("exiting...")
                break

            answer_list = find_similar_string(guess.lower(), result.upper(), answer_list)

        # Check total similar string found
        print("Total Similar String found :", len(answer_list))
        print(answer_list)
        print('--------------')

        # Find best word to guess
        guess_similar_string_counter = find_best_guessed_word(answer_list)
        min_index = guess_similar_string_counter.index(min(guess_similar_string_counter))

        # Print out
        print("best guess: ", answer_list[min_index])
        guess = answer_list[min_index]
        answer_list.pop(min_index)
        print()
        
main()