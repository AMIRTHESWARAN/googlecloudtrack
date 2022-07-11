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
    return render_template("index.html",name=name, arr=badges)
  else:
    if request.method == "POST":
      ll = request.form.get("qllink")
      if not ll[41:]:
        return render_template("wrongurl.html")
      elif(ll[12:17]=='cloud'):
        return redirect("https://googlecloud.open-web-tech.repl.co"+"/?"+ll[52:]) #Your website link
      elif(ll[12:17]=='qwickl'):
        return redirect("https://googlecloud.open-web-tech.repl.co"+"/?"+ll[41:]) #Your website link
      else:
        return render_template("wrongurl.html")
    return render_template("form.html")
app.run(host='0.0.0.0', port=8080)
