import logging 
import requests
import json
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup


API_TOKEN = '5266098737:AAGJBVeJcfDJAb6PEIpMVdZd2jtlL7wvYK8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

result = []

def download_page(url):
	response = requests.get(url)
	response.raise_for_status()
	return response.text
    
def main(url):
	content = download_page(url)
	soup = BeautifulSoup(content, 'html.parser')
	global result
	row = soup.find('ul', 'toc_list')
	for i in row.find_all('li'):
		title = i.a.get_text()
		result.append(title)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply('Hello, I am squ1et\'s bot')

@dp.message_handler(commands=['top'])
async def echo(message: types.Message): 
	result.pop()
	await message.answer('\n'.join(result))


if __name__ == "__main__":
	main('https://mc.today/rejting-onlajn-igr/')
	executor.start_polling(dp, skip_updates=True)
	