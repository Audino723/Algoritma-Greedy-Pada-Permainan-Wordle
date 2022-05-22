def read_file():
    with open('words.txt') as f:
        lines = f.readlines()
    f.close()

    words_list = []
    f2 = open("words2.txt", "a")

    for line in lines:
        line = line.split('\n')[0]
        line = line.split(':')[0]
        line = line.strip(' ').strip("'").strip(",").strip("'")
        f2.write(line + '\n')
        words_list.append(line)

    print(words_list)

read_file()
