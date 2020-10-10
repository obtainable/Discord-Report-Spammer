from colorama import Fore, init, Style
import threading, requests, ctypes, os

class Yolo:
    def __init__(self):
        self.session = requests.Session()
        self.session.trust_env = False
        self.sent = 0
        self.errors = 0

    def data(self, arg):
        if 'https://onyolo.com/m/' in arg:
            id = arg.split('https://onyolo.com/m/')[1]
            if '?w=' in id:
                id = id.split('?w=')[0]
            return id
        else:
            return None

    def title(self):
        ctypes.windll.kernel32.SetConsoleTitleW('Yolo Spammer | Sent: {0} | Errors: {1}'.format(self.sent, self.errors))

    def message(self, message, id):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8'
        }
        json = {'text': message, 'cookie': 'm3lh7qk39wgowcph2td18'}
        send = self.session.post('https://onyolo.com/{}/message'.format(id), headers = headers, json = json)
        if send.text == 'ok':
            self.sent += 1
            self.title()
        else:
            self.errors += 1
            self.title()

    def start(self):
        def my_function():
            self.message(self.msg, self.id)
        while True:
            if threading.active_count() <= self.threads:
                threading.Thread(target = my_function).start()

    def main(self):
        os.system('cls')
        self.url = str(input('\n{0} > {1}{2}URL: '.format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.msg = str(input('{0} > {1}{2}Message: '.format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.threads = int(input('{0} > {1}{2}Threads: '.format(Fore.GREEN, Fore.WHITE, Style.BRIGHT)))
        self.id = self.data(self.url)
        if self.id != None:
            self.start()

Yolo().main()