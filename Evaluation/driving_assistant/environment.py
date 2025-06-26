import json
import random
import time
from agent import Agent
from qlearning2 import QLearning2
from qlearning import QLearning
import os

# Global variables for tracking steps and generated cars
steps = 0
generated = 0

class World:
    def __init__(self):
        self.width = 500
        self.height = 4
        self.time_for_full_distance = 0.01
        self.speed_intervals = 5
        self.density = 0.1
        self.exploration = 0.2
        self.steps2 = 0
        self.other_cars = []
        # self.add_cars()

    def car_b(self):
        other_speeds = [30]
        car_id = random.randint(999, 9999)
        speed = random.choice(other_speeds)
        position = {"lane": 0, "column": self.width}
        # Add car to the world
        self.other_cars.append({"id": car_id, "speed": speed, "position": position, "spawn_time": self.current_time()})

    def move_cars_left(self, agent):
        if agent.speed != 0:
            for car in self.other_cars:
                relative_speed = agent.speed - car["speed"]
                dt = self.current_time() - car["spawn_time"]
                d = min(-(relative_speed * 10) + car["position"]["column"], 1000)
                car["spawn_time"] = self.current_time()
                car["position"]["column"] = d

    def current_time(self):
        return int(time.time() * 1000)

    def add_cars(self):
        global generated
        # print("Other cars:", self.other_cars)
        if len(self.other_cars) == 0 and self.steps2 >= 3 and random.random() < self.density:
            # print("Adding car")
            self.car_b()
            self.steps2 = 0
            generated += 1
        self.steps2 += 1

import json

def convert_qtable_to_json_serializable(qtable):
    # Convert each key (tuple) to a string representation
    return {str(key): value for key, value in qtable.items()}

def main(ui_input):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    w = World()
    agent = Agent(w)
    if ui_input == 1:
        learner = QLearning2(agent)
    else:
        learner = QLearning(agent)

    # Run and save data
    data = "speed,lane,proximity,action,next_speed,crashes,wrong_lane,over_limit\n"
    for i in range(1):
        data += learner.run()
        with open(dir_name+f"/experiments/run{i+1}.csv", "w") as file:
            file.write(data)
        print(f"Data saved for run {i+1}")

    # Convert qtable to JSON-serializable format
    qtable_data = json.dumps(convert_qtable_to_json_serializable(learner.qtable), indent=2)
    with open(dir_name+'/experiments/qtable.txt', 'w') as file:
        file.write(qtable_data)
        print("Q-table saved to qtable.txt")

    # Exploitation
    learner.epsilon /= 100
    exp_data = "Speed,Lane,Proximity,action,Speed,next_lane,next_proximity,crashes,wrong_lane,over_speed\n"
    agent.speed = 50
    agent.position["lane"] = 0
    w.other_cars = []
    learner.current_state = agent._get_state()
    exp_data += learner.run()
    with open(dir_name+"/experiments/exploitation.csv", "w") as file:
        file.write(exp_data)
        print(f"Exploitation data saved to {dir_name}/experiments/exploitation.csv")

if __name__ == '__main__':
    ui_input = int(input("Would you like to run the UI? (yes=1/no=2): "))
    main(ui_input)

