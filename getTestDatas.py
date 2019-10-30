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
import xlrd
# import datetime
from datetime import datetime
import time


CON = {
	"1" : "追加",
	"2" : "変更",
	"3" : "削除"
}

def modify_MT_UserRsrcAcntInfo_case(patho, paths):
	tableName = "MT_UserRsrcAcntInfo"
	ID = "000001"#getMMDDH()
	# NO = getYYMMDDHS()
	msg = {
		"user":[{
			"userID":"UB10%s"%ID,
			"logonID":"UserUB-%s"%ID,
			"EmpNo":"M1500",
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
			"userID":"UB20%s"%ID,
			"logonID":"UserUB2-%s"%ID,
			"EmpNo":"M2500",
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
			"userID":"UF90%s"%ID,
			"logonID":"UserUF-%s"%ID,
			"EmpNo":"J9500",
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
			"userID":"UT80%s"%ID,
			"logonID":"UserUT-%s"%ID,
			"EmpNo":"x8500",
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
		},{
			"userID":"UB11000003",
			"logonID":"UserUB-000003",
			"EmpNo":"M1100",
			"UserSector":"0",
			"MainDptName":"（GrpAcntSInfo）_社員",
			"DispName":"山田太郎(かわばたやすなり)",
			"FamilyName":"山田",
			"Name":"太郎",
			"KanaName":"yamataran",
			"AlphabetName":"やまだたろん",
			"StructureCode":"A_10",
			"TitleCode":"101",
			"HITOID":"08938293"
		},{
			"userID":"UB12000004",
			"logonID":"UserUB-000004",
			"EmpNo":"SX120",
			"UserSector":"0",
			"MainDptName":"（MBXPermissionInfoo）_社員",
			"DispName":"高橋藤原(たかほしふじくん)",
			"FamilyName":"高橋",
			"Name":"藤原",
			"KanaName":"takahosifujikun",
			"AlphabetName":"たかほしふじくん",
			"StructureCode":"A_10",
			"TitleCode":"102",
			"HITOID":"10138293"
		},{
			"userID":"UF91000004",
			"logonID":"UserUF-000004",
			"EmpNo":"SX120",
			"UserSector":"9",
			"MainDptName":"（MBXPermissionInfoo）_特殊ユーザー",
			"DispName":"高橋浩志(たかほしほしじん)",
			"FamilyName":"高橋",
			"Name":"浩志",
			"KanaName":"takahosihosijin",
			"AlphabetName":"たかほしほしじん",
			"StructureCode":"A_10",
			"TitleCode":"103",
			"HITOID":"110000004"
		},{
			"userID":"UB13000005",
			"logonID":"UserUB-000005",
			"EmpNo":"JM130",
			"UserSector":"0",
			"MainDptName":"（AccountAttributeReflect）_社員",
			"DispName":"福島溜池(ふくやまためさし)",
			"FamilyName":"福島",
			"Name":"溜池",
			"KanaName":"fukuyamatamesasi",
			"AlphabetName":"ふくやまためさし",
			"StructureCode":"A_10_23",
			"TitleCode":"104",
			"HITOID":"879000005"
		}],
		"resource":[{
			"resourceID":"RR10%s"%ID,
			"logonID":"rsrc-01",
			"RsrcSector":"010",
			"DispName":"0001会議室",
			"Password":"rr4321*"
		# },{
		# 	"resourceID":"RB00010001",
		# 	"logonID":"b-resource-01",
		# 	"RsrcSector":"020",
		# 	"DispName":"備品会議室",
		# 	"Password":"rb2431+"
		# },{
		# 	"resourceID":"RS00010001",
		# 	"logonID":"s-resource",
		# 	"RsrcSector":"030",
		# 	"DispName":"共有スケジュール会議室",
		# 	"Password":"rs1234#"
		},{
			"resourceID":"RB10000003",
			"logonID":"RsRB-000003",
			"RsrcSector":"020",
			"DispName":"0002備品会議室",
			"Password":"suijiRew"
		},{
			"resourceID":"RS10000004",
			"logonID":"RsRS-000004",
			"RsrcSector":"030",
			"DispName":"共有スケジュール会議室",
			"Password":"mbxPermission&%"
		},{
			"resourceID":"RX10000004",
			"logonID":"RsRX-000004",
			"RsrcSector":"010",
			"DispName":"0005会議室",
			"Password":"kaigisitu"
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
	len_user = len(msg["user"])
	len_resource = len(msg["resource"])
	lens = len_user + len_resource
	
	for jk in CON:
		# 追加 1
		if jk == "1":
			DATAS = []
			for i in range(0, lens):
				if i < len_user:
					NO = getYYMMDDHS()
					print("NO:",i)
					copy_con = copy(con_dict)
					copy_con["TrunsactNo"] = "%s"%NO
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
					copy_con["AfterCommandDate"] = getYYYYMMDD(1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["AfterArrivalDate"] = getYYYYMMDD(2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["AfterRetireDate"] = getYYYYMMDD(3)
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
					copy_con["AfterHITOID"] = msg["user"][i]["HITOID"]
					
					copy_con["UseToFileShareChangeSector"] = "1"
					copy_con["AfterUseToFileShare"] = "0"
					copy_con["UseToMBXChangeSector"] = "1"
					copy_con["AfterUseToMBX"] = "0"
					copy_con["UseToSkype4bChangeSector"] = "1"
					copy_con["AfterUseToSkype4b"] = "0"
					DATAS = []
					DATAS.append(copy_con)
					saveByNameAndUser(tableName, CON[jk], paths, DATAS,msg["user"][i]["userID"])
					#time.sleep(1)

				else:
					copy_con = copy(con_dict)
					j = i - len_user
					NO = getYYMMDDHS()
					print("NO:",j)
					copy_con["TrunsactNo"] = "%s"%NO
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
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][j]["logonID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["CommandDateChangeSector"] = jk
					copy_con["AfterCommandDate"] = getYYYYMMDD(1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["AfterArrivalDate"] = getYYYYMMDD(2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["AfterRetireDate"] = getYYYYMMDD(3)
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
					copy_con["AfterLogOnId"] = msg["resource"][j]["logonID"]
					copy_con["HITOIDChangeSector"] = jk
					# copy_con["AfterHITOID"] = "1010100%d"%i
					DATAS = []
					DATAS.append(copy_con)
					saveByNameAndUser(tableName, CON[jk], paths, DATAS,msg["resource"][j]["resourceID"])
					#time.sleep(1)

			# saveByName(tableName, CON[jk], paths, DATAS)

		elif jk == "2":
			DATAS = []
			for i in range(0, lens):
				if i < len_user:
					NO = getYYMMDDHS()
					#print("NO:",NO)
					copy_con = copy(con_dict)
					copy_con["TrunsactNo"] = "%s"%NO
					copy_con["RegistationDate"] = getCurDate()
					copy_con["UserId"] = msg["user"][i]["userID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["EmpNoChangeSector"] = jk
					copy_con["BeforeEmpNo"] = msg["user"][i]["EmpNo"]
					copy_con["AfterEmpNo"] = msg["user"][i]["EmpNo"]
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["user"][i]["DispName"]
					copy_con["AfterDispName"] = msg["user"][i]["DispName"]+"(改)"
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["BeforeFamilyName"] = msg["user"][i]["FamilyName"]
					copy_con["AfterFamilyName"] = msg["user"][i]["FamilyName"]+"(改)"
					copy_con["NameChangeSector"] = jk
					copy_con["BeforeName"] = msg["user"][i]["Name"]
					copy_con["AfterName"] = msg["user"][i]["Name"]+"(改)"
					copy_con["KanaNameChangeSector"] = jk
					copy_con["BeforeKanaName"] = msg["user"][i]["KanaName"]
					copy_con["AfterKanaName"] = msg["user"][i]["KanaName"]+"(kai)"
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["BeforeAlphabetName"] = msg["user"][i]["AlphabetName"]
					copy_con["AfterAlphabetName"] = msg["user"][i]["AlphabetName"]+"(かい)"
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["BeforeCompanyName"] = "御茶ノ水　ソフト日本"
					copy_con["AfterCompanyName"] = "御茶ノ水　ソフト日本(改)"
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["BeforeMainDptName"] = msg["user"][i]["MainDptName"]
					copy_con["AfterMainDptName"] = msg["user"][i]["MainDptName"]+"(改)"
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["BeforeMainSectGrpName"] = "(株)IT グループ"
					copy_con["AfterMainSectGrpName"] = "(株)IT グループ(改)"
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["BeforeWorkplaceName"] = "御茶ノ水"
					copy_con["AfterWorkplaceName"] = "御茶ノ水(改)"
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"],msg["user"][i]["logonID"])
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"],msg["user"][i]["logonID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["BeforeTitleName"] = "仕事の人"
					copy_con["AfterTitleName"] = "仕事の人(改)"
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["BeforeExLineNo"] = "045-336-688%d"%i
					copy_con["AfterExLineNo"] = "020-336-000%d"%i
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["BeforeExtentionNo"] = "82718%d"%i
					copy_con["AfterExtentionNo"] = "80000%d"%i
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["BeforeStructureCode"] = msg["user"][i]["StructureCode"]
					copy_con["AfterStructureCode"] = msg["user"][i]["StructureCode"]+",A_20"
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["BeforeTitleCode"] = msg["user"][i]["TitleCode"]
					copy_con["AfterTitleCode"] = msg["user"][i]["TitleCode"]+",0100"
					copy_con["CommandDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD(1)
					copy_con["AfterCommandDate"] = getYYYYMMDD(-1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["BeforeArrivalDate"] = getYYYYMMDD(2)
					copy_con["AfterCommandDate"] = getYYYYMMDD(-2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["BeforeRetireDate"] = getYYYYMMDD(3)
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
					copy_con["BeforeInetUse"] = "%d"%(i%3)
					copy_con["AfterInetUse"] = "%d"%((i+1)%3)
					copy_con["VLANPassWordChangeSector"] = jk
					copy_con["BeforeVLANPassWord"] = "134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["AfterVLANPassWord"] = "202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["md4PassWordChangeSector"] = jk
					copy_con["Beforemd4PassWord"] = "{md4}134402E37B7C2D4E9DB1EDD5BD36589E"
					copy_con["Aftermd4PassWord"] = "{md4}202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["BeforeLogOnId"] = msg["user"][i]["logonID"]
					copy_con["AfterLogOnId"] = msg["user"][i]["logonID"]
					copy_con["HITOIDChangeSector"] = jk
					copy_con["BeforeHITOID"] = msg["user"][i]["HITOID"]
					copy_con["AfterHITOID"] = msg["user"][i]["HITOID"]

					copy_con["UseToFileShareChangeSector"] = jk
					copy_con["BeforeUseToFileShare"] = "0"
					copy_con["AfterUseToFileShare"] = "1"
					copy_con["UseToMBXChangeSector"] = jk
					copy_con["BeforeUseToMBX"] = "0"
					copy_con["AfterUseToMBX"] = "1"
					copy_con["UseToSkype4bChangeSector"] = jk
					copy_con["BeforeUseToSkype4b"] = "0"
					copy_con["AfterUseToSkype4b"] = "1"
					DATAS = []
					DATAS.append(copy_con)
					saveByNameAndUser(tableName, CON[jk], paths, DATAS,msg["user"][i]["userID"])
					#time.sleep(1)

				else:
					copy_con = copy(con_dict)
					j = i - len_user
					NO = getYYMMDDHS()
					#print("NO:",NO)
					copy_con["TrunsactNo"] = "%s"%NO
					copy_con["RegistationDate"] = getCurDate()
					copy_con["ResourceCode"] = msg["resource"][j]["resourceID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["BeforeRsrcSector"] = msg["resource"][j]["RsrcSector"]
					copy_con["AfterRsrcSector"] = "020"
					copy_con["EmpNoChangeSector"] = jk
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["resource"][j]["DispName"]
					copy_con["AfterDispName"] = msg["resource"][j]["DispName"]+"(改)"
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["NameChangeSector"] = jk
					copy_con["KanaNameChangeSector"] = jk
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][j]["logonID"])
					copy_con["AfterMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][j]["logonID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["StructureCodeChangeSector"] = jk
					copy_con["TitleCodeChangeSector"] = jk
					copy_con["CommandDateChangeSector"] = jk
					copy_con["BeforeCommandDate"] = getYYYYMMDD(1)
					copy_con["AfterCommandDate"] = getYYYYMMDD(-1)
					copy_con["ArrivalDateChangeSector"] = jk
					copy_con["BeforeArrivalDate"] = getYYYYMMDD(2)
					copy_con["AfterArrivalDate"] = getYYYYMMDD(-2)
					copy_con["RetireDateChangeSector"] = jk
					copy_con["BeforeRetireDate"] = getYYYYMMDD(3)
					copy_con["AfterRetireDate"] = getYYYYMMDD(-3)
					copy_con["GALDispFlgChangeSector"] = jk
					copy_con["BeforeGALDispFlg"] = "%d"%(j%3)
					copy_con["AfterGALDispFlg"] = "%d"%((j+1)%3)
					copy_con["GALDispOrderChangeSector"] = jk
					copy_con["BeforeGALDispOrder"] = "0"
					copy_con["AfterGALDispOrder"] = "20"
					copy_con["MemoChangeSector"] = jk
					copy_con["BeforeMemo"] = msg["resource"][j]["DispName"]
					copy_con["AfterMemo"] = msg["resource"][j]["DispName"]+"(改)"
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
					copy_con["BeforeLogOnId"] = msg["resource"][j]["logonID"]
					copy_con["AfterLogOnId"] = msg["resource"][j]["logonID"]
					copy_con["HITOIDChangeSector"] = jk
					# copy_con["AfterHITOID"] = "1010100%d"%i
					DATAS = []
					DATAS.append(copy_con)
					saveByNameAndUser(tableName, CON[jk], paths, DATAS,msg["resource"][j]["resourceID"])
					#time.sleep(1)

				# saveByName(tableName, CON[jk], paths, DATAS)
		else:
			DATAS = []
			for i in range(0, lens):
				if i < len_user:
					NO = getYYMMDDHS()
					#print("NO:",NO)
					copy_con = copy(con_dict)
					copy_con["TrunsactNo"] = "%s"%NO
					copy_con["RegistationDate"] = getCurDate()
					copy_con["UserId"] = msg["user"][i]["userID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["EmpNoChangeSector"] = jk
					copy_con["BeforeEmpNo"] = msg["user"][i]["EmpNo"]
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["user"][i]["DispName"]+"(改)"
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["BeforeFamilyName"] = msg["user"][i]["FamilyName"]+"(改)"
					copy_con["NameChangeSector"] = jk
					copy_con["BeforeName"] = msg["user"][i]["Name"]+"(改)"
					copy_con["KanaNameChangeSector"] = jk
					copy_con["BeforeKanaName"] = msg["user"][i]["KanaName"]+"(kai)"
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["BeforeAlphabetName"] = msg["user"][i]["AlphabetName"]+"(かい)"
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["BeforeCompanyName"] = "御茶ノ水　ソフト日本(改)"
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["BeforeMainDptName"] = msg["user"][i]["MainDptName"]+"(改)"
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["BeforeMainSectGrpName"] = "(株)IT グループ(改)"
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["BeforeWorkplaceName"] = "御茶ノ水(改)"
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp;%s@nri.co.jp"%(msg["user"][i]["logonID"],msg["user"][i]["logonID"])
					copy_con["TitleNameChangeSector"] = jk
					copy_con["BeforeTitleName"] = "仕事の人(改)"
					copy_con["ExLineNoChangeSector"] = jk
					copy_con["BeforeExLineNo"] = "020-336-000%d"%i
					copy_con["ExtentionNoChangeSector"] = jk
					copy_con["BeforeExtentionNo"] = "80000%d"%i
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
					copy_con["BeforeInetUse"] = "%d"%((i+1)%3)
					copy_con["VLANPassWordChangeSector"] = jk
					copy_con["BeforeVLANPassWord"] = "202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["md4PassWordChangeSector"] = jk
					copy_con["Beforemd4PassWord"] = "{md4}202DD139D7B8DFB3ACD460193F01BB0A"
					copy_con["UserSector"] = msg["user"][i]["UserSector"]
					copy_con["LogOnIdChangeSector"] = jk
					copy_con["BeforeLogOnId"] = msg["user"][i]["logonID"]
					copy_con["HITOIDChangeSector"] = jk
					copy_con["BeforeHITOID"] = msg["user"][i]["HITOID"]

					copy_con["UseToFileShareChangeSector"] = jk
					copy_con["BeforeUseToFileShare"] = "1"
					copy_con["UseToMBXChangeSector"] = jk
					copy_con["BeforeUseToMBX"] = "1"
					copy_con["UseToSkype4bChangeSector"] = jk
					copy_con["BeforeUseToSkype4b"] = "1"
					DATAS = []
					DATAS.append(copy_con)
					saveByNameAndUser(tableName, CON[jk], paths, DATAS,msg["user"][i]["userID"])
					#time.sleep(1)

				else:
					copy_con = copy(con_dict)
					j = i - len_user
					NO = getYYMMDDHS()
					#print("NO:",NO)
					copy_con["TrunsactNo"] = "%s"%NO
					copy_con["RegistationDate"] = getCurDate()
					copy_con["ResourceCode"] = msg["resource"][j]["resourceID"]
					copy_con["ChangeSector"] = jk	# 追加
					copy_con["RsrcSectChangeSector"] = jk
					copy_con["BeforeRsrcSector"] = "020"
					copy_con["EmpNoChangeSector"] = jk
					copy_con["DispNameChangeSector"] = jk
					copy_con["BeforeDispName"] = msg["resource"][j]["DispName"]+"(改)"
					copy_con["FamilyNameChangeSector"] = jk
					copy_con["NameChangeSector"] = jk
					copy_con["KanaNameChangeSector"] = jk
					copy_con["AlphabetNameChangeSector"] = jk
					copy_con["CompanyNameChangeSector"] = jk
					copy_con["MainDptNameChangeSector"] = jk
					copy_con["MainSectGrpNameChangeSector"] = jk
					copy_con["WorkplaceNameChangeSector"] = jk
					copy_con["MailAddressChangeSector"] = jk
					copy_con["BeforeMailAddress"] = "%s@cub3.nri.co.jp"%(msg["resource"][j]["logonID"])
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
					copy_con["BeforeMemo"] = msg["resource"][j]["DispName"]+"(改)"
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
					copy_con["BeforeLogOnId"] = msg["resource"][j]["logonID"]
					copy_con["HITOIDChangeSector"] = jk
					# copy_con["AfterHITOID"] = "1010100%d"%i
					DATAS = []
					DATAS.append(copy_con)
					saveByNameAndUser(tableName, CON[jk], paths, DATAS,msg["resource"][j]["resourceID"])
					#time.sleep(1)

				# saveByName(tableName, CON[jk], paths, DATAS)

def modify_MT_GrpAcntInfo_case(patho, paths):
	tableName = "MT_GrpAcntInfo"
	ID = "000002" #getMMDDH()
	# NO = getYYMMDDHS()

	msg = [{
		"OrganizCode":"SB10%s"%ID,
		"SecGrpCode":"A_10_%s"%ID,
		"SecGrpName":"(東京大学大学院)"
	},{
		"OrganizCode":"SB11000003",
		"SecGrpCode":"GrpSB-000003",
		"SecGrpName":"(任意共有グループ)"
	},{
		"OrganizCode":"FL10000003",
		"SecGrpCode":"A_80_55_10",
		"SecGrpName":"(MT_GrpAcntSInfo)グループ"
	},{
		"OrganizCode":"SX10000004",
		"SecGrpCode":"GrpSX-000004",
		"SecGrpName":"(MT_MBXPermissionInfo)グループ"
	}]
		
	con_dict = openFile(patho, tableName)
	# print([x for x in con_dict])
	lens = len(msg)

	for jk in CON:
		# 追加 1
		if jk == "1":
			DATAS = []
			for i in range(0,lens):
				NO = getYYMMDDHS()
				#print("NO:",NO)
				copy_con = copy(con_dict)
				copy_con["TrunsactNo"] = "%s"%NO
				copy_con["RegistationDate"] = getCurDate()
				copy_con["OrganizCode"] = msg[i]["OrganizCode"]
				copy_con["ChangeSector"] = jk
				copy_con["SecGrpCodeChangeSector"] = jk
				copy_con["BeforeSecGrpCode"] = msg[i]["SecGrpCode"]
				copy_con["AfterSecGrpCode"] = msg[i]["SecGrpCode"]
				copy_con["SecGrpNameChangeSector"] = jk
				copy_con["AfterSecGrpName"] = msg[i]["SecGrpName"]
				copy_con["SecGrpExplnChangeSector"] = jk
				copy_con["AfterSecGrpExpln"] = "（Groupグループ）"
				copy_con["MailAddressChangeSector"] = jk
				copy_con["AfterMailAddress"] = "%s@cu.nri.co.jp"%msg[i]["SecGrpCode"]
				copy_con["GALDispFlgChangeSector"] = jk
				copy_con["AfterGALDispFlg"] = i%3
				copy_con["GALDisplayOrderChangeSector"] = jk
				copy_con["AfterGALDisplayOrder"] = "333222"
				DATAS = []
				DATAS.append(copy_con)
				saveByNameAndUser(tableName, CON[jk], paths, DATAS, msg[i]["OrganizCode"])
				#time.sleep(1)

			# saveByName(tableName, CON[jk], paths, DATAS)

		elif jk == "2":#変更 2
			DATAS = []
			for i in range(0,lens):
				NO = getYYMMDDHS()
				copy_con = copy(con_dict)
				#print("NO:",NO)
				copy_con["TrunsactNo"] = "%s"%NO
				copy_con["RegistationDate"] = getCurDate()
				copy_con["OrganizCode"] = msg[i]["OrganizCode"]
				copy_con["ChangeSector"] = jk
				copy_con["SecGrpCodeChangeSector"] = jk
				copy_con["BeforeSecGrpCode"] = msg[i]["SecGrpCode"]
				copy_con["AfterSecGrpCode"] = msg[i]["SecGrpCode"]
				copy_con["SecGrpNameChangeSector"] = jk
				copy_con["BeforeSecGrpName"] = msg[i]["SecGrpName"]
				copy_con["AfterSecGrpName"] = msg[i]["SecGrpName"]+"(改)"
				copy_con["SecGrpExplnChangeSector"] = jk
				copy_con["BeforeSecGrpExpln"] = "（Groupグループ）"
				copy_con["AfterSecGrpExpln"] = "（Groupグループ）(改)"
				copy_con["MailAddressChangeSector"] = jk
				copy_con["BeforeMailAddress"] = "%s@cu.nri.co.jp"%msg[i]["SecGrpCode"]
				copy_con["AfterMailAddress"] = "%s@cu.nri.co.jp"%msg[i]["SecGrpCode"]
				copy_con["GALDispFlgChangeSector"] = jk
				copy_con["BeforeGALDispFlg"] = i%3
				copy_con["AfterGALDispFlg"] = (i+1)%3
				copy_con["GALDisplayOrderChangeSector"] = jk
				copy_con["BeforeGALDisplayOrder"] = "333222"
				copy_con["AfterGALDisplayOrder"] = "111111"
				DATAS = []
				DATAS.append(copy_con)
				saveByNameAndUser(tableName, CON[jk], paths, DATAS, msg[i]["OrganizCode"])
				#time.sleep(1)

			# saveByName(tableName, CON[jk], paths, DATAS)
		else:#削除 3
			DATAS = []
			for i in range(0,lens):
				NO = getYYMMDDHS()
				#print("NO:",NO)
				copy_con = copy(con_dict)
				copy_con["TrunsactNo"] = "%s"%NO
				copy_con["RegistationDate"] = getCurDate()
				copy_con["OrganizCode"] = msg[i]["OrganizCode"]
				copy_con["ChangeSector"] = jk
				copy_con["SecGrpCodeChangeSector"] = jk
				copy_con["BeforeSecGrpCode"] = msg[i]["SecGrpCode"]
				copy_con["AfterSecGrpCode"] = msg[i]["SecGrpCode"]
				copy_con["SecGrpNameChangeSector"] = jk
				copy_con["BeforeSecGrpName"] = msg[i]["SecGrpName"]+"(改)"
				copy_con["SecGrpExplnChangeSector"] = jk
				copy_con["BeforeSecGrpExpln"] = "（Groupグループ）(改)"
				copy_con["MailAddressChangeSector"] = jk
				copy_con["BeforeMailAddress"] = "%s@cu.nri.co.jp"%msg[i]["SecGrpCode"]
				copy_con["GALDispFlgChangeSector"] = jk
				copy_con["BeforeGALDispFlg"] = (i+1)%3
				copy_con["GALDisplayOrderChangeSector"] = jk
				copy_con["BeforeGALDisplayOrder"] = "111111"
				DATAS = []
				DATAS.append(copy_con)
				saveByNameAndUser(tableName, CON[jk], paths, DATAS, msg[i]["OrganizCode"])
				#time.sleep(1)
			# saveByName(tableName, CON[jk], paths, DATAS)

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
	ID = "000003" #getMMDDH()
	# NO = getYYMMDDHS()
	# MT_GrpAcntSInfoで使用したユーザーやグループやリソース　全て存在した
	msg = {
		"OrganizCode":"SB11%s"%ID,
		"SecGrpCode":"GrpSB-%s"%ID,
		"SecGrpName":"(東京大学大学院)"
	}
	datas = [{
		"ID":"UB11%s"%ID,
		"logonID":"UserUB-%s"%ID,
		"AflOrgSector":"0"
	},{
		"ID":"FL10%s"%ID,
		"logonID":"A_80_55_10",
		"AflOrgSector":"1"
	},{
		"ID":"RB10%s"%ID,
		"logonID":"RsRB-%s"%ID,
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
				NO = getYYMMDDHS()
				#print("NO:",NO)
				MT_GrpAcntSInfo_value_change(copy_con, "%s"%NO, getCurDate(), msg["OrganizCode"], msg["SecGrpCode"], jk, \
					datas[i]["AflOrgSector"], datas[i]["ID"], datas[i]["logonID"])

				DATAS = []
				DATAS.append(copy_con)
				saveByNameAndUser(tableName, CON[jk], paths, DATAS, datas[i]["ID"])
				#time.sleep(1)
			# saveByName(tableName, CON[jk], paths, DATAS)
		else:#削除
			# DATAS = []
			for i in range(0,lens):
				NO = getYYMMDDHS()
				#print("NO:",NO)
				copy_con = copy(con_dict)

				MT_GrpAcntSInfo_value_change(copy_con, "%s"%NO, getCurDate(), msg["OrganizCode"], msg["SecGrpCode"], jk, \
					datas[i]["AflOrgSector"], datas[i]["ID"], datas[i]["logonID"])

				DATAS = []
				DATAS.append(copy_con)
				saveByNameAndUser(tableName, CON[jk], paths, DATAS, datas[i]["ID"])
				#time.sleep(1)

			# saveByName(tableName, CON[jk], paths, DATAS)

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
	ID = "000005" #getMMDDH()
	# NO = getYYMMDDHS()

	msg = [{
		"ValueName":"ext-Mail",
		"Value":"b-tanaka-01@nri.co.jp",
		"LogOnId":"UserUB-%s"%ID
	},{
		"ValueName":"personid",
		"Value":"222111",
		"LogOnId":"UserUB-%s"%ID
	},{
		"ValueName":"ext-addressBookMail",
		"Value":"f-tanaka-01-change@i-tech.nri.co.jp",
		"LogOnId":"UserUB-%s"%ID
	}]
		
	con_dict = openFile(patho, tableName)
	lens = len(msg)
	# DATAS = []	# when all data to one json
	for i in range(0,lens):
		DATAS = []	# when 別にjsonを保存するとき
		copy_con = copy(con_dict)
		NO = getYYMMDDHS()
		#print("NO:",NO)
		MT_AccountAttributeReflect_value_change(copy_con,"%s"%NO, getYYYYMMDD(), msg[i]["ValueName"], msg[i]["Value"], msg[i]["LogOnId"])
		DATAS.append(copy_con)
		saveByNameAndUser(tableName, "", paths, DATAS, msg[i]["ValueName"])
		#time.sleep(1)

	# saveByName(tableName, "", paths, DATAS)

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
	ID = "000004" #getMMDDH()
	# NO = getYYMMDDHS()
	msg = [{
			"UserIdRsrcCd":"UB12%s"%ID,
			"logonID":"UserUB-%s"%ID,
		},{
			"UserIdRsrcCd":"RS10%s"%ID,
			"logonID":"RsRS-%s"%ID,
		}]
	datas = {
		"user":[{
			"UserIdRsrcCd":"UF91%s"%ID,
			"SecGrpCd":"UserUF-%s"%ID,
			"MBXSector":"06"
		# },{
		# 	"UserIdRsrcCd":"RB00010001",
		# 	"SecGrpCd":"b-resource-01",
		# 	"MBXSector":"07"
		# },{
		# 	"UserIdRsrcCd":"SB00010001",
		# 	"SecGrpCd":"b-database",
		# 	"MBXSector":"08"
		}],
		"resource":[{
			"UserIdRsrcCd":"RX10%s"%ID,
			"SecGrpCd":"RsRX-%s"%ID,
			"MBXSector":"00"
		# },{
		# 	"UserIdRsrcCd":"RS00010001",
		# 	"SecGrpCd":"s-resource",
		# 	"MBXSector":"01"
		# },{
		# 	"UserIdRsrcCd":"SF00010002",
		# 	"SecGrpCd":"A_80_55",
		# 	"MBXSector":"02"
		}],
		"group":[{
			"UserIdRsrcCd":"SX10%s"%ID,
			"SecGrpCd":"GrpSX-%s"%ID,
			"MBXSector":"02"
		}]
	}
		
	con_dict = openFile(patho, tableName)
	lens = len(msg)	# +1は既定選択肢のため
	# print(lens)
	len_user = len(datas["user"])	#ユーザーの数
	len_resource = len(datas["resource"])	#リソースの数
	len_group = len(datas["group"])
	# sum = 0	#TrunsactNoの違う
	for jk in CON:
		# 追加 1
		sum = 0
		if jk == "1":
			DATAS = []
			for i in range(0,lens):
				if i == 0:# user
					for j in range(0,len_user):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)
						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], datas["user"][j]["MBXSector"], msg[i]["logonID"])
						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["user"][j]["UserIdRsrcCd"])
						#time.sleep(1)
					for j in range(0,len_resource):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], datas["resource"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["resource"][j]["UserIdRsrcCd"])
						sum = sum +1
						#time.sleep(1)
					for j in range(0, len_group):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["group"][j]["UserIdRsrcCd"], datas["group"][j]["SecGrpCd"], datas["group"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["group"][j]["UserIdRsrcCd"])
						#time.sleep(1)
				if i == 1:# resource
					for j in range(0,len_user):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)
						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], datas["user"][j]["MBXSector"], msg[i]["logonID"])
						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["user"][j]["UserIdRsrcCd"])
						#time.sleep(1)
					for j in range(0,len_resource):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], datas["resource"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["resource"][j]["UserIdRsrcCd"])
						sum = sum +1
						#time.sleep(1)
					for j in range(0, len_group):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["group"][j]["UserIdRsrcCd"], datas["group"][j]["SecGrpCd"], datas["group"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["group"][j]["UserIdRsrcCd"])
						#time.sleep(1)
				
				# else:#既定
			DATAS = []
			NO = getYYMMDDHS()
			#print("NO:",NO)
			MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[1]["UserIdRsrcCd"], "1", \
					"", "", "03", msg[1]["logonID"])
			DATAS.append(copy_con)
			sum = sum +1
			saveByNameAndUser(tableName, CON[jk], paths, DATAS, "noting")
			#time.sleep(1)

			# saveByName(tableName, CON[jk], paths, DATAS)

		elif jk == '2':
			DATAS = []
			for i in range(0,lens):
				if i == 0:# user
					for j in range(0,len_user):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], "04", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["user"][j]["UserIdRsrcCd"])
						#time.sleep(1)

					for j in range(0,len_resource):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], "05", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["resource"][j]["UserIdRsrcCd"])
						#time.sleep(1)
					for j in range(0, len_group):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["group"][j]["UserIdRsrcCd"], datas["group"][j]["SecGrpCd"], datas["group"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["group"][j]["UserIdRsrcCd"])
				DATAS = []
				NO = getYYMMDDHS()
				#print("NO:",NO)
				MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[1]["UserIdRsrcCd"], "1", \
						"", "", "08", msg[1]["logonID"])
				DATAS.append(copy_con)
				sum = sum +1
				saveByNameAndUser(tableName, CON[jk], paths, DATAS, "noting")		#time.sleep(1)
				# else:
				# 	copy_con = copy(con_dict)
				# 	MT_MBXPermissionInfo_value_change(copy_con, "52%s%d"%(NO,sum), getCurDate(), jk, msg[i%2]["UserIdRsrcCd"], "1", \
				# 			"", "", "10", msg[i%2]["logonID"])
				# 	DATAS.append(copy_con)
				# 	sum = sum +1

				# 	saveByNameAndUser(tableName, CON[jk], paths, DATAS, msg[i%2]["UserIdRsrcCd"])
			# saveByName(tableName, CON[jk], paths, DATAS)
			if i == 1:# resource
					for j in range(0,len_user):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], "04", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["user"][j]["UserIdRsrcCd"])
						#time.sleep(1)

					for j in range(0,len_resource):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], "05", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["resource"][j]["UserIdRsrcCd"])
						#time.sleep(1)
					for j in range(0, len_group):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["group"][j]["UserIdRsrcCd"], datas["group"][j]["SecGrpCd"], datas["group"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["group"][j]["UserIdRsrcCd"])

		else:
			DATAS = []
			copy_con = copy(con_dict)
			for i in range(0,lens):
				copy_con = copy(con_dict)
				if i == 0:# user
					for j in range(0,len_user):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], "04", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["user"][j]["UserIdRsrcCd"])
						#time.sleep(1)
					for j in range(0,len_resource):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], "05", msg[i]["logonID"])

						DATAS.append(copy_con)
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["resource"][j]["UserIdRsrcCd"])
						sum = sum +1
						#time.sleep(1)
					for j in range(0, len_group):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["group"][j]["UserIdRsrcCd"], datas["group"][j]["SecGrpCd"], datas["group"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXUser", CON[jk], paths, DATAS, datas["group"][j]["UserIdRsrcCd"])
				if i == 1:# resource
					for j in range(0,len_user):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"],"0", \
							 datas["user"][j]["UserIdRsrcCd"], datas["user"][j]["SecGrpCd"], "04", msg[i]["logonID"])

						DATAS.append(copy_con)
						sum = sum +1
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["user"][j]["UserIdRsrcCd"])
						#time.sleep(1)
					for j in range(0,len_resource):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["resource"][j]["UserIdRsrcCd"], datas["resource"][j]["SecGrpCd"], "05", msg[i]["logonID"])

						DATAS.append(copy_con)
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["resource"][j]["UserIdRsrcCd"])
						sum = sum +1
						#time.sleep(1)
					for j in range(0, len_group):
						DATAS = []
						NO = getYYMMDDHS()
						#print("NO:",NO)
						copy_con = copy(con_dict)

						MT_MBXPermissionInfo_value_change(copy_con, "%s"%NO, getCurDate(), jk, msg[i]["UserIdRsrcCd"], "0", \
							datas["group"][j]["UserIdRsrcCd"], datas["group"][j]["SecGrpCd"], datas["group"][j]["MBXSector"], msg[i]["logonID"])
						
						DATAS.append(copy_con)
						saveByNameAndUser("MBXRes", CON[jk], paths, DATAS, datas["group"][j]["UserIdRsrcCd"])
						#time.sleep(1)
				# else:#既定
				# 	copy_con = copy(con_dict)
					
				# 	MT_MBXPermissionInfo_value_change(copy_con, "53%s%d"%(NO,sum), getCurDate(), jk, msg[i%2]["UserIdRsrcCd"], "1", \
				# 			"", "", "10", msg[i%2]["logonID"])

				# 	DATAS.append(copy_con)
				# 	saveByNameAndUser(tableName, CON[jk], paths, DATAS, msg[i%2]["UserIdRsrcCd"])
				# 	sum = sum +1

			# saveByName(tableName, CON[jk], paths, DATAS)

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
		f.write(json.dumps(items,ensure_ascii=False,indent=2))

def saveByNameAndUser(tableName, fileName, paths, datas, user):
	"save modify file to path by name"
	items = {}
	items["tableName"] = tableName
	items["items"] = datas
	path_s = os.path.join(paths, "%s_%s_%s.json"%(tableName,fileName,user))

	with open(path_s,"w+",encoding="utf-8") as f:
		f.write(json.dumps(items,ensure_ascii=False,indent=2))

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
	"2019-10-01 10:13:14.123"
	# from time import gmtime, strftime
	nowtime = datetime.now()

	# newtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	newtime = nowtime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	# newtime = nowtime.strftime('%Y/%m/%d %H:%M:%S')
	return newtime
	# return "{{Date.yyyy-MM-dd HH:mm:ss.fff}}"
def getYYMMDDHS():
	"2019-10-01 10:13:14"
	nowtime = datetime.now()
	newtime = nowtime.strftime('%Y%m%d%H%M%S')
	return newtime
	# return "{{Date.yyyyMMddHHmmss}}"

def getYYYYMMDD(n=0):
	"20191001"
	import datetime
	# from time import gmtime, strftime
	nowtime = datetime.datetime.now() + datetime.timedelta(days=n)

	# newtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	# newtime = nowtime.strftime('%Y-%m-%d %H:%M:%S.%f%z')
	newtime = nowtime.strftime('%Y%m%d')
	return newtime
	# return "{{Date.yyyyMMdd}}"

def getMMDDH():
	nowtime = datetime.now()
	newtime = nowtime.strftime('%m%d%H')
	return newtime

def getMDHS():
	nowtime = datetime.now()
	newtime = nowtime.strftime('%m%d%H%M%S%f')
	return newtime

def randomNum(n=8):
	"random number"
	import random
	strs = ""
	for x in range(0,n):
		strs = strs+str(random.randint(1,9))
	return strs

def getDataFromExcel(fileName):
	"xlrd: read"
	"xlwt: write"
	"xlutils: read or write"
	excel_handle = xlrd.open_workbook(fileName)
	excel_name = excel_handle.sheet_names()
	for name in excel_name:
		sheet = excel_handle.sheet_by_name[name]
		print(sheet)

if __name__ == '__main__':
	print("--------------------------------------------")
	
	# time = "ddd"
	# url1 = "https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_%s_1/"%time
	# Token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImFQY3R3X29kdlJPb0VOZzNWb09sSWgydGlFcyIsImtpZCI6ImFQY3R3X29kdlJPb0VOZzNWb09sSWgydGlFcyJ9.eyJhdWQiOiJodHRwczovL2lkbS1hcGkuY3ViMy5ucmkuY28uanAvIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNmM5MzE0MTItNzZiMi00ZGRjLWI0NTItZGVmNjgxNWFkNmFiLyIsImlhdCI6MTU2OTkwNDI4NSwibmJmIjoxNTY5OTA0Mjg1LCJleHAiOjE1Njk5MDgxODUsImFjciI6IjEiLCJhaW8iOiJBVlFBcS84TUFBQUFxZkFOYnZzamVJK3hoQnpTcVFXVEFVNVZHNVVzcGgvcVRhQ0N3WlA5RkErbEY1WCtuenNwWFJVTG95SzdPejF5d0JKTzltM3ArT1JtOUt5dU1URVR6eVRLVFFyekNyUkhJcklhWkZFV0FQTT0iLCJhbXIiOlsicHdkIiwibWZhIl0sImFwcGlkIjoiOGE3ZTEyZDItZGZmYS00MzY3LThkOGEtMDBkMzdiNzMxMGMyIiwiYXBwaWRhY3IiOiIwIiwiaXBhZGRyIjoiMzYuMy44NC4xMjYiLCJuYW1lIjoi6LaZ44CA5p2wKGR3cCkiLCJvaWQiOiIxMDcyOGEwOS1iYTY3LTRjYWUtYjAyYi04MmM4OTgyNGM3MTciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjc3Mjg3MjE3Ni0yNDYzNTMxODI0LTM1NTY0OTIzMjQtMTA5NjEyIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiM0ZmSnU5blpQMll3bnF2a0VySVJ4WDVxMUowT0Zyam9KbC10YzZBcnpDZyIsInRpZCI6IjZjOTMxNDEyLTc2YjItNGRkYy1iNDUyLWRlZjY4MTVhZDZhYiIsInVuaXF1ZV9uYW1lIjoidG9uMDAwMDctZHdwQGN1YjMubnJpLmNvLmpwIiwidXBuIjoidG9uMDAwMDctZHdwQGN1YjMubnJpLmNvLmpwIiwidXRpIjoiam9xVG5Sc3d0MFctY3VKS3R1NFNBQSIsInZlciI6IjEuMCJ9.Gsg99IWSr1QKsEqMfFvXwANvnhEXrI0pIQCjiJw9mWwEMwDNcTzjC8nKjCHmkRw6rMTfjQNC3EHcFUOYHfX4oYG_u8SIJxtrdO4H5my2vrETUpK0jAV-0TAMOfmksskeUWzEb6x8MnYPTQlUaNIs2k_Bi18QBYrK-QVIIR1U0xCThlR5IRqJvTcz2EbokGvkJ9RNLrskGLhIYegpj7GmVW0yYbNorGJ8ESuRDHPca_XNHVd4Jly-OVaAyS1iah-rFj-s85INaMPaleYucN2LDbdzojYkKM_9aLW5gYfr4_7Op9JW2sc3vU7Q2PoeMe9Mg8PsZsdnPBJzmzQnxjT0ew"
	# token = Token if "Token" in globals() else getAccessToken()

	# getDiffData(token)
	# --------------------------------------------------------------------------------------------
	#	read file and modify sensitive message,then save
	#
	# PATHO = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Original"
	# PATHS = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Modify"
	# PATHSC = "C:\\Users\\liaga\\株式会社トップワンテック\\IDM - 04.テスト\\PH2.テストケース\\データ準備\\Modify_Case"
	# PATHOC = "C:\\Users\\liaga\\株式会社トップワンテック\\toponetec - ドキュメント\\96.personal\\ligaigai\\PH2.テストケース\\Sample"
	# patho = PATHO if "PATHO" in globals() else os.path.abspath(os.path.dirname(__file__))
	# paths = PATHS if "PATHS" in globals() else os.path.abspath(os.path.dirname(__file__))
	paths_c = PATHSC if "PATHSC" in globals() else os.path.abspath(os.path.dirname(__file__))
	patho_c = PATHOC if "PATHOC" in globals() else os.path.abspath(os.path.dirname(__file__))
	# --------------------------------------------------------------------------------------------
	# --------------------------------------------------------------------------------------------
	# modify_MT_UserRsrcAcntInfo_case(patho_c, paths_c)
	# modify_MT_GrpAcntInfo_case(patho_c, paths_c)
	# modify_MT_GrpAcntSInfo_case(patho_c, paths_c)
	# modify_MT_MBXPermissionInfo_case(patho_c, paths_c)
	# modify_MT_AccountAttributeReflect_case(patho_c, paths_c)
	# print(patho, paths)
	# --------------------------------------------------------------------------------------------
	print(getYYMMDDHS())
	# #time.sleep(1)
	print(getCurDate())
	print(getYYYYMMDD())
	print("----end----")
