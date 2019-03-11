# Michael Coleman
# Shunting Yard Algorithm

# function shunt
def shunt(infix):
    
    #set up variables
    specials = {'*' : 50,'.' : 40,'|' : 30}
    
    pofix = ""
    stack = ""
    
    #for loop running through each character in infix
    for c in infix:
        #if character = ( , then add to stack
        if c == '(':
            stack = stack + c
        # if character = ) , then remove each item on stack until ( is encountered
        elif c == ')':
            while stack[-1] != '('
                pofix ,stack = pofix + stack[-1], stack[:-1]
            # remove the last character again to remove the ) from the stack
            stack = stack[:-1]


            