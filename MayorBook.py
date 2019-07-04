#Simple searchable addressbook in python
print("""
      \t ---------------------Welcome to Mayor's Book----------------------
      \t
      \t--------------------------------------------------------------------
      """)

def displayuserinfo (userinfo):
    print("\t---------------------------------")
    print("\t!! Match found for ", userinfo[0], "", userinfo[1], "!!")
    print("\tFirst Name: ", userinfo[0])
    print("\tLast Name: ", userinfo[1])
    print("\tAddress: ", userinfo[2])
    print("\tEmail: ", userinfo[3])
    print("\tPhone No.: ", userinfo[4])
    print("\tWork Phno.: ", userinfo[5])
    print("\t---------------------------------")
    return

firstname=""
lastname=""
entryfound=""

#-------------------Getting User Input--------------------------
while firstname!="quit":
    firstname=input("Enter your First Name (quit to exit):")
    firstname=firstname.lower()
    
    if firstname=="quit":
        break
    else:
        lastname=input("Enter your Last Name:")
        lastname=lastname.lower()
        
#--------------------Checkadress Book-----------------------------
        
        addressbook=open("C:/Users/Pankhuri Trikha/Documents/MayorBook.txt",'r')
        for line in addressbook:
            userinfo=line.split("|")
            if((userinfo[0].lower()==(firstname or firstname.lower)) and (userinfo[1].lower()==(lastname or lastname.lower))):
                entryfound=True
                break
            else:
                entryfound=False
                continue
            
#------------------Display Data---------------------------------
                
    if entryfound==False:
        print("Sorry !! The firstname and lastname doesn't exists")
    else:
        displayuserinfo(userinfo)
    addressbook.close()
    entryfound=""
            
        

        

