sanat = ["kylläpä","taas","väsyttää","niin","paljon","että","pääpöytään"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri = laskuri +1

print(f"yli viiden kirjaimen sanoja on {laskuri}")