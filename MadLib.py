#MadLib.py
#Name: Gustavo Vargas
#Date: 1/28/2026
#Assignment: Lab 1 Madlib

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Give me a noun:")
  noun2 = input("Give me another noun:")
  verb1 = input("Give me a verb:")
  verb2 = input("Give me another verb:")
  adj1 = input("Give me an adjective:")
  adj2 = input("Give me another adjective:")
  #Print the story with the user supplied words.
  print("In the morning when i", verb1, "i am met with", noun1, ". The", adj1, "of", noun1, "was so weird, especially after seeing", noun2, "that it made me start ", verb2, "so much that i turned into a", adj2, "human.")
  

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()