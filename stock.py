import FinanceDataReader as fdr
from datetime import datetime
import time
import schedule
import requests
 
myToken = "myToken"
workspace = '#stock'
stock_list = {'005930':'Samsung Electronic',
              '000660':'SK Hynix',
              '001230':'Dongkuk Jaegang',
              '005380':'Hyundai Motors',
              '005935':'Samsung Electronics/ Woo',
              '011780':'Kumho Petrolem',
              '034020':'Doosan Heavy Industry'
}
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
def stock_check():

    today = datetime.today().strftime("%Y-%m-%d")
    now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    #print(today)

    #post_message(myToken,workspace,'-'*40)
    post_message(myToken,workspace,now)
    post_message(myToken,workspace,'-'*45)

    for index in stock_list:
        #print ("INDEX:", index, stock_list.get(index))
        df = fdr.DataReader(index, today, today)
        #print(df)

        val =  str(df.iloc[0][3]).rjust(10,'_') + ' : ' + stock_list.get(index)
        print(val)
        post_message(myToken,workspace,val)
    
#스케쥴 등록
schedule.every(1).seconds.do(stock_check)  # every 1 second
#schedule.every().monday.at("00:10").do(printhello)  # monday 00;10
schedule.every().day.at("15:30").do(stock_check)  # everyday 15:30

#무한루프 돌면서 스케쥴 유지
while True:
    schedule.run_pending()
    time.sleep(1)