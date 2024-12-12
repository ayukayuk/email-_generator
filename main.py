import random

def email_generator():
       name =["ayuk", "ako", "ruth", "rose", "tabe", "clara"]
       last_name = ["shiva", "frankline", "juith", "nicole"]
       erty = random.randint(0, 99)
       name_e = random.choice(name)
       ty = random.choice(last_name)
       tr =f'{name_e}{erty}@aycube.com'
       print(tr)
       
       print("print more")
       rt =input("types Y or N\n")
       
       if rt == "y":
              email_generator()
       else:
           quit()
email_generator()
