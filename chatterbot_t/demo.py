from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)

deepThought.train("chatterbot.corpus.english")

print(deepThought.get_response("Hello, how are you today"))
