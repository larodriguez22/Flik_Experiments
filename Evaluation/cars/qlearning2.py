import pygame
import random
import numpy as np
import time
from agent import Agent

class QLearning2:
    def __init__(self, agent, alpha=0.1, gamma=0.6, epsilon=0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.agent = agent
        self.actions = agent.actions
        self.current_state = agent._get_state()
        self.qtable = init_q_table(self.actions)

    def random_action(self):
        return random.randint(0, len(self.actions) - 1)

    def run(self):
        data = ""
        crashes = 0
        wrong_lanes = 0
        over_speed = 0
        i = 0

        # Initialize Pygame
        pygame.init()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Agent Simulation")
        clock = pygame.time.Clock()

        running = True
        while running and i < 8000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Decide action (randomly or by Q-value)
            if random.random() < self.epsilon:
                action = self.random_action()
            else:
                action = max(enumerate(self.qtable[tuple(self.current_state)]), key=lambda x: x[1])[0]

            # Execute the action and get new state
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

            # Log data
            data += f"{self.current_state},{self.actions[action]},{result[0]},{crashes},{wrong_lanes},{over_speed}\n"
            self.agent.world.add_cars()
            self.current_state = result[0]

            # Draw the current state in Pygame
            self.draw_world(screen, self.actions[action], i, result[1])
            # print(i)

            pygame.display.flip()
            clock.tick(1)
            i += 1

        pygame.quit()
        return data

    def step(self, action):
        eval(f"self.agent.{self.actions[action]}()")
        next_state = self.agent._get_state()
        reward_done = self.get_rewards(self.current_state, self.actions[action])
        return [next_state, reward_done[0], reward_done[1]]

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

    def draw_world(self, screen, action, iteration, reward):
        screen.fill((200, 200, 200))

        # Draw lanes
        pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 400), 5)

        # Draw agent car
        agent_x = 10 + self.agent.speed
        agent_y = 350 if self.agent.position["lane"] == 0 else 200
        pygame.draw.rect(screen, (0, 0, 255), (agent_x, agent_y, 40, 20))

        # Draw other cars
        # print(self.agent.world.other_cars)
        for car in self.agent.world.other_cars:
            car_x = car["position"]["column"]
            car_y = 350 if car["position"]["lane"] == 0 else 200
            pygame.draw.rect(screen, (255, 0, 0), (car_x, car_y, 40, 20))

        # Display agent's information
        font = pygame.font.Font(None, 24)
        speed_text = font.render(f"Speed: {self.agent.speed} km/h", True, (0, 0, 0))
        action_text = font.render(f"Action: {action}", True, (0, 0, 0))
        iteration_text = font.render(f"Iteration: {iteration}", True, (0, 0, 0))
        reward_text = font.render(f"Reward: {reward}", True, (0, 0, 0))

        screen.blit(speed_text, (10, 10))
        screen.blit(action_text, (10, 30))
        screen.blit(iteration_text, (10, 50))
        screen.blit(reward_text, (10, 70))

def init_q_table(actions):
    table = {}
    speeds = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for speed in speeds:
        for lane in [0, 1]:
            for proximity in range(1, 5):
                table[(speed, lane, proximity)] = [0] * len(actions)
    return table
