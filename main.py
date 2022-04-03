import functions

input_data = True

#Testovani zadanych vstupu - poctu zadanych cifer pro hadane cislo
while input_data:
  try:
    player = input('Hello my guest. Please, enter your name: ')
    number_length = int(input('Please, enter the number of digits (min 4 a max.10) for the searched word: '))
    assert 3 < number_length <= 9
  except AssertionError:
    print(f"Cislo neni v intervalu 4-9!")
  except ValueError:
    print("Zadej cislo znovu!")
  else:
    input_data = False
    print("Dekuji za zadana data!")

functions.main(player, number_length)
