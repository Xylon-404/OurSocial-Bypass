#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import random
import string
import time
import os
import json
import sys
import traceback
from datetime import datetime
from urllib.parse import urlparse, urljoin

# ---------- COLORS ----------
# colors
R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
C = "\033[1;96m"
P = "\033[1;95m"
RESET = "\033[0m"
###----------[ COLOUR 3]---------- ###
org = '\x1b[38;5;202m'
grn = '\033[32;1m'
red = '\033[31;1m'
A1 = '\033[1;31m'
A2 = '\033[1;32m'
A3 = '\033[1;33m'
A4 = '\033[1;34m'
A5 = '\033[1;35m'
A6 = '\033[1;36m'
A7 = '\033[1;37m'
###----------[ COLOUR 3]---------- ###
B   =  "\033[30m" 
R     =  "\033[31m" 
G   =  "\033[32m" 
YE  =  "\033[33m" 
B    =  "\033[34m" 
MA =  "\033[35m" 
CY    =  "\033[36m" 
W   =  "\033[37m" 
###----------[ COLOUR 5]---------- ###
BLACK   =  "\033[40m" 
RED     =  "\033[41m" 
GREEN   =  "\033[42m" 
###----------[ COLOUR 1]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

###----------[ COLOUR 2 ]---------- ###
Z2 = "[#000000]" # HITAM #Black
M2 = "[#FF0000]" # MERAH  #Rad
H2 = "[#00FF00]" # HIJAU #Tiya Coular
K2 = "[#FFFF00]" # KUNING #Holod
B2 = "[#00C8FF]" # BIRU #Nill
U2 = "[#AF00FF]" # UNGU #Halka Begoni
N2 = "[#FF00FF]" # PINK #Begoni
O2 = "[#00FFFF]" # BIRU MUDA #Frash
P2 = "[#FFFFFF]" # PUTIH #White
J2 = "[#FF8F00]" # JINGGA #Koyri
Y2 = "[#9FFF00]"
L2 = "[#00FFAF]"
A66 = '\x1b[1;92m\x1b[38;5;46m'
A77 = '\x1b[1;92m\x1b[38;5;47m'
A88 = '\x1b[1;92m\x1b[38;5;48m'
A99 = '\x1b[1;92m\x1b[38;5;49m'
A00 = '\x1b[1;92m\x1b[38;5;50m'

A11 = '\x1b[1;92m\x1b[38;5;208m'
A22 = '\x1b[1;92m\x1b[38;5;209m'
A33 = '\x1b[1;92m\x1b[38;5;210m'
A44 = '\x1b[1;92m\x1b[38;5;211m'
A55 = '\x1b[1;92m\x1b[38;5;212m'
# ---------- ASCII LOGO ----------

random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
url = "h"+""+"t"+""+"t"+""+"p"+""+"s"+""+":"+"/"+"/"+""+"x"+""+"y"+""+"l"+""+"o"+""+"n"+""+"."+""+"n"+""+"e"+""+"t"+""+"l"+""+"i"+""+"f"+""+"y"+""+"."+""+"a"+""+"p"+""+"p"

XALIF = f'''
\033[1;33m         _nnnn_
        dGGGGMMb     ,"""""""""""""""""""".
       @p~qp~~qMb    | \033[1;31moursocial bypass!\033[1;33m |
       M|@||@) M|   _;....................'
       @,----.JM| -'
\033[1;37m      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
\033[1;33m   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
\033[1;37m __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\033[1;33m\____   )MMMMMM|   .'
     `-'       `--' xalif

\033[0m'''

faaah =(f"{A2}⊰᯽⊱{A1}─╌{A2}⊰❊⊱{A1}╌──┈{A2}⊰᯽⊱{A3}━═━═━═━═━═━═━═━═━═━═━═━{A2}⊰᯽⊱{A1}┈──╌{A2}⊰❊⊱{A1}╌─{A2}⊰᯽⊱")

REGISTER_URL = ""
LOGIN_URL = ""
HOME_URL = ""

IMAGES_FOLDER = "./pics/"
ACCOUNTS_TO_CREATE = 0
DELAY_MIN = 3
DELAY_MAX = 7  # random delay between requests

OUTPUT_FILE = f"/storage/emulated/0/{random_name}.json"
ERROR_LOG_FILE = "/storage/emulated/0/error_log.txt"

BASE_HEADERS = {
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="148", "Android WebView";v="148", "Not/A)Brand";v="99"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "origin": "",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-BD,en-US;q=0.9,en;q=0.8",
}

COUNTRIES = [
    "Angola", "Bangladesh", "Brazil", "Canada", "China", "Egypt", "France",
    "Germany", "India", "Indonesia", "Japan", "Kenya", "Mexico", "Nigeria",
    "Pakistan", "Philippines", "Russia", "South Africa", "South Korea",
    "Spain", "Thailand", "Turkey", "Ukraine", "United Kingdom", "United States", "Vietnam"
]

# Rotating user agents to look more natural
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.101 Mobile Safari/537.36",
]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_status(msg, status="info"):
    symbols = {"info": "\033[1;32m[\033[1;31m*\033[1;32m]", "ok": "\033[1;32m[\033[1;31m✓\033[1;32m]", "fail": "\033[1;32m[\033[1;31m✗\033[1;32m]", "warn": "\033[1;32m[\033[1;31m!\033[1;32m]"}
    sym = symbols.get(status, "[*]")
    print(f"  {sym} {msg}")

def log_error(msg):
    os.makedirs(os.path.dirname(ERROR_LOG_FILE), exist_ok=True)
    with open(ERROR_LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

def rand_str(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def rand_username():
    chars = string.ascii_lowercase + string.digits + "_"
    return random.choice(string.ascii_lowercase + string.digits) + ''.join(random.choices(chars, k=9))

def rand_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com", "mail.com", "yandex.com"]
    return f"{rand_str(12)}@{random.choice(domains)}"

def rand_name():
    cons = "bcdfghjklmnpqrstvwxyz"
    vows = "aeiou"
    name = ""
    for i in range(random.randint(4, 8)):
        name += random.choice(cons if i % 2 == 0 else vows)
    return name.capitalize()

def rand_password(length=14):
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length))

def random_delay():
    delay = random.uniform(DELAY_MIN, DELAY_MAX)
    print_status(f"{A2}Waiting {A1}➢ {A4}{delay:.1f}s{A2}...", "info")
    time.sleep(delay)

def rotate_headers():
    headers = BASE_HEADERS.copy()
    headers["user-agent"] = random.choice(USER_AGENTS)
    return headers

def extract_input_values(html):
    inputs = re.findall(r'<input[^>]*name=["\']([^"\']+)["\'][^>]*value=["\']([^"\']*)["\']', html, re.IGNORECASE)
    inputs2 = re.findall(r'<input[^>]*value=["\']([^"\']*)["\'][^>]*name=["\']([^"\']+)["\']', html, re.IGNORECASE)
    result = {}
    for name, val in inputs:
        result[name] = val
    for val, name in inputs2:
        if name not in result:
            result[name] = val
    return result

def extract_csrf(html):
    csrf_match = re.search(r'name=["\']csrf_token["\'][^>]*value=["\']([a-f0-9]+)["\']', html, re.IGNORECASE)
    if csrf_match:
        return csrf_match.group(1)
    home_fields = extract_input_values(html)
    return home_fields.get('csrf_token')

def solve_captcha(html, page_name=""):
    """Extract math captcha answer from HTML."""
    # Try the "What is X + Y ?" pattern first
    match = re.search(r'What\s+is\s+(\d+)\s*([+\-*/])\s*(\d+)', html, re.IGNORECASE)
    if match:
        n1, op, n2 = int(match.group(1)), match.group(2), int(match.group(3))
        result = None
        if op == '+': result = str(n1 + n2)
        elif op == '-': result = str(n1 - n2)
        elif op == '*': result = str(n1 * n2)
        elif op == '/' and n2 != 0:
            result = str(n1 // n2) if n1 % n2 == 0 else str(round(n1 / n2, 2))
        if result:
            return result

    # Try hidden c_a and c_b fields
    fields = extract_input_values(html)
    if 'c_a' in fields and 'c_b' in fields:
        try:
            c_a = int(fields['c_a'])
            c_b = int(fields['c_b'])
            op_match = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', html)
            op = op_match.group(2) if op_match else '+'
            if op == '+': return str(c_a + c_b)
            if op == '-': return str(c_a - c_b)
            if op == '*': return str(c_a * c_b)
            if op == '/' and c_b != 0:
                return str(c_a // c_b) if c_a % c_b == 0 else str(round(c_a / c_b, 2))
            return str(c_a + c_b)
        except:
            pass

    # If we get here, captcha parsing failed
    debug_snippet = html[2000:3500] if len(html) > 2000 else html[:1500]
    print_status(f"Captcha parse failed on {page_name}", "fail")
    log_error(f"CAPTCHA_FAILED on {page_name}")
    log_error(f"Debug snippet: {debug_snippet}")
    return None

def get_random_image():
    if not os.path.isdir(IMAGES_FOLDER):
        print_status(f"Folder not found: {IMAGES_FOLDER}", "warn")
        return None

    valid_exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    images = [f for f in os.listdir(IMAGES_FOLDER) 
              if f.lower().endswith(valid_exts)]

    if not images:
        print_status("No image files found in folder", "warn")
        return None

    chosen = random.choice(images)
    return os.path.join(IMAGES_FOLDER, chosen)

def fetch_with_retry(session, url, headers, max_retries=3):
    """Fetch a page with retries."""
    for attempt in range(max_retries):
        try:
            resp = session.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp
            print_status(f"HTTP {resp.status_code} on {url}, retry {attempt+1}", "warn")
        except Exception as e:
            print_status(f"Error fetching {url}: {e}, retry {attempt+1}", "warn")
        time.sleep(2)
    return None
    
def register_account(session):
    """Register one account via referral link."""
    headers = rotate_headers()
    get_headers = {k: v for k, v in headers.items() if k != "content-type"}

    # Fetch register page
    resp = fetch_with_retry(session, REGISTER_URL, get_headers)
    if resp is None:
        print_status("Could not fetch register page after retries", "fail")
        log_error("REGISTER_PAGE_FETCH_FAILED")
        return None

    html = resp.text
    print_status(f"{A2}Page loaded {A1}➢{A4} ({len(html)} bytes)", "ok")

    # Solve captcha
    captcha_answer = solve_captcha(html, "register.php")
    if captcha_answer is None:
        print_status("Could not parse registration captcha", "fail")
        return None
    print_status(f"{A2}Captcha solved {A1}➢{A4} {captcha_answer}", "ok")

    # Generate random data
    username = rand_username()
    email = rand_email()
    first_name = rand_name()
    last_name = rand_name()
    password = rand_password()
    dob_day = str(random.randint(1, 28)).zfill(2)
    dob_month = str(random.randint(1, 12)).zfill(2)
    dob_year = str(random.randint(1980, 2005))
    country = random.choice(COUNTRIES)
    gender = random.choice(["male", "female"])

    # Extract ref code from URL
    ref_match = re.search(r'ref=([^&]+)', REGISTER_URL)
    ref_code = ref_match.group(1) if ref_match else ""

    data = {
        "ref_code": ref_code,
        "username": username,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "dob_day": dob_day,
        "dob_month": dob_month,
        "dob_year": dob_year,
        "country": country,
        "gender": gender,
        "password": password,
        "confirm_password": password,
        "captcha_answer": captcha_answer,
    }

    # Submit registration
    post_headers = {**headers, "content-type": "application/x-www-form-urlencoded",
                    "referer": REGISTER_URL,
                    "origin": urlparse(REGISTER_URL).scheme + "://" + urlparse(REGISTER_URL).netloc}

    try:
        post_resp = session.post(REGISTER_URL, headers=post_headers, data=data, timeout=30, allow_redirects=True)
    except Exception as e:
        print_status(f"POST failed: {e}", "fail")
        log_error(f"REGISTER_POST_FAILED: {e}")
        return None

    text_lower = post_resp.text.lower() if hasattr(post_resp, 'text') else ""
    final_url = post_resp.url.lower()

    # Check success indicators
    success_keywords = ["success", "account created", "welcome", "registration successful", "created successfully"]
    redirect_away = "register" not in final_url
    
    if any(kw in text_lower for kw in success_keywords) or redirect_away:
        print_status(f"{A2}Account Create! {A1}➢ {A6}{username} / {email}", "ok")
        account_info = {
            "username": username,
            "email": email,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "dob": f"{dob_year}-{dob_month}-{dob_day}",
            "country": country,
            "gender": gender,
            "ref": ref_code,
            "created_at": datetime.now().isoformat(),
            "image_posted": None,
            "status": "created"
        }
        return account_info

    # Failed — extract error message
    errors = re.findall(r'(?:error|alert|danger|msg|message|notification|warning)[^>]*>(.*?)</', post_resp.text, re.IGNORECASE | re.DOTALL)
    err_text = ""
    for e in errors[:3]:
        clean = re.sub(r'<[^>]+>', '', e).strip()
        if clean: err_text += clean + " "

    if not err_text:
        clean_text = re.sub(r'<[^>]+>', ' ', post_resp.text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        err_text = clean_text[:200]

    print_status(f"Registration failed: {err_text.strip()}", "fail")
    log_error(f"REGISTER_FAILED: {err_text.strip()} | user={username}")
    return None


def login_and_post_image(session, username, password, image_path):
    """Login and post image to the home feed."""
    headers = rotate_headers()
    get_headers = {k: v for k, v in headers.items() if k != "content-type"}

    # Get login page
    login_page_url = LOGIN_URL + "?redirect_to=home"
    resp = fetch_with_retry(session, login_page_url, get_headers)
    if resp is None:
        print_status("Could not fetch login page", "warn")
        return False

    html = resp.text
    fields = extract_input_values(html)

    login_data = {}
    login_data['redirect_to'] = fields.get('redirect_to', 'home')
    if 'c_a' in fields:
        login_data['c_a'] = fields['c_a']
    if 'c_b' in fields:
        login_data['c_b'] = fields['c_b']

    captcha_answer = solve_captcha(html, "login.php")
    if captcha_answer:
        login_data['captcha_answer'] = captcha_answer

    login_data['username'] = username
    login_data['password'] = password

    post_headers = {**headers, "content-type": "application/x-www-form-urlencoded",
                    "referer": LOGIN_URL,
                    "origin": urlparse(LOGIN_URL).scheme + "://" + urlparse(LOGIN_URL).netloc}

    try:
        login_resp = session.post(LOGIN_URL, headers=post_headers, data=login_data, timeout=30, allow_redirects=True)
    except Exception as e:
        print_status(f"Login POST failed: {e}", "warn")
        return False

    # Check if logged in by fetching home
    home_resp = fetch_with_retry(session, HOME_URL, get_headers)
    if home_resp is None:
        return False

    current_url = home_resp.url
    if "login" in current_url.lower():
        print_status("Still on login page — login failed", "warn")
        return False

    print_status("Logged in!", "ok")

    # Get CSRF from home page
    html = home_resp.text
    csrf_token = extract_csrf(html)

    if not csrf_token:
        print_status("Could not find CSRF token on home page", "warn")
        log_error(f"CSRF_NOT_FOUND for user={username}")
        return False

    print_status(f"CSRF token found", "ok")

    # Post image
    if not os.path.exists(image_path):
        print_status(f"Image not found: {image_path}", "warn")
        return False

    with open(image_path, "rb") as f:
        image_data = f.read()

    image_name = os.path.basename(image_path)
    boundary = "----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    body = ""
    body += f"--{boundary}\r\n"
    body += 'Content-Disposition: form-data; name="csrf_token"\r\n\r\n'
    body += f"{csrf_token}\r\n"

    body += f"--{boundary}\r\n"
    body += 'Content-Disposition: form-data; name="post_privacy"\r\n\r\n'
    body += "public\r\n"

    body += f"--{boundary}\r\n"
    body += 'Content-Disposition: form-data; name="post_content"\r\n\r\n'
    body += "\r\n"

    body += f"--{boundary}\r\n"
    body += f'Content-Disposition: form-data; name="post_image"; filename="{image_name}"\r\n'
    body += 'Content-Type: image/jpeg\r\n\r\n'

    body_bytes = body.encode('utf-8') + image_data + f"\r\n--{boundary}--\r\n".encode('utf-8')

    post_headers = {
        **headers,
        "content-type": f"multipart/form-data; boundary={boundary}",
        "referer": HOME_URL,
        "origin": urlparse(HOME_URL).scheme + "://" + urlparse(HOME_URL).netloc,
    }

    try:
        post_resp = session.post(HOME_URL, headers=post_headers, data=body_bytes, timeout=60, allow_redirects=True)
    except Exception as e:
        print_status(f"Image upload failed: {e}", "warn")
        return False

    # Check success
    if post_resp.status_code in [301, 302, 303, 200]:
        final_url = post_resp.url.lower()
        text_lower = post_resp.text.lower() if hasattr(post_resp, 'text') else ""
        
        success_keywords = ["success", "posted", "shared", "photo", "image"]
        redirect_home = "home" in final_url or "index" in final_url
        
        if any(kw in text_lower for kw in success_keywords) or redirect_home:
            return True

    print_status(f"Post response: HTTP {post_resp.status_code}", "warn")
    return False

def main():
    clear_screen()
    print(XALIF)
    print(faaah)
    
    # Global variables to modify
    global REGISTER_URL, LOGIN_URL, HOME_URL, ACCOUNTS_TO_CREATE, DELAY_MIN, DELAY_MAX, IMAGES_FOLDER
    
    # --- GET USER INPUT ---

    while True:
        ref_input = input(f"\n{A1}  ⃝     {A6}Enter Refer URL {A2}✒ {A6}✒ {A3} ").strip()
        if ref_input:
            # Normalize the URL
            if not ref_input.startswith("http"):
                ref_input = "https://" + ref_input
            
            # Parse it
            parsed = urlparse(ref_input)
            base = f"{parsed.scheme}://{parsed.netloc}"
            
            REGISTER_URL = ref_input
            LOGIN_URL = f"{base}/login.php"
            HOME_URL = f"{base}/home"
            print(f'{A22}')
            print_status(f"{G}REGISTER {A2}⌯⌲ {A22} {REGISTER_URL}", "info")
            print_status(f"{G}LOGIN {A2}⌯⌲ {A22} {LOGIN_URL}", "info")
            print_status(f"{G}HOME {A2}⌯⌲ {A22} {HOME_URL}", "info")
            break
        else:
            print_status("URL cannot be empty!", "warn")
    
    # Account count
    while True:
        try:
            count_input = input(f"\n{A1}  ⃝     {A6}Enter Account create amount {A2}✒ {A6}✒ {A3} ").strip()
            ACCOUNTS_TO_CREATE = int(count_input)
            if ACCOUNTS_TO_CREATE > 0:
                break
            else:
                print_status("Enter a positive number!", "warn")
        except ValueError:
            print_status("Enter a valid number!", "warn")
    
    # Images folder
    folder_input = input(f"\n{A2}〔{A1}➤{A2}〕{A6} Images folder {A2}[{A1}{IMAGES_FOLDER}{A2}] {A2}•{A3}•{A4}•{A1} ").strip()
    if folder_input:
        IMAGES_FOLDER = folder_input
    
    if not os.path.isdir(IMAGES_FOLDER):
        print_status(f"Warning: Folder '{IMAGES_FOLDER}' not found. Creating...", "warn")
        try:
            os.makedirs(IMAGES_FOLDER, exist_ok=True)
        except:
            print_status("Cannot create folder. Check path.", "warn")
            if input("  [?] Continue anyway? (y/n): ").lower() != 'y':
                print_status("Exiting...", "warn")
                return
    
    # Print summary
    print('')
    print(f"{A2}─────────{A1}୨ৎ{A2}─────────")
    print(f"{A1}📊 CONFIGURATION SUMMARY{A1}")
    print(f"{A2}─────────{A1}୨ৎ{A2}─────────")
    print(f"{G}REFERAL URL {A2}⌯⌲ {A22} {REGISTER_URL}")
    print(f"{R}AMOUNTS {A2}⌯⌲ {A22} {ACCOUNTS_TO_CREATE}")
    print(f"{P}IMAGE FOLDER {A2}⌯⌲ {A22} {IMAGES_FOLDER}")
    print(f"{C}OUTPUT FILE {A2}⌯⌲ {A22} {OUTPUT_FILE}")
    print(f"{Y}ERROR LOG {A2}⌯⌲ {A22} {ERROR_LOG_FILE}")
    print(f"{A2}─────────{A1}୨ৎ{A2}─────────")
    
    

    # Confirm start
    start_input = input(f"\n🚀 {A6}Start Attack (y/n) {A6}➤{A3}").strip().lower()
    if start_input != 'y':
        print_status("Cancelled by user.", "warn")
        return
    
    print()
    print(f"{A2}─────────{A1}୨ৎ{A2}─────────")
    print(f"{A2}  STARTING ACCOUNT CREATION")
    print(f"{A2}─────────{A1}୨ৎ{A2}─────────\n")
    
    # --- ENSURE OUTPUT DIRS ---
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    # Load existing accounts
    all_accounts = []
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f:
                all_accounts = json.load(f)
            print_status(f"{A6}Loaded {A1}{len(all_accounts)}{A6} existing accounts", "info")
        except:
            all_accounts = []
    
    start_from = len(all_accounts) + 1
    created = len(all_accounts)
    failed = 0
    consecutive_failures = 0
    
    start_time = time.time()
    
    for i in range(start_from, ACCOUNTS_TO_CREATE + 1):
        elapsed = time.time() - start_time
        rate = i / elapsed if elapsed > 0 else 0
        
        print(f"\n{A2}─────────────────────{A1}୨ৎ{A2}─────────────────────")
        print(f" {A2} Account{A6} {i}/{ACCOUNTS_TO_CREATE} | {A2}Elapsed{A6} {elapsed:.0f}s | {A2}Rate{A6} {rate:.2f}/min")
        print(f"{A2}─────────────────────{A1}୨ৎ{A2}─────────────────────")
        
        image_path = get_random_image()
        if not image_path:
            print_status("No images available. Stopping.", "fail")
            break
        
        image_name = os.path.basename(image_path)
        print_status(f"{A2}Image{A1} ➢{A4} {image_name}", "info")
        
        sess = requests.Session()
        
        try:
            account = register_account(sess)
            if account is None:
                failed += 1
                consecutive_failures += 1
                print_status(f"Total fails: {failed}", "info")
                
                # If we fail multiple times consecutively, wait longer
                if consecutive_failures >= 5:
                    print_status(f"{consecutive_failures} consecutive failures — waiting 30s (possible rate limit)...", "warn")
                    time.sleep(30)
                    consecutive_failures = 0
                else:
                    random_delay()
                continue
            
            # Reset fail counter on success
            consecutive_failures = 0
            
            username = account['username']
            password = account['password']
            
            # Login + post image
            post_success = login_and_post_image(sess, username, password, image_path)
            
            if post_success:
                account['image_posted'] = image_name
                account['status'] = "posted"
                print_status("Image posted successfully!", "ok")
            else:
                account['status'] = "post_failed"
                print_status("Image post failed", "fail")
            
            all_accounts.append(account)
            created += 1
            
            # Save JSON after each
            with open(OUTPUT_FILE, 'w') as f:
                json.dump(all_accounts, f, indent=2)
            
            print_status(f"Saved {A1}➢ {A4}({created}/{ACCOUNTS_TO_CREATE})", "ok")
        
        except Exception as e:
            print_status(f"Exception: {e}", "fail")
            log_error(f"EXCEPTION at account {i}: {e}")
            traceback.print_exc()
            failed += 1
            consecutive_failures += 1
        
        if i < ACCOUNTS_TO_CREATE:
            random_delay()
    
    # --- FINAL REPORT ---
    elapsed = time.time() - start_time
    posted = sum(1 for a in all_accounts if a.get('status') == 'posted')
    
    print(f"\n{A2}─────────────────────{A1}୨ৎ{A2}─────────────────────")
    print(f"  {A2}DONE! ({elapsed:.0f}s elapsed)")
    print(f"{A2}─────────────────────{A1}୨ৎ{A2}─────────────────────")
    print(f"  {A3}Total created:  {created}")
    print(f"  {A3}With post:      {posted}")
    print(f"  {A1}Failed:         {failed}")
    print(f"  {A3}Output:         {OUTPUT_FILE}")
    print(f"{A1}  Error log:      {ERROR_LOG_FILE}")
    print(f"{A2}─────────────────────{A1}୨ৎ{A2}─────────────────────")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  [!] Interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n  [!] Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
