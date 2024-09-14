class Automaton:
    def __init__(self, n, m, start_states, finish_states, transitions):
        self.n = n
        self.m = m
        self.start_states = set(start_states)
        self.finish_states = set(finish_states)
        self.transitions = transitions

    def accepts(self, string):
        current_states = self.start_states
        for symbol in string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            current_states = next_states
        return bool(current_states & self.finish_states)

def read_automaton(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        n = int(lines[0])
        m = int(lines[1])
        start_states = list(map(int, lines[2].split()))
        finish_states = list(map(int, lines[3].split()))
        transitions = {}
        for line in lines[4:]:
            parts = list(map(int, line.split()))
            state, symbol, next_state = parts[0], parts[1], parts[2]
            if (state, symbol) not in transitions:
                transitions[(state, symbol)] = []
            transitions[(state, symbol)].append(next_state)
    return Automaton(n, m, start_states, finish_states, transitions)

def test_1():
    automaton = Automaton(5, 2, [0, 2, 3], [0, 2, 3], {
        (2, '2'): [4],
        (3, '0'): [1]
    })
    assert automaton.accepts('2') == False
    print("Ok")

def test_2():
    automaton = Automaton(3, 2, [0], [0, 1], {
        (0, 'a'): [0],
        (2, 'a'): [2],
        (2, 'b'): [2],
        (0, 'b'): [1],
        (1, 'b'): [1],
        (1, 'a'): [2]
    })
    assert automaton.accepts('aabbb') == True
    assert automaton.accepts('bab') == False
    print("Ok")
    
def test_3():
    automaton = Automaton(4, 2, [0], [3], {
        (0, 'a'): [0,1],
        (0, 'b'): [0],
        (1, 'a'): [2],
        (1, 'b'): [2],
        (2, 'b'): [3],
        (2, 'a'): [3]
    })
    assert automaton.accepts('aaa') == True
    assert automaton.accepts('aaaaa') == True
    assert automaton.accepts('aa') == False
    assert automaton.accepts('bab') == False
    print("Ok")

def main():

    test_1()
    test_2()
    test_3()

    automaton = read_automaton('input.txt')
    test_string = input("Введите строку ")
    if automaton.accepts(test_string):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
