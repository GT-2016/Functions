#coding:utf-8
"""
1. https request paramsters change
2. get result
3. save result to a file
4. read this file and then save to another file by json
5. python get time by jmester.search
6. by this time get the json
7. save json to CuDB.json file
8. save the search condition

for 3-5 if can save file to a json file then donnot need to do 4th step
"""
import requests
import json
from jmespath import search
import os

def getUrl():
	url = "https://idm-api.cub3.nri.co.jp/api/cudb/get-diff-data"

	header = {"Content-Type":"application/json","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSIsImtpZCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSJ9.eyJhdWQiOiJodHRwczovL2lkbS1hcGkuY3ViMy5ucmkuY28uanAvIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNmM5MzE0MTItNzZiMi00ZGRjLWI0NTItZGVmNjgxNWFkNmFiLyIsImlhdCI6MTU2NTIzNjk4NywibmJmIjoxNTY1MjM2OTg3LCJleHAiOjE1NjUyNDA4ODcsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84TUFBQUFWcHJSL2tPbjF3QnBpbXQyMXdHSkd2dWxJU2xKQkxCblE0YUg4dGRZNVNEMzdSaTBydG1JblBORjBtb1hJLy93K3poK0JqSEFwUWdDS1JyV3B3ZDZXWUZVSWY2bVFucVI4RnU0ckpuQjlvOD0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiOGE3ZTEyZDItZGZmYS00MzY3LThkOGEtMDBkMzdiNzMxMGMyIiwiYXBwaWRhY3IiOiIwIiwiaXBhZGRyIjoiMzYuMy44NC4xMjYiLCJuYW1lIjoi5p2O44CA6LuNKGR3cCkiLCJvaWQiOiJlMDY5MjY4OS1kN2Y4LTRlYjgtYTViZi1jZjE3NGE2YTA5OTciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjc3Mjg3MjE3Ni0yNDYzNTMxODI0LTM1NTY0OTIzMjQtMTA5NjEwIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiVEJ1ZDJRQkF0STNWZnBaNmNHMmkyQW9nZnJ4MTRPVnVscGxDSnpRSGlfRSIsInRpZCI6IjZjOTMxNDEyLTc2YjItNGRkYy1iNDUyLWRlZjY4MTVhZDZhYiIsInVuaXF1ZV9uYW1lIjoidG9uMDAwMDUtZHdwQGN1YjMubnJpLmNvLmpwIiwidXBuIjoidG9uMDAwMDUtZHdwQGN1YjMubnJpLmNvLmpwIiwidXRpIjoiZERSMFpnLTMxRXVhOWVTMzY2Z2JBUSIsInZlciI6IjEuMCJ9.AV2OOgXjHqzpQQrNxZSoDTmhkGKEL0rupeVfYncwTBz2z_Re7qu5SRyHrWeXe8yFk4GKtnplIhqWDjiBNvnnzljW9-ThNY-R71lSF_vGGqPCgtqvbu-SQc_G-X0wmV9a_gHIWt9rh4cjQtZwSYkmo2C5FJogi2_WL7WnlcGGNWno-uQraToNKLjDTWetnSQcGVMlDOlF8trRyafOn8XxIn1wFTzVwFxjM8-Ix3aUOx-TFHI1OO3wih9PSsX8_YpvhTiIbeD5-12iRVfbv4m5I6OaPqZMSl17WHtGvUGMOK_QRaLSFcGvMm6HPaP090iRJnViBMU7x44Gf5vFDCgSBw"}
	body = {
	    "import_table_name": "MT_UserRsrcAcntInfo",
	    "import_date_time": "2019-07-01 17:26:26.310",
	    "trunsact_no": "20190610900004"
	}

	response = requests.post(url = url, headers = header,data = json.dumps(body))
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
	
	f = open("1.json","w+",encoding="utf-8")
	try:
		f.write(json.dumps(result,ensure_ascii=False,indent=1))
	except Exception as e:
		print("write error: ",e)
	finally:
		f.close()
	
	
	data_csdb = open("1.json","rb").read()
	print("data_csdb:",type(data_csdb))

	if data_csdb:
		json_csdb = json.loads(data_csdb)

		con_cudb = "length(items[].RegistationDate)"
		con_cudb = "items[].RegistationDate"

		li = search(con_cudb,json_csdb)

		if li:
			if isinstance(li, int):
				
				print(li)
			else:
				lin_len = len(li)
				print(li[lin_len-10001])
		else:
			print("not find")
	else:
		json_csdb = ""
	# print(data_csdb)
	#------------------------------
	# 保存成json格式
	#-------------------------------
	# f = open("test.json","w",encoding="utf-8")
	# f.write(json.dumps(result_json,ensure_ascii=False,indent=1))
	# f.close()

def downfile(fold, season, yearId, time):
	name = ["_fe_am_qs.pdf","_fe_am_ans.pdf","_fe_pm_ans.pdf", "_fe_pm_cmnt.pdf","_fe_pm_qs.pdf"]

	newname = list(map(lambda x:time +season +x, name))
	print(newname)

	for n in newname:
		url = "https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_%s_%d/"%(time,yearId)
		response = requests.get(url + n)
		# if "am" in n:

		# 	response = requests.get(url1+n)
		# else:
		# 	response = requests.get(url2+n)

		basepath = "C:\\liaga\\その他\\試験\\2019-04-19\\"
		filefold = fold
		newpath = os.path.join(basepath, filefold)

		if not os.path.exists(newpath):
			os.mkdir(newpath)


		with open(os.path.join(newpath, n),"wb") as file:
			file.write(response.content)

def downfileExe():
	year = 2009
	for i in range(21, 29):
		downfile("平成%d年春"%i,"h", 1,"%dh%d"%(year,i))
		downfile("平成%d年秋"%i,"a", 2,"%dh%d"%(year,i))
		year = year+1


def listFileSize(path):
	basepath = "C:\\liaga\\その他\\試験\\"
	newpath = os.path.join(basepath, path)

	paths = os.listdir(newpath)
	for p in paths:
		print(p,"-----------")
		ppath = os.path.join(newpath, p)

		if os.path.isdir(ppath):
			files = os.listdir(ppath)
			for file in files:
				filepath = os.path.join(ppath, file)
				size = os.path.getsize(filepath)
				print(file, sizeChange(size))

def sizeChange(bt):
	if bt < 1024:
		return str(bt)+" Bytes"
	elif bt < 1024 ** 2:
		return str(round(bt / 1024.0,1)) + ' KBytes'
	elif bt < 1024 ** 3:
		return str(round(bt / (1024.0 ** 2),1)) + ' MBytes'
	elif bt < 1024 ** 4:
		return str(round(bt / (1024.0 ** 3),1)) + ' GBytes'
	elif bt < 1024 ** 5:
		return str(round(bt / (1024.0 ** 4),1)) + ' TBytes'
	else:
		return str(round(bt),1) + ' Bytes'

if __name__ == '__main__':
	print("========================")
	
	# time = "ddd"
	# url1 = "https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_%s_1/"%time
	
	listFileSize("2019-04-19")
	print("----end----")
