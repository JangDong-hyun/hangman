#안녕하세요.


def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|         |         ",
              "|         |         ",
              "|         0         ",
              "|        /|-        ",
              "|        / -        ",
              "|                  ",]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman")


    while wrong < len(stages) -1:
        print("\n")
        char = input("Guess a letter")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong+=1
            print(" ".join(board))
            print("\n".join(stages[:wrong+1]))

            if "__" not in board:
                print("You win! It was:")
                print(" ".join(board))
                win = True
                break
    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))
        


hangman("cat")
            
