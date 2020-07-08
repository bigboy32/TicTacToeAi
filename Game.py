from minimax import Minimax

state_i = [0,0,0,0,0,0,0,0,0]
m = Minimax(1)

print("You are : 2")

while True:
    visstate = [state_i[0:3], state_i[3:6], state_i[6:10]]
    for row in visstate:
        print(row)
    action = int(input("Chose A Field: "))

    if state_i[action] != 2:
        state_i[action] = 2
    else:
        print("Oh No the fild is used! You have to skip this round!!")
    m.make_branch(state_i)
    m.take_action(state_i)
    state_i = m.a[0]
    odd = 0
    for item in state_i:
        if item != 0:
            odd = 1
        if odd == 9:
            exit()