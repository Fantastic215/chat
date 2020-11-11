import requests, sys, os


class Chat:
    def __init__(self, username):
        super(Chat, self).__init__()
        self.name = username
        self.chat = requests.get('http://localhost:5000/update').json()
        self.mess_id = str(len(self.chat.keys())+1)
        self.chat[self.mess_id] = {'system': f'пользователь {self.name} присоеденился к чату.'}
        requests.post('http://localhost:5000/send', json=self.chat)
        os.system('clear')
        for i in range(1, len(self.chat.keys())+1):
            for j in self.chat.get(str(i)).keys():
                print(j + ': ' + self.chat.get(str(i)).get(j))
        print(f'\nздравствуйте, {username}. вы вошли в чат.\nдля выхода напишите /exit\n')

    def send(self):
        while True:
            try:
                messenge = input("введите текст сообщения или enter что бы обновить\n")
                if messenge != '/exit' and messenge != '':
                    os.system('clear')
                    self.chat = requests.get('http://localhost:5000/update').json()
                    self.mess_id = str(len(self.chat.keys())+1)
                    self.chat[self.mess_id] = {self.name: messenge}
                    requests.post('http://localhost:5000/send', json=self.chat)
                    for i in range(1, len(self.chat.keys())+1):
                        for j in self.chat.get(str(i)).keys():
                            print(j + ': ' + self.chat.get(str(i)).get(j))

                elif messenge == '/exit':
                    os.system('clear')
                    self.chat = requests.get('http://localhost:5000/update').json()
                    self.mess_id = str(len(self.chat.keys())+1)
                    self.chat[self.mess_id] = {'system': f'{self.name} покинул чат'}
                    requests.post('http://localhost:5000/send', json=self.chat)
                    for i in range(1, len(self.chat.keys())+1):
                        for j in self.chat.get(str(i)).keys():
                            print(j + ': ' + self.chat.get(str(i)).get(j))

                    sys.exit()
                elif messenge == '':
                    self.chat = requests.get('http://localhost:5000/update').json()
                    os.system('clear')
                    for i in range(1,len(self.chat.keys())+1):
                        for j in self.chat.get(str(i)).keys():
                            print(j + ': ' + self.chat.get(str(i)).get(j))

            except Exception as e:
                print('какая то непредвиденная ошибка (' + str(e) + ')')


if __name__ == '__main__':
    os.system('clear')
    Chat(input('как вас звать?\n')).send()
