import requests

import cgi
form = cgi.FieldStorage()
dataToUseInCalculate = form.getvalue('text')
print(calculate(dataToUseInCalculate))

def calculate(str):
	"""
	Returns None if no response, even after re-querying.
	"""
	str = str.replace("is", "%3D")
	str = str.replace("sign", "sin")
	str = str.replace(" ", "+")
	appid = "U2VY24-QJJRRGHTP7"
	url = "https://api.wolframalpha.com/v2/query?input=" + str + "&format=plaintext&output=JSON&appid="+ appid
	response = requests.get(url)
	ans = response.json()['queryresult']
	if ans['error']:
		return None
	if ('didyoumeans' in ans):
		return calculate(ans['didyoumeans'][1]['val'] if isinstance(ans, list) else ans['didyoumeans']['val'])
	return ans