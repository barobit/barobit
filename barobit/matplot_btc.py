# 참고 사이트
# https://zephyrus1111.tistory.com/421

# 예외 처리
# https://docs.python.org/ko/3/tutorial/errors.html

# 모듈 설치
# pip3 install finance-datareader
# pip3 install matplotlib
# pip3 install urllib3
# pip3 install beautifulsoup4


# <warning>
# --no-warn-script-location
# path 경로 설정으로 해결


import FinanceDataReader as fdr
# import yfinance as yf
import pandas as pd
import pandas_datareader as pdr

# pip3 install datetime
from datetime import datetime 
from matplotlib import pyplot as plt

# import netsnmp

from matplotlib.gridspec import GridSpec



start_date = datetime(2021,11,1).strftime('%Y-%m-%d')
end_date = datetime(2021,12,31).strftime('%Y-%m-%d')

# https://financedata.github.io/posts/finance-data-reader-users-guide.html
# 비트코인 원화 가격 (빗썸)
df = fdr.DataReader('BTC/KRW', start_date, end_date)

print(df.head())

# 실행 단축키 : ctl + fn + f5
