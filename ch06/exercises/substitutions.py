import json

def main():
    news = open("news.txt", "r").read()
    sub_fptr = open("subs.json", "r") 
    subs = json.load(sub_fptr)
    print(subs, type(subs))

    for k,v in subs.items():
        news = text.replace(k,v)

    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()
