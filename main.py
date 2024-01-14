from openai import OpenAI

import random

from agents import *
from keys import get_key




# agents = []
# for i in range (5):
#     agents.append(Agent(random.randint(0, 100)))

# for agent in agents:
#     print(str(agent))

# # client = OpenAI(api_key="")
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages = [
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#             {"role": "user", "content": "Hello"},
#        {"role": "assistant", "content": "Hello, how can I help you?"},
#   ]
# )

# print(completion.choices[0].message)