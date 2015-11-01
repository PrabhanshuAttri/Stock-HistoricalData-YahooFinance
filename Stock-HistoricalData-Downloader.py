import urllib
from R2D2 import *

# Company Symbols on NASDAQ
symbol = ['AA', 'ABT', 'ABX', 'ADI', 'ADM', 'AET', 'AMD', 'AMR', 'APC', 'AVP', 'AXP', 'BA', 'BAC', 'BAX', 'BBY', 'BK', 'BMC', 'BMY', 'BNI', 'BP', 'CA', 'CAT', 'CI', 'CL', 'COP', 'CVX', 'DD', 'DE', 'DIS', 'DOW', 'EK', 'EMC', 'EMR', 'FNM', 'FRE', 'FRX', 'GE', 'GLW', 'GPS', 'GSK', 'HAL', 'HD', 'HON', 'HPQ', 'HRB', 'IBM', 'IGT', 'JNJ' , 'JPM', 'JWN', 'KO', 'KR', 'LLY', 'LOW', 'LTD', 'LUV', 'MCD', 'MDT', 'MMM', 'MO', 'MOT', 'MRK', 'MRO', 'MU', 'MYL', 'NKE', 'NSM', 'NWS', 'OXY', 'PEP', 'PFE', 'PG', 'RSH', 'SLB', 'SLE', 'SLM', 'STJ', 'SYK', 'SYY', 'TGT', 'TJX', 'TMX', 'TXN', 'UN', 'UNH', 'UTX', 'VOD', 'VZ', 'WAG', 'WFC', 'WMB', 'WMT', 'XOM', 'XRX']
strDate = "3"
strMon = "0"
strYear = "2010"
i = 0 
for x in symbol:
	url = "http://ichart.yahoo.com/table.csv?s=" + x +"&a=" + strMon + "&b=" + strDate + "&c=" + strYear
	print str(i+1),
	log("\tRetrieving : " + x)
	i+=1
	urllib.urlretrieve (url, x+".csv")