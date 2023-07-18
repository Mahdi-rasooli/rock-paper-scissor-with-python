
x = ['paper','scissor','rock']

import random

print('*** Hello welcome to the game ***\n')
print('###################################\n')


#if user == 'rock':
while True:

   user = eval(input('*** what is your choice ? 1.rock , 2.paper , 3.scissor = '))
   system = random.choice((['paper','scissor','rock']))


   if user == 1 and system =='paper':
      print('*** you choiced rock and system paper ***\n')
      print('*** system win ***')

   elif user == 1 and system =='scissor':
      print('***you choiced rock and system scissor ****\n')
      print('*** ////congragulation//// you win ***')


   elif user == 1 and system =='rock':
      print('*** you choiced rock and system same rock ***\n')
      print('*** equal ***')

#if user == 'paper':
    


   if user == 2 and system =='paper':
      print('*** you choiced paper and system same paper ***\n')
      print('*** equal ***')

   elif user == 2 and system =='scissor':
      print('*** you choiced paper and system scissor ****\n')
      print('*** system win ***')


   elif user == 2 and system =='rock':
      print('*** you choiced paper and system  rock ***')
      print('*** ////congragulation//// you win ***\n')


   if user == 3  and system =='paper':
      print('*** you choiced scissor and system  paper ***')
      print('*** ////congragulation//// you win ***\n')

   elif user == 3  and system =='scissor':
      print('*** you choiced scissor and system same scissor ****')
      print('*** equal ***\n')


   elif user == 3 and system =='rock':
      print('*** you choiced scissor and system  rock ***')
      print('*** system win ***\n')


   print('*** do you wanna play again ? \n')
   x = input('1.yes 2.no = ')

   if x == 2 or x == 'no':
     break


print('*** thanks for your play ***')
