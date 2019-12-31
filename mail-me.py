from fedora.client.fas2 import AccountSystem
from termcolor import colored

def main():
  my_account=AccountSystem(username='YOUR_USERNAME',password='YOUR_PASSWORD')    #initializing the account
  username=input(colored("[#]please enter the username you want to search for---->","green"))     
  if method2(my_account,username) != "USERNAME NOT FOUND":                    #well..you can change the method if you want,the results are the same
     print(colored("[-]here is his email:-->>> "+ method2(my_account,username),"yellow"))
  else:
     print(colored(method2(my_account,username)+"\n","red"))
def method1(account,user):
 try:
   val=account.person_by_username(user)
   return str(val['email'])
 except:
    return "USERNAME NOT FOUND"
def method2(account, user):
 try:
   val=account.people_by_key(key='email', search=user, fields=['id'])
   return  str(val).split('(')[1].split(':')[0][3:][:-1]      #magic code :)
 except:
   return "USERNAME NOT FOUND"
if __name__=='__main__':
   main()
