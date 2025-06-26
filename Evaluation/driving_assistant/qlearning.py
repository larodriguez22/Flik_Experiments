import random
import numpy as np

class QLearning:
    def __init__(self, agent, alpha=0.1, gamma=0.6, epsilon=0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.agent = agent
        self.actions = agent.actions
        # The current state is a tuple gathered from the agent
        self.current_state = agent._get_state()
        self.qtable = init_q_table(self.actions)

    def random_action(self):
        return random.randint(0, len(self.actions) - 1)

    def run(self):
        done = False
        action = -1
        data = ""
        crashes = 0
        wrong_lanes = 0
        over_speed = 0
        i = 0
        result = []

        while i < 8000:
            if random.random() < self.epsilon:
                action = self.random_action()
            else:
                # Choose the action with the highest Q-value for the current state
                # Convert self.current_state to a tuple before accessing the qtable
                action = max(enumerate(self.qtable[tuple(self.current_state)]), key=lambda x: x[1])[0]


            # Execute step and get the result [next_state, reward, done, info]
            result = self.step(action)
            old_value = self.qtable[tuple(self.current_state)][action]
            next_max = max(self.qtable[tuple(result[0])])
            new_value = (1 - self.alpha) * old_value + self.alpha * (result[1] + self.gamma * next_max)
            self.qtable[tuple(self.current_state)][action] = new_value
            self.current_state = tuple(result[0])


            # Track statistics
            if result[0][0] == 0:
                crashes += 1
            elif result[0][0] > 60:
                over_speed += 1
            if result[0][1] == 1:
                wrong_lanes += 1

            # Record data
            data += f"{self.current_state},{self.actions[action]},{result[0]},{crashes},{wrong_lanes},{over_speed}\n"
            self.current_state = result[0]
            self.agent.world.add_cars()
            # print(self.agent.world.other_cars)
            i += 1

        return data

    def step(self, action):
        # Execute the selected action
        eval(f"self.agent.{self.actions[action]}()")
        next_state = self.agent._get_state()
        reward_done = self.get_rewards(self.current_state, self.actions[action])
        info = f"Executed action: {self.actions[action]} at state {self.current_state}"
        return [next_state, reward_done[0], reward_done[1], info]

    def get_rewards(self, state, action):
        if state[0] == 0:
            return [-800, False]  # crash
        elif state[0] > 60:
            return [-600, False]  # too fast
        elif state[0] < 50:
            return [-600, False]  # too slow
        elif state[1] == 1:
            return [-500, False]  # wrong lane
        elif state[2] == 4:
            return [50, False]    # no car in front
        else:
            return [0, False]

def init_q_table(actions):
    table = {}
    speeds = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for speed in speeds:
        for lane in [0, 1]:
            for proximity in range(1, 5):
                # Use tuple as the dictionary key
                table[(speed, lane, proximity)] = [0] * len(actions)
    return table
