
import requests as req
import time
import threading
import os
from colorama import init,Fore, Back, Style
init()

password = 0
nickname = ""


def sendMsg(msg):
	req.post("http://WebJCou.pythonanywhere.com/send",json={'pass':password,'from':nickname,"msg":msg})

def printMsg(msg):
	print(Fore.CYAN + f"\r\r{msg['from']}:"+ Fore.RESET +f" {msg['msg']}"+'\n'+Fore.GREEN + f"@Вы: "+Fore.RESET,end='')

def listen():
	last=0;
	while True:
		end = 0
		while end != 1:
			msg = req.post(f"http://WebJCou.pythonanywhere.com/get/{password}/{last}").json()
			if 'state' in msg:
				end = 1
				break
			if msg["from"]!=nickname:
				printMsg(msg)
			last+=1
		time.sleep(0.5)


def main():
	os.system('clear')
	threading.Thread(target=listen).start()
	while True:
		msg = input(Fore.GREEN+f"@Вы: "+Fore.RESET)
		sendMsg(msg)


if __name__ == "__main__":
	os.system('clear')
	password = input("Введите пароль(от сервера): ")
	nickname = input("Введите ник: ")
	main()
