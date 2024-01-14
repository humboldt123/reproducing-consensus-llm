from openai import OpenAI

import prompts
from keys import get_key


class Agent1D:
    marker: -1
    pos = 0
    history = []
    latest = ""

    def __init__(self, marker, pos):
        self.marker = marker
        self.pos = pos
        
        self.history.append({"role": "system", "content": prompts.one_dimensional.agent_role})
        self.client = OpenAI(api_key=get_key())
    
    def update(self, pos):
        self.pos = pos
    
    def prompt(self, message):
        self.history.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.history
        )
        self.history.append({"role": "assistant", "content": completion.choices[0].message.content})
        self.latest = completion.choices[0].message.content

    def __str__(self):
        return "[Agent1D: {}]".format(self.pos)

class Agent2D:
    marker: -1
    x = 0
    y = 0
    history = []

    def __init__(self, marker, x, y):
        self.marker = marker
        self.x = x
        self.y = y
        
        self.history.append({"role": "system", "content": prompts.two_dimensional.agent_role})        
        self.client = OpenAI(api_key=get_key())

    def update(self, x, y):
        self.x = x
        self.y = y

    def prompt(self, id, message):
        self.history.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.history
        )
        self.latest = completion.choices[0].message
        self.history.append({"role": "assistant", "content": self.latest})

    def __str__(self):
        return "[Agent2D: (x: {}, y: {})]".format(self.x, self.y)