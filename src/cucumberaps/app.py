# /*!
#  * CucumberAPS_PythonLibrary | V.0.1
#  * (c) 2022 Afi
#  * Released under the MIT License.
#  */

"""

   _____                           _                      _____   _____  _____       _      _ _
  / ____|                         | |               /\   |  __ \ / ____||  __ \     | |    (_) |
 | |    _   _  ___ _   _ _ __ ___ | |__   ___ _ __ /  \  | |__) | (___  | |__) |   _| |     _| |__  _ __ __ _ _ __ _   _
 | |   | | | |/ __| | | | '_ ` _ \| '_ \ / _ \ '__/ /\ \ |  ___/ \___ \ |  ___/ | | | |    | | '_ \| '__/ _` | '__| | | |
 | |___| |_| | (__| |_| | | | | | | |_) |  __/ | / ____ \| |     ____) || |   | |_| | |____| | |_) | | | (_| | |  | |_| |
  \_____\__,_|\___|\__,_|_| |_| |_|_.__/ \___|_|/_/    \_\_|    |_____/ |_|    \__, |______|_|_.__/|_|  \__,_|_|   \__, |
                                                                    ______      __/ |                               __/ |
                                                                   |______|    |___/                               |___/
"""

import requests
import json

def caps_classic(license_key,option):
	token=requests.get('https://aktech.fr/api/v1/auth/init',headers={'Key':license_key})
	if token.status_code==200:
		token_i=json.loads(token.text);selfquery=token_i['token'];query={'token':selfquery};response=requests.get('https://aktech.fr/api/v1/auth/verify',params=query)
		if response.status_code==200:
			license=json.loads(response.text);code=license['code']
			if code=='LICENSE_AUTH_ACCEPTED':result=True
			elif code!='LICENSE_AUTH_ACCEPTED':code=license['code']
			else:result=False
		elif response.status_code==401:result=False;code='LICENSE_AUTH_REFUSED'
		elif response.status_code==500:result=False;code=' INTERNAL_SERVER_ERROR'
		elif response.status_code==404:result=False;code=' THE_API_NO_LONGER_EXISTS_AT_THIS_LOCATION'
		elif response.status_code==301:result=False;code=' THE_API_MOVED_TO_ANOTHER_LOCATION'
		else:result=False;code='API_UNREACHABLE'
	elif token.status_code==401:result=False
	elif token.status_code==500:result=False;code=' INTERNAL_SERVER_ERROR'
	elif token.status_code==404:result=False;code=' THE_API_NO_LONGER_EXISTS_AT_THIS_LOCATION'
	elif token.status_code==301:result=False;code=' THE_API_MOVED_TO_ANOTHER_LOCATION'
	else:result=False;code='API_UNREACHABLE'
	if option=='code':return code
	elif option=='query':return selfquery
	elif option=='license_key':return license_key
	elif option=='all':return code,selfquery,license_key
	else:return result
	return result

def caps_csap(callback_token,option):
	response=requests.get('https://aktech.fr/api/v1/auth/csap/callback',params={'token':callback_token})
	if response.status_code==200:
		sub_callback=json.loads(response.text);callback_token_return=sub_callback['token'];endpoint=requests.get('https://aktech.fr/api/v1/auth/csap/endpoint',headers={'Token':callback_token_return});sub=json.loads(endpoint.text);endpoint_token_return=sub['token']
		if option=='query':result=endpoint.text;return result
		elif option=='ip':result=sub['ip'];return result
		elif option=='key':result=sub['key'];return result
		elif option=='id':result=sub['id'];return result
		elif option=='project_id':result=sub['project_id'];return result
		elif option=='is_active':result=sub['is_active'];return result
		elif option=='is_banned':result=sub['is_banned'];return result
		elif option=='is_csap':result=sub['is_csap'];return result
		elif option=='ban_reason':result=sub['ban_reason'];return result
		elif option=='created_at':result=sub['created_at'];return result
		elif option=='updated_at':result=sub['updated_at'];return result
		elif endpoint_token_return==callback_token_return:result=True;return result
		else:result=False;return result
	elif response.status_code==401:result=False;return result
	else:result=False;return result
	result=False;return result

def caps_token(license_key,option,redirect_url):
	token=requests.get('https://aktech.fr/api/v1/auth/init',headers={'Key':license_key})
	if token.status_code==200:
		token_i=json.loads(token.text);result=token_i['token']
		if option=='link':
			if redirect_url!='':link='https://aktech.fr/api/v1/auth/csap/login?token='+token_i['token']+'&return_url='+redirect_url;return link,result
			link='https://aktech.fr/api/v1/auth/csap/login?token='+token_i['token'];return link,result
	else:result=False
	return result

def caps(type='classic',callback_token='',license_key='',option='',redirect_url='',multiple={}):
	try:
		if type=='csap':
			if not callback_token:raise ValueError('bad usage: type and callback_token are required for csap')
			else:0
		if not type:raise ValueError('bad usage: type and license_key are required')
		elif type=='classic':return caps_classic(license_key,option,**multiple)
		elif type=='csap':return caps_csap(callback_token,option,**multiple)
		elif type=='token':return caps_token(license_key,option,redirect_url,**multiple)
		elif type!='classic'and type!='csap'and type!='token'and type!='':raise ValueError('bad parameter: please choose csap parameter, token parameter or classic parameter')
	except:return'error'
	return