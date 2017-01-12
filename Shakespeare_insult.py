#Shakespeare insult script
import random


print "Welcome to the shakespeare insult script. Press any key to generate a new insult, or press control-c (command-c) to end\n"

column_one = open("shakecol1.txt", 'rb')
column_two = open("shakecol2.txt", 'rb')
column_three = open("shakecol3.txt", 'rb')

list_one = column_one.readlines()
list_two = column_two.readlines()
list_three = column_three.readlines()

while 1 == 1:
	raw_input()
	word1_var = random.randint(1,50)
	first_word = list_one[word1_var]
	first_word = first_word.rstrip()

	word2_var = random.randint(1,50)
	second_word = list_two[word2_var]
	second_word = second_word.rstrip()

	word3_var = random.randint(1,50)
	third_word = list_three[word3_var]
	third_word = third_word.rstrip()

	print "\nThou %s, %s, %s!" % (first_word, second_word, third_word)

