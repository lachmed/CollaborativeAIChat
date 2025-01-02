from flask import Flask
from flask_sock import Sock
from utils import Room
from text_generation import *
import json

app = Flask(__name__)
sock = Sock(app)



# keep all the rooms of the application in here
rooms = {}

@sock.route("/chat")
def reserve(ws):
    global rooms
    
    while True: 
        

        data = json.loads(ws.receive())
        roomId = data["roomId"]
        clientId = data["clientId"]
        message = data["msg"]
        msg_for = data["for"]
        
        
        #when getting a new message, check if there is already a room
        # if no room exists, create one and add this client to it if it is not 
        # already in the room    
        if roomId not in rooms.keys():
            rooms[roomId] = Room(roomId)
        
        room = rooms[roomId]

            
        #set the google ai api key 
        # print(data)

        if message == "____BEGIN____" and room.api_key==None:
            room.api_key = data["apiKey"]["apiKey"]
            # print("Begin: ",data["apiKey"]["apiKey"])

        # print("api_key: ",room.api_key)

        
        if clientId not in room.clients.keys():
            room.addClient(clientId,ws,[message])
        else:
            room.getClient(clientId)["messages"].append(message)        
        
        #send message for other clients in the room only
        #i.e. don't send the message to the client that sent it in the first place        


        if(message != "____BEGIN____"):

            if msg_for==0: # to other clients
                response = {
                    "client_message": message,
                    "ownerId": clientId,
                    "owner":"Client"         
                }
            else:

                try:
                    ai_response = chatting(message, room.api_key)
                except Exception as e:
                    print(e)
                    ai_response = "There was an error with AI, create a new room and make sure your API key is correct"
                
                response = {
                    "client_message": message,
                    "clientOwnerId": clientId,
                    "ai_model_message":ai_response,            
                    "owner":"AI",
                    "ownerId": "GoogleAI",
                }
            

            for id in room.clients.keys():
                if response["owner"]!="AI":
                    if id != clientId :
                        room.sendMessageForClient(id,json.dumps(response))
                else:
                    room.sendMessageForClient(id,json.dumps(response))



        # for k in rooms.keys():
        #     print(rooms[k].id)
        #     print(rooms[k].clients)

if __name__ == "__main__":
    app.run(debug=True)

    



