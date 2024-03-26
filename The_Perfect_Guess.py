import random

random=random.randint(1, 40)

class Auto:
    time=0
    def __init__(self,R_Num):
         i=True         
         while i == True:

          try:
            user=int(input("Enter a number\n"))
            if user<R_Num:
              print("Guess A Big Number")
              self.time+=1
            elif user>R_Num:
              print("Guess A Small Number")
              self.time+=1
            elif user==R_Num:
              print(f"You Guess The right Number At {self.time} Times\n")              
              break
          except Exception as error:
           print(f'You did not enter integer so it showing {error}')

    def Score(self):   
        file=open("highscore.txt",'r')
        read=int(file.read())

        if self.time<read:
         file.close()
         print("You Broke The High Score")
         file=open("highscore.txt",'w')
         file.write(str(self.time))
         file.close()
      



object=Auto(random)

object.Score()