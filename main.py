import functions

input_data = True

#Testovani zadanych vstupu - poctu zadanych cifer pro hadane cislo
while input_data:

  player = input('Hello my guest. Please, enter your name: ')
  if player.isalnum() == True:
    pass
  else:
    print("Enter your name again!")
    continue

  try:
    number_length = int(input('Please, enter the number of digits (min 4 a max. 9) for the searched word: '))
    assert 3 < number_length <= 9
  except AssertionError:
    print("The number is not in interval of numbers 4 and 9! Enter the number again:")
  except ValueError:
    print("Enter the number again!")
  else:
    input_data = False
    print("Thank you for entered data.")

functions.main(player, number_length)