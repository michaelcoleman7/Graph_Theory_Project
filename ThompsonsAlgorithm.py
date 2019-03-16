# Michael Coleman
# Thompson's Algorithm

# Shunt Function
def shunt(infix):
    """The Shunting Yard Algorithm for converting infix regular expressions to postfix"""
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
    
# Thompson's Algorithm
class state:
    label = None
    edge1 = None
    edge2 = None
    
class nfa:
    initial = None
    accept = None
    
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

# Compile Function
def compile(pofix):
    nfastack = []
    
    for c in pofix:
        if c == '.':
            # Pop two NFA's off stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # Connect first NFA's accept state to the seconds initial
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack
            newfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newfa)
            
        elif c =='|':
            # Pop two NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #Create a new initial state, connect it to initial state
            # of the two NFA's popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            #create a new accept state, connecting the accept states
            # of the two NFA's popped from the stack, to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            # push new NFA to the stack
            newfa = nfa(initial, accept)
            nfastack.append(newfa)
            
        elif c =='*':
            #Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Create new initial and accept states
            initial = state()
            accept = state()
            # Join the new initial state to nfa's initial state and new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # Join the old accept state to the new accept state and the nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack
            newfa = nfa(initial, accept)
            nfastack.append(newfa)
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            newfa = nfa(initial, accept)
            nfastack.append(newfa)
    
    # nfastack should only have a single nfa on it at this point
    return nfastack.pop()
    





            