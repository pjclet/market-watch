import yfinance as yf
import time
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from twitter import *
from credentials import api_key, api_secret_key, access_token, access_token_secret

'''

all  :  {'zip': '404000', 'sector': 'Technology', 'fullTimeEmployees': 1892, 'longBusinessSummary': "Daqo New Energy Corp., together with its subsidiaries, manufactures and sells polysilicon to photovoltaic product manufactures in the People's Republic of China. It offers ready-to-use polysilicon, and packaged to meet crucible stacking, pulling, and solidification products. The company was formerly known as Mega Stand International Limited and changed its name to Daqo New Energy Corp. in August 2009. Daqo New Energy Corp. was founded in 2006 and is based in Wanzhou, the People's Republic of China.", 'city': 'Wanzhou', 'phone': '86 23 6486 6666', 'country': 'China', 'companyOfficers': [], 'website': 'http://www.dqsolar.com', 'maxAge': 1, 'address1': '666 Longdu Avenue', 'industry': 'Semiconductor Equipment & Materials', 'previousClose': 62.33, 'regularMarketOpen': 60.6, 'twoHundredDayAverage': 32.01657, 'trailingAnnualDividendYield': None, 'payoutRatio': 0, 'volume24Hr': None, 'regularMarketDayHigh': 68.55, 'navPrice': None, 'averageDailyVolume10Day': 2550280, 'totalAssets': None, 'regularMarketPreviousClose': 62.33, 'fiftyDayAverage': 48.36073, 'trailingAnnualDividendRate': None, 'open': 60.6, 'toCurrency': None, 'averageVolume10days': 2550280, 'expireDate': None, 'yield': None, 'algorithm': None, 'dividendRate': None, 'exDividendDate': None, 'beta': 0.83727, 'circulatingSupply': None, 'startDate': None, 'regularMarketDayLow': 60.43, 'priceHint': 2, 'currency': 'USD', 'trailingPE': 65.14423, 'regularMarketVolume': 1395666, 'lastMarket': None, 'maxSupply': None, 'openInterest': None, 'marketCap': 4707527680, 'volumeAllCurrencies': None, 'strikePrice': None, 'averageVolume': 2831866, 'priceToSalesTrailing12Months': 8.6092825, 'dayLow': 60.43, 'ask': 68.29, 'ytdReturn': None, 'askSize': 800, 'volume': 1395666, 'fiftyTwoWeekHigh': 68.81, 'forwardPE': 19.357143, 'fromCurrency': None, 'fiveYearAvgDividendYield': None, 'fiftyTwoWeekLow': 8.318, 'bid': 67.96, 'tradeable': False, 'dividendYield': None, 'bidSize': 800, 'dayHigh': 68.55, 'exchange': 'NYQ', 'shortName': 'DAQO New Energy Corp.', 'longName': 'Daqo New Energy Corp.', 'exchangeTimezoneName': 'America/New_York', 'exchangeTimezoneShortName': 'EST', 'isEsgPopulated': False, 'gmtOffSetMilliseconds': '-18000000', 'quoteType': 'EQUITY', 'symbol': 'DQ', 'messageBoardId': 'finmb_84196527', 'market': 'us_market', 'annualHoldingsTurnover': None, 'enterpriseToRevenue': 8.541, 'beta3Year': None, 'profitMargins': 0.13983, 'enterpriseToEbitda': 25.083, '52WeekChange': 4.8405175, 'morningStarRiskRating': None, 'forwardEps': 3.5, 'revenueQuarterlyGrowth': None, 'sharesOutstanding': 69483800, 'fundInceptionDate': None, 'annualReportExpenseRatio': None, 'bookValue': 9.241, 'sharesShort': 6900587, 'sharesPercentSharesOut': 0.099300005, 'fundFamily': None, 'lastFiscalYearEnd': 1577750400, 'heldPercentInstitutions': 0.84562, 'netIncomeToCommon': 76709600, 'trailingEps': 1.04, 'lastDividendValue': None, 'SandP52WeekChange': 0.14317095, 'priceToBook': 7.3314576, 'heldPercentInsiders': 0.11934, 'nextFiscalYearEnd': 1640908800, 'mostRecentQuarter': 1601424000, 'shortRatio': 3.44, 'sharesShortPreviousMonthDate': 1605225600, 'floatShares': None, 'enterpriseValue': 4670011392, 'threeYearAverageReturn': None, 'lastSplitDate': 1605571200, 'lastSplitFactor': '5:1', 'legalType': None, 'lastDividendDate': None, 'morningStarOverallRating': None, 'earningsQuarterlyGrowth': 3.166, 'dateShortInterest': 1607990400, 'pegRatio': 0.24, 'lastCapGain': None, 'shortPercentOfFloat': None, 'sharesShortPriorMonth': 6575255, 'impliedSharesOutstanding': None, 'category': None, 'fiveYearAverageReturn': None, 'regularMarketPrice': 60.6, 'logo_url': 'https://logo.clearbit.com/dqsolar.com'}


y = [100,200,300]
print(y)


plt.plot(y)
plt.title("Price Graph for test")
plt.xlabel("Time since start")
plt.ylabel("Price")
plt.show()

	
	


'''


def initialize_data(data, tracking):

	message = "Tracker now live:\nTickers online: "

	for name, buy_price in tracking:
		print("Checking and ititializing: " + name)	

		temp_ticker = yf.Ticker(name)

		'''		if !temp_ticker:
			return	
		else'''

		name_test = check_name(name)
		if (not name_test[0]):
			print(name + " is not a valid Ticker ID.")
		else:
			temp_data = {}
			print(temp_ticker.info)
			temp_data["all"] = temp_ticker.info

			#temp_data["current_price"] = temp_data["all"]["ask"]

			t = temp_ticker.history()
			last_quote = (t.tail(1)['Close'].iloc[0])
			temp_data["current_price"] = last_quote
			temp_data["buy_price"] = buy_price
			temp_data["minute_change"] = 0.0
			temp_data["past_prices"] = [temp_data["current_price"]]
			data[name] = temp_data

			message += "\n  {} | {}".format(name, name_test[1]) 

		print("---")

	print(message)
	# t = Twitter(auth=OAuth(access_token, access_token_secret, api_key, api_secret_key))
	# t.statuses.update(status=message)



	'''
	msft = yf.Ticker("MSFT")
	
	data['MSFT'] = {"current_price" : msft.info['regularMarketPrice'] , "minute_change" : 0.00} 

	tsla = yf.Ticker("TSLA")
	data['TSLA'] = {"current_price" : tsla.info['regularMarketPrice'] , "minute_change" : 0.00} 
	'''

def check_name(name):
	ticker_file = open("nasdaqlisted.txt", "r")
	is_valid = False
	while True:
		line = ticker_file.readline()
		if not line:
			break
		else:
			parsed_line = line.split("|")
			if parsed_line[0] == name:
				print("Now tracking: {}, {}".format(parsed_line[0], parsed_line[1]))
				return (True, parsed_line[1])

	ticker_file = open("otherlisted.txt", "r")
	while True:
		line = ticker_file.readline()
		if not line:
			break
		else:
			parsed_line = line.split("|")
			if parsed_line[0] == name:
				print("Now tracking: {}, {}".format(parsed_line[0], parsed_line[1]))
				return (True, parsed_line[1])
	return (False, "")



def update_data(data):
	read = json.loads(open("data.json", "r").read())
	for name in read:
		print("updating: " + name)

		temp_ticker = yf.Ticker(name)

		data[name]["all"] = temp_ticker.info

		# data[name]["current_price"] = data[name]["all"]['ask']
		t = temp_ticker.history()
		last_quote = (t.tail(1)['Close'].iloc[0])
		data[name]["current_price"] = last_quote

		data[name]["minute_change"] = float((data[name]["current_price"] - read[name]["current_price"]) / read[name]["current_price"])
		data[name]["past_prices"].append(data[name]["current_price"])

		with open("data.json", "w") as outfile:
			json.dump(data, outfile, indent = 2)
		outfile.close()


def print_data():
	read = json.loads(open("data.json", "r").read())
	for key , val in read.items():
		print(key + " -- ")
		for key2, val2 in val.items():
			print(key2, " : ", val2)
		print("\n")


def update_graph():
	read = json.loads(open("data.json", "r").read())

	for name in read:
		mpl.use("tkagg")

		y = np.array(read[name]["past_prices"])
		# print(y)
		x = np.array(list(range(0,len(y))))
		dydx = [100 * (x - z) for x,z in zip(y[:-1], y[1:])]

		print(x)
		print(y)
		print(dydx)

		upper = y[0] + (0.005 * y[0])
		lower = y[0] - (0.005 * y[0])

		yUpper = np.ma.masked_where(y < upper, y)
		yLower = np.ma.masked_where(y > lower, y)
		yMiddle = np.ma.masked_where((y < lower) | (y > upper), y)

		fig,ax = plt.subplots()
		ax.plot(x, yMiddle, color="b")
		ax.plot(x, yUpper, color="g")
		ax.plot(x, yLower, color="r")

		plt.axhline(y=read[name]["buy_price"], color ="violet", linestyle="--")

		plt.draw()
		plt.title("Price Graph for {}".format(name))
		plt.xlabel("Time since start")
		plt.ylabel("Price")
		plt.savefig("{}Chart.png".format(name))
		plt.clf()

		'''
		points = np.array([x,y]).T.reshape(-1,1,2)
		segments = np.concatenate([points[:-1], points[1:]], axis=1)

		fig, axs = plt.subplots(1,1,sharex=True, sharey=True)

		norm = plt.Normalize(min(dydx), max(dydx))
		lc = LineCollection(segments, cmap="viridis", norm=norm)
		lc.set_array(dydx)
		lc.set_linewidth(2)
		'''
		#line = axs[0].add_collection(lc)
		#fig.colorbar(line, ax=axs[0])
		# print(x)





		# plt.plot(x,y)
		
def tweet_update(message):
	t = Twitter(auth=OAuth(access_token, access_token_secret, api_key, api_secret_key))
	t.statuses.update(status=message)

def tweet_picture_update(message, name):
	t = Twitter(auth=OAuth(access_token, access_token_secret, api_key, api_secret_key))

	with open("{}Chart.png".format(name), "r") as imagefile:
		imagedata = imagefile.read()

	t_upload = Twitter(domain='upload.twitter.com',
    	auth=OAuth(access_token, access_token_secret, api_key, api_secret_key))

	id_img = t_upload.media.uploa(media=imagedata)["media_id_string"]

	t.statuses.update(status=message, media_ids=id_img)


if __name__ == "__main__":

	print("Enter the stocks you would like to track today: ")

	tracking = []
	use_last = False

	# all new inputs
	while True:
		inp = input().upper()
		if inp == "":
			break;
		if inp == "USE LAST" or inp == "CONTINUE" or inp == "C":
			use_last = True
			break
		else:
			print("Buy price: ")
			inp2 = input().upper()
			temp = (inp, float(inp2))
			tracking.append(temp)

	data = {}
	if not use_last:
		initialize_data(data, tracking)
	else:
		print("using last now")
		data = json.loads(open("data.json", "r").read())

	#json_test = json.dumps(data, indent = 2)
	#print(json_test)

	with open("data.json", "w") as outfile:
		json.dump(data, outfile, indent = 2)

	# t = Twitter(auth=OAuth(access_token, access_token_secret, api_key, api_secret_key))

	


	time.sleep(1)

	# read the data

	
	print_data()
	tweet_picture_update("Test picture tweet: ", "PRTY")

	



	
	while True:

		update_data(data)
		print_data()
		update_graph()

		time.sleep(10)

	


		#print(i)
	#for i in read:
	#	print(i)

	# message = "MSFT's current market price is {:.2f}.".format(msft.info['regularMarketPrice'])

	# status = api.PostUpdate(message)
	# t.statuses.update(status=message)
	# t.direct_messages.new(screen_name="pj_clet", text=message)
	# t.direct_messages.new( user="pj_clet", text="I think yer swell!")




	print("success")
