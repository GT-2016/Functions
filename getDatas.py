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
		"refresh_token":"AQABAAAAAAAP0wLlqdLVToOpA4kwzSnxOvZrudC01VzBQZ5MAMJoABjIF0LsdMbwwREPvS2WTIGLWsc63oCbEW0j6LFN_UeNKyTRqazB_o5T6BBUU_RR2U8cBnbPa4kxnx9C74QNwB5Xw9BOZW5R4fOE7QKHduMN6SrbN9Oe-I2yz6OWZKT10Ka-agIm5DttmaUxUA-Ah_CgzlC41cYYPCVH6MK_rkn9w2qcG14bVHEccJcdqpoxWWY6VobjJ6XfKqo8qUu31hdsxKJcc8ALMLc6q_qHp3r0N8kuE_I0d_vyqemP22r2aP4DuD9p4Ko2LiIBHYO4DkGnG-laFe4XHsKjf2uduIFOjDwGk17Xxo7r0XWlmBF9iIo0UKG6CF3EzRPTkj-o3bMBZkA1H7tPyr1RcUaBccuYdYNMgqjk9k9XVHIDvByObKuMhkzpXJxgExfZINKczEh1Q-8aC6zv85TxOxNpVt9yLXAnMvpnheAtKG2M2gnCAiTAyFuR0NBLAa12aTkv_MgYfRMgGZPelnikVm88Yfgy7twiNoYBOtu_U6kct1WFBivGPzPcTVsHc1fioMo6CVR3P6-UBbr46PdG3FpjbA0zQt8ZiI3gbb0Y9NXLF11066g1wOLX7-A9MLnFg9SSEAm3Xh5nNGUiI1C6f23AJGk3zGEnwJrUtbFJ7lfWWkruUQCeGIiOIK2xMXlbGnIh4EBCzx8kUutMSniCeCgH1sYHi2ecaiu4jK0p-GIP419SBsqFnyKs32vschfQ7RhqgAkwqk36xjYC86-S-s2D0419T2HJQ3qqdysKnYMsgawSd4cbtep9vmrCGcUA4Y6smOQwvtjjXGNkFtTkn5rAaBBhy1J3uMAlBltUQuaYJ6wsVySy_8bGArUKPExuAyO3pb000JBhcExz6ZsR1cWNv1hRcCWfnlir1vOiOLlhRS-qriAA",
		"grant_type":"refresh_token"

	}

	response = requests.post(url = url, headers = header,data = parse.urlencode(body))
	result = response.content
	
	result = str(result, encoding = "utf-8")
	result = json.loads(result)

	# with open("1.json","w+",encoding="utf-8") as f:
	# 	f.write(json.dumps(result,ensure_ascii=False,indent=1))
	# print(result["access_token"])
	return result["access_token"]

def getDataBySql():
	tables = ["MT_UserRsrcAcntInfo","MT_GrpAcntInfo","MT_GrpAcntSInfo","MT_AccountAttributeReflect","MT_MBXPermissionInfo"]


	url = "https://idm-api.cub3.nri.co.jp/api/cudb/get-data-by-sql"
	token = getAccessToken()

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
		copy_con["items"][i]["TrunsactNo"] = "4200000000000%d"%i
		copy_con["items"][i]["RegistarId"] = "BATCHFAKE"
		if copy_con["items"][i]["UserId"]:
			copy_con["items"][i]["UserId"] = "UBFAKE000%d"%i

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
			copy_con["items"][i]["BeforeMailAddress"] = "true.mailaddress_%d@test.com.cn"%i
		if copy_con["items"][i]["BeforeStructureCode"]:
			copy_con["items"][i]["BeforeStructureCode"] = "A_fake_%d"%i

		if copy_con["items"][i]["AfterLog_onId"]:
			copy_con["items"][i]["AfterLog_onId"] = "adcfake%d"%i
		if copy_con["items"][i]["AfterMailAddress"]:
			copy_con["items"][i]["AfterMailAddress"] = "fake.mailaddress_%d@test.com.cn"%i
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

		# copy_con["items"][i]["BeforeSecGrpCode"] = "NB_00%d"%i
		# # copy_con["items"][i]["AfterSecGrpCode"] = "N_00%d"%i
		# copy_con["items"][i]["BeforeSecGrpName"] = "TRUE_NAME"
		# # copy_con["items"][i]["AfterSecGrpName"] = "FAKE_NAME"
		# copy_con["items"][i]["BeforeSecGrpExpln"] = "TRUE_開発部門"
		# # copy_con["items"][i]["AfterSecGrpExpln"] = "FAKE_開発部門"
		# copy_con["items"][i]["BeforeMailAddress"] = "true.mail_%d@test.com.cn"%i
		# # copy_con["items"][i]["AfterMailAddress"] = "fake.mail_%d@test.com.cn"%i

		# MT_GrpAcntInfo
		# copy_con["items"][i]["TrunsactNo"] = "3200000000000%d"%i
		# copy_con["items"][i]["RegistarId"] = "BATCHFAKE"
		# copy_con["items"][i]["OrganizCode"] = "SLFAKE000%d"%i
		# copy_con["items"][i]["BeforeSecGrpCode"] = "NB_00%d"%i
		# # copy_con["items"][i]["AfterSecGrpCode"] = "N_00%d"%i
		# copy_con["items"][i]["BeforeSecGrpName"] = "TRUE_NAME"
		# # copy_con["items"][i]["AfterSecGrpName"] = "FAKE_NAME"
		# copy_con["items"][i]["BeforeSecGrpExpln"] = "TRUE_開発部門"
		# # copy_con["items"][i]["AfterSecGrpExpln"] = "FAKE_開発部門"
		# copy_con["items"][i]["BeforeMailAddress"] = "true.mail_%d@test.com.cn"%i
		# # copy_con["items"][i]["AfterMailAddress"] = "fake.mail_%d@test.com.cn"%i


		# MT_MBXPermissionInfo
		# copy_con["items"][i]["TrunsactNo"] = "1000000000000%d"%i
		# copy_con["items"][i]["RegistarId"] = "MBEXFAKE"
		# copy_con["items"][i]["UserId_RsrcCd"] = "UBFAKE000%d"%i
		# copy_con["items"][i]["Log_onId"] = "adcfake%d"%i
		# copy_con["items"][i]["MBXUserId_RsrcCd_OrgCd"] = "SBFAKE000%d"%i
		# copy_con["items"][i]["MBXLogonId_SecGrpCd"] = "A_fake_%d"%i

		# MT_AccountAttributeReflect
		# copy_con["items"][i]["RecordNo"] = "10000%d"%i
		# copy_con["items"][i]["Log_onId"] = "fake.burns-eu"
		# copy_con["items"][i]["ApplicationStartDay"] = "20190927"
		# copy_con["items"][i]["Value"] = "fake.email%d@test.com"%i

		# MT_GrpAcntSInfo
		# copy_con["items"][i]["TrunsactNo"] = "2100000000000%d"%i
		# copy_con["items"][i]["RegistarId"] = "MBEXFAKE"
		# copy_con["items"][i]["OrganizCode"] = "SBFAKE000%d"%i
		# copy_con["items"][i]["SecGrpCode"] = "G_00%d"%i
		# copy_con["items"][i]["AflUserId_RsrcCd_OrgCd"] = "UFFAKE"
		# copy_con["items"][i]["AflLogonId_SecGrpCd"] = "fake-log"
		#変更
		


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

			path_s = os.path.join(paths, "MT_MBXPermissionInfo_%s_10_m.json"%jk)
			
			with open(path_s,"w+",encoding="utf-8") as f:
				f.write(json.dumps(copy_con,ensure_ascii=False,indent=4))

		except Exception as e:
			print("MT_MBXPermissionInfo: File or path not exist")
			continue
	


def getCurDate():
	# from datetime import datetime
	from time import gmtime, strftime
	# nowtime = datetime.now()

	newtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	return newtime

if __name__ == '__main__':
	print("========================")
	
	# time = "ddd"
	# url1 = "https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_%s_1/"%time
	
	# # getAccessToken()


	# getCurDate()
	# --------------------------------------------------------------------------------------------
	#	read file and modify sensitive message,then save
	#
	PATHO = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Original"
	PATHS = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Modify"
	patho = PATHO if "PATHO" in globals() else os.path.abspath(os.path.dirname(__file__))
	paths = PATHS if "PATHS" in globals() else os.path.abspath(os.path.dirname(__file__))
	modify_MT_UserRsrcAcntInfo(patho, paths)
	modify_MT_GrpAcntInfo(patho, paths)
	modify_MT_GrpAcntSInfo(patho, paths)
	modify_MT_AccountAttributeReflect(patho, paths)
	modify_MT_MBXPermissionInfo(patho, paths)
	# --------------------------------------------------------------------------------------------
	
	# print(patho, paths)

	print("----end----")
