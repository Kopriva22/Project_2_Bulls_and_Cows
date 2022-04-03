import random
import string
import csv
import pandas as pd

#Hlavni funkce programu
def main(player_name:str,number_length:int):
  # Definovani promennych
  SEPARATOR = '-' * 40
  guess_number_trully_enter = True        #pro while cyklus pri testovani spravneho zadani cisla
  guess_number_entered = True             #pro while cyklus pri testovani na opakovani znaku
  csv_header = ["number","bulls","cows"]

  #Privitani hosta a uvod do hry  
  welcome(player_name,SEPARATOR,number_length)

  #Generovani nahodneho cisla pro hadani
  random_choice_number(number_length)
  print(f"{random_number} - kontrolni tisk")  #Kontrolni tisk overeni cisla - bude zakomentovano
  
  #Zapis hlavicky do vysledneho csv souboru
  with open("results.csv","w+",newline="") as file:
    writer = csv.DictWriter(file,csv_header)
    writer.writeheader()

  #Hlavni cyklus pro zadani, provereni a vyhodnoceni zadaneho cisla
  while guess_number_entered:
    print(SEPARATOR, end="\n")
    guess_number = input('Enter the number: ')
    guess_number_trully_enter = guess_number_verification(number_length,guess_number,guess_number_trully_enter)
    guess_number_counter = guess_number_same_digits(guess_number)
    
    #Rozhodovani, zda-li je cislo zadano spravne
    if guess_number_trully_enter or guess_number_counter:
      continue
    else:
      guess_number_entered = False
      pass

    #Porovnání čísel a zapis do souboru
    compare(random_number,guess_number)
    singular_plural_number(bulls,cows)
    print(f'{bulls_description}  {bulls}  and  {cows_description}  {cows}')
    csv_file_write(csv_header, guess_number,bulls,cows)
    
    #Ukonceni programu na zaklade zadani q
    konec = input("Pokud si přejete ukončit hadani, zadejte Q, jinak zadejte cokoliv jineho: ").lower()
    if konec == "q":
      data = pd.read_csv("results.csv")
      print(
        data[["number","bulls","cows"]].round(0),
        SEPARATOR,
        data.describe().round(2),
        sep="\n")
      
      ukonceni = input("Pro konec programu zvolte e: ").lower()
      
      if ukonceni == "e":
        print("Ukončení hry! Děkujeme Vám!")
        quit()
      else:
        pass 

    else:
      guess_number_entered = True
  

#Funkce definujici privitani hosta a uvod do hry 
def welcome(name,SEPARATOR,length):
  print(
    SEPARATOR, 
    f'Hi {name.title()},',
    'Welcome to the BULLS & COWS GAME!',
    f'I have generated a random {length} digits number for you.', 
    "Try your luck. Let's play!",
    SEPARATOR,
    sep='\n'
  )

#Funkce pro náhodný výběr čísla
def random_choice_number(length:int):
  global random_number
  number = list(string.digits)
  random_number = ''
  #Sestaveni nahodneho cisla
  for index in range(length):
    random_number+= random.choice(number)
    while random_number[0] == '0':
      random_number.replace('0',random.choice(number))
      number.append('0')
    number.pop(number.index(random_number[index]))
  #Vrati string random_number
  print(f"{number} - nevybrana cisla - kontrolní tisk")       #Kontrolni tisk
  return random_number 

#Funkce pro overeni zadaneho cisla (znaky misto cisel, delsi/kratsi cislo, cislo zacina nulou)
def guess_number_verification(number_length,guess_number, guess_number_trully_enter):
  if not guess_number.isnumeric():
    print('Not all entered symbols are digits.')
  elif len(guess_number) < number_length:
    print('You have entered less digits.')
  elif len(guess_number) > number_length:
    print('You have entered more digits.')
  elif guess_number[0] == '0':
    print('Your number starts with ZERO.')
  else:
    guess_number_trully_enter = False
  
  return guess_number_trully_enter

#Funkce pro overeni vyskytu ruznych cisel
def guess_number_same_digits(guess_number:str):
  counter = 0
  for a in range(0,len(guess_number)-1):
    for b in range(a+1,len(guess_number)):
      if guess_number[a] == guess_number[b]:
        print(
          f'Your number contains 2 same numbers at positions',
          f'{a+1} and {b+1}.',
          )
        counter += 1
  if counter > 0:
    guess_number_counter = True
  else:
    guess_number_counter = False

  return guess_number_counter 


#Funkce pro porovnani cisel a urceni poctu bulls and cows
def compare(random_number,guess_number):
  global bulls,cows,csv_header
  bulls,cows = 0,0
  for index in range(len(guess_number)):
    if guess_number[index] == random_number[index]:
      bulls += 1
    else:
      for c in range(len(guess_number)):
        if guess_number[index] == random_number[c] and (index != c):
          cows += 1
  
  return bulls, cows

def singular_plural_number(bulls,cows):
  global bulls_description, cows_description
  if bulls == 1:
    bulls_description = "bull"
  else:
    bulls_description = "bulls"

  if cows == 1:
    cows_description = "cow"
  else:
    cows_description = "cows"
  
  return bulls_description, cows_description

def csv_file_write(csv_header,guess_number,bulls,cows):
  
  row = {"number":guess_number, "bulls":bulls, "cows":cows} 

  with open("results.csv","a+",newline="") as file:
    writer = csv.DictWriter(file,csv_header)
    writer.writerow(row)