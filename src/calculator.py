import requests, cgi
#form = cgi.FieldStorage()
#dataToUseInCalculate = form.getvalue('text')
#print(calculate(dataToUseInCalculate))

def calculate(str):
	"""
	Returns None if no response, even after re-querying.
	"""
	#str = str.replace("is", "%3D")
	str = str.lower()
	str = str.replace("sign", "sin")
	str = str.replace("Sign", "sin")
	str = str.replace("+", "%2B")
	str = str.replace("DX", "dX")
	str = str.replace("Derivative", "d%2Fdt")
	str = str.replace("derivative", "d%2Fdt")
	str = str.replace(" ", "+")

	appid = "U2VY24-QJJRRGHTP7"
	url = "https://api.wolframalpha.com/v2/query?input=" + str + "&format=plaintext&output=JSON&appid="+ appid
	response = requests.get(url)
	ans = response.json()['queryresult']
	print(str)
	if ans['error']:
		return None
	if ('didyoumeans' in ans):
		correction = ans['didyoumeans']
		return calculate(correction[0]['val'] if isinstance(correction, list) else correction['val'])
	pods = ans['pods']
	solution = ""
	figure = ""
	for obj in pods:
		title = obj['title']
		if ("Solution" in title or title == 'Complex solutions' or "Result" in title or 'Differential equation solution' in title or 'Indefinite integral' in title):
			solution += obj['subpods'][0]['plaintext']
		if (title == 'Geometric figure'):
			figure = obj['subpods'][0]['plaintext']
	answer = "The answer is " + solution + "."
	if (figure != ""):
		answer += "The geometric figure is a " + figure
	answer = answer.replace("sqrt", " root  ")
	answer = answer.replace("^", " to the power of ")
	answer = answer.replace("-", " minus ")
	answer = answer.replace("!", " not ")
	answer = answer.replace("/", " divided by ")
	answer = answer.replace("XMPTools", " plus ")
	answer = answer.replace("_", "")

	return answer
