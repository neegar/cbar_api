from flask import Flask, request, jsonify
import flask
import requests
import xmltodict
# from flask.ext.cache import Cache
# from pymemcache.client.base import Client
# from werkzeug.contrib.cache import MemcachedCache



app = flask.Flask(__name__)
#app.config["DEBUG"] = True

# cache = Cache(app, config={
#     'CACHE_TYPE': 'memcached',
#     'CACHE_MEMCACHED_SERVERS': ['127.0.0.1:11211'],
#     'CACHE_DEFAULT_TIMEOUT': 0
# })

# client = Client(('localhost', 11211))
# client.set('some_key', 'some_value')
# result = client.get('some_key')
# cache = MemcachedCache(['127.0.0.1:11311'])

# mydata = cache.get('currencies')
# cache.set('currencies', liste, timeout=10)

@app.route('/currency', methods=['GET'])
# @cache.cached(timeout=15 * 60)
def allCurrency():
    url = "https://www.cbar.az/currencies/11.06.2019.xml"
    result = requests.get(url)
    mydictionary = xmltodict.parse(result.text)
    my_list=mydictionary['ValCurs']['ValType'][1]['Valute']

    new_list = []
    for i in my_list:
        
        com_res={
            'key': i['@Code'],
            'value': i['Value']
        }
        new_list.append(com_res)
    return jsonify(new_list)




@app.route('/currency/<string:id>', methods=['GET'])
# @cache.cached(timeout=15 * 60)
def specialCurrency(id):
    url = "https://www.cbar.az/currencies/11.06.2019.xml"
    result = requests.get(url)
    mydictionary = xmltodict.parse(result.text)
    my_list=mydictionary['ValCurs']['ValType'][1]['Valute']

    for i in my_list:
        if i['@Code'] == id.upper():
            special_res = {
                    'key': id,
                    'value': i['Value']
                }
            return jsonify(special_res)
        else:
            return 'Enter valid currency'
    

if __name__=="__main__":
    app.run(host='0.0.0.0')