import requests

def vritualEnv():
	print(requests.__version__)


def getGoogle():
	google = requests.get('http://www.google.com/')
	r = requests.get('https://raw.githubusercontent.com/GevinUA/404_Lab/main/version_print.py')
	print(r.text)


def main():
	vritualEnv()
	getGoogle()

main()