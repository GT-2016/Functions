#coding:utf-8

"""
関数：いろんな機能を实现
"""
import json
import pandas as pd
import jmespath
from jmespath import functions

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



if __name__ == '__main__':
	jmesreplace()
	
	print("end~")

	
	