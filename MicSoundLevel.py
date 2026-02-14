from microbit import *
print("\nMICROPHONE SOUND LEVEL MONITOR BY \u00A3\u20AC\u00D8 \u00A9A\u00AEVALHO")
print("\nOnce upon a long, long time ago, in a kingdom far, far away...\n")
#------------------------------------------------------------------------
#                                                          
#                                                     columns       
#                                                    /       \ 
#                                                  . 0 1 2 3 4 X
#                                                   +---------+
#                                        row4      0|5 6 7 8 9| <--- 5X5 LED MATRIX                                                 
#                                                   | \ \ \ \ |                                             
#                                        row3      1|4 5 6 7 8|\                                                 
#                                                   | \ \ \ \ | \                                            
#                                        row2      2|3 4 5 6 7|\ \                                                
#                                                   | \ \ \ \ | \ \                                           
#                                        row1      3|2 3 4 5 6|\ \ \                                               
#                                                   | \ \ \ \ | \ \ \                                           
#                                        row0      4|1 2 3 4 5|\ \ \ \                                              
#                                                   +---------+ \ \ \ \                                          
#                                                  Y   \ \ \ \ \ \ \ \ \                                        
# brightness levels: (0) off ~ (9) full on.             \ \ \ \ \ \ \ \ \                                       
#                                                      0 1 2 3 4 5 6 7 8 9                                      
#                row4  row3  row2  row1  row0          | | | | | | | | | |
levels = [Image("00000:00000:00000:00000:00000"), # <--+ | | | | | | | | | 
          Image("00000:00000:00000:00000:10000"), # <----+ | | | | | | | | QUIET
          Image("00000:00000:00000:20000:12000"), # <------+ | | | | | | |
          Image("00000:00000:30000:23000:12300"), # <--------+ | | | | | |
          Image("00000:40000:34000:23400:12340"), # <----------+ | | | | |
          Image("50000:45000:34500:23450:12345"), # <------------+ | | | | MIDI RANGE
          Image("56000:45600:34560:23456:12345"), # <--------------+ | | |
          Image("56700:45670:34567:23456:12345"), # <----------------+ | |
          Image("56780:45678:34567:23456:12345"), # <------------------+ |
          Image("56789:45678:34567:23456:12345")] # <--------------------+ NOISY

#------------------------------------------------------------------------

def main():

    while True:
        
#       x = 25 # if input level MAX (255)   ---> output will be 0 ~ 10 (10 will cause index error. do not use!!!)
#       x = 26 # increase     sensitivity \
        x = 27 # intermediate sensitivity  +------------------> 0 ~  9 ( fire at will!!!)
#       x = 28 # decrease     sensitivity /
#       x = 29 # if input level MAX (255)   ---> output will be 0 ~  8 ( 9 will never be obtained. do not use!!!)

# 0 <= input  <= 255 <--- microphone.sound_level()
# 0 <= output <=   9 ---> index to levels

        display.show(levels[int(microphone.sound_level() / x)])    

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        display.clear()
        print("And they lived happily ever after and th-th-that's all, folks!\n") 

#------------------------------------------------------------------------
