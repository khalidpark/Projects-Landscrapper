#from flask import Flask, render_template, request, redirect
#from scrapper import extract_land
from scrapper import get_lands

get_lands = get_lands()




#app = Flask("Man_Seok_Kkun")

#db = {}

#@app.route("/")
#def home():
#  return render_template("home.html")

#@app.route("/test")
#def test():
#  return extract_land('https://new.land.naver.com/offices?ms=37.7668564,126.7116667,17&a=TJ&b=A1&e=RETAIL&g=10000&ad=true')

#@app.route("/report")
#def report():
#  word = request.args.get('word')
#  if word:
#    word = word.lower()
#    existingLands = db.get(word)
#    if existingLands:
#      lands = existingLands
#    else : 
#      lands = get_lands(word)
#      db[word] = lands
#  else :
#    return redirect("/")
#  return render_template("report.html", searchingBy = word, resultsNumber=len(jobs), jobs=jobs)

#app.run(host="0.0.0.0")