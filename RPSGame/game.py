# :vim filecoding=utf-8


import random


# 这里是 Python 的异常，将异常情况和正常逻辑分别处理，可以使逻辑更清晰。
class BadInput(Exception):
    pass


# 石头
ROCK = 0
# 布
PAPER = 1
# 剪刀
SCISSOR = 2


# 赢
WIN = 1
# 平
DRAW = 0
# 负
LOSE = -1


def isGuessWinOrDrawOrLose(guess, computer):
    if guess == computer:
        return DRAW

    if guess == ROCK and computer == SCISSOR:
        return WIN

    if guess == PAPER and computer == ROCK:
        return WIN

    if guess == SCISSOR and computer == PAPER:
        return WIN

    return LOSE


def displayWinMessage():
    print("你真牛B，赢了，奖励共享女友一个。")


def displayDrawMessage(remain):
    print("平局，来来来决战到天亮,你还有%d次机会。" % remain)


def displayLoseMessage(remain):
    print("哈哈，去洗洗手再来吧，你输了,你还在%d次机会" % remain)


def displayGameOverMessage():
    print("次数用尽，bye")


def throwByComputer():
    return random.randint(0, 2)


def throwByGuess():
    guess = int(input("请输入你要猜的数字（0：拳头 1：布 2：剪刀):"))
    if guess >= 3:
        raise BadInput()
    return guess


def play(attempt_times):
    computer = throwByComputer()
    print(computer)
    guess = throwByGuess()

    if isGuessWinOrDrawOrLose(guess, computer) == WIN:
        displayWinMessage()
        return
    elif isGuessWinOrDrawOrLose(guess, computer) == DRAW:
        displayDrawMessage(attempt_times-1)
    else:
        displayLoseMessage(attempt_times-1)

    if attempt_times > 1:
        play(attempt_times-1)
    else:
        displayGameOverMessage()


while True:
    try:
        play(4)
        break
    except BadInput:
        pass
