import random
import itertools

class code_breaker:

	def __init__(self,possible_colours):
		self.set_of_codes=[]
		self.possible_set=[list(p) for p in itertools.product(possible_colours,repeat=4)] #Step 1 of the algorithm
		first_code=random.choice(self.possible_set)
		self.possible_set.remove(first_code)
		self.set_of_codes.append(first_code)

	def check_response(self,pattern,response):
		pattern_response=[]
		temp=pattern.copy()
		code_temp=self.set_of_codes[-1].copy()
		for i in range(len(code_temp)):
			if(code_temp[i]==temp[i]):
					pattern_response.append('Red')
					temp[i]='Done'
					code_temp[i]='Done'

		for i in code_temp:
			if(i in temp and i!='Done'):
				pattern_response.append('White')
				temp[temp.index(i)]='Done'
				code_temp[code_temp.index(i)]='Done'
		
		while(len(response)<4):
			pattern_response.append('Empty')
		
		pattern_response=sorted(pattern_response)
		response=sorted(response)

		return pattern_response==response

	def solve(self,response):
		#algorithm
		#Step 1: Start with a set of all possible combinations.
		#Step 2: Take a random guess from the set you're currently using. Send the guess as your pattern. Remove this guess from your set. 
		#Step 3: Look at the response to the pattern. If it is all red, you've won and your pattern was correct. 
		#Step 4: If not, choose all those patterns in your set which give you the same response to YOUR pattern. This is your new set. 
		#Step 5: Repeat step 2 
		for pattern in self.possible_set:
			if(self.check_response(pattern,response)):
				continue
			else:
				self.possible_set.remove(pattern)
		guess=self.minimax()
		self.possible_set.remove(guess)
		self.set_of_codes.append(guess)
		print(len(self.possible_set))

		return guess

	def minimax(self):
		
		return pattern



		
