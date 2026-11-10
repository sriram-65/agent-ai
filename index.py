class AgentIndex:
    def __init__(self):
        print("Agent Started")

    def LLM(self , msg):
        r = self.sendToLLM(msg)
        return r



    