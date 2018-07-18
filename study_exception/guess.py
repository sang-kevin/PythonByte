# coding=utf-8
# 猜数字的小游戏
import random

num = random.randint(1, 100)
# print num

while True:
    try:
        guess = int(raw_input("Enter 1~100: "))
    except ValueError as e:
        print"Please input integer!", e
        continue
    if guess > num:
        print("guess smaller than %s" % guess)
    elif guess < num:
        print("guess bigger than %s" % guess)
    else:
        print("Guess OK, Game Over!")
        break
    print

# 保证了程序的健壮性，错误输入的时候程序也能继续运行
