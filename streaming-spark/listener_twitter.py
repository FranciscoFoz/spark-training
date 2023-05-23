import socket
import tweepy
import time

HOST = 'localhost'
PORT = 8001


s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")

s.listen(5)
connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

token = 'AAAAAAAAAAAAAAAAAAAAAGyzlQEAAAAAaMWf55m0Dzy%2Fugc%2BGnVxP6Pp6h4%3DykHqTs8KhSU8rBIy6ah0z6nzSCG9ZQsWAVO3ZDm6LJHXoPNsB1'
keyword = 'Biblioteconomia' 

class GetTweets(tweepy.StreamingClient):
    
    def on_tweet(self,tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('utf-8','ignore'))
        
printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

