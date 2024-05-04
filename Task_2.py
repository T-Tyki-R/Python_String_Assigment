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

def passwordChecker(password):
    lowerCase = 'abcdefghijklmnopqrstuvwxyz'
    upperCase = lowerCase.upper()
    for i in range(len(password)):
        return f"{password} is an appropriate password" if len(upperCase[i]) >= 1 and len(lowerCase[i]) >= 1 and password[i].isalnum() and len(password) >= 8 else "Your password needs to have the following:\n8 or more characters\nAt least 1 uppercase character\nAt least 1 lowercase character\nAt least 1 number"

print(passwordChecker("python2")) #<---- fail
print(passwordChecker("Tam20eka")) #<----- pass

#Task 3 Psuedocode

#   Create a func called emailFormatChecker w/ 1 para
#      Define 2 vars = character and number
#        Check if password is at least 8 characters long, has at least 1 upper and lowercase characters, and contains a number
#               if so, return an approval message        
#               if not, return an error message      

def emailFormatChecker(email):
    char_At_Symbol = "@"
    char_Dot_Symbol = "."
    domainNames = ["com", "net"]

    for i in email: #<- also tried range(len(email))
        # return "You entered a valid email address" if email[i].isalnum() and char_At_Symbol[i] in email[i] and char_Dot_Symbol[i] in email[i] and domainNames[i] in email[i] else "You entered an invalid email address..."
        return "You entered a valid email address" if email.isalnum() and char_At_Symbol in email and char_Dot_Symbol in email and domainNames[i] in email else "You entered an invalid email address..."

#^ Getting else condition as the return?

        
print(emailFormatChecker("tamekaR2@xxxx.net")) #<---- pass