#Shakespeare insult script
import random


print "Welcome to the shakespeare insult script. Press any key to generate a new insult, or press control-c (command-c) to end\n"

#column_one = open("shakecol1.txt", 'rb')
#column_two = open("shakecol2.txt", 'rb')
#column_three = open("shakecol3.txt", 'rb')

#list_one = column_one.readlines()
#list_two = column_two.readlines()
#list_three = column_three.readlines()

#print "list one: %r" % list_one
#print "list two: %r" % list_two
#print "list three: %r" % list_three

list_one = ['artless\n', 'bawdy\n', 'beslubbering\n', 'bootless\n', 'churlish\n', 'cockered\n', 'clouted\n', 'craven\n',
'churrish\n', 'dankish\n', 'dissembling\n', 'droning\n', 'errant\n', 'fawning\n', 'fobbing\n', 'froward\n', 'frothy\n',
'gleeking\n', 'goatish\n', 'gorbellied\n', 'impertinent\n', 'infectious\n', 'jarring\n', 'loggerheaded\n', 'lumpish\n',
'mammering\n', 'mangled\n', 'mewling\n', 'paunchy\n', 'pribbling\n', 'puking\n', 'puny\n', 'qualling\n', 'rank\n', 'reeky\n',
'roguish\n', 'ruttish\n', 'saucy\n', 'spleeny\n', 'spongy\n', 'surly\n', 'tottering\n', 'unmuzzled\n', 'vain\n', 
'venomed\n', 'villainous\n', 'warped\n', 'wayward\n', 'weedy\n', 'yeasty\n']

list_two = ['base-court\n', 'bat-fowling\n', 'beef-witted\n', 'beetle-headed\n', 'boil-brained\n', 'clapper-clawed\n', 
'clay-brained\n', 'common-kissing\n', 'crook-pated\n', 'dismal-dreaming\n', 'dizzy-eyed\n', 'doghearted\n', 'dread-bolted\n', 
'earth-vexing\n', 'elf-skinned\n', 'fat-kidneyed\n', 'fen-sucked\n', 'flap-mouthed\n', 'fly-bitten\n', 'folly-fallen\n', 
'fool-born\n', 'full-gorged\n', 'guts-griping\n', 'half-faced\n', 'hasty-witted\n', 'hedge-horn\n', 'hell-hated\n',
'idle-headed\n', 'ill-breeding\n', 'ill-nurtured\n', 'knotty-pated\n', 'milk-livered\n', 'motley-minded\n', 'onion-eyed\n', 
'plume-plucked\n', 'pottle-deep\n', 'pox-marked\n', 'reeling-ripe\n', 'rough-hewn\n', 'rude-growing\n', 'rump-fed\n', 'shard-borne\n', 
'sheep-biting\n', 'spur-galled\n', 'swag-bellied\n', 'tardy-gaited\n', 'tickle-brained\n', 'toad-spotted\n', 'unchin-snouted\n', 'weather-bitten\n']


list_three = ['apple-john\n', 'baggage\n', 'barnacle\n', 'bladder\n', 'boar-pig\n', 'bugbear\n', 'bum-bailey\n', 'canker-blossom\n', 
'clack-dish\n', 'clotpole\n', 'coxcomb\n', 'codpiece\n', 'death-token\n', 'dewberry\n', 'flap-dragon\n', 'flax-wench\n', 'flirt-gill\n', 
'foot-licker\n', 'fustilarian\n', 'giglet\n', 'gudgeon\n', 'haggard\n', 'harpy\n', 'hedge-pig\n', 'horn-beast\n', 'hugger-mugger\n', 
'joithead\n', 'lewdster\n', 'lout\n', 'maggot-pie\n', 'malt-worm\n', 'mammet\n', 'measle\n', 'minnow\n', 'miscreant\n', 'moldwarp\n', 
'mumble-news\n', 'nut-hook\n', 'pigeon-egg\n', 'pignut\n', 'puttock\n', 'pumpion\n', 'ratsbane\n', 'scut\n', 'skainsmate\n', 'strumpet\n', 
'varlot\n', 'vassal\n', 'whey-face\n', 'wagtail\n']

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
	
#raw_input("press any key...")