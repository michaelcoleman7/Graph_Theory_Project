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

print(compile("ab.cd.|"))
    





            