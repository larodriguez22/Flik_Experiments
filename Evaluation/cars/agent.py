class Agent:
    def __init__(self, world):
        # environment in which the agent lives
        self.world = world
        # agent-specific state
        self.speed = 50
        # lane: 0 = right, 1 = left
        self.position = {"lane": 0, "column": 10}
        self.collision_time = 0
        # self.passenger = None
        self.actions = get_methods(Agent)

    def straight(self):
        # skip - do nothing
        pass

    def slow_down(self):
        if self.speed > 0:
            self.speed -= 10

    def speed_up(self):
        if self.speed < 80:
            self.speed += 10

    def steer_left(self):
        self.position["lane"] = 1

    def steer_right(self):
        self.position["lane"] = 0

    def _time_to_collision(self):
        cars = [car for car in self.world.other_cars if car["position"]["lane"] == self.position["lane"]]
        # print("agent", cars)
        distances = []
        for car in cars:
            dx = round((car["position"]["column"] - self.position["column"]) * 0.005)
            dv = self.speed - car["speed"]
            dt = 100
            if dv != 0:
                dt = round((dx / dv * 200) * 2) / 2
            distances.append(dt)

        ordered = sorted(distances)
        dt = 100 if not ordered else ordered[0]

        if 0 < dt < 20:
            return 1
        elif 20 <= dt < 30:
            return 2  # it can still slow down
        elif 30 <= dt < 50:
            return 3
        else:
            return 4

    def _check_crashed(self):
        if self.speed != 0:
            for c in self.world.other_cars:
                # print("car", c)
                # print(c["position"])
                if c["position"]["lane"] == self.position["lane"]:
                    dx = c["position"]["column"] - self.position["column"]
                    if dx < 100:
                        self.speed = 0
                        c["position"]["column"] = -1

    def _get_state(self):
        # state: {speed, lane, proximity}
        self.world.move_cars_left(self)
        self._check_crashed()
        self.world.other_cars = [c for c in self.world.other_cars if c["position"]["column"] > 0]
        return [self.speed, self.position["lane"], self._time_to_collision()]


def get_methods(cls):
    return [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("_") and func != "constructor"]
