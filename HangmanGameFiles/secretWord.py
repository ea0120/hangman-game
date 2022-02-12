import random

secretWord_dic = {
    1: "heavenlyfather",
    2: "gosple",
    3: "joesephsmith",
    4: "jesus",
    5: "temple"
}

def getRandomWord():
    rnum = random.randrange(1,5)
    return secretWord_dic[rnum]