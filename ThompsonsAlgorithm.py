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
        elif c =='*':
        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfastack.append(nfa(initial, accept))
    





            