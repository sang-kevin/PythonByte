# coding=utf-8
# 猜数字的小游戏
# NOTE: 2018/4/27:增加查看输入的历史记录的功能

import random
import pickle
from collections import deque

num = random.randint(1, 100)
print num
history = deque([], 5)
history = pickle.load(open('files/history'))
while True:
    guess = raw_input("Enter 1~100: ")
    if guess.isdigit():
        guess = int(guess)
        history.append(guess)
        print list(history)
        if guess > num:
            print("guess smaller than %s" % guess)
        elif guess < num:
            print("guess bigger than %s" % guess)
        else:
            pickle.dump(history, open('files/history', 'w'))
            print("Guess OK, Game Over!")
            break
    elif guess == 'history' or guess == 'h?':
        print list(history)
