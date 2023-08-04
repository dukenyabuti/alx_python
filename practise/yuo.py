class Robot:
    def __init__(self, 
                 name=None,
                 build_year=None):
        self.name = name
        self.build_year = build_year
    def say_hi(self):
        if self.name:
            print("Hi I am " + self.name)
        else:
            print("Hi, I am a robot without name")
        if self.build_year:
            print("i was built in " + str(self.build_year))
        else:
            print("I dont know when I was built")
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_build_year(self, by):
        self.build_year = by
    def get_build_year(self):
        return self.build_year
x = Robot("Henry", 2008)
y = Robot()
y.set_name("mafin")
x.say_hi()
y.say_hi()

