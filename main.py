from flask import Flask, render_template, request, redirect
from urllib.request import urlopen
from bs4 import BeautifulSoup
app = Flask('app')
@app.route('/', methods =["GET", "POST"])
def gfg():
  if request.query_string:
    badges =[]
    url1 = str(request.query_string)[2:-1]
    url="https://www.cloudskillsboost.google/public_profiles/"+url1
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html,'html5lib')
    name = soup.find('h1', attrs={'class':'ql-headline-1'}).text
    if (name[1:-1]=="Jumpstart your cloud career"):
      return render_template("wrongurl.html") #wrong url entered
    if (not name[1:-1]):
      return render_template("wrongurl.html")
    for a in soup.findAll('span', attrs={'class':'ql-subhead-1 l-mts'}):
      badges.append(a.text[1:-1])
    res = [''] * 60
    ress = ['']* 60
    t = ['Google Cloud Essentials', 'Getting Started: Create and Manage Cloud Resources ', 'Baseline: Infrastructure', 'Perform Foundational Infrastructure Tasks in Google Cloud', 'Networking in Google Cloud',
 'Build and Secure Networks in Google Cloud', 'Kubernetes in Google Cloud ', 'Deploy to Kubernetes in Google Cloud ', 'Cloud Engineering ', 'Setup and Configure a Cloud Environment in Google Cloud', 'DevOps Essentials', 'Implement DevOps in Google Cloud',
  'Understanding Your Google Cloud Costs', 'Google Cloud Solutions I', 'Cloud Architecture', 'Cloud Architecture: Design, Implement, and Manage', "Google Cloud's Operations Suite", 'Monitor and Log with Google Cloud Operations Suite', 'Google Developer Essentials', 
  'OK Google: Build Interactive Apps with Google Assistant', 'Build Interactive Apps with Google Assistant', 'Cloud Development', 'Website on Google Cloud',
 'Build a Website on Google Cloud', 'Baseline: Deploy & Develop', 'Exploring APIs', 'IoT in the Google Cloud', 'Workspace: Add-ons', 'Build Apps & Websites with Firebase',
     'Serverless Firebase Development', 'Google Cloud Run Serverless Workshop', 'Serverless Cloud Run Development', 'BigQuery Basics for Data Analysts ', 'Insights from Data with BigQuery ',
      'BigQuery for Machine Learning','Create ML Models with BigQuery ML', 'BigQuery for Marketing Analysts', 'Bracketology with Google Cloud', 'Applied Data: Blockchain', 'Data Engineering', 'Engineer Data in Google Cloud', 
      'Cloud SQL','BigQuery for Data Warehousing', 'Build and Optimize Data Warehouses with BigQuery', 'Scientific Data Processing', 'Google Cloud Solutions II: Data and Machine Learning', 'Baseline: Data, ML, AI', 'Perform Foundational Data, ML, and AI Tasks in Google Cloud', 
      'Explore Machine Learning Models with Explainable AI',
      'Intro to ML: Language Processing', 'Intro to ML: Image Processing', 'Machine Learning APIs', 'Integrate with Machine Learning APIs', 'Intermediate ML: TensorFlow on Google Cloud', 'Advanced ML: ML Infrastructure',
      'Cloud Logging', 'Security & Identity Fundamentals', 'Ensure Access & Identity in Google Cloud', 'Language, Speech, Text, & Translation with Google Cloud APIs', 'Cloud Healthcare API']
    a = 'w3-green'
    for i in range(60):
      if t[i] in badges:
        res[i]='w3-green'
    return render_template("index.html",name=name, arr=badges)
  else:
    if request.method == "POST":
      ll = request.form.get("qllink")
      if not ll[41:]:
        return render_template("wrongurl.html")
      elif(ll[12:17]=='cloud'):
        return redirect("https://googlecloud.open-web-tech.repl.co"+"/?"+ll[52:])
      elif(ll[12:17]=='qwickl'):
        return redirect("https://googlecloud.open-web-tech.repl.co"+"/?"+ll[41:])
      else:
        return render_template("wrongurl.html")
    return render_template("form.html")
app.run(host='0.0.0.0', port=8080)
