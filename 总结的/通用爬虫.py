import requests
#爬取一个网页全部信息，构造了请求头
# def getHTMLText(url):
# 	try:
# 		kv = {'user-agent':'Mozilla/5.0'}
# 		response = requests.get(url, headers=kv)	#请求url链接，
# 		response.raise_for_status()	#如果状态码不是200，引发HTTPError
# 		response.encoding = response.apparent_encoding	#用apparent_encoding代替encoding使得解码正确解码
# 		return response.text	#返回网页内容
# 	except:
# 		return "产生异常"

#向百度提交请求词爬取信息，百度本身提供关键词接口，是：https://www.baidu.com/s?wd=keyword
def BaiDuSearch():
	keyword = "python"
	try:
		kv = {'wd':keyword}
		response = requests.get("https://www.baidu.com/s", params=kv)
		print(response.request.url)
		response.raise_for_status()
		print(len(response.text))
	except:
		print("爬取失败")



if __name__ == "__main__":
	# url = "https://www.baidu.com/"
	# print(getHTMLText(url))
	BaiDuSearch()