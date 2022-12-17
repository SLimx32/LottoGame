import random as RD
import datetime as DT

TODAY_NUMBERS = []
WIN_LIST = []
PLAYER_NUMBERS = []


def play_time():
    date_now = DT.datetime.now()
    print(date_now.strftime("%d-%m-%y %H:%M:%S"))


def player_details():
    name = input("Please enter your full name : ")
    age = input("Please enter your borning date : ")
    print(f"{name.title()} Welcome to LOTO 6/49")
    tiket = input("How many numbers would you like to bet?? :: ")
    file = open("LotoPlayerDetails.txt", "a")
    file.write(
        f"Player Name : {name}\nYears: {age}\n"
        f"Playing date and time : {play_time()}\n"
        f"Day Numbers : {TODAY_NUMBERS}\n"
        f"Play Numbers : {PLAYER_NUMBERS}\n")
    file.close()


def today_numbers():
    list_of_numbers = list(range(1, 50))
    pick = RD.sample(list_of_numbers, k=6)
    pick.sort()
    for x in pick:
        TODAY_NUMBERS.append(x)
    print(f"Today wining numbers are : {pick}")


def play():
    n_list = []
    while True:
        try:
            number = int(input("Enter a number between 1 - 49  : "))
        except ValueError:
            print("You can choose only numbers between 1 - 49 !!")
            continue
        if number in range(1, 50):
            if number not in n_list:
                print("Corect enter the next number:  ")
                n_list.append(number)
            else:
                print("You already picked this number!!"
                      "     Try one more time !!")
        else:
            print("        Incorect number!!"
                  "The number must be between 1 and 49 !!")
            n_list.sort()
            print(f"Your numbers  {n_list}")
            for x in n_list:
                PLAYER_NUMBERS.append(x)
            break


def wining_details():
    win_list = [x for x in TODAY_NUMBERS if x in PLAYER_NUMBERS]
    print(f"You guessed {len(win_list)} number == **{str(win_list)}**")
    if len(win_list) == 1:
        print("Non-winning ticket !!")
    elif len(win_list) == 2:
        print("Non-winning ticket!!")
    elif len(win_list) == 3:
        print("You won 30 $ !!")
    elif len(win_list) == 4:
        print("You won 180 $ !!!")
    elif len(win_list) == 5:
        print("Congrats you won 4567 $")
    elif len(win_list) == 6:
        print("********** YOU WON THE BIG PRIZE **********")
        print("--------------12.090.240.110 $----------")
    else:
        print("You lost")


play()
wining_details()
