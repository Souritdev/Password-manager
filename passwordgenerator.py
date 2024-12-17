from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
      key_file.write(key) '''


def load_key():
     file = open("key.key", "rb")
     key = file.read()
     file.close()
     return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()     # load key is getting stored as read bytes so transferring the master_pwd as bytes instead

fer = Fernet(key)



def view():
    with open('passwords.txt' , 'r') as f:
        for line in f.readlines():
           print(line.rstrip())
           data = line.rstrip()
           user , passw = data.split("|")
           print("User:", user , "| Password:",  
                 fer.decrypt(passw.encode()).decode())

def add():
    name = input ('Account Name: ')
    pwd =  input("Password: ")

    with open('passwords.txt', 'a') as f:
       f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
       
# a mode -> only can be read;
# r mode -> only can be read also;
# w mode -> only can be written
       

while True:
   mode = input("Would you like to add a new password or view the existing ones (view,add) , press q to quit? " ).lower()
   if mode == "q":
      break
   
   if mode == "view":
      view()
   elif mode == "add":
      add()
   else:
      print("Invalid Error!")
      continue



