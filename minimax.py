class Minimax:

    def __init__(self, mark):
        self.Tree = []
        self.Mark = mark
        self.a = None
    def check_score(self, state_i):
        visstate = [state_i[0:3], state_i[3:6], state_i[6:10]]
        r1 = 0
        r2 = 0

        if visstate[0][0] and visstate[1][1] and visstate[2][2] == 1:
            r1 = 1
        elif visstate[0][0] and visstate[1][1] and visstate[2][2] == 2:
            r2 = 1
        elif visstate[2][0] and visstate[1][1] and visstate[0][2] == 1:
            r1 = 1
        elif visstate[2][0] and visstate[1][1] and visstate[0][2] == 2:
            r2 = 1
        elif visstate[0][0] and visstate[0][1] and visstate[0][2] == 1:
            r1 = 1
        elif visstate[0][0] and visstate[0][1] and visstate[0][2] == 2:
            r2 = 1
        elif visstate[1][0] and visstate[1][1] and visstate[1][2] == 1:
            r1 = 1 
        elif visstate[1][0] and visstate[1][1] and visstate[1][2] == 2:
            r2 = 1
        elif visstate[2][0] and visstate[2][1] and visstate[2][2] == 1:
            r1 = 1
        elif visstate[2][0] and visstate[2][1] and visstate[2][2] == 2:
            r2 = 1

        else:
            pass

        if self.Mark == 1:
            return r1
        else:
            return r2
    def make_branch(self, current_state):
        empty_poses = []
        for item in current_state:
            if item == 0:
                empty_poses.append(current_state.index(item))
        for item in empty_poses:
            state_i = current_state
            state_i[item] = self.Mark
            score = self.check_score(state_i)

            self.Tree.append([state_i, score])

    def take_action(self, current_state):
        T = self.Tree
        best_score = []
        for item in T:
            if item != current_state:
                if best_score == []:
                    best_score.append([item[0], item[1]])
                else:
                    if item[1] > best_score[0][1]:
                        best_score = []
                        best_score.append([item[0], item[1]])
        self.a = best_score[0]
