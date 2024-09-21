import copy

class Automaton:
    def __init__(self, n, m, start_states, accept_states, transitions):
        self.n = n
        self.m = m
        self.start_states = set(start_states)
        self.accept_states = set(accept_states)
        self.transitions = transitions
        self.states_list=[list(sorted(start_states))]
        self.new_transitions={}
        self.new_accept_states = set()

    def check_if_finish_state(self,state):
        for sub_state in state:
            if sub_state in self.accept_states:
                self.new_accept_states.add(tuple(state))
                break
        
    def accepts(self):
        current_states = [tuple(sorted(list(self.start_states)))]
        new_current_states = []
        while len(current_states)!=0:
            for symbol in range (self.m):
                next_state = set()
                for state in current_states:
                    for sub_state in state:
                        if (sub_state, symbol) in self.transitions:
                            next_state.update(self.transitions[(sub_state, symbol)])
                    if len(next_state)!=0:
                        next_state_copy  = sorted(next_state)
                        self.check_if_finish_state( next_state_copy)
                        self.new_transitions[(state,symbol)]=tuple( next_state_copy)
                if  next_state_copy not in self.states_list:
                     self.states_list.append( next_state_copy)
                     new_current_states.append(tuple( next_state_copy))
            current_states= copy.deepcopy(new_current_states)
            new_current_states.clear()
            #print(current_states)
        return self.new_transitions

def read_automaton(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        n = int(lines[0])
        m = int(lines[1])
        start_states = list(map(int, lines[2].split()))
        accept_states = list(map(int, lines[3].split()))
        transitions = {}
        for line in lines[4:]:
            parts = list(map(int, line.split()))
            state, symbol, next_state = parts[0], parts[1], parts[2]
            if (state, symbol) not in transitions:
                transitions[(state, symbol)] = []
            transitions[(state, symbol)].append(next_state)
    return Automaton(n, m, start_states, accept_states, transitions)

def test():
    automaton = Automaton(3, 2, [0], [2], {
        (0, 0): [0,1],
        (0, 1): [ 0],
        (1, 1): [2]
    })
    
    correct_answer={((0,), 0): (0, 1),
((0,), 1): (0,),
((0, 1), 0): (0, 1),
((0, 1), 1): (0, 2),
((0, 2), 0): (0, 1),
((0, 2), 1): (0,)}
    
    res = automaton.accepts()
    
    assert  correct_answer==res 
    
    for key, value in res.items():
        print(f"{key}: {value}")

def main():
    test()

if __name__ == "__main__":
    main()

