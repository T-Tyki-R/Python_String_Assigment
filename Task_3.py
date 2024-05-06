#   Interactive Help Desk Bot

support_bot = ["help", "issue", "contact support"]
further_support_bot = ["login","performance","error"]

def support_service(support_bot, further_support_bot):
        print("\tMenu Option\n\t------------\nhelp\nissue\ncontact support\n")
        user_in = input("Hello, I am Help_Bot! How can I help you today? ")
        for i in support_bot:
            i = user_in.lower()
            if i == "help":
                return "Certainly! Please tell me how I can be of assistance..."
            elif i == "issue":
                print("\nlogin\nperformance\nerror\n")
                user_in2 = input("Which of the following can I further assist you in? ")
                for x in further_support_bot:
                    x = user_in2.lower()
                    if x == "login":
                        return "I'll send you over to someone who can help you further..."
                    elif x == "performance":
                        return "Certainly, I'll connect you with a tech support rep..."
                    elif x == "error":
                        return "Please enter the error code that is displayed..."
            elif i == "contact support":
                return "Please hold as I connect you with an agent..."
            else:
                return "You entered an invalid option"

                

print(support_service(support_bot, further_support_bot))