import requests
import pandas as pd
import re
import numpy as np
from bs4 import BeautifulSoup
import datetime

def TradeDateProcess(excelpath):
    
    TradeDateExcelPath = excelpath
    
    DateSeries = pd.read_excel(TradeDateExcelPath)['Date']
    DateDf = DateSeries.apply(lambda x: x.strftime('%Y%m%d')).to_frame()
    DateList = DateDf['Date'].tolist()
    
    return DateList
    
def ReForLongShort(text):
    
    WebText = text
    
    reForLong = '<data text=".*?                        " value="1">\n    <instrumentid>\n     .*?\n    </instrumentid>\n    <tradingday>\n     .*?\n    </tradingday>\n    <datatypeid>\n     .*?\n    </datatypeid>\n    <rank>\n     .*?\n    </rank>\n    <shortname>\n     .*?\n    </shortname>\n    <volume>\n     .*?\n    </volume>\n    <varvolume>\n     (.*?)\n    </varvolume>\n    <partyid>\n     .*?\n    </partyid>\n    <productid>\n     .*?\n    </productid>\n   </data>\n'
    reForShort = '<data text=".*?                        " value="2">\n    <instrumentid>\n     .*?\n    </instrumentid>\n    <tradingday>\n     .*?\n    </tradingday>\n    <datatypeid>\n     .*?\n    </datatypeid>\n    <rank>\n     .*?\n    </rank>\n    <shortname>\n     .*?\n    </shortname>\n    <volume>\n     .*?\n    </volume>\n    <varvolume>\n     (.*?)\n    </varvolume>\n    <partyid>\n     .*?\n    </partyid>\n    <productid>\n     .*?\n    </productid>\n   </data>\n'

    LongVarV = re.findall(reForLong,WebText.prettify())
    LongVarV_int = [int(i) for i in LongVarV]

    ShortVarV = re.findall(reForShort,WebText.prettify())
    ShortVarV_int = [int(i) for i in ShortVarV]

    LongVarV_sum_SaveList.append(np.sum(LongVarV_int))
    ShortVarV_sum_SaveList.append(np.sum(ShortVarV_int))
    
    return LongVarV_sum_SaveList, ShortVarV_sum_SaveList


def GetQuery(kind,DateList):
    
    kind, DateList = kind, DateList

    LongVarV_sum_SaveList = []
    ShortVarV_sum_SaveList = []

    for TradeDate in DateList:
        Y_m = TradeDate[:6]
        d = TradeDate[6:]

        URL = 'http://www.cffex.com.cn/sj/ccpm/'+Y_m+'/'+d+'/'+kind+'.xml'
        r = requests.get(url=URL)

        WebText = BeautifulSoup(r.text,"lxml")
        r.close()
        
        print(TradeDate+' '+kind+' Complete',end='\r')
        
    return ReForLongShort(WebText)
    
def OutPut(longdatalist,shortdatalist,OutPutPath):
    
    LongVarV_sum_SaveList, ShortVarV_sum_SaveList = longdatalist, shortdatalist
    
    SaveDf = pd.DataFrame({'日期':DateList,'多单持仓增量':LongVarV_sum_SaveList,'空单持仓增量':ShortVarV_sum_SaveList})
    SaveDf.to_excel(OutPutPath+kind+'蜘蛛网策略数据更新至'+DateList[-1]+'.xlsx')
    
def Run(DateList,kindList,OutPutPath):
    
    for kind in kindList:
        LongVarV_sum_SaveList, ShortVarV_sum_SaveList = GetQuery(kind,DateList)
        OutPut(longdatalist,shortdatalist,OutPutPath)
    
### RUN ###
    
if __name__ == '__main__':
    
    # 日期数据，原始文件为excel：一列、列名Date、数据格式为日期形式
    TradeDateExcelPath = 'C:/Users/Thinkpad/Desktop/TradeDate.xlsx'
    
    # 爬取种类
    kindList = ['IF','IC','IH']
    
    # 数据输出路径
    OutPutPath = 'C:/Users/Thinkpad/Desktop/'
    
    # 日期数据处理
    DateList = TradeDateProcess(TradeDateExcelPath)
    
    # 爬取数据
    Run(DateList,kindList,OutPutPath)