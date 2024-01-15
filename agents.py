from openai import OpenAI

import prompts
from keys import get_key


class Agent1D:
    marker: -1
    latest = ""
    
    pos = 0
    queued_pos = 0

    memory = []
    history = []

    def __init__(self, marker, pos):
        self.marker = marker
        self.pos = pos
        self.history = [pos]

        self.memory.append({"role": "system", "content": prompts.one_dimensional.agent_role})
        self.client = OpenAI(api_key=get_key())

    
    def queue(self, pos):
        self.queued_pos = pos
    
    def update(self):
        self.pos = self.queued_pos
        self.history.append(self.pos)
    
    def prompt(self, message):
        self.memory.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.memory
        )
        self.memory.append({"role": "assistant", "content": completion.choices[0].message.content})
        self.latest = completion.choices[0].message.content

    def __str__(self):
        return "[Agent1D: {}]".format(self.pos)

class Agent2D:
    marker: -1
    latest = ""

    pos = []
    queued_pos = []

    memory = []
    history = []

    def __init__(self, marker, pos):
        self.marker = marker
        self.pos = pos
        self.history = [pos]

        self.memory.append({"role": "system", "content": prompts.two_dimensional.agent_role})        
        self.client = OpenAI(api_key=get_key())

    def queue(self, pos):
        self.queued_pos = pos
    
    def update(self):
        self.pos = self.queued_pos
        self.history.append(self.pos)

    def prompt(self, message):
        self.memory.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.memory
        )
        self.memory.append({"role": "assistant", "content": completion.choices[0].message.content})
        self.latest = completion.choices[0].message.content

    def __str__(self):
        return "[Agent2D: (x: {}, y: {})]".format(self.pos[0], self.pos[1])