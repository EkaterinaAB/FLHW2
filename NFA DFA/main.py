class Automaton:
    def __init__(self, n, m, start_states, accept_states, transitions):
        self.n = n
        self.m = m
        self.start_states = set(start_states)
        self.accept_states = set(accept_states)
        self.transitions = transitions

    def accepts(self, string):
        current_states = self.start_states
        for symbol in string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            current_states = next_states
        return bool(current_states & self.accept_states)

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

def test_automaton():
    automaton = Automaton(5, 2, [0, 2, 3], [0, 2, 3], {
        (2, '2'): [4],
        (3, '0'): [1]
    })
    assert automaton.accepts('2') == False
    assert automaton.accepts('20') == True
    assert automaton.accepts('202') == False
    assert automaton.accepts('200') == True
    print("Все тесты пройдены!")

def main():
    automaton = read_automaton('input.txt')
    test_string = input("Введите строку для проверки: ")
    if automaton.accepts(test_string):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()

test_automaton()
