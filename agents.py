from openai import OpenAI

import prompts
from keys import get_key


class Agent:
    pos = 0
    history = []

    def __init__(self, pos):
        self.pos = pos
        
        self.history.append({"role": "system", "content": prompts.one_dimensional.agent_role})
        self.client = OpenAI(api_key=get_key())

    def update(self, pos):
        self.pos = pos
    def __str__(self):
        return "[Agent1D: {}]".format(self.pos)

class Agent2D:
    x = 0
    y = 0
    history = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.history.append({"role": "system", "content": prompts.two_dimensional.agent_role})        
        self.client = OpenAI(api_key=get_key())


    def update(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "[Agent2D: (x: {}, y: {})]".format(self.x, self.y)