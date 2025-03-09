# import random

# total_score=0
# nop = int(input("enter number of players: "))

# names = []
# for i in range(1,nop + 1):
#     name_players = input(f"enter name player {i}: ")
#     names.append(name_players)
# while True:
#     count = nop * 5
#     Rnum = random.randint(50, 99)
#     print(f"number is: {Rnum}")




#     choiceN = random.randint(0,nop-1)
#     choice=names[choiceN]
#     print(f"\ntern: {choice}\n")

#     for i in range(count):
#         count -= 1
#         guess = int(input("Make a guess from numbers 50 to 99: "))
#         scores = 100 - (i * 20)
  


#         # print(scores)
#         if guess == Rnum:
#             a=print(f"WOW YOU WIN!! \nyour score is {scores}")
#             total_score+=scores
#             break
#         if count == 0:
#             print(f"YOU LOSE!\n number was: {Rnum}")

#         if guess > Rnum:
#             print("GO DOWN")
#         else:
#             print("GO UP")


#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again != 'yes':
#         print(f"your score is: {total_score}")
#         break








# import random

# total_score = 0
# nop = int(input("enter number of players: "))

# names = []
# where=random.randint(1,nop)
# names.insert(where,"BOT")

# for i in range(1, nop + 1):
#     name_players = input(f"enter name player {i}: ")
#     names.append(name_players)

# current_player_index = random.randint(0, nop - 1)  

# while True:
#     count = nop * 5
#     Rnum = random.randint(50, 99)
#     print(f"number is: {Rnum}")

#     while count > 0:
#         choice = names[current_player_index]
#         print(f"\nIt's {choice}'s turn to guess.\n")
        
#         guess = int(input("Make a guess from numbers 50 to 99: "))
#         scores = 100 - ((nop * 5 - count) * 20)
#         count -= 1

# # robot


#         if guess == Rnum:
#             print(f"WOW YOU WIN!! \nyour score is {scores}")
#             total_score += scores
#             break
#         if count == 0:
#             print(f"YOU LOSE!\n number was: {Rnum}")
            
#             if guess > Rnum:
#                 print("GO DOWN")
#             else:
#                 print("GO UP")

#         current_player_index = (current_player_index + 1) % nop  

#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again != 'yes':
#         print(f"your score is: {total_score}")
#         break

    

        
import random

total_score = 0
nop = int(input("enter number of players: "))

names = []
where = random.randint(0, nop)  # انتخاب تصادفی موقعیت ربات

for i in range(nop):
    name_players = input(f"enter name player {i+1}: ")
    names.append(name_players)

names.insert(where, "BOT")  # اضافه کردن ربات در لیست بازیکنان

while True:
    count = nop * 5
    Rnum = random.randint(50, 99)

    low, high = 50, 99  # محدوده اولیه برای BOT

    current_player_index = random.randint(0, nop)  # بازیکن اول تصادفی انتخاب می‌شود

    while count > 0:
        choice = names[current_player_index]
        print(f"\nIt's {choice}'s turn to guess.\n")

        if choice == "BOT":
            guess = random.randint(low, high)
            print(f"BOT guessed {guess}")
        else:
            guess = int(input("Make a guess from numbers 50 to 99: "))

        scores = 100 - ((nop * 5 - count) * 20)
        count -= 1

        if guess == Rnum:
            print(f"WOW YOU WIN!! \nyour score is {scores}")
            total_score += scores
            break
        elif guess > Rnum:
            print("GO DOWN")
            high = min(high, guess - 1)  # به‌روزرسانی high برای همه
        else:
            print("GO UP")
            low = max(low, guess + 1)  # به‌روزرسانی low برای همه

        if count == 0:
            print(f"YOU LOSE!\n number was: {Rnum}")

        # تغییر نوبت به بازیکن بعدی
        current_player_index = (current_player_index + 1) % len(names)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print(f"your total score is: {total_score}")
        break
