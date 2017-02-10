users = []
cohort = {}
def main():
	
	print("Welcome!")
	AskUserToAdd()


		

def AskUserToAdd():
	print("Press enter to exit")
	user = input("What is your Name? ")

	skill = input('What skill do you want to add? ')
	if skill == "":
		print("ByeBye ", user)
		return False
	learnt = input("Have you learnt this skill yet? ('Answer with 'True' or 'False' ) ")
	learnt = learnt.lower()
	addSkill(skill, learnt)
	
	
	while True:
		
		skill = input('What skill do you want to add? ')
		if skill != "":
			learnt = input("Have you learnt this skill yet? ('Answer with 'True' or 'False' ) ")
			learnt = learnt.lower()
			addSkill(skill, learnt)
			
			
		else:
			print("Saved successfully")
			
			main()
			
		
def addSkill(skill, learnt):
	if learnt == "true":
		learnt = True
	elif learnt == "false":
		learnt = False
	cohort[skill] = learnt


		
if __name__ == '__main__':
	main()
