#coding:utf-8
import json
from jmespath import search
# import os

html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<style>
		table, th, td {
		  border: 1px solid black;
		  border-collapse: collapse;
		}
		th, td {
		  padding: 5px;
		  text-align: left;
		}
	</style>
	<title></title>
</head>
<body>
	<h2>%s</h2>
	<p>%s</p>
	<table>
	<tr>
		<th>テーブル名</th>
		<th>テーブルID</th>
		<th>CuDB</th>
		<th>CosmosDB</th>
		<th>結果</th>
	</tr>
	<tr>
		<td>AD個別属性</td>
		<td>IDM_Import_MT_AccountAttributeReflect</td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
	</tr>
	<tr>
		<td>グループアカウント変更情報</td>
		<td>MT_GrpAcntInfo </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
	</tr>
	<tr>
		<td>グループアカウント所属変更情報</td>
		<td>MT_GrpAcntSInfo </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
	</tr>
	<tr>
		<td>Exアクセス権</td>
		<td>MT_MBXPermissionInfo </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
	</tr>
	<tr>
		<td>ユーザ、リソースAD、Ex属性</td>
		<td>MT_UserRsrcAcntInfo </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
	</tr>
	</table>
</body>
</html>
"""

# =========================
#
# difference Cosmosdb and CuDB
#
#==========================
import os
def getPathName():
	"get gived path's all path "

	allpath = []
	for root, dirs, files in os.walk(os.getcwd()):
		for dir in dirs:
			allpath.append(dir)

	# print(paths)
	return allpath


def JudgeNumFixed(num1, num2):
	"Judge whether num1 is equal num2, if equal then = str1, or = str2 "
	"num2 is bigger than num1"
	result = '一致' if (num1 == num2) else '＊不一致: ' +'%d件'%(num2-num1)

	return result

def changeJson(lt,key):
	"change list to json"
	diff = []
	
	for i in lt:
		temp = {}
		temp[key] = i
		diff.append(temp)

	return diff

if __name__ == "__main__":

	datas = []

	# for path in paths:
	# print("path :" ,path)
	# os.chdir(realPath)
	# path_file = os.path.join(realPath, path)


	data_u_1 = open("IDM_Import_MT_AccountAttributeReflect\\CuDB.json","rb").read()
	data_u_2 = open("MT_GrpAcntInfo\\CuDB.json","rb").read()
	data_u_3 = open("MT_GrpAcntSInfo\\CuDB.json","rb").read()
	data_u_4 = open("MT_MBXPermissionInfo\\CuDB.json","rb").read()
	data_u_5 = open("MT_UserRsrcAcntInfo\\CuDB.json","rb").read()

	json_u_1 = json.loads(data_u_1)
	json_u_2 = json.loads(data_u_2)
	json_u_3 = json.loads(data_u_3)
	json_u_4 = json.loads(data_u_4)
	json_u_5 = json.loads(data_u_5)

	con_u = "length(items)"

	con_u_dif = "items[].OrganizCode"

	res_u_1 = search(con_u,json_u_1)
	res_u_2 = search(con_u,json_u_2)
	res_u_3 = search(con_u,json_u_3)
	res_u_4 = search(con_u,json_u_4)
	res_u_5 = search(con_u,json_u_5)

	
	# res_u_2_dif = search(con_u_dif,json_u_2)
	# res_u_3_dif = search(con_u_dif,json_u_3)
	# res_u_4_dif = search(con_u_dif,json_u_4)
	# res_u_5_dif = search(con_u_dif,json_u_5)

	data_s_1 = open("IDM_Import_MT_AccountAttributeReflect\\CosmosDB.json","rb").read()
	data_s_2 = open("MT_GrpAcntInfo\\cosmosdb.json","rb").read()
	data_s_3 = open("MT_GrpAcntSInfo\\cosmosdb.json","rb").read()
	data_s_4 = open("MT_MBXPermissionInfo\\cosmosdb.json","rb").read()
	data_s_5 = open("MT_UserRsrcAcntInfo\\cosmosdb.json","rb").read()

	json_s_1 = json.loads(data_s_1)
	json_s_2 = json.loads(data_s_2)
	json_s_3 = json.loads(data_s_3)
	json_s_4 = json.loads(data_s_4)
	json_s_5 = json.loads(data_s_5)

	con_s_1 = "length([?sysName=='ImportCUDBData-TblIDMImportMTAccountAttributeReflect'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'])"
	con_s_2 = "length([?sysName=='ImportCUDBData-TblMTGrpAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'])"
	con_s_3 = "length([?sysName=='ImportCUDBData-TblMTGrpAcntSInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'])"
	con_s_4 = "length([?sysName=='ImportCUDBData-TblMTMBXPermissionInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'])"
	con_s_5 = "length([?sysName=='ImportCUDBData-TblMTUserRsrcAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'])"


	con_s_1_dif = "[?sysName=='ImportCUDBData-TblIDMImportMTAccountAttributeReflect'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'].identityName"
	con_s_2_dif = "[?sysName=='ImportCUDBData-TblMTGrpAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'].identityName"
	con_s_3_dif = "[?sysName=='ImportCUDBData-TblMTGrpAcntSInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'].identityName"
	con_s_4_dif = "[?sysName=='ImportCUDBData-TblMTMBXPermissionInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'].identityName"
	con_s_5_dif = "[?sysName=='ImportCUDBData-TblMTUserRsrcAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'].identityName"

	res_s_1 = search(con_s_1,json_s_1)
	res_s_2 = search(con_s_2,json_s_2)
	res_s_3 = search(con_s_3,json_s_3)
	res_s_4 = search(con_s_4,json_s_4)
	res_s_5 = search(con_s_5,json_s_5)

	
	# res_s_2_dif = search(con_s_2_dif,json_s_2)
	# res_s_3_dif = search(con_s_3_dif,json_s_3)
	# res_s_4_dif = search(con_s_4_dif,json_s_4)
	# res_s_5_dif = search(con_s_5_dif,json_s_5)

	# result_1 = '一致' if (res_u_1 == res_s_1) else '**不一致'
	# result_2 = '一致' if (res_u_2 == res_s_2) else '**不一致'
	# result_3 = '一致' if (res_u_3 == res_s_3) else '**不一致'
	# result_4 = '一致' if (res_u_4 == res_s_4) else '**不一致'
	# result_5 = '一致' if (res_u_5 == res_s_5) else '**不一致'

	result_1 = JudgeNumFixed(res_u_1, res_s_1)
	result_2 = JudgeNumFixed(res_u_2, res_s_2)
	result_3 = JudgeNumFixed(res_u_3, res_s_3)
	result_4 = JudgeNumFixed(res_u_4, res_s_4)
	result_5 = JudgeNumFixed(res_u_5, res_s_5)
	if result_1 != '一致':
		res_u_1_dif = search(con_u_dif,json_u_1)
		# res_u_1_dif = changeJson(res_u_1_dif, "RegistarId")
		res_s_1_dif = search(con_s_1_dif,json_s_1)
		# res_s_1_dif = changeJson(res_s_1_dif, "identityName")

		f = open("IDM_Import_MT_AccountAttributeReflect-cu.json","w+",encoding="utf-8")
		f.write(json.dumps(res_u_1_dif,ensure_ascii=False,indent=1))
		f.close()
		f = open("IDM_Import_MT_AccountAttributeReflect-cos.json","w+",encoding="utf-8")
		f.write(json.dumps(res_s_1_dif,ensure_ascii=False,indent=1))
		f.close()
	if result_2 != '一致':
		res_u_2_dif = search(con_u_dif,json_u_2)
		# res_u_2_dif = changeJson(res_u_2_dif, "RegistarId")
		res_s_2_dif = search(con_s_2_dif,json_s_2)
		# res_s_2_dif = changeJson(res_s_2_dif, "identityName")
		f = open("MT_GrpAcntInfo-cu.json","w+",encoding="utf-8")
		f.write(json.dumps(res_u_2_dif,ensure_ascii=False,indent=1))
		f.close()
		f = open("MT_GrpAcntInfo-cos.json","w+",encoding="utf-8")
		f.write(json.dumps(res_s_2_dif,ensure_ascii=False,indent=1))
		f.close()
	if result_3 != '一致':
		res_u_3_dif = search(con_u_dif,json_u_3)
		# res_u_3_dif = changeJson(res_u_3_dif, "RegistarId")
		res_s_3_dif = search(con_s_3_dif,json_s_3)
		# res_s_3_dif = changeJson(res_s_3_dif, "identityName")
		f = open("MT_GrpAcntSInfo -cu.json","w+",encoding="utf-8")
		f.write(json.dumps(res_u_3_dif,ensure_ascii=False,indent=1))
		f.close()
		f = open("MT_GrpAcntSInfo -cos.json","w+",encoding="utf-8")
		f.write(json.dumps(res_s_3_dif,ensure_ascii=False,indent=1))
		f.close()
	if result_4 != '一致':
		res_u_4_dif = search(con_u_dif,json_u_4)
		# res_u_4_dif = changeJson(res_u_4_dif, "RegistarId")
		res_s_4_dif = search(con_s_4_dif,json_s_4)
		# res_s_4_dif = changeJson(res_s_4_dif, "identityName")
		f = open("MT_MBXPermissionInfo -cu.json","w+",encoding="utf-8")
		f.write(json.dumps(res_u_4_dif,ensure_ascii=False,indent=1))
		f.close()
		f = open("MT_MBXPermissionInfo -cos.json","w+",encoding="utf-8")
		f.write(json.dumps(res_s_4_dif,ensure_ascii=False,indent=1))
		f.close()
	if result_5 != '一致':
		res_u_5_dif = search(con_u_dif,json_u_5)
		# res_u_5_dif = changeJson(res_u_5_dif, "RegistarId")
		res_s_5_dif = search(con_s_5_dif,json_s_5)
		# res_s_5_dif = changeJson(res_s_5_dif, "identityName")
		f = open("MT_UserRsrcAcntInfo-cu.json","w+",encoding="utf-8")
		f.write(json.dumps(res_u_5_dif,ensure_ascii=False,indent=1))
		f.close()
		f = open("MT_UserRsrcAcntInfo-cos.json","w+",encoding="utf-8")
		f.write(json.dumps(res_s_5_dif,ensure_ascii=False,indent=1))
		f.close()


	datas.append(res_u_1)
	datas.append(res_s_1)
	datas.append(result_1)
	datas.append(res_u_2)
	datas.append(res_s_2)
	datas.append(result_2)
	datas.append(res_u_3)
	datas.append(res_s_3)
	datas.append(result_3)
	datas.append(res_u_4)
	datas.append(res_s_4)
	datas.append(result_4)
	datas.append(res_u_5)
	datas.append(res_s_5)
	datas.append(result_5)
		# break

	print(datas)

	# data_cudb = open("IDM_Import_MT_AccountAttributeReflec\\cosmosdb.json","rb").read()
	# json_cudb = json.loads(data_cudb)

	# con_cudb = "length([?sysName=='ImportCUDBData-TblMTGrpAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'])"
	# result_cudb = search(con_cudb,json_cudb)
	# print("cudb :",result_cudb)
#

# 	# argv[]説明
# 	# ユーザ: user
# 	# グループ: group
# 	# リソース: absource
	h_content = ""
	p_content = ""

	f = open("Report.html","w+",encoding="utf-8")

	f.write(html%(h_content,p_content,datas[0],datas[1],datas[2],datas[3],datas[4],datas[5],datas[6],datas[7],datas[8],datas[9],datas[10],datas[11],datas[12],datas[13],datas[14]))


	f.close()


