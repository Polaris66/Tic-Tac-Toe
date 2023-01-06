import numpy as np
import os

NO_OF_SQUARES = 3
#TODO: Implement for bigger squares

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
        self.done = False
        self.winner = 0
        self.count = 0
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
        if self.done:
            self._render()
            print(self.winner," won")
            self.reset()
        else:
            idx = action
            if(self.state[idx]==0):
                self.state[idx] = self.turn
                self.turn*=-1
                self._render()
                self._check_game_over()
        
    def _check_game_over(self):
        self.count+=1
        winner = 0
        for i in range(3):
            if (self.state[i] == self.state[i+3]) and (self.state[i+6] == self.state[i+3]):
                winner = self.state[i] 
        
        for i in [0,3,6]:
            if (self.state[i] == self.state[i+1]) and (self.state[i+2] == self.state[i+1]):
                winner = self.state[i] 
       
        if (self.state[0] == self.state[4]) and (self.state[8] == self.state[4]):
                winner = self.state[0] 
        
        if (self.state[2] == self.state[4]) and (self.state[6] == self.state[4]):
                winner = self.state[2] 
        
        if(winner!=0):
            self.done = True
            self.winner = winner
        if(self.count==9):
            self.done = True
            self.winner = 0

if __name__ == '__main__':
    game = Game()
    while not game.done:
        action = int(input()) # Replace with Model
        game.play_step(action)
    game._render()
    print(Symbol[game.winner],"Won")