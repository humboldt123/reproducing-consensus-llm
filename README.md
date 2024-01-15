# Reproducing Results: Multi-Agent Coonsensus Seeking via Large Language Models
Reproducing the results of Westlake Intelligent Robotics' [Consensus LLM Paper](https://github.com/WestlakeIntelligentRobotics/ConsensusLLM-code)

## Prerequisites
- Make sure you have [Python](https://www.python.org/downloads/) installed
- This project has a few dependencies, install them with `pip install -r requirements.txt`
- You'll also need one or more valid OpenAI API keys. When you have them in hand, create a file titled `secrets.yml` and add them in the following format:
        ```yml
        api_keys:
            0: "sk-YourFirstAPIKeyHere"
            1: "sk-YourSecondAPIKeyHere"
            2: "sk-YourThirdAPIKeyHere"
        ```