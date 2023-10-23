from time import sleep
import uuid
from websocket import create_connection
import pdb

chat_id = str(uuid.uuid4())
url = "wss://commonserviceidc.testing.comm100dev.io/webrtcSignalingService/signaling.ashx?chatId="+chat_id

ws_agent = create_connection(url)
print("ws_agent receive_connection", ws_agent.recv())

ws_visitor = create_connection(url)
print("ws_visitor receive_connection", ws_visitor.recv())

# pdb.set_trace()
# sleep(5)
receive_count1_for_agent =  ws_agent.recv()
print("receive_count1_for_agent Received '%s'" % receive_count1_for_agent)

receive_count_for_visitor =  ws_visitor.recv()
print("receive_count_for_visitor Received '%s'" % receive_count_for_visitor)

# after visitor joins, agent need to do receive again to receive the count as 2
receive_count2_for_agent =  ws_agent.recv()
print("receive_count2_for_agent Received '%s'" % receive_count2_for_agent)


# pdb.set_trace()
ws_agent.send("Hello from agent")

receive_hello_for_visitor =  ws_visitor.recv()
print("receive_hello_for_visitor Received '%s'" % receive_hello_for_visitor)

ws_visitor.send("Hello back to you from visitor")

receive_hello_back_for_agent =  ws_agent.recv()
print("receive_hello_back_for_agent Received '%s'" % receive_hello_back_for_agent)

ws_agent.send("bye from agent")
receive_bye_for_visitor = ws_visitor.recv()
print("receive_bye_for_visitor Received '%s'" % receive_bye_for_visitor)

ws_visitor.send("bye from visitor")
receive_bye_for_agent = ws_agent.recv()
print("receive_bye_for_agent Received '%s'" % receive_bye_for_agent)


ws_agent.close()
print("ws_agent close status", ws_agent.status)

ws_visitor.close()
print("ws_visitor close status", ws_visitor.status)