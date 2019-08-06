#coding:utf-8
import json
from jmespath import search
import os

"""
Read identityName from CosmosDB\\Identities.json
Read sAMAccountName from CuDB\\all.json
Then compare the two datas
If id not in all.json file then write in diff.txt
when the two datas are completely the same, the test result is right.

Change Contents:

------------------------------------------------------
1. modify file name from diff.txt to todo-list.json
2. change the datas saving formality from list to json

------------------------------------------------------

1.add flag to distinguish id and hs
------------------------------------------------------
1. change difference between function

Date: 2019-07-31

------------------------------------------------------
1. save nonemailbox datas to todo-list_nonemailbox.json
2. change file name to todo-list_id.json or todo-list_hs.json base on Flag

"""

Flag = "id" # id or hs query
flag_mailbox = 0	# nonemailbox default value is 0, donnot save file

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
		<th></th>
		<th>CuDB</th>
		<th>CosmosDB</th>
		<th>結果</th>
		<th>オンプレEx</th>
		<th>ExOnline</th>
		<th>NoneMailbox</th>
	</tr>
	<tr>
		<td>ユーザ </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%d件</td>
	</tr>
	<tr>
		<td>グループ </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%d件</td>
	</tr>
	<tr>
		<td>リソース </td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%s</td>
		<td>%d件</td>
		<td>%d件</td>
		<td>%d件</td>
	</tr>
	</table>
</body>
</html>
"""

def Diff2Lists(li1, li2): 
	return (list(set(li1) - set(li2))) 

def compToListByDict(list1, list2, key):
	"compare two lists then put the result to another list but display a Dictionary,data in list1 but not in list2"
	"list1 is all.json data, list2 in list1"
	diff = []

	for i in list1:
		temp = {}
		if i not in list2:
			temp[key] = i
			diff.append(temp)

	return diff

def JudgeNum(num1, num2, str1, str2):
	"Judge whether num1 is equal num2, if equal then = str1, or = str2 "
	"num2 is bigger than num1"
	result = str1 if (num1 == num2) else str2 +':　%d件'%(num2-num1)
	return result

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

	# ------------------------------------
	# search in Identities.json
	#-------------------------------------

	data = open("CosmosDB\\Identities.json","rb").read()

	data_json = json.loads(data)

	#con = input("input condition: \n")
	

	if Flag == "hs":

		con_user = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='user'])"
		con_group = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-Group'&&type=='group'])"
		con_resource = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='resource'])"
		
		con_user_id = "[?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='user'].identityName"
		con_group_id = "[?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-Group'&&type=='group'].identityName"
		con_resource_id = "[?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='resource'].identityName"

		
		con_user_server = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='user'&&formattedData.exchangeType=='server'])"
		con_user_online = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='user'&&formattedData.exchangeType=='online'])"
		con_user_mail = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='user'&&formattedData.exchangeType=='noneMailbox'])"

		con_group_server = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-Group'&&type=='group'&&formattedData.exchangeType=='server'])"
		con_group_online = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-Group'&&type=='group'&&formattedData.exchangeType=='online'])"
		con_group_mail = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-Group'&&type=='group'&&formattedData.exchangeType=='noneMailbox'])"


		con_resource_server = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='resource'&&formattedData.exchangeType=='server'])"
		con_resource_online = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='resource'&&formattedData.exchangeType=='online'])"
		con_resource_mail = "length([?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='resource'&&formattedData.exchangeType=='noneMailbox'])"


		con_user_nonemail_id = "[?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='user'&&formattedData.exchangeType=='noneMailbox'].identityName"
		con_group_nonemail_id = "[?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-Group'&&type=='group'&&formattedData.exchangeType=='noneMailbox'].identityNam"
		con_resource_nonemail_id = "[?ns=='Cu1Stg'&&objCls=='hs'&&sysName=='ImportCUDBData-User'&&type=='resource'&&formattedData.exchangeType=='noneMailbox'].identityNam"


	elif Flag == 'id':
		con_user = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='user'])"
		con_group = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-Group'&&type=='group'])"
		con_resource = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='resource'])"

		con_user_id = "[?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='user'].identityName"
		con_group_id = "[?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-Group'&&type=='group'].identityName"
		con_resource_id = "[?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='resource'].identityName"


		con_user_server = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='user'&&data.exchangeType=='server'])"
		con_user_online = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='user'&&data.exchangeType=='online'])"
		con_user_mail = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='user'&&data.exchangeType=='noneMailbox'])"

		con_group_server = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-Group'&&type=='group'&&data.exchangeType=='server'])"
		con_group_online = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-Group'&&type=='group'&&data.exchangeType=='online'])"
		con_group_mail = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-Group'&&type=='group'&&data.exchangeType=='noneMailbox'])"


		con_resource_server = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='resource'&&data.exchangeType=='server'])"
		con_resource_online = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='resource'&&data.exchangeType=='online'])"
		con_resource_mail = "length([?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='resource'&&data.exchangeType=='noneMailbox'])"


		con_user_nonemail_id = "[?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='user'&&data.exchangeType=='noneMailbox'].identityName"
		con_group_nonemail_id = "[?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-Group'&&type=='group'&&data.exchangeType=='noneMailbox'].identityName"
		con_resource_nonemail_id = "[?ns=='Cu1Stg'&&objCls=='id'&&createSrc.sysName=='ImportCUDBData-User'&&type=='resource'&&data.exchangeType=='noneMailbox'].identityName"

	else:
		raise Exception("Can't find search condition, Please enter id or hs")

	res_user = search(con_user, data_json)
	res_group = search(con_group, data_json)
	res_resource = search(con_resource, data_json)
	res_user_id = search(con_user_id, data_json)
	res_group_id = search(con_group_id, data_json)
	res_resource_id = search(con_resource_id, data_json)


	res_user_server = search(con_user_server, data_json)
	res_user_online = search(con_user_online, data_json)
	res_user_mail = search(con_user_mail, data_json)
	# print("res_user_server :",res_user_server)
	# print("res_user_online :",res_user_online)
	# print("res_user_mail :",res_user_mail)


	res_group_server = search(con_group_server, data_json)
	res_group_online = search(con_group_online, data_json)
	res_group_mail = search(con_group_mail, data_json)
	# print("res_group_server :",res_group_server)
	# print("res_group_online :",res_group_online)
	# print("res_group_mail :",res_group_mail)


	res_resource_server = search(con_resource_server, data_json)
	res_resource_online = search(con_resource_online, data_json)
	res_resource_mail = search(con_resource_mail, data_json)
	# print("res_resource_server :",res_resource_server)
	# print("res_resource_online :",res_resource_online)
	# print("res_resource_mail :",res_resource_mail)

	res_user_nonemail_id = search(con_user_nonemail_id, data_json)
	res_group_nonemail_id = search(con_group_nonemail_id, data_json)
	res_resource_nonemail_id = search(con_resource_nonemail_id, data_json)

	# ------------------------------------
	# search in all.json
	#-------------------------------------
	datas = open("CuDB\\all.json","rb").read()

	data_jsons = json.loads(datas)

	con_user_a = "length(user)"
	con_group_a = "length(group)"
	con_resource_a = "length(resource)"

	con_user_a_id = "user[].sAMAccountName"
	con_group_a_id = "group[].sAMAccountName"
	con_resource_a_id = "resource[].sAMAccountName"

	res_user_a = search(con_user_a, data_jsons)
	res_group_a = search(con_group_a, data_jsons)
	res_resource_a = search(con_resource_a, data_jsons)

	res_user_a_id = search(con_user_a_id, data_jsons)
	res_group_a_id = search(con_group_a_id, data_jsons)
	res_resource_a_id = search(con_resource_a_id, data_jsons)

	# num = 0
	

	diff_all = {}
	
	diff_user = []
	diff_group = []
	diff_resource = []

	diff_user = compToListByDict(res_user_a_id, res_user_id, "sAMAccountName")
	diff_group = compToListByDict(res_group_a_id, res_group_id, "sAMAccountName")
	diff_resource = compToListByDict(res_resource_a_id, res_resource_id, "sAMAccountName")


	# --------------------------------
	# Diff 時だけには、　diff.txt 生成ます
	#---------------------------------

	if diff_user:
		diff_all["user"] = diff_user
	if diff_group:
		diff_all["group"] = diff_group
	if diff_resource:
		diff_all["resource"] = diff_resource

	if diff_all:
		if Flag == "id":
			f = open("todo-list.json","w+",encoding="utf-8")
			f.write(json.dumps(diff_all,ensure_ascii=False,indent=1))
			f.close()
		else:
			f = open("todo-list.json","w+",encoding="utf-8")
			f.write(json.dumps(diff_all,ensure_ascii=False,indent=1))
			f.close()	

	
	nonemail_all = {}
	
	nonemail_user = []
	nonemail_group = []
	nonemail_resource = []

	nonemail_user = changeJson(res_user_nonemail_id, "sAMAccountName")
	nonemail_group = changeJson(res_group_nonemail_id, "sAMAccountName")
	nonemail_resource = changeJson(res_resource_nonemail_id, "sAMAccountName")

	if nonemail_user:
		nonemail_all["user"] = nonemail_user
	if nonemail_group:
		nonemail_all["group"] = nonemail_group
	if nonemail_resource:
		nonemail_all["resource"] = nonemail_resource

	if flag_mailbox == 1:
		if nonemail_all:
			if Flag == "id":
				f = open("todo-list_nonemailbox.json","w+",encoding="utf-8")
				f.write(json.dumps(nonemail_all,ensure_ascii=False,indent=1))
				f.close()
			else:
				f = open("todo-list_nonemailbox.json","w+",encoding="utf-8")
				f.write(json.dumps(nonemail_all,ensure_ascii=False,indent=1))
				f.close()

	paths = "Report.html"

	# os.makedirs(os.path.dirname(paths), exist_ok=True)

	f = open(paths,"w+",encoding="utf-8")

	result_user = JudgeNumFixed(res_user, res_user_a)

	result_group = JudgeNumFixed(res_group, res_group_a)

	result_resource = JudgeNumFixed(res_resource, res_resource_a)

	h_content = ""
	p_content = ""

	# argv[]説明
	# ユーザ: user
	# グループ: group
	# リソース: absource

	html_argvs = []
	html_argvs.append(h_content)
	html_argvs.append(p_content)
	html_argvs.append(res_user_a)
	html_argvs.append(res_user)
	html_argvs.append(result_user)
	html_argvs.append(res_user_server)
	html_argvs.append(res_user_online)
	html_argvs.append(res_user_mail)
	html_argvs.append(res_group_a)
	html_argvs.append(res_group)
	html_argvs.append(result_group)
	html_argvs.append(res_group_server)
	html_argvs.append(res_group_online)
	html_argvs.append(res_group_mail)
	html_argvs.append(res_resource_a)
	html_argvs.append(res_resource)
	html_argvs.append(result_resource)
	html_argvs.append(res_resource_server)
	html_argvs.append(res_resource_online)
	html_argvs.append(res_resource_mail)

	# f.write(html%(h_content,p_content,res_user_a,res_user,result_user,res_user_server,res_user_online,res_user_mail,res_group_a,res_group,result_group,res_group_server,res_group_online,res_group_mail,res_resource_a,res_resource,result_resource,res_resource_server,res_resource_online,res_resource_mail))

	f.write(html%(tuple(html_argvs)))
	
	f.close()
	print("end~")


