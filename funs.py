#coding:utf-8

"""
関数：いろんな機能を实现
"""
import json
import pandas as pd
import jmespath
from jmespath import functions
import requests
import sys

def compToList(list1, list2):
	"compare two lists then put the result to another list,data in list1 but not in list2"
	
	diff = []
	
	for i in list1:
		if i not in list2:
			diff.append(i)

	return diff

def compToListByDict(list1, list2, key):
	"compare two lists then put the result to another list but display a Dictionary,data in list1 but not in list2"

	diff = []

	for i in res_user_a_id:
		temp = {}
		if i not in res_user_id:
			temp[key] = i
			diff.append(temp)

	return diff

def saveToJsonOrtxt(fn, datas):
	"save data to a file(data formate: json/txt...)"

	f = open(fn,"w+",encoding="utf-8")
	f.write(json.dumps(datas,ensure_ascii=False,indent=1))
	f.close()

def saveToOrig(fn, datas):
	"save to original file by bytes"

	f = open(fn,"wb")
	f.write(datas)
	f.close()

def isPathExist(path):
	"If path is not exist, then make dir this folder"
	os.makedirs(os.path.dirname(paths), exist_ok=True)
	# cwd = os.getcwd()
	# path = os.path.join(cwd, 'a')
	# os.chdir(path)

def spliceListToName(datas):
	"Traversing the array then splice a string to assignment but has a problem"
	"datas = ['Table ', 14, 14, '一致', 14] →　datas[0],datas[1],datas[2],datas[3],datas[4],実は　tuple(datas)"

	len_datas = len(datas)
	strs = ""
	for i in range(len_datas):
		strs = strs + r"datas[%d],"%i
	data_len = len(strs)
	str_data = strs[0:data_len-1]

	return eval(str_data)	# like tuple(datas) 結果

def html_temp1():
	"html テンプレート Ⅰ"

	html = """<!DOCTYPE html>
	<html lang="en">
	<head><meta charset="UTF-8"></head>
	<body>
	  <table border='1'>
	    <thead>
	     <tr>
	       <th>Date</th>
	     </tr>
	    </thead>
	    <tr>
			<th></th>
			<th>%s</th>
			<th>%d</th>
		</tr>
		<tr>
			<td>Test </td>
			<td>%s件</td>
		</tr>
	</body>
	</html>"""

	return html


def Diff2Lists(li1, li2): 
	"compare difference between li1 and li2"

	return (list(set(li1) - set(li2))) 

def JudgeNum(num1, num2, str1, str2):
	"Judge whether num1 is equal num2, if equal then = str1, or = str2 "
	"num2 is bigger than num1"
	result = str1 if (num1 == num2) else str2 +':　%d'%(num2-num1)
	return result

def countsList(list1):
	"Count the times in list1's variable"
	"return variable: counts"

	# list1 = [23,"Hello", "Hello", "89",87, "Bill", "Molly","Bill", "Bill"]

	timesDict = pd.value_counts(list1)

	return timesDict

def creatVarName(var,value):
	"create dynamicly variable names and assignment"
	# You can change by your options

	vars={}
	for x in range(1,10):
	    vars["string{0}".format(x)]="Hello"

	return vars

	"throw string1... get value"
	# for x in range(1,10):
	#     globals()["string%d"%x] = "Hello"

def jmesreplace():
	#
	datas = {
	    "foo": {
	        "bar": [
	            {"name": "one"}, 
	            {"name": "two"}
	        ]
	   	}
	}

	# new_data = jmespath.replace("foo.bar[1].name","hhhhh", datas)# dont have
	new_data = jmespath.remove("foo.bar[1]","hhhhh", datas)# dont have module 'jmespath' has no attribute 'remove'
	print(new_data)

def getJson(fname):
	"read file string and return json "
	temp = open(fname,"rb").read()
	js = json.loads(temp)

	return js

def searchJson(condition, data):
	"use jmespath module: 意味が少しです"
	# condition: serarch 条件
	# data: json 格式

	result = jmespath.search(con_u,json_u_1)

	return result

def getUrl():
	url = "https://idm-api.cub3.nri.co.jp/api/cudb/get-diff-data"

	header = {"Content-Type":"application/json","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSIsImtpZCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSJ9.eyJhdWQiOiJodHRwczovL2lkbS1hcGkuY3ViMy5ucmkuY28uanAvIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNmM5MzE0MTItNzZiMi00ZGRjLWI0NTItZGVmNjgxNWFkNmFiLyIsImlhdCI6MTU2NTIzNjk4NywibmJmIjoxNTY1MjM2OTg3LCJleHAiOjE1NjUyNDA4ODcsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84TUFBQUFWcHJSL2tPbjF3QnBpbXQyMXdHSkd2dWxJU2xKQkxCblE0YUg4dGRZNVNEMzdSaTBydG1JblBORjBtb1hJLy93K3poK0JqSEFwUWdDS1JyV3B3ZDZXWUZVSWY2bVFucVI4RnU0ckpuQjlvOD0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiOGE3ZTEyZDItZGZmYS00MzY3LThkOGEtMDBkMzdiNzMxMGMyIiwiYXBwaWRhY3IiOiIwIiwiaXBhZGRyIjoiMzYuMy44NC4xMjYiLCJuYW1lIjoi5p2O44CA6LuNKGR3cCkiLCJvaWQiOiJlMDY5MjY4OS1kN2Y4LTRlYjgtYTViZi1jZjE3NGE2YTA5OTciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjc3Mjg3MjE3Ni0yNDYzNTMxODI0LTM1NTY0OTIzMjQtMTA5NjEwIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiVEJ1ZDJRQkF0STNWZnBaNmNHMmkyQW9nZnJ4MTRPVnVscGxDSnpRSGlfRSIsInRpZCI6IjZjOTMxNDEyLTc2YjItNGRkYy1iNDUyLWRlZjY4MTVhZDZhYiIsInVuaXF1ZV9uYW1lIjoidG9uMDAwMDUtZHdwQGN1YjMubnJpLmNvLmpwIiwidXBuIjoidG9uMDAwMDUtZHdwQGN1YjMubnJpLmNvLmpwIiwidXRpIjoiZERSMFpnLTMxRXVhOWVTMzY2Z2JBUSIsInZlciI6IjEuMCJ9.AV2OOgXjHqzpQQrNxZSoDTmhkGKEL0rupeVfYncwTBz2z_Re7qu5SRyHrWeXe8yFk4GKtnplIhqWDjiBNvnnzljW9-ThNY-R71lSF_vGGqPCgtqvbu-SQc_G-X0wmV9a_gHIWt9rh4cjQtZwSYkmo2C5FJogi2_WL7WnlcGGNWno-uQraToNKLjDTWetnSQcGVMlDOlF8trRyafOn8XxIn1wFTzVwFxjM8-Ix3aUOx-TFHI1OO3wih9PSsX8_YpvhTiIbeD5-12iRVfbv4m5I6OaPqZMSl17WHtGvUGMOK_QRaLSFcGvMm6HPaP090iRJnViBMU7x44Gf5vFDCgSBw"}
	body = {
		"import_table_name": "MT_UserRsrcAcntInfo",
		"import_date_time": "2019-07-01 17:26:26.310",
		"trunsact_no": "20190610900004"
	}

	response = requests.post(url = url, headers = header,data = json.dumps(body))
	# if Content-Type:application/x-www-form-urlencoded, data = parse.urlencode(body)
	result = response.content
	# print(result)
	print(type(result))		# <class 'bytes'>
	# result_json = result.decode('utf-8')
	# print(len(result_json))
	# print(result_json)

	# return result_json
	#------------------------------
	# test:html无转义
	#-------------------------------
	f = open("1.json","wb")
	f.write(result)
	f.close()

	

	#------------------------------
	# 保存成json格式
	#-------------------------------
	# f = open("test.json","w",encoding="utf-8")
	# f.write(json.dumps(result_json,ensure_ascii=False,indent=1))
	# f.close()

	# data = eval(response.decode())
 
	# data = json.dumps(data,indent=4,separators=(',', ': '),ensure_ascii=False)
	# print(data)

def modifyJsonKey():

	temp = {
		"name":"July",
		"age": 24,
		"enjoy": "creative"
	}

	temp["element"] = temp.pop("name")
	print(json.dumps(temp))

def getFilesName():
	import os
	dir_new = os.getcwd()
	dir_new = "C:\\liaga\\その他\\Network\\書作\\世界经典名著电子书\\一生必读的60部名著"
	filess = []
	for curdir,dirs,files in os.walk(dir_new):
		# print(dirs)
		filess.append(files)
		break
	
	# print(len(files))
	# filesss = filter(lambda x:x != "[]", filess)
	# print(filess)
	
	with open("fileName.txt","a+",encoding="utf-8") as f:
		for i in range(0,len(filess[0])):
			try:
				f.write(filess[0][i]+"\n")
			except Exception as e:
				print("write failed, ",e)
				break

	# print(dir)

if __name__ == '__main__':
	print("starting ")
	# data = getUrl()
	# modifyJsonKey()
	# getItem()
	# print([x for x in range(0,2)])
	# print(pow(2,31)-1)
	getFilesName()
	print("end~")

	
	