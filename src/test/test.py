# /*!
#  * CucumberAPS_PythonLibrary | V.0.1
#  * (c) 2022 Afi
#  * Released under the MIT License.
#  */

from cucumberaps import *
from flask import Flask,render_template,redirect,url_for,request
import tempfile
app=Flask(__name__)
tmp=tempfile.NamedTemporaryFile()

@app.route('/')
def main():return render_template('index.html')

@app.route('/classic_method',methods=['GET','POST'])
def classic_method():
	result=None
	if request.method=='POST':
		if request.form['license']:
			license=request.form['license'];result=caps(type='classic',license_key=license)
			if result==True:result='True'
			else:result='False'
		else:result='False'
	return render_template('classic_method.html',result=result)

def token(result):
	with open(tmp.name,'w')as f:f.write(result)

@app.route('/csap_verification')
def csap_verification():
	with open(tmp.name,'r')as f:f.seek(0);tmp_token=f.read()
	result=caps(type='csap',callback_token=tmp_token);print(result)
	if result==True:
		with open(tmp.name,'w')as f:result='True';f.write(result)
		return redirect(url_for('csap_method'))
	else:return redirect(url_for('csap_method'))

@app.route('/csap_method',methods=['GET','POST'])
def csap_method():
	result='None'
	with open(tmp.name,'r')as f:f.seek(0);result_csap_verification=f.read()
	if result_csap_verification=='True':
		with open(tmp.name,'w')as f:result='';f.write(result)
		result='True'
	elif result_csap_verification=='False':
		with open(tmp.name,'w')as f:result='';f.write(result)
		result='False'
	elif request.method=='POST':
		if request.form['license']:
			license=request.form['license']
			try:link,result=caps(type='token',license_key=license,option='link',redirect_url=request.host_url+'csap_verification');token(result=result);return redirect(link,code=302)
			except:result='False'
		else:result='False'
	return render_template('csap_method.html',result=result)

@app.route('/endpoint_verification')
def get_endpoint_verification():
	with open(tmp.name,'r')as f:f.seek(0);tmp_token=f.read()
	result=caps(type='csap',callback_token=tmp_token,option='query')
	if result!='':
		with open(tmp.name,'w')as f:f.write(result)
		return redirect(url_for('get_endpoint'))
	else:return redirect(url_for('get_endpoint'))

@app.route('/get_endpoint',methods=['GET','POST'])
def get_endpoint():
	result='None'
	with open(tmp.name,'r')as f:f.seek(0);result_endpoint_verification=f.read()
	if result_endpoint_verification!='':
		with open(tmp.name,'w')as f:result='';f.write(result)
		result=result_endpoint_verification
	elif request.method=='POST':
		if request.form['license']:
			license=request.form['license']
			try:link,result=caps(type='token',license_key=license,option='link',redirect_url=request.host_url+'endpoint_verification');token(result=result);return redirect(link,code=302)
			except:result='False'
		else:result='False'
	return render_template('get_license_endpoint.html',result=result)

if __name__=='__main__':app.run(host='0.0.0.0',port=80)