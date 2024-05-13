# User Input Data Processor

#Task 1 Psuedocode

#   Create a func called nameChecker w/ 2 paras
#           check to see if both names are at least 2 characters long. 
#                if so, return names
#               if not, return an error message 

def nameChecker(fName, lName):
    return f"{fName} {lName}" if len(fName) >= 2 and len(lName) >= 2 else "First and last names must be 2 characters long..."

print(nameChecker("Tameka", "Roberson"))

#Task 2 Psuedocode

#   Create a func called passwordChecker w/ 1 para
#        Check if password is at least 8 characters long, has at least 1 upper and lowercase characters, and contains a number
#               if so, return an approval message        
#               if not, return an error message      

def password_checker(password):
    lowerCase = 'abcdefghijklmnopqrstuvwxyz'
    upperCase = lowerCase.upper()
    for i in range(len(password)):
        return f"{password} is an appropriate password\n" if len(upperCase[i]) >= 1 and len(lowerCase[i]) >= 1 and password[i].isalnum() and len(password) >= 8 else "Your password needs to have the following:\n8 or more characters\nAt least 1 uppercase character\nAt least 1 lowercase character\nAt least 1 number\n"

print(password_checker("python2")) #<---- fail
print(password_checker("Tam20eka")) #<----- pass


def email_format_checker(email):
    email = email.lower()
    local_part, domain_part = email.split('@', 1)
  
    if not local_part or not domain_part:
        return False
  
    if ' ' in local_part or ' ' in domain_part:
        return False
   
    if '.' not in domain_part or domain_part == '.':
        return False
    
    if not local_part.isalnum() and not domain_part.isalpha():
        return False
    
    return True
      
print(email_format_checker("abc111@xxx.com")) #<---- pass
print(email_format_checker("ffff@ddddcom"))#<---- fail