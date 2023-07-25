from chat13.chat import chat_conversation
from chat13.learn import learn 

def main():
    chat_conversation.greeting()
    while True:
        data = input(f'prajwal: ')
        learn(data)
    

if __name__ == "__main__":
    main()