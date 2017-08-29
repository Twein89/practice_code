import nltk
from nltk.tokenize import sent_tokenize

para = "Hello World. It's good to see you. Thanks for buying this book"

tokens = nltk.word_tokenize(para)
print(tokens)
