#FirstProgram.py
#Name: Gustavo Vargas
#Date: 01/28/2026
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name

  name = input("What is your name?: ")

  #Use the user's name in the program.
  print("Hello" , name)
  #Ask the user for their age.
  age = input("How old are you?: ")
  age = int(age)
  year = 2026 - age
  year = int(year)
  #Tell the user what year they were born in.
  print( "you were born in" , year - 1)
  
  
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
