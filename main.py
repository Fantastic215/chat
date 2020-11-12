import requests, sys, os


class Chat:
    def __init__(self, username):
        super(Chat, self).__init__()
        self.name = username
        try:
            self.chat = requests.get('http://213.176.246.150:5000/update').json()
            self.mess_id = str(len(self.chat.keys())+1)
            self.chat[self.mess_id] = {'system': f'пользователь {self.name} присоеденился к чату.'}
            requests.post('http://213.176.246.150:5000/send', json=self.chat)
            os.system('cls')
            for i in range(1, len(self.chat.keys())+1):
                for j in self.chat.get(str(i)).keys():
                    print(j + ': ' + self.chat.get(str(i)).get(j))
            print(f'\nздравствуйте, {username}. вы вошли в чат.\nдля выхода напишите /exit\n')
        except :
            print('ошибка подключения(возможно)')
            sys.exit()

    def send(self):
        while True:
            try:
                messenge = input("введите текст сообщения или enter что бы обновить (для выхода напишите /exit)\n")
                if messenge != '/exit' and messenge != '':
                    os.system('cls')
                    self.chat = requests.get('http://213.176.246.150:5000/update').json()
                    self.mess_id = str(len(self.chat.keys())+1)
                    self.chat[self.mess_id] = {self.name: messenge}
                    requests.post('http://213.176.246.150:5000/send', json=self.chat)
                    for i in range(1, len(self.chat.keys())+1):
                        for j in self.chat.get(str(i)).keys():
                            print(j + ': ' + self.chat.get(str(i)).get(j))

                elif messenge == '/exit':
                    os.system('cls')
                    self.chat = requests.get('http://213.176.246.150:5000/update').json()
                    self.mess_id = str(len(self.chat.keys())+1)
                    self.chat[self.mess_id] = {'system': f'{self.name} покинул чат'}
                    requests.post('http://213.176.246.150:5000/send', json=self.chat)
                    for i in range(1, len(self.chat.keys())+1):
                        for j in self.chat.get(str(i)).keys():
                            print(j + ': ' + self.chat.get(str(i)).get(j))

                    sys.exit()
                elif messenge == '':
                    self.chat = requests.get('http://213.176.246.150:5000/update').json()
                    os.system('cls')
                    for i in range(1,len(self.chat.keys())+1):
                        for j in self.chat.get(str(i)).keys():
                            print(j + ': ' + self.chat.get(str(i)).get(j))

            except Exception as e:
                print('какая то непредвиденная ошибка (' + str(e) + ')')


if __name__ == '__main__':
    os.system('cls')
    Chat(input('как вас звать?\n')).send()
