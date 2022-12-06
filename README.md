# Cryptos-ma-alerts
The script fetches data from Binance on a selection of cryptocurrencies and then sends alerts twice a day through telegram, when these cryptocurrencies cross above or below their 50-periods moving average.

## Structure:
The script includes 3 functions:
1) binanceapidata: get the data from Binance. Parameters:
- symbol: list of cryptocurrencies tickers
- lookback: relative history start date
- frq: frequency of the data (daily, hourly, monthly)

2) telegram_bot_sendtext: sends the text through Telegram. Parameters:
- bot_message: the message to be sent
- TOKEN: Token of your bot
- bot_chatID: chatID of your discussion with your bot

3) telegrambot: it sets the required parameters, calls the 1st function to get the data, checks the moving average condition, and calls the 2nd function to send the message 

## Pre-requisite:
- Build a bot on Telegram using BotFather (more info here: https://blog.devgenius.io/how-to-set-up-your-telegram-bot-using-botfather-fd1896d68c02)
- Input the TOKEN of your newly-created bot in the 'TOKEN' variable
- Input the 'chatID' of your newly-created bot in the 'chatID' variable
- Fill your selection of cryptocurrencies in the 'coins' variable
- Run the Python script and have fun! =)

## Options:
- You can change the length of the moving average with the 'W' variable
- You can change the frequency of data with the 'frq' variable (e.g. '1h', '12h', '1d', '1w', '1m')

You can run the code manually to check the conditions and send a message every x hours, or you can have a cloud server infrastructure such as GCP schedule it (better). 

Open to suggestions, feel free to reach out! 
