import tkinter as tk
from tkinter import ttk
import urllib.request,urllib.parse,urllib.error
import json
from bs4 import BeautifulSoup

"""建議輸入關鍵字:
	JUMP FORCE
	MY HERO ONE'S JUSTICE
	Grand Theft Auto V
	Tom Clancy's Rainbow Six Siege
	PLAYERUNKNOWN'S BATTLEGROUNDS
"""
root=tk.Tk()
root.title("AGE")#設定GUI標題
root.geometry('400x250')#設定GUI大小

label=ttk.Label(root, text = "What's game do you want?")   #建立標籤物件
label.pack()       #將元件放入容器

ent = ttk.Entry(root,show=None)#建立輸入物件
ent.pack()

var = tk.StringVar()#變動字串

#搜尋價錢功能函式
def search_price_steam():
	g_n = ent.get()#取得輸入
	game_search = urllib.parse.quote(g_n)
	try:
		url_s_search = "https://store.steampowered.com/search/?term={}".format(game_search)#利用網站搜尋找到遊戲商品頁面
		f = urllib.request.urlopen(url_s_search)
		soup = BeautifulSoup(f ,'html.parser')
		#預設第一項搜尋結果為目標找到其超連結
		s_list = soup.find(id="search_result_container")
		link = s_list.find_all('a')
		l = list(link[0].get('href'))
		#存取網址方式
		count = 0
		page_store = ''
		for letter in l:
			page_store += letter
			if letter is "/":
				count += 1
			if count == 6:
				break
		details = urllib.request.urlopen(page_store)
		s_soup = BeautifulSoup(details ,'html.parser')
		#找到HTML中出現商品價格的節點
		con_money = s_soup.find(class_="game_purchase_price price")
		var.set(con_money.text.strip())
	except:
		var.set("No data. the game might have not released or your input is wrong.")


button_1=ttk.Button(root, text="(1)show the price", command = search_price_steam)
button_1.pack()     #將元件放入容器

#找出宣傳片的函式
def trailer():
	g_n = ent.get()
	game_search = urllib.parse.quote(g_n)
	game_name = g_n + " trailer"
	#youtube data api key
	api_key = "AIzaSyCeFY2SXS2UgXwYC7nzwg5Y1KYQEHRuzLk"
	game_name_search = urllib.parse.quote(game_name)
	try:
		#-----確認商店有沒有此商品用--------
		url_s_search = "https://store.steampowered.com/search/?term={}".format(game_search)#利用網站搜尋找到遊戲商品頁面
		f0 = urllib.request.urlopen(url_s_search)
		soup = BeautifulSoup(f0 ,'html.parser')
		s_list = soup.find(id="search_result_container")
		link = s_list.find_all('a')
		l = list(link[0].get('href'))
		#-------確認商店有沒有此商品用-----
		url_yt = "https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&type=video&key={}".format(game_name_search,api_key)
		f = urllib.request.urlopen(url_yt)
		data = json.loads(f.read())
		#請求會回傳json 找到videoid的value
		video = data['items'][0]['id']['videoId']
		global url_v
		url_v = "https://www.youtube.com/watch?v={}".format(video)
		output = data['items'][1]['snippet']['title'] + '\n' + url_v
		var.set(output)
	except:
		var.set("No data. the game might have not released or your input is wrong.")

button_2=ttk.Button(root, text="(2)watch the trailer", command = trailer)
button_2.pack()     #將元件放入容器

#顯示發行商資料的函式
def company_profile():
	g_n = ent.get()
	game_search = urllib.parse.quote(g_n)
	try:
		#利用上述搜尋價格的方式再找一次
		url_s_search = "https://store.steampowered.com/search/?term={}".format(game_search)
		f = urllib.request.urlopen(url_s_search)
		soup = BeautifulSoup(f ,'html.parser')
		s_list = soup.find(id="search_result_container")
		link = s_list.find_all('a')
		l = list(link[0].get('href'))
		count = 0
		page_store = ''
		for letter in l:
			page_store += letter
			if letter is "/":
				count += 1
			if count == 6:
				break
		details = urllib.request.urlopen(page_store)
		s_soup = BeautifulSoup(details ,'html.parser')
		#找出有顯示發行商名稱的節點
		find_com = s_soup.find_all(class_="dev_row")
		com_name = ''
		for cont in find_com :
			if type(cont.b) == type(cont):
				if cont.b.text == "Publisher:":
					com_name = cont.a.text
		#發行商名稱作為關鍵字
		api_key = "AIzaSyCOgskkEbsoA8oePMRdNq7oGtdBvo7ptfQ"#google map place api
		com_name_s = urllib.parse.quote(com_name)
		#利用 place api的搜尋功能
		url_p_search = "https://maps.googleapis.com/maps/api/place/queryautocomplete/json?key={}&input={}".format(api_key,com_name_s)
		r = urllib.request.urlopen(url_p_search)
		data = json.loads(r.read())
		#預設第一項搜尋結果為目標 找到第一項搜尋結果的位置及電話
		com_p_id = data['predictions'][0]['place_id']
		url_p = "https://maps.googleapis.com/maps/api/place/details/json?placeid={}&fields=name,formatted_address,rating,formatted_phone_number&key={}".format(com_p_id,api_key)
		f = urllib.request.urlopen(url_p)
		'''soup_com = BeautifulSoup(f, 'html.parser')
		print(soup_com.prettify())'''
		place = json.loads(f.read())
		answer = com_name
		try:
			answer = answer + "\n" + "Adress: " + place['result']['formatted_address']
		except:
			answer = answer + "\n" + "Adress: " + "None"
		try:
			answer = answer + "\n" + "Phone number: " + place['result']['formatted_phone_number']
		except:
			answer = answer + "Phone number: " + "None"
		var.set(answer)
	except:
		var.set("No data. the game might have not released or your input is wrong.")

button_3=ttk.Button(root, text="(3)detail of the publisher", command = company_profile)
button_3.pack()     #將元件放入容器

#結果顯示框
result = ttk.Label(root, textvariable=var)
result.pack()

root.mainloop()