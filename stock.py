import FinanceDataReader as fdr
from slacker import Slacker
from datetime import datetime
import time
import schedule

def stock_check():
    today = datetime.today().strftime("%Y-%m-%d")
    now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    #print(today)

    df = fdr.DataReader("005930", today, today)
    #print(df)
    val = str(now) + ': ' + '삼성전자 ' + str(df.iloc[0][3])
    print(val)

    slack = Slacker('xoxb-1554855987762-1548129974950-PcymvgFLFxhcDY22A3F5PSPQ')
    slack.chat.post_message('#secstock',val)

schedule.every(10).seconds.do(stock_check)  # 30분마다 실행
#schedule.every().monday.at("00:10").do(printhello)  # 월요일 00:10분에 실행
#schedule.every().day.at("09:00").do(stock_check)  # 매일 10시30분에

while True:
    schedule.run_pending()
    time.sleep(1)