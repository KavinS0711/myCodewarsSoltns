class Ghost(object):  
    def __init__(self):
        import random
        x = random.randint(0,3)
        l = ["white","yellow","purple","red"]
        self.color = l[x]