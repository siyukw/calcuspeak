import wolframalpha as wa

inp = input("Wolfram Alpha input: ")
app_id = "AW2GL5-U4233G232U"
client = wa.Client(app_id)

res = client.query(inp)
answer = next(res.results).text

print(answer)
