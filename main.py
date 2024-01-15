from openai import OpenAI

import random
import json

from agents import *
import prompts

agents = []
rounds = 10

# we create our list of agents and add them to the list
for id_marker in range(2):
    agents.append(Agent2D(id_marker, [random.randint(0, 100), random.randint(0, 100)]))

# todo: async
# todo: err handling
for r in range(rounds):
    print("===ROUND {} ===".format(r))
    if not all(agent.pos == agents[0].pos for agent in agents):
        for i, agent in enumerate(agents):
            # give our agent game description on the first round
            # and the updated text after that
            
            # two_dimensional -> one_dimensional for 1d arrays 
            message = prompts.two_dimensional.round_description if r > 0 else prompts.two_dimensional.game_description
            props = message.format(
                agent.pos, "[{}]".format(
                    ", ".join(map(lambda a : str(a.pos), filter(lambda a: a.marker != agent.marker, agents)))
                    )
            )
            print("---------") # debug line
            print("AGENT", agent.marker) # debug line

            # you guessed it (debug)
            print("Position: {}\nPeers: {}".format(agent.pos, "[{}]".format(", ".join(map(lambda a : str(a.pos), filter(lambda a: a.marker != agent.marker, agents))))))

            try:
                # ask the agent where to move
                agent.prompt(props + " " + prompts.agent_output_form)
                # queue agent move to our desired location
                agent.queue(json.loads(agent.latest.split("\nPosition: ")[1])) # json.loads is for 2Dagents (for arrays) 
            except:
                print("Failed to move agent {}. Output: {} ".format(agent.marker, agent.latest))

            print(agent.latest) # debug line
            print("---------\n") # debug line

        # poll agents and update their positions :3
        list(map(lambda agent: agent.update(), agents))
    else:
        print("Consensus reached on round {}", r - 1)


for agent in agents:
    print("{}: {}".format(agent.marker, agent.history))