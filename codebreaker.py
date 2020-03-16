import random

class code_breaker:

	def __init__(self,possible_colours):
		self.set_of_codes=[]
		first_code=[]
		for i in range(4):
			first_code.append(random.choice(possible_colours))
		self.set_of_codes.append(first_code)

	def solve(self,response):
		
		return ['Black', 'Dark_Blue','Light_Blue','Green']