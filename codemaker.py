import random

class code_maker:
	
	def __init__(self,possible_colours):
		self.code=[]
		for i in range(4):
			self.code.append(random.choice(possible_colours))
		
	def response(self,code_breaker_code):
		response=[]
		temp=code_breaker_code.copy()
		code_temp=self.code.copy()
		for i in range(len(code_temp)):
			if(code_temp[i]==temp[i]):
					response.append('Red')
					temp[i]='Done'
					code_temp[i]='Done'

		for i in code_temp:
			if(i in temp and i!='Done'):
				response.append('White')
				temp[temp.index(i)]='Done'
				code_temp[code_temp.index(i)]='Done'
		
		while(len(response)<4):
			response.append('Empty')
		
		random.shuffle(response)
		return response



