import requests
import time
import schedule
import pandas as pd
from binance.client import Client
client = Client()

def binanceapidata(symbol, lookback, frq):
    frame = pd.DataFrame(client.get_historical_klines(symbol,
                                                     frq,
                                                     lookback + ' days ago UTC'))
    frame = frame.iloc[:,:5]
    #check if token has data
    if len(frame.columns) > 0:
        frame.columns = ['Time','Open','High','Low','Close'] #keep only interesting columns
    else:
        return 
    
    frame.Time = pd.to_datetime(frame.Time, unit='ms') #change date format
    frame[['Open','High','Low','Close']] = frame[['Open','High','Low','Close']].astype(float) #change format from string to float
    #frame = frame.set_index('Time') #set index of df
    
    return frame

def telegram_bot_sendtext(bot_message, TOKEN, bot_chatID):
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def telegrambot():
    TOKEN = '5254207098:AAEEY3_TJ_XkKTJzI1PQtIwCBFeIFcwZCOw'
    bot_chatID = '5081465356'
    coins = ('ETHUSDT','ILVUSDT','MATICUSDT','MLNUSDT','AVAXUSDT','AAVEUSDT','BNBUSDT','SOLUSDT','GMTUSDT','LUNAUSDT','ADAUSDT','AXSUSDT','CELOUSDT','SANDUSDT','FLUXUSDT','FTMUSDT','ALGOUSDT','YFIUSDT')
    W = 50
    lookback = str(W+1)
    frq='12h'
    count = 0
    
    for coin in coins:
        print(coin)
        prices = binanceapidata(coin,lookback,frq)['Close']
        sma  = prices.rolling(window=W,center=False).mean()
        cond1 = prices.iloc[-2] > sma.iloc[-2]
        cond2 = prices.iloc[-1] > sma.iloc[-1]

        if cond1 != cond2:
            if cond1 == True:
                message = coin + " crossed below its moving average (" + str(W) + " periods)"
                msg = telegram_bot_sendtext(message, TOKEN, bot_chatID)
                print(msg)
                count =+ 1

            else:
                message = coin + " crossed above its moving average (" + str(W) + " periods)"
                msg = telegram_bot_sendtext(message, TOKEN, bot_chatID)
                print(msg)
                count =+ 1

    if count == 0:
        message = "Nothing to report!"
        msg = telegram_bot_sendtext(message, TOKEN, bot_chatID)
        print(msg)
        
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])
        
        
     schedule.every().day.at("12:05").do(telegrambot)
schedule.every().day.at("00:05").do(telegrambot)

while True:
    schedule.run_pending()
    time.sleep(60)
