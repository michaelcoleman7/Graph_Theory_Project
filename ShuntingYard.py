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
            while stack[-1] != '(':
                pofix ,stack = pofix + stack[-1], stack[:-1]
                
            # remove the last character again to remove the ) from the stack
            stack = stack[:-1]
            
        # if character is in specials e.g. '*','.' or '|'
        elif c in specials:
            # while stack is not empty, Check Precedence of special character from infix
            # and compare with last character on stack
            # while c is less than last character on stack, add last character on stack onto pofix
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
                
            # Add c to stack
            stack = stack + c
        else:
            # Add c to pofix
            pofix = pofix + c
            
    # add remaining characters onto pofix    
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
              
    return pofix
    
print(shunt("(a.b)|(c*.d)"))


            