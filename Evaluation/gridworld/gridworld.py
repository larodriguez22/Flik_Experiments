import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

import time
import random
import copy
import matplotlib


class Gridworld:
    def __init__(self, board, initial_state = (0,0), walls = None):
        self.nrows, self.ncols = len(board),len(board[0])
        self.grid = np.zeros((self.nrows, self.ncols))
        self.colors = np.zeros((self.nrows, self.ncols))
        self.is_terminal = False
        self.walls = walls
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "*":
                    self.grid[i][j] = -2
                elif board[i][j] == "+1":
                    self.grid[i][j] = 1
                elif board[i][j] == "+100":
                    self.grid[i][j] = 100
                elif board[i][j] == "-1":
                    self.grid[i][j] = -1
                elif board[i][j] == "-100":
                    self.grid[i][j] = -100
                elif board[i][j] == "R":
                    self.colors[i][j] = 3
                elif board[i][j] == "G":
                    self.colors[i][j] = 4
                elif board[i][j] == "B":
                    self.colors[i][j] = 5
                elif board[i][j] == "Y":
                    self.colors[i][j] = 6
        # self.grid[-1, -1] = 1  # set the final state to have a reward of 1
        # print("grid despues",self.grid)
        self.initial_state = initial_state
        self.state = initial_state
        
    def get_states(self):
        return [(i, j) for i in range(len(self.grid)) for j in range(len(self.grid[0]))]

    def get_current_state(self):
        return self.state

    def get_possible_actions(self, state):
        i, j = state
        actions = []
        if self.grid[state]==0 or self.grid[state]==-1:
            if j > 0 and self.grid[i][j-1] != -2:
                actions.append('down')
            if j < self.ncols - 1 and self.grid[i][j+1] != -2:
                actions.append('up')
            if i > 0 and self.grid[i-1][j] != -2 and (self.walls == None or self.walls[i-1][j] != "l"):
                actions.append('left')
            if i < self.nrows - 1 and self.grid[i+1][j] != -2 and (self.walls == None or self.walls[i+1][j] != "r"):
                actions.append('right')
        elif self.grid[state] != -2:
            actions.append("end")
        elif self.grid[state] == -2:
            return [None]
        return actions
    
    def get_next_states(self, state, action):
        i, j = state
        reward = 0
        if action == 'left' :
            i -= 1
        elif action == 'right':
            i += 1
        elif action == 'down':
            j -= 1
        elif action == 'up':
            j += 1
        elif action == 'end':
            reward = self.grid[i, j]
        self.state = (i, j)
        return reward, self.state

    def do_action(self, action):
        i, j = self.state
        reward = 0
        done = False
        if action == 'left' :
            i -= 1
        elif action == 'right':
            i += 1
        elif action == 'down':
            j -= 1
        elif action == 'up':
            j += 1
        elif action == 'end':
            reward = self.grid[i, j]
            done = True
            
        self.state = (i, j)
        return reward, self.state, done

    def reset(self):
        self.state = self.initial_state

    def is_terminal(self):
        return self.grid[self.state] == 1
    
    def plot(self):
        fig1 = plt.figure(figsize=(10, 10))
        ax1 = fig1.add_subplot(111, aspect='equal')
        
        # Lineas
        for i in range(0, len(self.grid)+1):
            ax1.axvline(i , linewidth=2, color="#2D2D33")
        for j in range(0, len(self.grid[0])+1):
            ax1.axhline(j , linewidth=2, color="#2D2D33")
        
        # Amarillo - inicio
        ax1.add_patch(patches.Rectangle(self.initial_state, 1, 1, facecolor = "#F6D924"))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1 or self.grid[i][j] == 100 or self.colors[i][j] == 4: # verde
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#68FF33"))
                if self.grid[i][j] == -2: # gris
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#6c7780"))
                if self.colors[i][j] == 6: # amarillo
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#F6D924"))
                if self.colors[i][j] == 5: # amarillo
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "blue"))
                if self.grid[i][j] == -1 or self.grid[i][j] == -100 or self.colors[i][j] == 3: # rojo
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#cc0000"))
                if self.walls!= None and self.walls[i][j] == "r":
                    ax1.add_patch(patches.Rectangle((i+0.9,j), 0.1, 1, facecolor = "#6c7780"))
                if self.walls!= None and self.walls[i][j] == "l":
                    ax1.add_patch(patches.Rectangle((i,j), 0.1, 1, facecolor = "#6c7780"))
                
        plt.scatter(self.state[0] + 0.5, self.state[1] +0.5, s = 100, color = "black", marker = "o", facecolor = "blue", edgecolors = "blue", zorder = 10)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j] == -2:
                    ax1.text(i+0.5, j+0.5, "*", ha='center', va='center')
                elif self.colors[i, j] == 3:
                    ax1.text(i+0.5, j+0.5, "R", ha='center', va='center')
                elif self.colors[i, j] == 4:
                    ax1.text(i+0.5, j+0.5, "G", ha='center', va='center')
                elif self.colors[i, j] == 5:
                    ax1.text(i+0.5, j+0.5, "B", ha='center', va='center')
                elif self.colors[i, j] == 6:
                    ax1.text(i+0.5, j+0.5, "Y", ha='center', va='center')
                else:
                    ax1.text(i+0.5, j+0.5, self.grid[i, j], ha='center', va='center')
        plt.axis("off")
        plt.show()
        
    def get_action_test(self, action):
        if action=='left':
            return '<'
        if action=='right':
            return '>'
        if action=='up':
            return '^'
        if action=='down':
            return 'v'
        if action=='exit':
            return 'x'
        
    def plot_action(self, actions, values):
        fig1 = plt.figure(figsize=(10, 10))
        ax1 = fig1.add_subplot(111, aspect='equal')
        
        # Lineas
        for i in range(0, len(self.grid)+1):
            ax1.axvline(i , linewidth=2, color="#2D2D33")
        for j in range(0, len(self.grid[0])+1):
            ax1.axhline(j , linewidth=2, color="#2D2D33")
        
        # Amarillo - inicio
        ax1.add_patch(patches.Rectangle(self.initial_state, 1, 1, facecolor = "#F6D924"))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1 or self.grid[i][j] == 100 or self.colors[i][j] == 4: # verde
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#68FF33"))
                if self.grid[i][j] == -2: # gris
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#6c7780"))
                if self.colors[i][j] == 6: # amarillo
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#F6D924"))
                if self.colors[i][j] == 5: # amarillo
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "blue"))
                if self.grid[i][j] == -1 or self.grid[i][j] == -100 or self.colors[i][j] == 3: # rojo
                    ax1.add_patch(patches.Rectangle((i,j), 1, 1, facecolor = "#cc0000"))
                if self.walls!= None and self.walls[i][j] == "r":
                    ax1.add_patch(patches.Rectangle((i+0.9,j), 0.1, 1, facecolor = "#6c7780"))
                if self.walls!= None and self.walls[i][j] == "l":
                    ax1.add_patch(patches.Rectangle((i,j), 0.1, 1, facecolor = "#6c7780"))
        self.reset()
        plt.scatter(self.state[0] + 0.5, self.state[1] +0.5, s = 100, color = "black", marker = "o", facecolor = "blue", edgecolors = "blue", zorder = 10)
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i, j] == -2:
                    ax1.text(i+0.5, j+0.5, "*", ha='center', va='center')
                elif self.colors[i, j] == 3:
                    ax1.text(i+0.5, j+0.5, "R", ha='center', va='center')
                elif self.colors[i, j] == 4:
                    ax1.text(i+0.5, j+0.5, "G", ha='center', va='center')
                elif self.colors[i, j] == 5:
                    ax1.text(i+0.5, j+0.5, "B", ha='center', va='center')
                elif self.colors[i, j] == 6:
                    ax1.text(i+0.5, j+0.5, "Y", ha='center', va='center')
                else:
                    try:
                        ax1.text(i+0.5, j+0.75, round(values[i, j],2), ha='center', va='center')
                        text2=self.get_action_test(actions[(i,j)])
                        ax1.text(i+0.5, j+0.25, text2, ha='center', va='center')
                    except:
                        ax1.text(i+0.5, j+0.75, 0, ha='center', va='center')
                        ax1.text(i+0.5, j+0.25, "None", ha='center', va='center')
        plt.axis("off")
        plt.show()


class Learner:
    def __init__(self, env, alpha=0.1, gamma=0.6, epsilon=0.1, episodes=10):
        #hyper parameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.environment = env
        # self.agent = agent          #actual agent
        self.qtable = self.__initdic__() #rewards table
        self.episodes = episodes
    
    def __initdic__(self):
        table = dict()
            
        # Initialize Q table with 0 for each state-action pair
        for state in self.environment.get_states():
            table[state] = np.zeros(len(self.environment.get_possible_actions(state)))
        print(table)
        # print(table[0,1])
        return table

    def run(self, ui_input):
        done = False
        contador = 0
        for i in range(self.episodes):
            done = False
            while not done:
                current_state = copy.deepcopy(self.environment.state)
                if random.uniform(0,1) < self.epsilon:
                    action = self.randomAction(current_state)
                else:
                    action = np.argmax(self.qtable[current_state]) 
                next_state, reward, done, info = self.step(action)
                old_value = self.qtable[current_state][action]
                next_max = np.max(self.qtable[next_state])
                new_value = (1 - self.alpha)*old_value + self.alpha*(reward + self.gamma*next_max)
                self.qtable[current_state][action] = new_value
                contador += 1
            if ui_input == 1:
                actions, values = self.actions_values()
                self.environment.plot_action(actions, values)
            self.environment.reset()
            # print("----------------")
        print(contador)
        return self.qtable

    def randomAction(self, current_state):
        return random.randint(0,len(self.environment.get_possible_actions(current_state))-1)

    def step(self, action):
        old_state = copy.deepcopy(self.environment.state)
        reward, new_state, done = self.environment.do_action(self.environment.get_possible_actions(old_state)[action])
        next_state = copy.deepcopy(self.environment.state)
        info = f'Executed action: {action} at state {old_state}'
        return next_state, reward, done, info
    
    def actions_values(self):
        actions = {}
        self.environment.reset()
        values = np.zeros_like(self.environment.grid)
        for state in self.environment.get_states():
            action = np.argmax(self.qtable[state]) 
            actions[state] = self.environment.get_possible_actions(state)[action]
            values[state] = np.max(self.qtable[state])
        return actions, values

if __name__ == '__main__':
    ui_input = int(input("Would you like to run showing the UI? (this might take longer)[yes=1/no=2]: "))
    board = [
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', '*', ' ', ' '],
    [' ', ' ', '*', '*', '*','*', '*', '*', ' ', ' '],
    [' ', ' ', '-1', ' ', '+1','-1', ' ', ' ', ' ', ' '],
    [' ', ' ', '-1', ' ', ' ',' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
    ]

    initial_state = (0, 9)

    env = Gridworld(board, initial_state)

    learner = Learner(env)

    learner.run(ui_input)

    actions, values = learner.actions_values()
    env.plot_action(actions, values)