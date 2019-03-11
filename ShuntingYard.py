# Michael Coleman
# Shunting Yard Algorithm

# function shunt
def shunt(infix):
    
    #set up variables
    specials = {'*' : 50,'.' : 40,'|' : 30}
    
    pofix = ""
    stack = ""


            