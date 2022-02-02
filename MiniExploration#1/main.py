import random

class Display:
	def __init__(self, barlength, bars):
		self.screen = None
		self.barlength = barlength
		self.height = 9
		self.bar_amount = bars
		self.rows = []

	def create(self):
		for i in range(self.height):
		 	self.rows.append(Row(self.barlength, self.bar_amount)) #puts nine Row objects into list

		for i in range(len(self.rows)): #creates content of all objects, making the odd objects spaces
			if i % 2 == 1:
				self.rows[i].space()
			else:
				self.rows[i].line()

	def show(self): #prints each of the rows
		for row in self.rows:
			print("|"+row.get()+"|")


	def add_note(self, drum, measure, beat): #adds a drum to a specific beat in the music
		self.beat = beat
		self.measure = measure
		self.translate_note(drum)
		self.distance = int(self.measure*(1+self.barlength)+(self.beat*4-3)-(1+self.barlength)) #finds the index of the beat based on the measure, bar length, and beat of the measure.

		self.row_list = []
		for character in self.rows[self.line-1].contents: #breaks down string into a list to replace individual character
			self.row_list.append(character)
		self.row_list[self.distance] = self.symbol
		self.row_list_merge = ""
		for character in self.row_list: #repairs the altered list into a string
			self.row_list_merge += character
		self.rows[self.line-1].contents = self.row_list_merge #assigns the string

	def translate_note(self, drum): #returns the line of the staff that the character belongs on and the symbol representing it
		if drum == "HH":
			self.line = 1
			self.symbol = "X"
		elif drum =="SD":
			self.line = 4
			self.symbol = "0"
		elif drum == "KD":
			self.line = 8
			self.symbol = "0"

class Row: #row object - makes up the display
	def __init__(self, width, bar_amount):
		self.width = width
		self.contents = "|"
		self.bar_amount = bar_amount
	def line(self):
		for i in range(self.bar_amount):
			for i in range(int(self.width)):
				self.contents += "-"
			self.contents += "|"
	def space(self):
		for i in range(self.bar_amount):
			for i in range(int(self.width)):
				self.contents += " "
			self.contents += "|"
	def get(self):
		return(self.contents)

class Types:
	def __init__(self, beat, beat_type, complexity):
		self.beat = beat
		self.display = self.beat.display
		self.type = beat_type
		self.complexity = complexity
	def start(self):
		if self.type == "rock":
			self.rock()
		if self.type == "goofy":
			self.goofy()
	def rock(self): #interacts with the display to create a beat based on the complexity
		complexity_margin = int(0 + 5*self.complexity) #complexity affecting chances of beat placement
		self.true_chance = int(0 + complexity_margin)
		self.false_chance = int(100 - complexity_margin)

		self.quarter_highhat = random_boolean(self.true_chance, self.false_chance) #quarter note/eightnote rock
		for bar in range(1, self.beat.num_bars+1):
			for twobeat in range(2, 2*self.beat.beat+2):
				beat = twobeat/2
				if self.quarter_highhat == False:
					if int(beat) == float(beat):
						self.display.add_note("HH",bar,beat)
				else:
					self.display.add_note("HH",bar,beat)
				if beat == 1 or beat == 3:
					self.display.add_note("KD",bar,beat)
				else:
					self.bass_drum = random_boolean(self.true_chance, self.false_chance)
					if self.bass_drum == True:
						self.display.add_note("KD",bar,beat)
				if beat == 2 or beat == 4:
					self.display.add_note("SD",bar,beat)
				else:
					self.snare_drum = random_boolean(self.true_chance, self.false_chance)
					if self.snare_drum == True:
						self.display.add_note("SD",bar,beat)
				
				
	def goofy(self): #goofy beat
		complexity_margin = int(0 + 5*self.complexity) #complexity affecting chances of beat placement
		self.true_chance = int(0 + complexity_margin)
		self.false_chance = int(100 - complexity_margin)

		for bar in range(1, self.beat.num_bars+1):
			for twobeat in range(2, 2*self.beat.beat+2):
				beat = twobeat/2
				if random_boolean(self.true_chance, self.false_chance) == False:
					self.display.add_note("HH",bar,beat)
				if random_boolean(self.true_chance, self.false_chance) == True:
					self.display.add_note("SD",bar,beat)
				if random_boolean(self.true_chance, self.false_chance) == True:
					self.display.add_note("KD",bar,beat)

class Beat: #beat object with all of the information and accumlates 
	def __init__(self, timesignature =[], num_bars=0, beat_type="", complexity=0):
		self.beats = timesignature[0]
		self.beat = timesignature[1]
		self.num_bars = num_bars
		self.beat_type = beat_type
		self.complexity = complexity
		self.display = Display(self.beats*4, self.num_bars)
	def customize(self):
		self.display.create()
		type = Types(self, self.beat_type, self.complexity)
		type.start()


		# for bar in range(1, 9):
		# 	for beat in range(1, 5):
		# 		self.display.add_note("HH",bar,beat)
		# 		self.display.add_note("HH",bar,beat+0.5)

	def show(self):
		self.display.show()

	def unpack_type(self, data):
		pass


def random_boolean(True_chance, False_chance):
	if True_chance + False_chance != 100:
		print("true and false chance do not equal 100\n true:",True_chance,"\n false:",False_chance)
	else:
		random_number = random.randint(0, 100)
		if random_number <= True_chance: 
			return(True)
		else:
			return(False)

def space(number):
	for i in range(number):
		print("")
		
	

def main():
	space(10)
	print("Welcome to Drumming with Python!")
	space(2)
	style_choice = input("Would you like your drum beat to obey the basic structure of drumming? (Yes or No): ")
	if style_choice.lower() == "yes":
		style = "rock"
		space(1)
	elif style_choice.lower() == "no":
		style = "goofy"
		space(1)
	else:
		print("Please answer with Yes or No.")
		main()
	space(2)
	complexity_choice = input("How complex would you like your beat to be? (Enter an integer from 0-10 or type Random): ")
	if complexity_choice in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
		complexity = int(complexity_choice)
	elif complexity_choice.lower() == "random":
		complexity = random.randint(0, 10)
	else:
		print("Please enter a number from 0-10 or type 'random' for a random complexity")
		main()
	space(2)
	print("Finally, what time signature would you like your beat to be in? (First enter a integar for the numerator, hit enter, then enter an integar for the denomentator.")
	time_sig_num =int(input("Numerator: "))
	time_sig_den = int(input("Denomenator: "))
	space(2)
	print("Your beat is ready!")
	beat = Beat([time_sig_num, time_sig_den], 4, style, complexity)
	beat.customize()
	beat.show()
	space(2)
	print("This is a", style, "beat with complexity ", complexity)
	space(2)


main()
