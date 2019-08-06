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
		<td>グループアカウント所属変更情報</td>
		<td>MT_GrpAcntSInfo </td>
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

def getJson(fname):
	"read file string and return json "
	temp = open(fname,"rb").read()
	js = json.loads(temp)

	return js

if __name__ == "__main__":
	
	datas = []

	# for path in paths:
	# print("path :" ,path)
	# os.chdir(realPath)
	# path_file = os.path.join(realPath, path)


	json_u_1 = getJson("IDM_Import_MT_AccountAttributeReflect\\CuDB.json")
	json_u_2 = getJson("MT_GrpAcntInfo\\CuDB.json")
	json_u_3 = getJson("MT_GrpAcntSInfo\\CuDB.json")
	json_u_4 = getJson("MT_MBXPermissionInfo\\CuDB.json")
	json_u_5 = getJson("MT_UserRsrcAcntInfo\\CuDB.json")

	con_u = "length(items)"

	res_u_1 = search(con_u,json_u_1)
	res_u_2 = search(con_u,json_u_2)
	res_u_3 = search(con_u,json_u_3)
	res_u_4 = search(con_u,json_u_4)
	res_u_5 = search(con_u,json_u_5)

	json_s_1 = getJson("IDM_Import_MT_AccountAttributeReflect\\CosmosDB.json")
	json_s_2 = getJson("MT_GrpAcntInfo\\cosmosdb.json",)
	json_s_3 = getJson("MT_GrpAcntSInfo\\cosmosdb.json")
	json_s_4 = getJson("MT_MBXPermissionInfo\\cosmosdb.json")
	json_s_5 = getJson("MT_UserRsrcAcntInfo\\cosmosdb.json")

	con_s_1 = "length([?sysName=='ImportCUDBData-TblIDMImportMTAccountAttributeReflect'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'])"
	con_s_2 = "length([?sysName=='ImportCUDBData-TblMTGrpAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'])"
	con_s_3 = "length([?sysName=='ImportCUDBData-TblMTGrpAcntSInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='group'])"
	con_s_4 = "length([?sysName=='ImportCUDBData-TblMTMBXPermissionInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'])"
	con_s_5 = "length([?sysName=='ImportCUDBData-TblMTUserRsrcAcntInfo'&&ns=='Cu1Stg'&&objCls=='history'&&type=='user'])"

	res_s_1 = search(con_s_1,json_s_1)
	res_s_2 = search(con_s_2,json_s_2)
	res_s_3 = search(con_s_3,json_s_3)
	res_s_4 = search(con_s_4,json_s_4)
	res_s_5 = search(con_s_5,json_s_5)

	result_1 = '一致' if (res_u_1 == res_s_1) else '**不一致'
	result_2 = '一致' if (res_u_2 == res_s_2) else '**不一致'
	result_3 = '一致' if (res_u_3 == res_s_3) else '**不一致'
	result_4 = '一致' if (res_u_4 == res_s_4) else '**不一致'
	result_5 = '一致' if (res_u_5 == res_s_5) else '**不一致'

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

	f = open("result.html","w+",encoding="utf-8")

	f.write(html%(h_content,p_content,datas[0],datas[1],datas[2],datas[3],datas[4],datas[5],datas[6],datas[7],datas[8],datas[9],datas[10],datas[11],datas[12],datas[13],datas[14]))


	f.close()


