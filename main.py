# 55555 นายเก่งจริงนายทำเอง
import requests as XMLHttpRequest
import os
import random
from bs4 import BeautifulSoup as bs
import webbrowser

def home_process():
	os.system("clear")
	data = XMLHttpRequest.get("https://www.test-like.com/login_v2").text
	getdata = bs(data, "html.parser")
	usercode = getdata.find("input", attrs={"id": "user-code"})['value']
	session = getdata.find("button", attrs={"id": "btn-verify-login"})['onclick'][14:46]
	# สิ้นสุดการดึงข้อมูล
	linkverify = "https://fb.com/device?user_code=" + usercode
	print(" คำเตือน : การปั้มติดตามจะต้องล็อกอินเฟสที่ต้องการจะปั้มเท่านั้น! มีสิทธิ์เฟซล็อกได้เนื่องจากนี่เป็นระบบไลค์แลกไลค์ หากเกิดปัญหาทางเราจะไม่รับผิดชอบทุกกรณีเนื่องจากทางเราได้ระบุไว้แล้ว กรุณาใช่อย่างระมัดระวังจาก GENIX SHOP")
	print()
	print("     USER-CODE :", usercode)
	print()
	webbrowser.open(linkverify)
	print("  [1] Continue")
	print("  [2] Exit")
	print()
	print(" Enter the options")
	r = input("--> ")
	print()
	if r == "1" or r == "01":
		resp = XMLHttpRequest.get(f"https://www.test-like.com/ajax/verifyLogin?code={session}",headers={"cookie": "_ga=GA1.1.1386408812.1683443150;PHPSESSID=rumabjgd9rk8arku41thkh6q85;_ga_BM8KH05M50=GS1.1.1683461030.2.1.1683461051.0.0.0","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"})
		if (resp.status_code == 200):
			cookies = resp.headers['set-cookie'][:25]
			os.system("clear")
			print("     AUTO FOLLOWS BY TEST-LIKE.COM | GENIX SHOP")
			print()
			loop = True
			color_list = ['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[00m']
			while loop:
				pb = random.choice(color_list)
				req = XMLHttpRequest.post("https://www.test-like.com/ajax/follows",headers={"cookie": "_ga=GA1.1.1386408812.1683443150;PHPSESSID=rumabjgd9rk8arku41thkh6q85;{cookies};_ga_BM8KH05M50=GS1.1.1683461030.2.1.1683461168.0.0.0","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"})
				# code200 {"success": true,"message": "ประสบความสำเร็จ 2! เวลา 1","type": "success","like_sucess": 2,"error": 8,"next": "2023/05/07 19:42:55"}
				status = req.json()['success']
				if (status == True):
					total_follows = req.json()['like_sucess']
					print(f"   [+] SEND FOLLOWS TOTAL {total_follows} SUCCESS !")
				else:
					print(f"   {pb}[-] ตอนนี้คุณไม่สามารถปั๊มได้เนื่องจากติดคูลดาวน์ กรุณารอสักครู่...\033[00m", end="\r")
		else:
			print(" [-] ไม่สามารถล็อกอินได้ !")
	else:
		print(" [-] GET OUT PROGRAMS SUCCESS !")
		exit()
	# code200 {"success": "true","type": "success","message": "เข้าสู่ระบบสำเร็จแล้ว!!!","action": "location.reload();"}
	# code400 login failed
	
home_process()
