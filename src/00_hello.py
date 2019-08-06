# Print "Hello, world!" to your terminal
# print("Hello World!")

# a = 10

# def foo(x):
#     a = 5 #Tell python that "a" is a global
#     return x + a

# print((foo(2))) #7
# print(a) #10
##########################################
# def foo(x):
#     total = 0
    
#     def bar(y):
#         nonlocal total #Backup level of scope, use the second one
#         total += y
        
#     for i in range(x):
#         bar(i)
        
#     return total
# print(foo(2))

##########################################

#Variables are either global or function-local.
#Since there are no declarations, there's no block-level scope.

##########################################

class Animal:
    def __init__(self): #constructor
      self.leg_count = 4
      
    def get_leg_count(self):
        return self.leg_count
    
    def sef_leg_count(self, c):
        self.leg_count = c

class Centipede(Animal): #inheritance
    def __init__(self): #constructor
      self.leg_count = 100
      
a = Animal() #construct a new animal instance

a.set_leg_count(6)
print(a.get_leg_count())

c = Centipede()
print(c.get_leg_count())

  