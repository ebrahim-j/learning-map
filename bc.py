foo = {'skill1':True, 'skill2':False, 'skill3':True}
print "1.Add skill "
print "2.View skills"
print "3.Mark complete"
print "4.View Studied"
print "5.view Unstudied"
choice = raw_input("what do you want to do?")

nlist = []

def view_skills():
    print foo.keys()

def view_studied():
    for key, value in foo.iteritems():
        if value == True:
            nlist.append(key)
    print nlist

def view_unstudied():
    for key, value in foo.iteritems():
        if value == False:
            nlist.append(key)
    print nlist

if choice == "1":
    '''hello'''
elif choice == "2":
    view_skills()
elif choice == "3":
    '''hello'''
elif choice == "4":
    view_studied()
elif choice == "5":
    view_unstudied()
else:
    print "invalid input"




