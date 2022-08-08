from flask import Flask, render_template, request
from neo4j import GraphDatabase
import json

app = Flask(__name__)





driver = GraphDatabase.driver("bolt://localhost:11012", auth=("neo4j", "Helen332992"))


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/search')
def get_search():
    return render_template('search.html')

@app.route('/education')
def get_education():
    return render_template('education.html')

@app.route('/transport')
def get_transport():
    return render_template('transport.html')

@app.route('/cities')
def get_cities():
    return render_template('cities.html')

@app.route('/energy')
def get_energy():
    return render_template('energy.html')

@app.route('/health')
def get_health():
    return render_template('health.html')

@app.route('/international')
def get_international():
    return render_template('international.html')

@app.route('/introduction')
def get_introduction():
    return render_template('introduction.html')




@app.route('/graph',methods=['GET'])
def get_graph():
    i = json.load(open('data.json', 'r', encoding='utf-8'))
    return i


@app.route('/result',methods=['POST','GET'])
def search():
    content = request.form.get('content')
    with driver.session() as session:
        results = session.run('match p=(n)-[r:ns0__landingPage]->(m)where (n:ns0__Dataset and n:'+content+') return n.ns1__title,m.uri,n.ns1__description ').values()
    results_list = []
    for i in results:
        dic = {'title':i[0],'url':i[1],'description':i[2]}
        results_list.append(dic)
    return render_template('result.html',results=results_list,content=content)

@app.route('/result_publisher',methods=['POST','GET'])
def search_publisher():
    publisher = request.form.get('publisher')
    with driver.session() as session:
        results = session.run('MATCH p=(n:ns0__Dataset)-[r:ns1__publisher]->(m) where m.ns4__name="'+publisher+'" return n.ns1__title, n.uri').values()
    results_list = []
    for i in results:
        dic = {'dataset': i[0], 'url': i[1]}
        results_list.append(dic)
    return render_template('result_publisher.html',results=results_list, publisher=publisher )





if __name__ == '__main__':
    app.run(debug=True)