from fastapi import FastAPI
from urllib import request

app = FastAPI()

@app.get("/")
def hello():
  return {"path root"}
@app.get("/hola")
def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

@app.get("/suma")
def sum(a,b):
    return {"result":a+b}


@app.get("/hola-mundo")
def hello():
  return {"Hello world!"}

@app.get("/archivo")
def archivo():

    def get_pib(url, country='ES'):
        f = request.urlopen(url)
        data = f.read().decode('utf-8').split('\n') 
        data = [i.split('\t') for i in data] 
        data = [list(map(str.strip, i)) for i in data] 
        for i in data:
                i[0] = i[0].split(',')[-1] 
        data[0][0] = 'years'
        data = {i[0]:i[1:] for i in data}
        result = {data['years'][i]:data[country][i] for i in range(len(data['years']))}
        return result

    variable =  get_pib('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true').items()
    return variable