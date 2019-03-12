# Michael Coleman
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
            nfastack.append(nfa.initial, nfa2.accept)
        elif c =='|':
            # Pop two NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #Create a new initial state, connect it to initial state
            # of the two NFA's popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            intiial.edge2 = nfa2.initial
            #create a new accept state, connecting the accept states
            # of the two NFA's popped from the stack, to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            # push new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c =='*':
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial, accept))
    





            