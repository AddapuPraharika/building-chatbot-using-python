from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)
trainer.train(['Hello!','Hi there!','How are you doing?','I am doing great.','Thanks','You are welcome.'])
response = chatbot.get_response('Hello!')
print(response)
response = chatbot.get_response('How are you doing?')
print(response)
