from openai import OpenAI
import random

from agents import *
import prompts




agents = []


# todo: add way to queue updates, print more stuff
for i in range(3):
    agents.append(Agent1D(i, random.randint(0, 100)))

for agent in agents:
    print(str(agent))

for i in range(len(agents)):
    agent = agents[i]
    message = prompts.one_dimensional.game_description.format(agent.pos, "[{}]".format(", ".join(map(lambda a : str(a.pos), filter(lambda a: a.marker != agent.marker, agents)))))
    print("AGENT", agent.marker)
    print("---------")
    print("Position: {}\nPeers: {}".format(agent.pos, "[{}]".format(", ".join(map(lambda a : str(a.pos), filter(lambda a: a.marker != agent.marker, agents))))))
    agent.prompt(message + " " + prompts.agent_output_form)
    print(agent.latest)
    agent.update(agent.latest.split("\nPosition: ")[1])
    print("---------")

for agent in agents:
    print(str(agent))