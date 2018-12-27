import flask 
from flask import request
import psycopg2
import sys
import json
import decimal

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def getDrugPropotion():
	conn = psycopg2.connect("dbname=handydb user=postgres port=5555 password=***")
	cur = conn.cursor()
	disease = request.args.get('disease')
	sql = """select drug,mg from disease where disease='"""+disease+"""'"""
	cur.execute(sql)
	res=cur.fetchall()
	cur.close()
	conn.commit()
	rows = [ r for r in res ]
	return "{\"drugs\": "+str(rows).replace('(','{').replace(')','}')+"}"#json.dumps(''.join(res))

app.run()