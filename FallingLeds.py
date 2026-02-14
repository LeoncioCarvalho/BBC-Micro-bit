from microbit import *
from random   import *
T = const(41)
V = const(63)
display.clear()
seed(running_time())
set_volume(V)                 # 0 ~ 255

#           01234      x = 0
#            12345     x = 1
#             23456    x = 2
#              34567   x = 3
#               45678  x = 4
#
#                      i = 4  5  6  7  8  9 10 11 12 13 14 15 16 17 
string00 = "000000000" #   4|
string01 = "000000000" #   3| 4|
string02 = "000000000" #   2| 3| 4|
string03 = "000000000" #   1| 2| 3| 4|
string04 = "000090000" #   0| 1| 2| 3| 4|
string05 = "000080000" #      0| 1| 2| 3| 4|
string06 = "000070000" #         0| 1| 2| 3| 4|
string07 = "000060000" #            0| 1| 2| 3| 4|
string08 = "000050000" #               0| 1| 2| 3| 4|
string09 = "000040000" #                  0| 1| 2| 3| 4|
string10 = "000030000" #                     0| 1| 2| 3| 4|
string11 = "000020000" #                        0| 1| 2| 3| 4|
string12 = "000010000" #                           0| 1| 2| 3| 4|
string13 = "000000000" #                              0| 1| 2| 3| 4|
string14 = "000000000" #                                 0| 1| 2| 3|
string15 = "000000000" #                                    0| 1| 2|
string16 = "000000000" #                                       0| 1|
string17 = "000000000" #                                          0|

strings  = [string00, string01, string02, string03, string04, string05, string06, string07, string08,
            string09, string10, string11, string12, string13, string14, string15, string16, string17]

x = 0
y = 0

while True:

    while (x == y):
        x = randint(0, 4)

#   audio.play(Sound.HELLO, wait=False)

    for i in range(4, 18, 1): # 18 = 17 + 1

        imagex = Image( (strings[i-0][x:(x+5)]) + # row 0
                  ":" + (strings[i-1][x:(x+5)]) + # row 1
                  ":" + (strings[i-2][x:(x+5)]) + # row 2
                  ":" + (strings[i-3][x:(x+5)]) + # row 3
                  ":" + (strings[i-4][x:(x+5)]) ) # row 4

        display.show(imagex)

        sleep(T)
        
    y = x                                                                                         
