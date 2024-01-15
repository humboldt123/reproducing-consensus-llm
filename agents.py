from openai import OpenAI

import prompts
from keys import get_key

class Agent:
    identifier = ""
    latest = "" # latest msg
    pos, queued_pos = None, None
    memory = []
    position_history = []

    def __init__(self, id, pos):
        self.identifier = id
        self.pos = pos
        self.position_history = [pos]
        self.client = OpenAI(api_key=get_key())

        self.define_system()

    def define_system(self):
        pass

    def prompt(self):
        pass

    def queue(self, pos):
        self.queued_pos = pos
    
    def update(self):
        self.pos = self.queued_pos
        self.position_history.append(self.pos)
    
    def __str__(self):
        return "[Abstract Agent]"

class Agent1D(Agent):
    def define_system(self):
        self.memory.append({"role": "system", "content": prompts.one_dimensional.agent_role})

    
    def prompt(self, message):
        self.memory.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.memory
        )
        self.memory.append({"role": "assistant", "content": completion.choices[0].message.content})
        self.latest = completion.choices[0].message.content

    def __str__(self):
        return "[Agent1D ({}): {}]".format(self.identifier, self.pos)

class Agent2D(Agent):
    def define_system(self):
        self.memory.append({"role": "system", "content": prompts.two_dimensional.agent_role})    

    def prompt(self, message):
        self.memory.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = self.memory
        )
        self.memory.append({"role": "assistant", "content": completion.choices[0].message.content})
        self.latest = completion.choices[0].message.content

    def __str__(self):
        return "[Agent2D ({}): (x: {}, y: {})]".format(self.identifier, self.pos[0], self.pos[1])