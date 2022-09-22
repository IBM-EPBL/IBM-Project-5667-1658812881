import random
#temperature generation
t=random.randint(1,300)
#humidity generation
h=random.randint(1,50)
if(t>150):
    print("ALERT!, Temperature is High")
else:
    print("NORMAL, Temperature is Fine")
