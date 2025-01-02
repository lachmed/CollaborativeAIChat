class Room:


    def __init__(self, id):
        self.id = id
        self.clients = {}
        self.api_key = None


    def addClient(self,clientId,ws,messages):
        self.clients[clientId] = {
            "ws":ws,
            "messages":messages
        }
        
    def getClient(self, clientId):
        return self.clients[clientId]
    

    def sendMessageForClient(self, clientId, message):
        self.clients[clientId]["ws"].send(message)
    



