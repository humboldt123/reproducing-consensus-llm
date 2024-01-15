from openai import OpenAI
import random

from agents import *
import prompts

agents = []
rounds = 2

# we create our list of agents and add them to the list
for id_marker in range(3):
    agents.append(Agent1D(id_marker, random.randint(0, 100)))


for r in range(rounds):
    for i, agent in enumerate(agents):
        # give our agent game description on the first round
        # and the updated text after that
        message = prompts.one_dimensional.round_description if r > 0 else prompts.one_dimensional.game_description
        props = message.format(
            agent.pos, "[{}]".format(
                ", ".join(map(lambda a : str(a.pos), filter(lambda a: a.marker != agent.marker, agents)))
                )
        )
        print("---------") # debug line
        print("AGENT", agent.marker) # debug line

        # you guessed it (debug)
        print("Position: {}\nPeers: {}".format(agent.pos, "[{}]".format(", ".join(map(lambda a : str(a.pos), filter(lambda a: a.marker != agent.marker, agents))))))

        agent.prompt(props + " " + prompts.agent_output_form) # ask the agent where to move
        agent.queue(agent.latest.split("\nPosition: ")[1]) # queue agent move to our desired location

        print(agent.latest) # debug line
        print("---------\n") # debug line

    # poll agents and update their positions :3
    list(map(lambda agent: agent.update(), agents))


for agent in agents:
    print("{}: {}".format(agent.marker, agent.history))