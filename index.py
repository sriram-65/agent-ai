class AgentIndex:
    def __init__(self):
        print("Agent Started")

    def LLM(self , msg):
        r = self.sendToLLM(msg)
        return r

    def sendToLLM(self , msg):

        return f"Hello iam Large Language Model Thanks for sending msg : {msg}"




    