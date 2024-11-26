
import requests,bs4,json,os,sys,random,time,re,webbrowser
import urllib3,rich,base64
from cfonts import render, say

webbrowser.open('https://t.me/Svvd9')
id = [] 
Bes_Tok = [] 
uid = []
ses=requests.Session()
logo = render('File', colors=['white', 'green'], align='center')
cook = render('File', colors=['white', 'yellow'], align='center')

Bes_Red = '\033[1;31m'
Bes_Yell = '\033[1;33m'
Bes_Green = '\033[1;32m' 
Bes_Bl = '\033[1;34m'
Bes_White = '\033[0;97m'

def clear():
    os.system('clear')


def login():
	try:
		clear()
		print(cook)
		cookie = input(f'{Bes_White} حط كوكيز ')
		open("/sdcard/HMODE/File_Ids/.cok.txt", "w").write(cookie)
		with requests.Session() as HMODE:
			try:
			
				HMODE.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = HMODE.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open("/sdcard/HMODE/File_Ids/.token.txt", "w").write(token)
					print(f"{Bes_Green} - Login Done √ {Bes_White}") 
				else:
					print(f'{Bes_Yellow} - Failed To Login ! ')
			except:
				print(f'{Bes_Red} - Failled To Get Token ! ')
		time.sleep(2)
		menu()
	except Exception as e:
		os.system("rm -f /sdcard/HMODE/File_Ids/.token.txt")
		os.system("rm -f /sdcard/HMODE/File_Ids/.cok.txt")
		print(f'{Bes_White} - Cookies Not Found')
		exit()
		
#------------------[ @SHIMUL خالدالمشهوري ]----------------#
def menu():
	try:
		token = open('/sdcard/HMODE/File_Ids/.token.txt','r').read()
		cok = open('/sdcard/HMODE/File_Ids/.cok.txt','r').read()
	except IOError:
		print(f'{Bes_White} - Cookies Not Found')
		time.sleep(2)
		login()
	os.system('clear')
	print(logo)
	
	print(f'(1-)makefile(صنع ملف)')
	print(f'')
	print('(2-) Delete duplicate(حذف المكرر) ')
	Bes_H = input(f' ➪ ' )
	if Bes_H in ['1']:
		Bes_Menu_1()
	elif Bes_H in ['2']:
		Bes_Rev()
	elif Bes_H in ['0']:
		os.system('rm -rf /sdcard/HMODE/File_Ids/.token.txt')
		os.system('rm -rf /sdcard/Bes/Bes_Login/.cookie.txt')
		print(f'{Bes_Yellow} - Cookies Was Deleted Done √ ')
		exit()
	else:
		print(f'{Bes_Red} - Choice Incorrect ')
		exit()
		

def Bes_Menu_1():
	os.system('clear');print(logo)
	try:
		token = open('/sdcard/HMODE/File_Ids/.token.txt','r').read()
		cok = open('/sdcard/HMODE/File_Ids/.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		Bes_File = input('file Name ')
		Bes_Tota_Id = int(input(f' ID (عدد الايديات)'))
		# ادا كان شيء غلط ب عدد
	except ValueError:
	    exit()
	
	if Bes_Tota_Id<1 or Bes_Tota_Id>1000:
	    exit()
	ses=requests.Session()
	
	id_number = 0
	for Bes_H_H in range(Bes_Tota_Id):
		id_number+=1
		Enter_id = input(f' ID  📟 '+str(id_number)+' : ')
		uid.append(Enter_id)
	for user in uid:
	    try:
			
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
	       if len(id) == 0:
	           params = ({'access_token': token,'fields': "friends"})
	       else:
	           params = ({'access_token': token,'fields': "friends"})
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for HMODE in url['friends']['data']:
	           try:

	               HMODE_H = (HMODE['id']+'|'+HMODE['name']);open(f'%s'%(Bes_File),'a').write(HMODE['id']+'|'+HMODE['name']+'\n')
	               if HMODE_H in id:pass
	               else:id.append(HMODE_H)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print('');print(f"{Bes_White} ID   "+str(len(id))) 
	      print(f'  file name  🗃 {Bes_Green}{Bes_File}{Bes_White}')
	      time.sleep(5);menu()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

def Bes_Rev():
    try:
        os.system('clear');print(logo)
        print('')
        filename = input(' - File : ')
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        lines = sorted(set(lines))
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        print('')
        print(f'{Bes_Green} - Done Delete Doubles Ids ')
        print(f'{Bes_White} - Saved As Same File {Bes_Green}[{filename}]')
        exit()
    except:
    	print(' - Not Found a Doubles Ids ');exit()


if __name__=='__main__':
	try:os.mkdir("/sdcard/HMODE")
	except:pass
	try:os.mkdir("/sdcard/HMODE/HMODE_H")
	except:pass
	try:os.mkdir("/sdcard/HMODE/File_Ids")
	except:pass
	login()
	
	