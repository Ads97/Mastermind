class board:
	
	def __init__(self,code=[],codebreaker_code=[],response=[]):
		self.codemaker_code=code
		self.codebreaker_code=codebreaker_code
		self.response=response

	def end_game(self):
		if(self.response==['Red','Red','Red','Red']):
			return 1
		else:
			return 0

	def print_board(self):
		print('Code maker\'s code',self.codemaker_code)
		if(self.codebreaker_code):
			for i in self.codebreaker_code:
				print('CodeBreaker\'s code',i)
				print('Response',self.response[self.codebreaker_code.index(i)])

		




