import random
import os
from re import sub

def banner():
    print(f" __ __  __ _____ _  _   __   _____ ___  __ _____  ")
    print(f"|  V  |/  \_   _| || |/' _/ |_   _| __/' _/_   _| ")
    print(f"| \_/ | /\ || | | >< |`._`.   | | | _|`._`. | |   ")
    print(f"|_| |_|_||_||_| |_||_||___/   |_| |___|___/ |_|   ")


def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]]).capitalize()

user_stats = {}


def get_random_number(range):
	return random.randrange(range)

def multiply_number(first,second):
	return first * second

def add_number(first,second):
	return first + second

def subtract_number(first,second):
	return abs(first - second)
	
def calculate_answer_function(number, num1, num2):
	if number == 0:
		return multiply_number(num1, num2)
	if number == 1:
		return add_number(num1, num2)
	if number == 2:
		return subtract_number(num1, num2)

def get_operator_function(number):
	if number == 0:
		return 'x'
	if number == 1:
		return '+'
	if number == 2:
		return '-'
	

def greet_person():
	name = input('Hi - What is your name? ').upper()
	if user_stats.get( name ) == None :
		print(f'I see you have not played before, welcome {name}')
		user_stats[name]=0
	else:
		print(f'Welcome back {camel_case(name)}, Your current score is {user_stats[name]}')
	
	return name

def quiz(name):
	max_range=13
	rand_function_number = get_random_number(3)
	if rand_function_number > 0:
		max_range=100
	num1 = get_random_number(max_range)
	num2 = get_random_number(max_range)
	
	correct_answer = calculate_answer_function(rand_function_number, num1, num2)

	while (True):
	
		their_answer = input(f'What is {num1} {get_operator_function(rand_function_number)} {num2} ? ')
		if their_answer != '' and their_answer.isnumeric():
			break
		else:
			print('Invalid input! Please type a number only')
		
	 
	if correct_answer == int(their_answer):
		print(f'Correct! Well done {camel_case(name)} ')
		add_point(name)
	else:
		print(f'Incorrect! The correct answer was {correct_answer}. You guessed incorrectly with {their_answer}')
	return False



def add_point(name):
    current_score = user_stats.get(name)
    new_score = current_score + 1
    user_stats.update( {name: new_score})
    print(f'`--- Your current score is {user_stats[name]}')

def play_again(name):
	response = input(f'Do you want to play again, {camel_case(name)} ? Type [Y] or [N] ')
	if response.lower() == 'y':
		return True
	
	return False

def write_scores():
	open(".maths_scores.txt", 'w').close()
	f = open(".maths_scores.txt", "a")
	for key,value in user_stats.items():
		f.write(f'{key},{value}\n')
	f.close()
	
def read_scores():
	f = open(".maths_scores.txt", "r")
	contents = f.readlines()
	for content in contents:
		items = content.split(',')
		key=items[0]
		value=int(items[1])
		user_stats[key] = value
	#print()
	print(f' =+= The Leaderboard =+= ')
	for key,value in  sorted(user_stats.items(), key=lambda item: int(item[1]) , reverse=True):
		print(f'   {camel_case(key)} : {value}')
			

clear = lambda: os.system('cls')
clear()
banner()

print(f'\n')
print(f'\n')
print(f'-----------------------------------------------------------------------------------')
print(f'Welcome to Kurian\'s home written maths test, made in Python programming language  ')
print(f'-----------------------------------------------------------------------------------\n')
print(f'\n')

read_scores()
print(f'\n')

name = greet_person()

quiz(name)

while (play_again(name)):
	quiz(name)

write_scores()

print('Thanks for playing, Bye!\n')
read_scores()


