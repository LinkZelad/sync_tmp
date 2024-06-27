from node import Node
from searchs import bfs, Node, node_to_path

MAX_NUM = 3


# west bank -> east bank
class McState:
    def __init__(self, missionary, cannibals, boat_position):
        self.wm = missionary  # west m
        self.wc = cannibals
        self.em = MAX_NUM - self.wm
        self.ec = MAX_NUM - self.wc
        self.wb = boat_position  # boat is on the west or not, True yes False no

    def __str__(self):
        return (
            f"There are {self.wm} missionaries and {self.wc} cannibals on the west bank.\n"  # noqa: E501
            f"And {self.em} missionaries and {self.ec} cannibals on the east bank.\n"
            f"The boat is on {'west' if self.wb else 'east'}."
        )

    def goal_test(self):
        return self.is_legal and self.ec == MAX_NUM and self.em == MAX_NUM

    @property
    def is_legal(self):
        if self.wc > self.wm and self.wm > 0:
            return False
        if self.ec > self.em and self.em > 0:
            return False
        return True

    def successor(self):
        success = []
        if self.wb:
            if self.wm > 1:
                success.append(McState(self.wm - 2, self.wc, not self.wb))
            if self.wm > 0:
                success.append(McState(self.wm - 1, self.wc, not self.wb))
            if self.wc > 1:
                success.append(McState(self.wm, self.wc - 2, not self.wb))
            if self.wc > 0:
                success.append(McState(self.wm, self.wc - 1, not self.wb))

            if self.wc > 0 and self.wm > 0:
                success.append(McState(self.wm - 1, self.wc - 1, not self.wb))

        else:
            if self.em > 1:
                success.append(McState(self.wm + 2, self.wc, not self.wb))
            if self.em > 0:
                success.append(McState(self.wm + 1, self.wc, not self.wb))
            if self.ec > 1:
                success.append(McState(self.wm, self.wc + 2, not self.wb))
            if self.ec > 0:
                success.append(McState(self.wm, self.wc + 1, not self.wb))

            if self.ec > 0 and self.em > 0:
                success.append(McState(self.wm + 1, self.wc + 1, not self.wb))

        return [x for x in success if x.is_legal]

    def display_solution(self, path):
        if len(path) == 0:
            return
        old_state = path[0]
        print("-" * 20)
        print(old_state)
        for current_state in path[1:]:
            if current_state.wb:
                print(
                    f"{current_state.wm - old_state.wm} missionaries and {current_state.wc - old_state.wc} cannibals move from east to west bank."  # noqa: E501
                )
            else:
                print(
                    f"{current_state.em - old_state.em} missionaries and {current_state.ec - old_state.ec} cannibals move from west to east bank."  # noqa: E501
                )
            print(current_state)
            print("-" * 20)
            old_state = current_state


if __name__ == "__main__":
    Mc = McState(MAX_NUM, MAX_NUM, True)
    solutions = bfs(Mc, McState.goal_test, McState.successor)
    if solutions:
        path = node_to_path(solutions)
        Mc.display_solution(path)
    else:
        print("No solution")
