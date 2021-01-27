from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("Man_Seok_Kkun")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else : 
      jobs = get_jobs(word)
      db[word] = jobs
  else :
    return redirect("/")
  return render_template("report.html", searchingBy = word, resultsNumber=len(jobs), jobs=jobs)

app.run(host="0.0.0.0")