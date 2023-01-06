import numpy as np
import os

NO_OF_SQUARES = 3

Symbol = {
    0:" ",
    1:"X",
    -1:"O"
}

class Game:
    def __init__(self) -> None:
        self.reset()
        #self._render()

    def reset(self):
        self.state = np.zeros(NO_OF_SQUARES*NO_OF_SQUARES,dtype = int)
        self.turn = 1
        #print(self.state)
    
    def _render(self):
        os.system('clear')
        for i in range(NO_OF_SQUARES):
            s=""
            for j in range(NO_OF_SQUARES):
                idx = i*NO_OF_SQUARES + j
                s+=Symbol[self.state[idx]]
            print(s)
        

    def play_step(self,action):
        idx = action
        self.state[idx] = self.turn
        self.turn*=-1
        self._render()

if __name__ == '__main__':
    game = Game()
    for i in range(9):
        action = int(input())
        game.play_step(action)