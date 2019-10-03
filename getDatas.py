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
import zipfile
from pathlib import Path
import shutil
from copy import copy

CON = {
	"1" : "追加",
	"2" : "変更",
	"3" : "削除"
}

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

def unZip():
	file = "C:\\liaga\\その他\\Network\\書作\\世界经典名著电子书\\《世界名著合集54本》经典珍藏.zip"	
	zF = zipfile.ZipFile(file, 'r')

	for x in zF.namelist():
		newf = x.encode("cp437").decode("gbk")
		with open(newf, "wb") as output_file:
			with zF.open(x, 'r') as origin_file:
				shutil.copyfileobj(origin_file, output_file)
		# extracted_path = Path(zF.extract(x, "C:\\liaga\\その他\\Network\\書作\\世界经典名著电子书\\《世界名著合集54本》经典珍藏\\"))
		# extracted_path.rename(x.encode("cp437").decode("gbk"))

	zF.close()

def getAccessToken():
	from urllib import parse
	url = "https://login.microsoftonline.com/cub3.nri.co.jp/oauth2/token/"
	header = {
		"Content-Type":"application/x-www-form-urlencoded"
	}

	body = {
		"client_id":"8a7e12d2-dffa-4367-8d8a-00d37b7310c2",
		"resource":"https://idm-api.cub3.nri.co.jp/",
		"refresh_token":"AQABAAAAAAAP0wLlqdLVToOpA4kwzSnxL86pAZv332qnAXXjZlMyAJiuxYN4RGHDjIGATNCfKw6azbkzLzs319ziTBqGDyUyS_NFuH_2niafccRMjzLZ2Gz7atOVOHBhHYOf4nGEx3bfjor0O35pE0J4QFwOS7zlafpnjLK0pJvJCpw56cGvcR8Z8SIOsAlSty_sONCqJoSIWl_dwaI4gbxgtx8u0R4OaewlBM2AtzuAJpqDpIs4D8TBXS-ojrRxYLEdrViLr0X1pvAqMAMBWKrmWcwOzODAeyJEX0UuI4VJYdGb_tvT3PiSarwg0vjAFdmU130D0pDLnwScWy-ehRygeP0iUP6IbHkvcJ1WYZ2ncJnzjQcnehTJGtaPS_QR0fPNZBBwNBCbwV4btPdZYCrhf6NH2BW9HSATk5TDOYL16yfoxb2WLbgh67CqY5AnIoxGKLuH6b8hkFup2GN7WLQfYJqqjLq5Dp4oqAM-zBpxVy55rmyrjWwdsVhkbe1geJrR28tsJMLWoEGoOlDUM91jH44WHkuCIyE2mbBcmVUmt2nyZ_XHq93BPZMEzOK66D-PJ8IJQ-Apq0-_G_ji9PuYhxFbBGW6Br7ZQV5lLqv2YzIyeYjKSfy7KrG7mSCWIAHCqVnscdDqVflZbReRMEPd8ISh9XavbViDgMm5SS0WxBgNwr4aajbCC1dSTwjfjQ40ojISsjUZ-ZWdEURUSAukgfmV-GLGUaO2doE5bZn1tBJuHEKULraYbyN8HQw3clINVmDQGGyLPkKfJVSyBupdblV2LaRA3xq52bfbfc8eSLwZs0GHEEM7G_mwCsbxDH3bZLyV2PmKDVxYEFZ5qOK-E011U8RMsnPJBjrOwNK0wFqgDURWR_9aJaHMzm_F9ua2m_dlOrij5HG6SMWQpxWa5a9Q-mCWJ1ea1s3gpCw6nLz4I1ugdyAA",
		"grant_type":"refresh_token"

	}

	response = requests.post(url = url, headers = header,data = parse.urlencode(body))
	result = response.content
	
	result = str(result, encoding = "utf-8")
	result = json.loads(result)

	with open("1.json","w+",encoding="utf-8") as f:
		f.write(result["access_token"])
	try:
		access = result["access_token"]
		return access
	except Exception as e:
		print("error", e)
		return ""

def getDataBySql(token):
	tables = ["MT_UserRsrcAcntInfo","MT_GrpAcntInfo","MT_GrpAcntSInfo","MT_AccountAttributeReflect","MT_MBXPermissionInfo"]

	url = "https://idm-api.cub3.nri.co.jp/api/cudb/get-data-by-sql"

	header = {
		"Content-Type":"application/json",
		"Authorization":"Bearer %s"%token
	}
	for db in tables:
		if db == 'MT_AccountAttributeReflect':
			body = {
			   "sql":"select top 10 * from idsvsch.MT_AccountAttributeReflect"
			}

			response = requests.post(url = url, headers = header,data = json.dumps(body))
			result = response.content
			result = str(result, encoding = "utf-8")
			result = json.loads(result)

			f = open("%s_10.json"%db,"w+",encoding="utf-8")
			try:
				f.write(json.dumps(result,ensure_ascii=False,indent=1))
				# f.write(result)
			except Exception as e:
				print("write error: ",e)
			finally:
				f.close()

		else:

			for i in range(1, 4):
				if db == 'MT_GrpAcntSInfo':
					body = {
					   "sql":"select top 10 * from idsvsch.MT_GrpAcntSInfo where AflChangeSector='%d' order by TrunsactNo DESC"%i
					}
				else:
					body = {
					   "sql":"select top 10 * from idsvsch.%s where ChangeSector='%d' order by TrunsactNo DESC"%(db,i)
					}

				response = requests.post(url = url, headers = header,data = json.dumps(body))
				result = response.content
				result = str(result, encoding = "utf-8")
				result = json.loads(result)

				if i == 1:
					f = open("%s_追加_10.json"%db,"w+",encoding="utf-8")
				elif i == 2:
					f = open("%s_変更_10.json"%db,"w+",encoding="utf-8")
				else:
					f = open("%s_削除_10.json"%db,"w+",encoding="utf-8")

				try:
					f.write(json.dumps(result,ensure_ascii=False,indent=1))
					# f.write(result)
				except Exception as e:
					print("write error: ",e)
				finally:
					f.close()

def getDiffData(token):

	tables = ["MT_UserRsrcAcntInfo","MT_GrpAcntInfo","MT_GrpAcntSInfo","IDM_Import_MT_AccountAttributeReflect","MT_MBXPermissionInfo"]

	url = "https://idm-api.cub3.nri.co.jp/api/cudb/get-diff-data"
	
	header = {
		"Content-Type":"application/json",
		"Authorization":"Bearer %s"%token
	}

	for t in tables:
		body = {
			 "import_table_name":"%s"%t,
			 "import_date_time":"2019-08-01 17:36:58.657",
			 "trunsact_no":"8639852"	# pow(2,31)-1 = 2147483647 Int32.maxint
		}
		response = requests.post(url = url, headers = header,data = json.dumps(body))
		result = response.content
		result = str(result, encoding = "utf-8")
		result = json.loads(result)

		try:
			with open("json\\%s_diff.json"%t,"w+") as f:
				f.write(json.dumps(result,ensure_ascii=False,indent=4))

		except Exception as e:
			print("open file failed ", e)
		

def modifyJson():
	
	# path = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Modify"
	file = "MT_UserRsrcAcntInfo_変更_10.json"

	# path_f = os.path.join(path, file)
	with open(file, "r",encoding="utf-8") as f:
		content = f.read()

	content = json.loads(content)

	lens = len(content["items"])
	print("len: ",len)

	copy_con = copy(content)
	# copy_con["status"] = "tableName"

	for i in range(0, lens):
		# MT_UserRsrcAcntInfo
		pass

	f = open(file,"w+",encoding="utf-8")
	f.write(json.dumps(copy_con,ensure_ascii=False,indent=1))
	f.close()

def modify_MT_UserRsrcAcntInfo(patho, paths):
	"table name: MT_UserRsrcAcntInfo"

	file = "MT_UserRsrcAcntInfo_変更_10.json"
	jouken = ["追加", "変更", "削除"]

	for jk in jouken:
		try:
			fs = os.path.join(patho, "MT_UserRsrcAcntInfo_%s_10.json"%jk)
			
			with open(fs, "r",encoding="utf-8") as f:
				content = f.read()


			content = json.loads(content)
			lens = len(content["items"])

			copy_con = copy(content)
			copy_con.pop("status")
			copy_con["tableName"] = "MT_UserRsrcAcntInfo"

			for i in range(0, lens):
				# MT_UserRsrcAcntInfo
				copy_con["items"][i]["TrunsactNo"] = "4200000000000%d"%i
				copy_con["items"][i]["RegistarId"] = "BATCH"
				copy_con["items"][i]["ADImpStatusSector"] = "0"
				copy_con["items"][i]["ADImpDate"] = ""
				copy_con["items"][i]["EXImpStatusSector"] = "0"
				copy_con["items"][i]["EXImpDate"] = ""


				if copy_con["items"][i]["UserId"]:
					copy_con["items"][i]["UserId"] = "UB0000000%d"%i

				if copy_con["items"][i]["BeforeLog_onId"]:
					copy_con["items"][i]["BeforeLog_onId"] = "adctrue%d"%i
				if copy_con["items"][i]["BeforeDispName"]:
					copy_con["items"][i]["BeforeDispName"] = "before 表示名%d"%i
				if copy_con["items"][i]["BeforeFamilyName"]:
					copy_con["items"][i]["BeforeFamilyName"] = "before 苗字%d"%i
				if copy_con["items"][i]["BeforeName"]:
					copy_con["items"][i]["BeforeName"] = "before 名前%d"%i
				if copy_con["items"][i]["BeforeCompanyName"]:
					copy_con["items"][i]["BeforeCompanyName"] = "before 会社の名前%d"%i
				if copy_con["items"][i]["BeforeMainDptName"]:
					copy_con["items"][i]["BeforeMainDptName"] = "before 部門の名前%d"%i
				if copy_con["items"][i]["BeforeKanaName"]:
					copy_con["items"][i]["BeforeKanaName"] = "ソフトウェアエンジニア%d"%i
				if copy_con["items"][i]["BeforeAlphabetName"]:
					copy_con["items"][i]["BeforeAlphabetName"] = "SOFUTOWUE ENJINIA%d"%i
				if copy_con["items"][i]["BeforeMailAddress"]:
					copy_con["items"][i]["BeforeMailAddress"] = "before.fake.mailaddress_%d@test.com.cn"%i
				if copy_con["items"][i]["BeforeStructureCode"]:
					copy_con["items"][i]["BeforeStructureCode"] = "A_fake_%d"%i

				if copy_con["items"][i]["AfterLog_onId"]:
					copy_con["items"][i]["AfterLog_onId"] = "adcfake%d"%i
				if copy_con["items"][i]["AfterMailAddress"]:
					copy_con["items"][i]["AfterMailAddress"] = "after.fake.mailaddress_%d@test.com.cn"%i
				if copy_con["items"][i]["AfterStructureCode"]:
					copy_con["items"][i]["AfterStructureCode"] = "AA_fake_%d"%i
				if copy_con["items"][i]["AfterDispName"]:
					copy_con["items"][i]["AfterDispName"] = "After 表示名%d"%i
				if copy_con["items"][i]["AfterFamilyName"]:
					copy_con["items"][i]["AfterFamilyName"] = "After 苗字%d"%i
				if copy_con["items"][i]["AfterName"]:
					copy_con["items"][i]["AfterName"] = "After 名前%d"%i
				if copy_con["items"][i]["AfterCompanyName"]:
					copy_con["items"][i]["AfterCompanyName"] = "After 会社の名前%d"%i
				if copy_con["items"][i]["AfterMainDptName"]:
					copy_con["items"][i]["AfterMainDptName"] = "After 部門の名前%d"%i
				if copy_con["items"][i]["AfterKanaName"]:
					copy_con["items"][i]["AfterKanaName"] = "後ソフトウェアエンジニア%d"%i
				if copy_con["items"][i]["AfterAlphabetName"]:
					copy_con["items"][i]["AfterAlphabetName"] = "GO SOFUTOWUE ENJINIA%d"%i 
				if copy_con["items"][i]["AfterWorkplaceName"]:
					copy_con["items"][i]["AfterWorkplaceName"] = "GO 東京都_%d"%i

				copy_con["items"][i]["LogOnIdChangeSector"] = copy_con["items"][i].pop("Log_onIdChangeSector")
				copy_con["items"][i]["BeforeLogOnId"] = copy_con["items"][i].pop("BeforeLog_onId")
				copy_con["items"][i]["AfterLogOnId"] = copy_con["items"][i].pop("AfterLog_onId")
				copy_con["items"][i]["HITOIDChangeSector"] = copy_con["items"][i].pop("HITO_ID_ChangeSector")
				copy_con["items"][i]["BeforeHITOID"] = copy_con["items"][i].pop("BeforeHITO_ID")
				copy_con["items"][i]["AfterHITOID"] = copy_con["items"][i].pop("AfterHITO_ID")

			path_s = os.path.join(paths, "MT_UserRsrcAcntInfo_%s_10_m.json"%jk)

			with open(path_s,"w+",encoding="utf-8") as f:
				f.write(json.dumps(copy_con,ensure_ascii=False,indent=4))

		except Exception as e:
			print("MT_UserRsrcAcntInfo : File or path not exist")
			continue

def modify_MT_GrpAcntInfo(patho, paths):
	"table name: MT_GrpAcntInfo"

	path = "C:\\liaga\\その他\\Python3"

	jouken = ["追加", "変更", "削除"]

	for jk in jouken:
		try:
			fs = os.path.join(patho, "MT_GrpAcntInfo_%s_10.json"%jk)
			
			with open(fs, "r",encoding="utf-8") as f:
				content = f.read()


			content = json.loads(content)
			lens = len(content["items"])

			copy_con = copy(content)
			copy_con.pop("status")
			copy_con["tableName"] = "MT_GrpAcntInfo"

			for i in range(0, lens):
				# MT_GrpAcntInfo
				copy_con["items"][i]["TrunsactNo"] = "3200000000000%d"%i
				copy_con["items"][i]["RegistarId"] = "BATCH"
				copy_con["items"][i]["ADImpStatusSector"] = "0"
				copy_con["items"][i]["ADImpDate"] = ""
				copy_con["items"][i]["EXImpStatusSector"] = "0"
				copy_con["items"][i]["EXImpDate"] = ""
				copy_con["items"][i]["OrganizCode"] = "SL0000000%d"%i

				if copy_con["items"][i]["BeforeSecGrpCode"]:
					copy_con["items"][i]["BeforeSecGrpCode"] = "NB_00%d"%i
				if copy_con["items"][i]["AfterSecGrpCode"]:
					copy_con["items"][i]["AfterSecGrpCode"] = "NA_00%d"%i
				if copy_con["items"][i]["BeforeSecGrpName"]:
					copy_con["items"][i]["BeforeSecGrpName"] = "Before_fake_NAME"
				if copy_con["items"][i]["AfterSecGrpName"]:
					copy_con["items"][i]["AfterSecGrpName"] = "After_fake_NAME"
				if copy_con["items"][i]["BeforeSecGrpExpln"]:
					copy_con["items"][i]["BeforeSecGrpExpln"] = "Before_fake_開発部門"
				if copy_con["items"][i]["AfterSecGrpExpln"]:
					copy_con["items"][i]["AfterSecGrpExpln"] = "After_fake_開発部門"
				if copy_con["items"][i]["BeforeMailAddress"]:
					copy_con["items"][i]["BeforeMailAddress"] = "before.fake.mail_%d@test.com.cn"%i
				if copy_con["items"][i]["AfterMailAddress"]:
					copy_con["items"][i]["AfterMailAddress"] = "after.fake.mail_%d@test.com.cn"%i
				
			path_s = os.path.join(paths, "MT_GrpAcntInfo_%s_10_m.json"%jk)

			with open(path_s,"w+",encoding="utf-8") as f:
				f.write(json.dumps(copy_con,ensure_ascii=False,indent=4))

		except Exception as e:
			print("MT_GrpAcntInfo : File or path not exist")
			continue

def modify_MT_GrpAcntSInfo(patho, paths):
	"table name: MT_GrpAcntSInfo"

	jouken = ["追加", "変更", "削除"]

	for jk in jouken:
		try:
			fs = os.path.join(patho, "MT_GrpAcntSInfo_%s_10.json"%jk)
			
			with open(fs, "r",encoding="utf-8") as f:
				content = f.read()


			content = json.loads(content)
			lens = len(content["items"])

			copy_con = copy(content)
			copy_con.pop("status")
			copy_con["tableName"] = "MT_GrpAcntSInfo"

			for i in range(0, lens):
				# MT_GrpAcntSInfo
				copy_con["items"][i]["TrunsactNo"] = "2100000000000%d"%i
				copy_con["items"][i]["ADImpStatusSector"] = "0"
				copy_con["items"][i]["ADImpDate"] = ""
				copy_con["items"][i]["EXImpStatusSector"] = "0"
				copy_con["items"][i]["EXImpDate"] = ""
				copy_con["items"][i]["RegistarId"] = "BATCH"
				copy_con["items"][i]["OrganizCode"] = "SB0000000%d"%i
				copy_con["items"][i]["SecGrpCode"] = "NA_00%d"%i
				copy_con["items"][i]["AflUserId_RsrcCd_OrgCd"] = "UF0000"
				copy_con["items"][i]["AflLogonId_SecGrpCd"] = "fake-log"

				copy_con["items"][i]["AflUserIdRsrcCdOrgCd"] = copy_con["items"][i].pop("AflUserId_RsrcCd_OrgCd")
				copy_con["items"][i]["AflLogonIdSecGrpCd"] = copy_con["items"][i].pop("AflLogonId_SecGrpCd")
				
			path_s = os.path.join(paths, "MT_GrpAcntSInfo_%s_10_m.json"%jk)
			
			with open(path_s,"w+",encoding="utf-8") as f:
				f.write(json.dumps(copy_con,ensure_ascii=False,indent=4))

		except Exception as e:
			print("MT_GrpAcntSInfo: File or path not exist")
			continue

def modify_MT_AccountAttributeReflect(patho, paths):
	"table name: MT_AccountAttributeReflect"

	# jouken = ["追加", "変更", "削除"]

	# for jk in jouken:
	try:
		fs = os.path.join(patho, "MT_AccountAttributeReflect_10.json")
		
		with open(fs, "r",encoding="utf-8") as f:
			content = f.read()


		content = json.loads(content)
		lens = len(content["items"])

		copy_con = copy(content)
		copy_con.pop("status")
		copy_con["tableName"] = "MT_AccountAttributeReflect"

		for i in range(0, lens):
			# MT_AccountAttributeReflect
			copy_con["items"][i]["RecordNo"] = "10000%d"%i
			copy_con["items"][i]["Log_onId"] = "fake.burns-eu"
			copy_con["items"][i]["ApplicationStartDay"] = "20190927"
			if copy_con["items"][i]["ApplicationEndDay"]:
				copy_con["items"][i]["ApplicationEndDay"] = ""
			copy_con["items"][i]["StatusSector"] = "0"
			if copy_con["items"][i]["Value"] == "ext-addressBookMail":
				copy_con["items"][i]["Value"] = "fake.address.book.mail%d@test.com"%i
			elif copy_con["items"][i]["Value"] == "ext-Mail":
				copy_con["items"][i]["Value"] = "fake.mail%d@test.com"%i
			else:
				# personid
				copy_con["items"][i]["Value"] = "fake.personid.%d"%i

			copy_con["items"][i]["LogOnId"] = copy_con["items"][i].pop("Log_onId")

		path_s = os.path.join(paths, "MT_AccountAttributeReflect_10_m.json")
		
		with open(path_s,"w+",encoding="utf-8") as f:
			f.write(json.dumps(copy_con,ensure_ascii=False,indent=4))

	except Exception as e:
		print("MT_AccountAttributeReflect: File or path not exist")

def modify_MT_MBXPermissionInfo(patho, paths):
	"table name: MT_MBXPermissionInfo"

	jouken = ["追加", "変更", "削除"]

	for jk in jouken:
		try:
			fs = os.path.join(patho, "MT_MBXPermissionInfo_%s_10.json"%jk)
			
			with open(fs, "r",encoding="utf-8") as f:
				content = f.read()


			content = json.loads(content)
			lens = len(content["items"])

			copy_con = copy(content)
			copy_con.pop("status")
			copy_con["tableName"] = "MT_MBXPermissionInfo"

			for i in range(0, lens):
				# MT_MBXPermissionInfo
				
				copy_con["items"][i]["TrunsactNo"] = "1000000000000%d"%i
				copy_con["items"][i]["RegistarId"] = "BATCH"
				copy_con["items"][i]["EXImpStatusSector"] = "0"
				copy_con["items"][i]["EXImpDate"] = ""
				copy_con["items"][i]["UserId_RsrcCd"] = "UB0000000%d"%i
				copy_con["items"][i]["Log_onId"] = "fake-logid%d"%i
				copy_con["items"][i]["MBXUserId_RsrcCd_OrgCd"] = "SB0000000%d"%i
				copy_con["items"][i]["MBXLogonId_SecGrpCd"] = "A_fake_%d"%i

				copy_con["items"][i]["LogOnId"] = copy_con["items"][i].pop("Log_onId")
				copy_con["items"][i]["UserIdRsrcCd"] = copy_con["items"][i].pop("UserId_RsrcCd")
				copy_con["items"][i]["MBXUserIdRsrcCdOrgCd"] = copy_con["items"][i].pop("MBXUserId_RsrcCd_OrgCd")
				copy_con["items"][i]["MBXLogonIdSecGrpCd"] = copy_con["items"][i].pop("MBXLogonId_SecGrpCd")

			path_s = os.path.join(paths, "MT_MBXPermissionInfo_%s_10_m.json"%jk)
			
			with open(path_s,"w+",encoding="utf-8") as f:
				f.write(json.dumps(copy_con,ensure_ascii=False,indent=4))

		except Exception as e:
			print("MT_MBXPermissionInfo: File or path not exist")
			continue

def modify_MT_UserRsrcAcntInfo_case(patho, paths):
	tableName = "MT_UserRsrcAcntInfo"

	msg = {
		"user":[{
			"userID":"UB00010001",
			"logonID":"b-tanaka-01",
			"EmpNo":"M8001",
			"UserSector":"0",
			"MainDptName":"（ソフトウェア）_社員",
			"DispName":"夏目漱石(なつめそうせき 1867-1916)",
			"FamilyName":"夏目",
			"Name":"漱石",
			"KanaName":"natumesouseki",
			"AlphabetName":"なつめそうせき",
			"StructureCode":"A",
			"TitleCode":"0100",
			"HITOID":"10101001"
		},{
			"userID":"UB00010004",
			"logonID":"b-tanaka-04",
			"EmpNo":"M8005",
			"UserSector":"1",
			"MainDptName":"（ソフトウェア）_派遣",
			"DispName":"芥川 龍之介(あくたがわりゅうのすけ 1892-1927)",#1927
			"FamilyName":"芥川",
			"Name":"龍之介",
			"KanaName":"akutagawasyounosuke",
			"AlphabetName":"あくたがわりゅうのすけ",
			"StructureCode":"A_80",
			"TitleCode":"04,21",
			"HITOID":"10101002"
		},{
			"userID":"UF00010001",
			"logonID":"f-tanaka-01",
			"EmpNo":"J9006",
			"UserSector":"9",
			"MainDptName":"（ソフトウェア）_特殊ユーザー",
			"DispName":"太宰 治(だざいおさむ 1909-1948)",
			"FamilyName":"太宰",
			"Name":"治",
			"KanaName":"dazaiokimu",
			"AlphabetName":"だざいおさむ",
			"StructureCode":"A_80_55",
			"TitleCode":"04,21,21",
			"HITOID":"10101003"
		},{
			"userID":"UT00010001",
			"logonID":"t-tanaka",
			"EmpNo":"x8001",
			"UserSector":"8",
			"MainDptName":"役員",
			"DispName":"川端康成(かわばたやすなり 1899-1972)",
			"FamilyName":"川端",
			"Name":"康成",
			"KanaName":"kawabatayasunari",
			"AlphabetName":"かわばたやすなり",
			"StructureCode":"A_80_55_10",
			"TitleCode":"06,30,30,63,63",
			"HITOID":"10101004"
		}],
		"resource":[{
			"resourceID":"RR00010001",
			"logonID":"r-resource-01",
			"RsrcSector":"010",
			"DispName":"0001会議室",
			"Password":"rr4321*"
		},{
			"resourceID":"RB00010001",
			"logonID":"b-resource-01",
			"RsrcSector":"020",
			"DispName":"備品会議室",
			"Password":"rb2431+"
		},{
			"resourceID":"RS00010001",
			"logonID":"s-resource",
			"RsrcSector":"030",
			"DispName":"共有スケジュール会議室",
			"Password":"rs1234#"
		}]
	}

	# os.chdir(patho)
	# try:
	# 	with open("MT_UserRsrcAcntInfo_sample.json") as f:
	# 		content = f.read()
	# except Exception as e:
	# 	print("MT_UserRsrcAcntInfo_sample.json file not found : ",e)
		
		
	# print(content)
	con_dict = openFile(patho, tableName)

	lens = 7
	
	for jk in CON:
		# 追加 1
		if jk == "1":
			DATAS = []
			for i in range(0, lens):
				if i < 4:
					copy_con = copy(con_dict)
					copy_con["TrunsactNo"] = "4000000000000%d"%i
					copy_con["RegistationDate"] = getCurDate()
					copy_con["UserId"] = msg["user"][i]["userID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["EmpNoChangeSector"] = jk
					copy_con["AfterEmpNo"] = msg["user"][i]["EmpNo"]
					copy_con["DispNameChangeSector"] = jk
					copy_con["AfterDispName"] = msg["user"][i]["DispName"]
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["AfterFamilyName"] = msg["user"][i]["FamilyName"]
					copy_con["NameChangeSector"] = jk
					copy_con["AfterName"] = msg["user"][i]["Name"]
					copy_con["KanaNameChangeSector"] = jk
					copy_con["AfterKanaName"] = msg["user"][i]["KanaName"]
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["AfterAlphabetName"] = msg["user"][i]["AlphabetName"]
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["AfterCompanyName"] = "御茶ノ水　ソフト日本"
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["AfterMainDptName"] = msg["user"][i]["MainDptName"]
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["AfterMainSectGrpName"] = "(株)IT グループ"
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["AfterWorkplaceName"] = "御茶ノ水"
					copy_con["MailAddressChangeSector"] = jk
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"],msg["user"][i]["logonID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["AfterTitleName"] = "仕事の人"
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["AfterExLineNo"] = "045-336-688%d"%i
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["AfterExtentionNo"] = "82718%d"%i
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["AfterStructureCode"] = msg["user"][i]["StructureCode"]
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["AfterTitleCode"] = msg["user"][i]["TitleCode"]
					copy_con["CommandDateChangeSector"] = jk
					copy_con["AfterCommandDate"] = getYYYYMMDD()
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["AfterArrivalDate"] = getYYYYMMDD()
					copy_con["RetireDateChangeSector"] = jk
					copy_con["AfterRetireDate"] = getYYYYMMDD()
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["AfterGALDispFlg"] = i%3
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["AfterGALDispOrder"] = "0"
					copy_con["MemoChangeSector"] = jk
					# copy_con["AfterMemo"] = 
					copy_con["PortalSGCodeChangeSector"] = jk
					# copy_con["AfterPortalSGCode"] = 
					copy_con["PasswordChangeSector"] = jk
					# copy_con["AfterPassword"] = 
					copy_con["InetUseChangeSector"] = jk
					copy_con["AfterInetUse"] = i%3
					copy_con["VLANPassWordChangeSector"] = jk
					copy_con["AfterVLANPassWord"] = "134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["md4PassWordChangeSector"] = jk
					copy_con["Aftermd4PassWord"] = "{md4}134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["AfterLogOnId"] = msg["user"][i]["logonID"]
					copy_con["HITOIDChangeSector"] = jk
					copy_con["AfterHITOID"] = "1010100%d"%i
					
					copy_con["UseToFileShareChangeSector"] = "1"
					copy_con["AfterUseToFileShare"] = "22"
					copy_con["UseToMBXChangeSector"] = "1"
					copy_con["AfterUseToMBX"] = "22"
					copy_con["UseToSkype4bChangeSector"] = "1"
					copy_con["AfterUseToSkype4b"] = "22"
					DATAS.append(copy_con)

				else:
					copy_con = copy(con_dict)
					j = i - 4
					copy_con["TrunsactNo"] = "4000000000000%d"%i
					copy_con["RegistationDate"] = getCurDate()
					copy_con["ResourceCode"] = msg["resource"][j]["resourceID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["AfterRsrcSector"] = msg["resource"][j]["RsrcSector"]
					copy_con["EmpNoChangeSector"] = jk
					copy_con["DispNameChangeSector"] = jk
					copy_con["AfterDispName"] = msg["resource"][j]["DispName"]
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["NameChangeSector"] = jk
					copy_con["KanaNameChangeSector"] = jk
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["MailAddressChangeSector"] = jk
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][j]["resourceID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["CommandDateChangeSector"] = jk
					copy_con["AfterCommandDate"] = getYYYYMMDD()
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["AfterArrivalDate"] = getYYYYMMDD()
					copy_con["RetireDateChangeSector"] = jk
					copy_con["AfterRetireDate"] = getYYYYMMDD()
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["AfterGALDispFlg"] = j%3
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["AfterGALDispOrder"] = "0"
					copy_con["MemoChangeSector"] = jk
					copy_con["AfterMemo"] = msg["resource"][j]["DispName"]
					copy_con["PortalSGCodeChangeSector"] = jk
					# copy_con["AfterPortalSGCode"] = 
					copy_con["PasswordChangeSector"] = jk
					copy_con["AfterPassword"] = msg["resource"][j]["Password"]
					copy_con["InetUseChangeSector"] = jk
					# copy_con["AfterInetUse"] = i%3
					copy_con["VLANPassWordChangeSector"] = jk
					# copy_con["AfterVLANPassWord"] = "134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["md4PassWordChangeSector"] = jk
					# copy_con["Aftermd4PassWord"] = "{md4}134402E37B7C2D4E9DB1EDD5BD36589E"
					# copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["AfterLogOnId"] = msg["resource"][j]["resourceID"]
					copy_con["HITOIDChangeSector"] = jk
					# copy_con["AfterHITOID"] = "1010100%d"%i

					DATAS.append(copy_con)

			saveByName(tableName, CON[jk], paths, DATAS)

		elif jk == "2":
			DATAS = []
			for i in range(0, lens):
				if i < 4:
					copy_con = copy(con_dict)
					copy_con["TrunsactNo"] = "4100000000000%d"%i
					copy_con["RegistationDate"] = getCurDate()
					copy_con["UserId"] = msg["user"][i]["userID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["EmpNoChangeSector"] = jk
					copy_con["BeforeEmpNo"] = msg["user"][i]["EmpNo"]
					copy_con["AfterEmpNo"] = msg["user"][i]["EmpNo"]+"2"
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["user"][i]["DispName"]
					copy_con["AfterDispName"] = msg["user"][i]["DispName"]+"2"
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["BeforeFamilyName"] = msg["user"][i]["FamilyName"]
					copy_con["AfterFamilyName"] = msg["user"][i]["FamilyName"]+"2"
					copy_con["NameChangeSector"] = jk
					copy_con["BeforeName"] = msg["user"][i]["Name"]
					copy_con["AfterName"] = msg["user"][i]["Name"]+"2"
					copy_con["KanaNameChangeSector"] = jk
					copy_con["BeforeKanaName"] = msg["user"][i]["KanaName"]
					copy_con["AfterKanaName"] = msg["user"][i]["KanaName"]+"aaa"
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["BeforeAlphabetName"] = msg["user"][i]["AlphabetName"]
					copy_con["AfterAlphabetName"] = msg["user"][i]["AlphabetName"]+"あああ"
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["BeforeCompanyName"] = "御茶ノ水　ソフト日本"
					copy_con["AfterCompanyName"] = "水道橋　ソフト日本"
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["BeforeMainDptName"] = msg["user"][i]["MainDptName"]
					copy_con["AfterMainDptName"] = msg["user"][i]["MainDptName"]+" change"
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["BeforeMainSectGrpName"] = "(株)IT グループ"
					copy_con["AfterMainSectGrpName"] = "(株)IT グループ(change)"
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["BeforeWorkplaceName"] = "御茶ノ水"
					copy_con["AfterWorkplaceName"] = "水道橋"
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"],msg["user"][i]["logonID"])
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"]+"2",msg["user"][i]["logonID"]+"2")
					copy_con["TitleNameChangeSector"] = jk
					copy_con["BeforeTitleName"] = "仕事の人"
					copy_con["AfterTitleName"] = "仕事の人(change)"
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["BeforeExLineNo"] = "045-336-688%d"%i
					copy_con["AfterExLineNo"] = "020-336-600%d"%i
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["BeforeExtentionNo"] = "82718%d"%i
					copy_con["AfterExtentionNo"] = "80010%d"%i
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["BeforeStructureCode"] = msg["user"][i]["StructureCode"]
					copy_con["AfterStructureCode"] = msg["user"][i]["StructureCode"]+",A_20"
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["BeforeTitleCode"] = msg["user"][i]["TitleCode"]
					copy_con["AfterTitleCode"] = msg["user"][i]["TitleCode"]+",0100"
					copy_con["CommandDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD()
					copy_con["AfterCommandDate"] = getYYYYMMDD(-1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["BeforeArrivalDate"] = getYYYYMMDD()
					copy_con["AfterCommandDate"] = getYYYYMMDD(-2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["BeforeRetireDate"] = getYYYYMMDD()
					copy_con["AfterCommandDate"] = getYYYYMMDD(-3)
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["BeforeGALDispFlg"] = i%3
					copy_con["AfterGALDispFlg"] = (i+1)%3
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["BeforeGALDispOrder"] = "0"
					copy_con["AfterGALDispOrder"] = "99"
					copy_con["MemoChangeSector"] = jk
					# copy_con["BeforeMemo"] = 
					copy_con["PortalSGCodeChangeSector"] = jk
					# copy_con["BeforePortalSGCode"] = 
					copy_con["PasswordChangeSector"] = jk
					# copy_con["BeforePassword"] = 
					copy_con["InetUseChangeSector"] = jk
					copy_con["BeforeInetUse"] = i%3
					copy_con["AfterInetUse"] = (i+1)%3
					copy_con["VLANPassWordChangeSector"] = jk
					copy_con["BeforeVLANPassWord"] = "134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["AfterVLANPassWord"] = "202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["md4PassWordChangeSector"] = jk
					copy_con["Beforemd4PassWord"] = "{md4}134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["Aftermd4PassWord"] = "{md4}202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["BeforeLogOnId"] = msg["user"][i]["logonID"]
					copy_con["AfterLogOnId"] = msg["user"][i]["logonID"]+"2"
					copy_con["HITOIDChangeSector"] = jk
					copy_con["BeforeHITOID"] = "1010100%d"%i
					copy_con["AfterHITOID"] = "2019100%d"%i

					copy_con["UseToFileShareChangeSector"] = jk
					copy_con["BeforeUseToFileShare"] = "22"
					copy_con["AfterUseToFileShare"] = "33"
					copy_con["UseToMBXChangeSector"] = jk
					copy_con["BeforeUseToMBX"] = "22"
					copy_con["AfterUseToMBX"] = "330"
					copy_con["UseToSkype4bChangeSector"] = jk
					copy_con["AfterUseToSkype4b"] = "22"
					copy_con["AfterUseToSkype4b"] = "333"

					DATAS.append(copy_con)

				else:
					copy_con = copy(con_dict)
					j = i - 4
					copy_con["TrunsactNo"] = "4100000000000%d"%i
					copy_con["RegistationDate"] = getCurDate()
					copy_con["ResourceCode"] = msg["resource"][j]["resourceID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["BeforeRsrcSector"] = msg["resource"][j]["RsrcSector"]
					copy_con["AfterRsrcSector"] = msg["resource"][(j+1)%3]["RsrcSector"]
					copy_con["EmpNoChangeSector"] = jk
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["resource"][j]["DispName"]
					copy_con["AfterDispName"] = msg["resource"][(j+1)%3]["DispName"]
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["NameChangeSector"] = jk
					copy_con["KanaNameChangeSector"] = jk
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][j]["resourceID"])
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][(j+1)%3]["resourceID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["CommandDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD()
					copy_con["AfterCommandDate"] = getYYYYMMDD(-1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["BeforeArrivalDate"] = getYYYYMMDD()
					copy_con["AfterArrivalDate"] = getYYYYMMDD(-2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["BeforeRetireDate"] = getYYYYMMDD()
					copy_con["AfterRetireDate"] = getYYYYMMDD(-3)
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["BeforeGALDispFlg"] = j%3
					copy_con["AfterGALDispFlg"] = (j+1)%3
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["BeforeGALDispOrder"] = "0"
					copy_con["AfterGALDispOrder"] = "20"
					copy_con["MemoChangeSector"] = jk
					copy_con["BeforeMemo"] = msg["resource"][j]["DispName"]
					copy_con["AfterMemo"] = msg["resource"][(j+1)%3]["DispName"]
					copy_con["PortalSGCodeChangeSector"] = jk
					# copy_con["AfterPortalSGCode"] = 
					copy_con["PasswordChangeSector"] = jk
					copy_con["BeforePassword"] = msg["resource"][j]["Password"]
					copy_con["AfterPassword"] = "111222"
					copy_con["InetUseChangeSector"] = jk
					# copy_con["AfterInetUse"] = i%3
					copy_con["VLANPassWordChangeSector"] = jk
					# copy_con["AfterVLANPassWord"] = "134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["md4PassWordChangeSector"] = jk
					# copy_con["Aftermd4PassWord"] = "{md4}134402E37B7C2D4E9DB1EDD5BD36589E"
					# copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["BeforeLogOnId"] = msg["resource"][j]["resourceID"]
					copy_con["AfterLogOnId"] = msg["resource"][(j+1)%3]["resourceID"]
					copy_con["HITOIDChangeSector"] = jk
					# copy_con["AfterHITOID"] = "1010100%d"%i

					DATAS.append(copy_con)

				saveByName(tableName, CON[jk], paths, DATAS)
		else:
			DATAS = []
			for i in range(0, lens):
				if i < 4:
					copy_con = copy(con_dict)
					copy_con["TrunsactNo"] = "4200000000000%d"%i
					copy_con["RegistationDate"] = getCurDate()
					copy_con["UserId"] = msg["user"][i]["userID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["EmpNoChangeSector"] = jk
					copy_con["BeforeEmpNo"] = msg["user"][i]["EmpNo"]+"2"
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["user"][i]["DispName"]+"2"
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["BeforeFamilyName"] = msg["user"][i]["FamilyName"]+"2"
					copy_con["NameChangeSector"] = jk
					copy_con["BeforeName"] = msg["user"][i]["Name"]+"2"
					copy_con["KanaNameChangeSector"] = jk
					copy_con["BeforeKanaName"] = msg["user"][i]["KanaName"]+"aaa"
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["BeforeAlphabetName"] = msg["user"][i]["AlphabetName"]+"あああ"
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["BeforeCompanyName"] = "水道橋　ソフト日本"
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["BeforeMainDptName"] = msg["user"][i]["MainDptName"]+" change"
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["BeforeMainSectGrpName"] = "(株)IT グループ(change)"
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["BeforeWorkplaceName"] = "水道橋"
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"]+"2",msg["user"][i]["logonID"]+"2")
					copy_con["TitleNameChangeSector"] = jk
					copy_con["BeforeTitleName"] = "仕事の人(change)"
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["BeforeExLineNo"] = "020-336-600%d"%i
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["BeforeExtentionNo"] = "80010%d"%i
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["BeforeStructureCode"] = msg["user"][i]["StructureCode"]+",A_20"
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["BeforeTitleCode"] = msg["user"][i]["TitleCode"]+",0100"
					copy_con["CommandDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD(-1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD(-2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD(-3)
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["BeforeGALDispFlg"] = (i+1)%3
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["MemoChangeSector"] = jk
					copy_con["PortalSGCodeChangeSector"] = jk
					copy_con["PasswordChangeSector"] = jk
					copy_con["InetUseChangeSector"] = jk
					copy_con["BeforeInetUse"] = (i+1)%3
					copy_con["VLANPassWordChangeSector"] = jk
					copy_con["BeforeVLANPassWord"] = "202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["md4PassWordChangeSector"] = jk
					copy_con["Beforemd4PassWord"] = "{md4}202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["BeforeLogOnId"] = msg["user"][i]["logonID"]+"2"
					copy_con["HITOIDChangeSector"] = jk
					copy_con["BeforeHITOID"] = "2019100%d"%i

					copy_con["UseToFileShareChangeSector"] = jk
					copy_con["BeforeUseToFileShare"] = "33"
					copy_con["UseToMBXChangeSector"] = jk
					copy_con["BeforeUseToMBX"] = "330"
					copy_con["UseToSkype4bChangeSector"] = jk
					copy_con["BeforeUseToSkype4b"] = "333"

					DATAS.append(copy_con)

				else:
					copy_con = copy(con_dict)
					j = i - 4
					copy_con["TrunsactNo"] = "4200000000000%d"%i
					copy_con["RegistationDate"] = getCurDate()
					copy_con["ResourceCode"] = msg["resource"][j]["resourceID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["BeforeRsrcSector"] = msg["resource"][(j+1)%3]["RsrcSector"]
					copy_con["EmpNoChangeSector"] = jk
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["resource"][(j+1)%3]["DispName"]
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["NameChangeSector"] = jk
					copy_con["KanaNameChangeSector"] = jk
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][(j+1)%3]["resourceID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["CommandDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD(-1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["BeforeArrivalDate"] = getYYYYMMDD(-2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["BeforeRetireDate"] = getYYYYMMDD(-3)
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["BeforeGALDispFlg"] = (j+1)%3
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["BeforeGALDispOrder"] = "20"
					copy_con["MemoChangeSector"] = jk
					copy_con["BeforeMemo"] = msg["resource"][(j+1)%3]["DispName"]
					copy_con["PortalSGCodeChangeSector"] = jk
					# copy_con["BeforePortalSGCode"] = 
					copy_con["PasswordChangeSector"] = jk
					copy_con["BeforePassword"] = "111222"
					copy_con["InetUseChangeSector"] = jk
					# copy_con["BeforeInetUse"] = i%3
					copy_con["VLANPassWordChangeSector"] = jk
					# copy_con["BeforeVLANPassWord"] = "134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["md4PassWordChangeSector"] = jk
					# copy_con["Beforemd4PassWord"] = "{md4}134402E37B7C2D4E9DB1EDD5BD36589E"
					# copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["BeforeLogOnId"] = msg["resource"][(j+1)%3]["resourceID"]
					copy_con["HITOIDChangeSector"] = jk
					# copy_con["AfterHITOID"] = "1010100%d"%i

					DATAS.append(copy_con)

				saveByName(tableName, CON[jk], paths, DATAS)

def modify_MT_GrpAcntInfo_case(patho, paths):
	tableName = "MT_GrpAcntInfo"

	msg = [{
		"OrganizCode":"SB00010001",
		"SecGrpCode":"b-database",
		"SecGrpName":"(東京大学大学院)"
	},{
		"OrganizCode":"SF00010001",
		"SecGrpCode":"f-database",
		"SecGrpName":"(任意共有グループ)"
	},{
		"OrganizCode":"BL00010001",
		"SecGrpCode":"bl-database",
		"SecGrpName":"(ビル 水道橋)"
	}]
		
	con_dict = openFile(patho, tableName)
	# print([x for x in con_dict])
	lens = len(msg)

	for jk in CON:
		# 追加 1
		if jk == "1":
			DATAS = []
			for i in range(0,lens):
				copy_con = copy(con_dict)
				copy_con["TrunsactNo"] = "3000000000000%d"%i
				copy_con["RegistationDate"] = getCurDate()
				copy_con["OrganizCode"] = msg[i]["OrganizCode"]
				copy_con["ChangeSector"] = jk
				copy_con["SecGrpCodeChangeSector"] = jk
				copy_con["BeforeSecGrpCode"] = msg[i]["OrganizCode"]
				copy_con["AfterSecGrpCode"] = msg[i]["OrganizCode"]
				copy_con["SecGrpNameChangeSector"] = jk
				copy_con["AfterSecGrpName"] = msg[i]["SecGrpName"]
				copy_con["SecGrpExplnChangeSector"] = jk
				copy_con["AfterSecGrpExpln"] = "（Groupグループ）"
				copy_con["MailAddressChangeSector"] = jk
				copy_con["AfterMailAddress"] = "%s@cu.nri.co.jp"%msg[i]["OrganizCode"]
				copy_con["GALDispFlgChangeSector"] = jk
				copy_con["AfterGALDispFlg"] = i%3
				copy_con["GALDisplayOrderChangeSector"] = jk
				copy_con["AfterGALDisplayOrder"] = "333222"

				DATAS.append(copy_con)
			saveByName(tableName, CON[jk], paths, DATAS)

		elif jk == "2":#変更 2
			DATAS = []
			for i in range(0,lens):
				copy_con = copy(con_dict)
				copy_con["TrunsactNo"] = "3100000000000%d"%i
				copy_con["RegistationDate"] = getCurDate()
				copy_con["OrganizCode"] = msg[i]["OrganizCode"]
				copy_con["ChangeSector"] = jk
				copy_con["SecGrpCodeChangeSector"] = jk
				copy_con["BeforeSecGrpCode"] = msg[i]["OrganizCode"]
				copy_con["AfterSecGrpCode"] = msg[i]["OrganizCode"]+"-s"
				copy_con["SecGrpNameChangeSector"] = jk
				copy_con["BeforeSecGrpName"] = msg[i]["SecGrpName"]
				copy_con["AfterSecGrpName"] = msg[i]["SecGrpName"]+"(change)"
				copy_con["SecGrpExplnChangeSector"] = jk
				copy_con["BeforeSecGrpExpln"] = "（Groupグループ）"
				copy_con["AfterSecGrpExpln"] = "（東京グループ）(change)"
				copy_con["MailAddressChangeSector"] = jk
				copy_con["BeforeMailAddress"] = "%s@cu.nri.co.jp"%msg[i]["OrganizCode"]
				copy_con["AfterMailAddress"] = "%s@cu.nri.co.jp"%(msg[i]["OrganizCode"]+"-s")
				copy_con["GALDispFlgChangeSector"] = jk
				copy_con["BeforeGALDispFlg"] = i%3
				copy_con["AfterGALDispFlg"] = (i+1)%3
				copy_con["GALDisplayOrderChangeSector"] = jk
				copy_con["BeforeGALDisplayOrder"] = "333222"
				copy_con["AfterGALDisplayOrder"] = "111111"

				DATAS.append(copy_con)

			saveByName(tableName, CON[jk], paths, DATAS)
		else:#削除 3
			DATAS = []
			for i in range(0,lens):
				copy_con = copy(con_dict)
				copy_con["TrunsactNo"] = "3200000000000%d"%i
				copy_con["RegistationDate"] = getCurDate()
				copy_con["OrganizCode"] = msg[i]["OrganizCode"]
				copy_con["ChangeSector"] = jk
				copy_con["SecGrpCodeChangeSector"] = jk
				copy_con["BeforeSecGrpCode"] = msg[i]["OrganizCode"]+"-s"
				copy_con["AfterSecGrpCode"] = msg[i]["OrganizCode"]+"-s"
				copy_con["SecGrpNameChangeSector"] = jk
				copy_con["BeforeSecGrpName"] = msg[i]["SecGrpName"]+"(change)"
				copy_con["SecGrpExplnChangeSector"] = jk
				copy_con["BeforeSecGrpExpln"] = "（東京グループ）(change)"
				copy_con["MailAddressChangeSector"] = jk
				copy_con["BeforeMailAddress"] = "%s@cu.nri.co.jp"%(msg[i]["OrganizCode"]+"-s")
				copy_con["GALDispFlgChangeSector"] = jk
				copy_con["BeforeGALDispFlg"] = (i+1)%3
				copy_con["GALDisplayOrderChangeSector"] = jk
				copy_con["BeforeGALDisplayOrder"] = "111111"

				DATAS.append(copy_con)
			saveByName(tableName, CON[jk], paths, DATAS)

def MT_GrpAcntInfo_value_change(copy_con,TrunsactNo,RegistationDate,OrganizCode,ChangeSector,SecGrpCodeChangeSector,BeforeSecGrpCode,AfterSecGrpCode,\
	SecGrpNameChangeSector,BeforeSecGrpName,AfterSecGrpName,SecGrpExplnChangeSector,BeforeSecGrpExpln,AfterSecGrpExpln,MailAddressChangeSector,BeforeMailAddress,\
	AfterMailAddress,GALDispFlgChangeSector,BeforeGALDispFlg,AfterGALDispFlg,GALDisplayOrderChangeSector,BeforeGALDisplayOrder,AfterGALDisplayOrder):
	# ---------------------------------------------------------------------------------------------------------------------------------------
	#
	# 
	# ---------------------------------------------------------------------------------------------------------------------------------------

	copy_con["TrunsactNo"] = TrunsactNo
	copy_con["RegistationDate"] = RegistationDate
	copy_con["OrganizCode"] = OrganizCode
	copy_con["ChangeSector"] = ChangeSector
	copy_con["SecGrpCodeChangeSector"] = SecGrpCodeChangeSector
	copy_con["BeforeSecGrpCode"] = BeforeSecGrpCode
	copy_con["AfterSecGrpCode"] = AfterSecGrpCode
	copy_con["SecGrpNameChangeSector"] = SecGrpNameChangeSector
	copy_con["BeforeSecGrpName"] = BeforeSecGrpName
	copy_con["AfterSecGrpName"] = AfterSecGrpName
	copy_con["SecGrpExplnChangeSector"] = SecGrpExplnChangeSector
	copy_con["BeforeSecGrpExpln"] = BeforeSecGrpExpln
	copy_con["AfterSecGrpExpln"] = AfterSecGrpExpln
	copy_con["MailAddressChangeSector"] = MailAddressChangeSector
	copy_con["BeforeMailAddress"] = BeforeMailAddress
	copy_con["AfterMailAddress"] = AfterMailAddress
	copy_con["GALDispFlgChangeSector"] = GALDispFlgChangeSector
	copy_con["BeforeGALDispFlg"] = BeforeGALDispFlg
	copy_con["AfterGALDispFlg"] = AfterGALDispFlg
	copy_con["GALDisplayOrderChangeSector"] = GALDisplayOrderChangeSector
	copy_con["BeforeGALDisplayOrder"] = BeforeGALDisplayOrder
	copy_con["AfterGALDisplayOrder"] = AfterGALDisplayOrder

def modify_MT_GrpAcntSInfo_case(patho, paths):
	tableName = "MT_GrpAcntSInfo"
	jouken = ["1", "3"]

	msg = {
		"OrganizCode":"SB00010001",
		"SecGrpCode":"b-database",
		"SecGrpName":"(東京大学大学院)"
	}
	datas = [{
		"ID":"UB00010001",
		"logonID":"b-tanaka-01",
		"AflOrgSector":"0"
	},{
		"ID":"ST00010002",
		"logonID":"A_80_55_10",
		"AflOrgSector":"1"
	},{
		"ID":"RR00010001",
		"logonID":"r-resource-01",
		"AflOrgSector":"2"
	}]

	con_dict = openFile(patho, tableName)
	lens = len(datas)

	for jk in jouken:
		# 追加 1
		if jk == "1":
			DATAS = []
			for i in range(0,lens):
				copy_con = copy(con_dict)

				MT_GrpAcntSInfo_value_change(copy_con, "2000000000000%d"%i, getCurDate(), msg["OrganizCode"], msg["SecGrpCode"], jk, \
					datas[i]["AflOrgSector"], datas[i]["ID"], datas[i]["logonID"])

				DATAS.append(copy_con)

			saveByName(tableName, CON[jk], paths, DATAS)
		else:#削除
			DATAS = []
			for i in range(0,lens):
				copy_con = copy(con_dict)

				MT_GrpAcntSInfo_value_change(copy_con, "2300000000000%d"%i, getCurDate(), msg["OrganizCode"], msg["SecGrpCode"], jk, \
					datas[i]["AflOrgSector"], datas[i]["ID"], datas[i]["logonID"])
				DATAS.append(copy_con)

			saveByName(tableName, CON[jk], paths, DATAS)

def MT_GrpAcntSInfo_value_change(copy_con,TrunsactNo,RegistationDate,OrganizCode,SecGrpCode,AflChangeSector,AflOrgSector,\
	AflUserIdRsrcCdOrgCd,AflLogonIdSecGrpCd):
	# ---------------------------------------------------------------------------------------------------------------------------------------
	# | TrunsactNo | RegistationDate | OrganizCode | SecGrpCode | AflChangeSector | AflOrgSector | AflUserIdRsrcCdOrgCd | AflLogonIdSecGrpCd |
	# ---------------------------------------------------------------------------------------------------------------------------------------
	# | トランザクションNo| 登録日時 | 中間DBグループコード | セキュリティグループコード | 所属変更区分 | 所属識別区分 | 所属ユーザーID/リソースCD/| 所属ログオンID/セキュリティグループコード |
	#---------------------------------------------------------------------------------------------------------------------------------------
	copy_con["TrunsactNo"] = TrunsactNo
	copy_con["RegistationDate"] = RegistationDate
	copy_con["OrganizCode"] = OrganizCode
	copy_con["SecGrpCode"] = SecGrpCode
	copy_con["AflChangeSector"] = AflChangeSector
	copy_con["AflOrgSector"] = AflOrgSector
	copy_con["AflUserIdRsrcCdOrgCd"] = AflUserIdRsrcCdOrgCd
	copy_con["AflLogonIdSecGrpCd"] = AflLogonIdSecGrpCd

def modify_MT_AccountAttributeReflect_case(patho, paths):
	tableName = "MT_AccountAttributeReflect"

	msg = [{
		"ValueName":"ext-Mail",
		"Value":"b-tanaka-01@nri.co.jp",
		"LogOnId":"b-tanaka-01"
	},{
		"ValueName":"personid",
		"Value":"222111",
		"LogOnId":"b-tanaka-04"
	},{
		"ValueName":"ext-addressBookMail",
		"Value":"f-tanaka-01-change@i-tech.nri.co.jp",
		"LogOnId":"f-tanaka-01"
	}]
		
	con_dict = openFile(patho, tableName)
	lens = len(msg)
	DATAS = []
	for i in range(0,lens):
		copy_con = copy(con_dict)

		MT_AccountAttributeReflect_value_change(copy_con,"1000000000000%d"%i, getYYYYMMDD(), msg[i]["ValueName"], msg[i]["Value"], msg[i]["LogOnId"])
		DATAS.append(copy_con)

	saveByName(tableName, "", paths, DATAS)

def MT_AccountAttributeReflect_value_change(copy_con,RecordNo,ApplicationStartDay,ValueName,Value,LogOnId):
	# -----------------------------------------------------------------
	# | RecordNo | ApplicationStartDay | ValueName | Value | LogOnId |
	# -----------------------------------------------------------------
	# | インデックス | 　　適用開始日 　　　 |   属性名　| 属性値 | ログオンID |
	# -----------------------------------------------------------------
	copy_con["RecordNo"] = RecordNo
	copy_con["ApplicationStartDay"] = ApplicationStartDay
	copy_con["ValueName"] = ValueName
	copy_con["Value"] = Value
	copy_con["LogOnId"] = LogOnId

def modify_MT_MBXPermissionInfo_case(patho, paths):
	tableName = "MT_MBXPermissionInfo"

	msg = [{
			"UserIdRsrcCd":"UB00010001",
			"logonID":"b-tanaka-01",
		},{
			"UserIdRsrcCd":"RR00010001",
			"logonID":"r-resource-01",
		}]
	datas = {
		"user":[{
			"UserIdRsrcCd":"UB00010004",
			"SecGrpCd":"b-tanaka-04",
			"MBXSector":"06"
		},{
			"UserIdRsrcCd":"RB00010001",
			"SecGrpCd":"b-resource-01",
			"MBXSector":"07"
		},{
			"UserIdRsrcCd":"SB00010001",
			"SecGrpCd":"b-database",
			"MBXSector":"08"
		}],
		"resource":[{
			"UserIdRsrcCd":"UF00010001",
			"SecGrpCd":"f-tanaka-01",
			"MBXSector":"00"
		},{
			"UserIdRsrcCd":"RS00010001",
			"SecGrpCd":"s-resource",
			"MBXSector":"01"
		},{
			"UserIdRsrcCd":"SF00010002",
			"SecGrpCd":"A_80_55",
			"MBXSector":"02"
		}]
	}
		
	con_dict = openFile(patho, tableName)
	lens = len(msg)+1	# +1は既定選択肢のため
	# print(lens)
	len_user = len(datas["user"])	#ユーザーの数
	len_resource = len(datas["resource"])	#リソースの数
	# sum = 0	#TrunsactNoの違う
	for jk in CON:
		# 追加 1
		sum = 0
		if jk == "1":
			DATAS = []
			for i in range(0,lens):
				if i == 0:# user
					for j in range(0,len_user):
						copy_con = copy(con_dict)
						MT_MBXPermissionInfo_value_change(copy_con, "5100000000000%d"%sum, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], datas["user"][j]["MBXSector"], msg[i]["logonID"])
						DATAS.append(copy_con)
						sum = sum +1
				elif i == 1:# resource
					for j in range(0,len_resource):
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "5100000000000%d"%sum, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], datas["resource"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						sum = sum +1
				else:#既定
					MT_MBXPermissionInfo_value_change(copy_con, "5100000000000%d"%sum, getCurDate(), jk, msg[i%2]["UserIdRsrcCd"], "1", \
							"", "", "03", msg[i%2]["logonID"])
					DATAS.append(copy_con)
					sum = sum +1

			saveByName(tableName, CON[jk], paths, DATAS)

		elif jk == '2':
			DATAS = []
			for i in range(0,lens):
				if i == 0:# user
					for j in range(0,len_user):
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "5200000000000%d"%sum, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], "04", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1

				elif i == 1:
					for j in range(0,len_resource):
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "5200000000000%d"%sum, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], "05", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
				else:
					copy_con = copy(con_dict)
					MT_MBXPermissionInfo_value_change(copy_con, "5200000000000%d"%sum, getCurDate(), jk, msg[i%2]["UserIdRsrcCd"], "1", \
							"", "", "10", msg[i%2]["logonID"])
					DATAS.append(copy_con)
					sum = sum +1

			saveByName(tableName, CON[jk], paths, DATAS)

		else:
			DATAS = []
			copy_con = copy(con_dict)
			for i in range(0,lens):
				copy_con = copy(con_dict)
				if i == 0:# user
					for j in range(0,len_user):
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "5300000000000%d"%sum, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], "04", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
				elif i == 1:#resource
					for j in range(0,len_resource):
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "5300000000000%d"%sum, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], "05", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
				else:#既定
					copy_con = copy(con_dict)
					
					MT_MBXPermissionInfo_value_change(copy_con, "5300000000000%d"%sum, getCurDate(), jk, msg[i%2]["UserIdRsrcCd"], "1", \
							"", "", "10", msg[i%2]["logonID"])

					DATAS.append(copy_con)
					sum = sum +1

			saveByName(tableName, CON[jk], paths, DATAS)

def MT_MBXPermissionInfo_value_change(copy_con,TrunsactNo,RegistationDate,ChangeSector,UserIdRsrcCd,MBXDefaultSector,\
	MBXUserIdRsrcCdOrgCd,MBXLogonIdSecGrpCd,MBXSector,LogOnId):
	"Package into a function"
	# ------------------------------------------------------------------------------------------------------------------------------------------------------------
	# | TrunsactNo | RegistationDate | ChangeSector | UserIdRsrcCd | MBXDefaultSector | MBXUserIdRsrcCdOrgCd | MBXLogonIdSecGrpCd | MBXSector | LogOnId |
	# ------------------------------------------------------------------------------------------------------------------------------------------------------------
	# | トランザクションNo | 登録者ID | 登録日時 | 変更区分 | ユーザーID/リソースCD | MBX権限既定区分 | MBXユーザーID/リソースCD | MBXログオンID/セキュリティグループコード | MBX権限区分 | ログオンID
	# ------------------------------------------------------------------------------------------------------------------------------------------------------------
	copy_con["TrunsactNo"] = TrunsactNo
	copy_con["RegistationDate"] = RegistationDate
	copy_con["ChangeSector"] = ChangeSector
	copy_con["UserIdRsrcCd"] = UserIdRsrcCd
	copy_con["MBXDefaultSector"] = MBXDefaultSector
	copy_con["MBXUserIdRsrcCdOrgCd"] = MBXUserIdRsrcCdOrgCd
	copy_con["MBXLogonIdSecGrpCd"] = MBXLogonIdSecGrpCd
	copy_con["MBXSector"] = MBXSector
	copy_con["LogOnId"] = LogOnId

def saveByName(tableName, fileName, paths, datas):
	"save modify file to path by name"
	items = {}
	items["tableName"] = tableName
	items["items"] = datas
	path_s = os.path.join(paths, "%s_%s.json"%(tableName,fileName))

	with open(path_s,"w+",encoding="utf-8") as f:
		f.write(json.dumps(items,ensure_ascii=False,indent=4))

def openFile(patho, fileName):
	"open files and return content"
	os.chdir(patho)
	try:
		with open("%s_sample.json"%fileName) as f:
			content = f.read()

		return json.loads(content)

	except Exception as e:
		print("%s.json file not found : "%fileName, e)
		# raise e

def getCurDate():
	"2019-10-01 10:13:14"
	from datetime import datetime
	# from time import gmtime, strftime
	nowtime = datetime.now()

	# newtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	# newtime = nowtime.strftime('%Y-%m-%d %H:%M:%S.%f%z')
	newtime = nowtime.strftime('%Y/%m/%d %H:%M:%S')
	return newtime

def getYYYYMMDD(n=0):
	"20191001"
	import datetime
	# from time import gmtime, strftime
	nowtime = datetime.datetime.now() + datetime.timedelta(days=n)

	# newtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	# newtime = nowtime.strftime('%Y-%m-%d %H:%M:%S.%f%z')
	newtime = nowtime.strftime('%Y%m%d')
	return newtime
if __name__ == '__main__':
	print("--------------------------------------------")
	
	# time = "ddd"
	# url1 = "https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_%s_1/"%time
	# Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImFQY3R3X29kdlJPb0VOZzNWb09sSWgydGlFcyIsImtpZCI6ImFQY3R3X29kdlJPb0VOZzNWb09sSWgydGlFcyJ9.eyJhdWQiOiJodHRwczovL2lkbS1hcGkuY3ViMy5ucmkuY28uanAvIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNmM5MzE0MTItNzZiMi00ZGRjLWI0NTItZGVmNjgxNWFkNmFiLyIsImlhdCI6MTU2OTkwNDI4NSwibmJmIjoxNTY5OTA0Mjg1LCJleHAiOjE1Njk5MDgxODUsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84TUFBQUFxZkFOYnZzamVJK3hoQnpTcVFXVEFVNVZHNVVzcGgvcVRhQ0N3WlA5RkErbEY1WCtuenNwWFJVTG95SzdPejF5d0JKTzltM3ArT1JtOUt5dU1URVR6eVRLVFFyekNyUkhJcklhWkZFV0FQTT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiOGE3ZTEyZDItZGZmYS00MzY3LThkOGEtMDBkMzdiNzMxMGMyIiwiYXBwaWRhY3IiOiIwIiwiaXBhZGRyIjoiMzYuMy44NC4xMjYiLCJuYW1lIjoi6LaZ44CA5p2wKGR3cCkiLCJvaWQiOiIxMDcyOGEwOS1iYTY3LTRjYWUtYjAyYi04MmM4OTgyNGM3MTciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjc3Mjg3MjE3Ni0yNDYzNTMxODI0LTM1NTY0OTIzMjQtMTA5NjEyIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiM0ZmSnU5blpQMll3bnF2a0VySVJ4WDVxMUowT0Zyam9KbC10YzZBcnpDZyIsInRpZCI6IjZjOTMxNDEyLTc2YjItNGRkYy1iNDUyLWRlZjY4MTVhZDZhYiIsInVuaXF1ZV9uYW1lIjoidG9uMDAwMDctZHdwQGN1YjMubnJpLmNvLmpwIiwidXBuIjoidG9uMDAwMDctZHdwQGN1YjMubnJpLmNvLmpwIiwidXRpIjoiam9xVG5Sc3d0MFctY3VKS3R1NFNBQSIsInZlciI6IjEuMCJ9.Gsg99IWSr1QKsEqMfFvXwANvnhEXrI0pIQCjiJw9mWwEMwDNcTzjC8nKjCHmkRw6rMTfjQNC3EHcFUOYHfX4oYG_u8SIJxtrdO4H5my2vrETUpK0jAV-0TAMOfmksskeUWzEb6x8MnYPTQlUaNIs2k_Bi18QBYrK-QVIIR1U0xCThlR5IRqJvTcz2EbokGvkJ9RNLrskGLhIYegpj7GmVW0yYbNorGJ8ESuRDHPca_XNHVd4Jly-OVaAyS1iah-rFj-s85INaMPaleYucN2LDbdzojYkKM_9aLW5gYfr4_7Op9JW2sc3vU7Q2PoeMe9Mg8PsZsdnPBJzmzQnxjT0ew"
	# token = Token if "Token" in globals() else getAccessToken()

	# getDiffData(token)
	# print(getYYYYMMDD())
	# --------------------------------------------------------------------------------------------
	#	read file and modify sensitive message,then save
	#
	PATHO = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Original"
	PATHS = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Modify"
	PATHSC = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Modify_Case"
	PATHOC = "C:\\Users\\liaga\\株式会社トップワンテック\\toponetec - ドキュメント\\96.personal\\ligaigai\\PH2.テストケース\\Sample"
	patho = PATHO if "PATHO" in globals() else os.path.abspath(os.path.dirname(__file__))
	paths = PATHS if "PATHS" in globals() else os.path.abspath(os.path.dirname(__file__))
	paths_c = PATHSC if "PATHSC" in globals() else os.path.abspath(os.path.dirname(__file__))
	patho_c = PATHOC if "PATHOC" in globals() else os.path.abspath(os.path.dirname(__file__))
	# modify_MT_UserRsrcAcntInfo(patho, paths)
	# modify_MT_GrpAcntInfo(patho, paths)
	# modify_MT_GrpAcntSInfo(patho, paths)
	# modify_MT_AccountAttributeReflect(patho, paths)
	# modify_MT_MBXPermissionInfo(patho, paths)
	# --------------------------------------------------------------------------------------------
	# --------------------------------------------------------------------------------------------
	modify_MT_UserRsrcAcntInfo_case(patho_c, paths_c)
	modify_MT_GrpAcntInfo_case(patho_c, paths_c)
	modify_MT_GrpAcntSInfo_case(patho_c, paths_c)
	modify_MT_AccountAttributeReflect_case(patho_c, paths_c)
	modify_MT_MBXPermissionInfo_case(patho_c, paths_c)
	# print(patho, paths)
	# --------------------------------------------------------------------------------------------

	print("----end----")
