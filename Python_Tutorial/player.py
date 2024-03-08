"""
Module for the player
"""

def speak(person, message):
	print('{} : {}'.format(person, message))

def goodbye():
	print('Goodbye :)!')

speak('Ibba','Bonjour')
goodbye()