print('''               Welcome To FB-Bruteforce-Attack
           This Tool Is Created By Ravneet Waraich
       Please do not spam it, It's Just For Knowledge ...
                     Happy Hacking Day ! 
           
           
           ''')
abc = input("Enter Victim Facebook Registered Email or Mob. : ")
if abc == "" : print("Enter Valid Mob. or Email !") 
if abc == " " : print("Enter Valid Mob. or Email !")
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint("Trying To Hack : " + abc)
slowprint("Trying Password 1 : ******** : Failed")
slowprint("Trying Password 2 : ******** : Failed")
slowprint("Trying Password 3 : ******** : Failed")
slowprint("Trying Password 4 : ******** : Failed")
slowprint("Trying Password 5 : ******** : Failed")
slowprint("Trying Password 6 : ******** : Failed")
slowprint("Trying Password 7 : ******** : Failed")
slowprint("Trying Password 8 : ******** : Failed")
slowprint("Trying Password 9 : ******** : Failed")
slowprint("Trying Password 10 : ******** : Failed")
slowprint("Trying Password 11 : ******** : Failed")
slowprint("Trying Password 12 : ******** : Passed")
slowprint("Account Hacked ! ")
print("Are You Sure To See Password : "   )
while True:
    a = input("Enter Y/n to continue : ")
    if a=="Y": print("Your Password Is : Rautg@20211")
    if a=="y": print('''Error !
Please Type Capital Y''')

    elif a=="n": print("Thanks For Using FB-Bruteforce-Attack")
    elif a=="N": print('''Error !
Please Enter Small n !''')
    break 
else:
        print("Enter either y/n")
