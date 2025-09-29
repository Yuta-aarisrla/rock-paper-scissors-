import random

# กำหนดตัวเลือก
rock = "✊ Rock"
paper = "✋ Paper"
scissors = "✌ Scissors"
image = [rock, paper, scissors]

# กำหนดตัวแปรเริ่มต้น
count = 0
win = 0
lose = 0

while True:
    # รับค่าจากผู้เล่น
    print("What do you choose? \n(0) rock \n(1) paper \n(2) scissors")
    user = int(input("Enter your choice: "))
    print(image[user])  # แสดงรูปที่เลือก
    count += 1  # นับรอบเล่น

    # คอมเลือก
    com = random.randint(0, 2)
    print("Computer choose:")
    print(image[com])

    # ตรวจผลเกม
    if user == com:
        print("It's a draw!")
    elif user == 0 and com == 2:
        print("You win!\n")
        win += 1
    elif user == 1 and com == 0:
        print("You win!\n")
        win += 1
    elif user == 2 and com == 1:
        print("You win!\n")
        win += 1
    else:
        print("You lose!\n")
        lose += 1

    # แสดงคะแนน
    print(f"You: {win}, Computer: {lose}\n-----------")

    # เมื่อเล่นครบ 5 รอบ จะถามว่าจะเล่นต่อหรือไม่
    if count == 5:
        play_again = input("Play again? (yes/no): ").lower()
        if play_again == 'yes':  # เล่นต่อ
            count = 0
        else:  # ไม่เล่นต่อ
            print("--------")
            print("Thanks for playing!")
            break