nlist = []
mlist =[]

foo = {}
def main():
	

	print ("1.Add skill")
	print ("2.View skills")
	print ("3.Mark complete")
	print ("4.View Studied")
	print ("5.view Unstudied")
	print ("6.Exit")
	
	choice = input("what do you want to do?")

	if choice == "1":
		AskUserToAdd()
	elif choice == "2":
		view_skills()
	elif choice == "3":
		AskUserToAdd()
	elif choice == "4":
		view_studied()
	elif choice == "5":
		view_unstudied()
	elif choice =="6":
		exit()
	else:
		print ("invalid input")
		


		

def AskUserToAdd():
	print("Press enter to exit")
	#user = input("What is your Name? ")

	skill = input('What skill do you want to add? ')
	if skill == "":
		print("ByeBye ", user)
		main()
		return False
	learnt = input("Have you learnt this skill yet? ('Answer with 'True' or 'False' ) ")
	learnt = learnt.lower()
	addSkill(skill, learnt)
	main()
	
	
	'''while True:
		
		skill = input('What skill do you want to add? ')
		if skill != "":
			learnt = input("Have you learnt this skill yet? ('Answer with 'True' or 'False' ) ")
			learnt = learnt.lower()
			addSkill(skill, learnt)
			
			
		else:
			print("Saved successfully")
			
			main()'''
			
		
def addSkill(skill, learnt):
	if learnt == "true":
		learnt = True
	elif learnt == "false":
		learnt = False
	foo[skill] = learnt
	
def view_skills():
    print (foo.keys())
    main()

def view_studied():
    for key in foo:
        if foo[key] == True:
            mlist.append(key)
    print (mlist)
    main()

def view_unstudied():
    for key in foo:
        if foo[key] == False:
            nlist.append(key)
    print (nlist)
    main()

		
if __name__ == '__main__':
	main()

