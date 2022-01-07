infile = "../input/input.txt"

states = []
num_fish = 0    

def add_new_fish(n):
    global num_fish
    for _ in range(n):
        states.append(8)
        num_fish += 1

def set_next_state():
    global states
    n_fish = 0

    for i in range(len(states)):
        if states[i] == 0:
            n_fish += 1
            states[i] = 6
        else:
            states[i] -= 1

    add_new_fish(n_fish)

def set_n_state(n):
    for _ in range(n):
        set_next_state()

with open(infile) as file:
    states = file.readline().rstrip().split(',')
    states = [int(x) for x in states]
    num_fish = len(states)
    set_n_state(18)
    print(num_fish)


