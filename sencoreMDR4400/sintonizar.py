import http.client, http.cookiejar, urllib, json, time

cookie_name_list = []
cookie_value_list = []

def sintonizar(multicast, interface, puerto) -> dict: 

    cookies = http.cookiejar.CookieJar()
    cookie_processor = urllib.request.HTTPCookieProcessor(cookies)
    opener = urllib.request.build_opener(cookie_processor)
    urllib.request.install_opener(opener)

    url = "http://10.177.18.228/webservice.fcgi"
    data = urllib.parse.urlencode({"action": "csf.login", "user": "admin", "pass": ""}).encode("utf-8")
    request = urllib.request.Request(url, data = data)
    response = opener.open(request)
    for cookie in cookies:
        cookie_name_list.append(cookie.name)
        cookie_value_list.append(cookie.value)
    cookie_name = str(cookie_name_list[0] + "=" + cookie_value_list[0])
    cookie_value = str(cookie_name_list[1] + "=" + cookie_value_list[1])
    ready_cookie = str(cookie_name + ";" + " " + cookie_value)

    multicast = multicast
    port = puerto
    interface = interface

    url = "IRD-IP-ADDRESS" #Put the IP address of your SENCORE MDR4400 Here
    conn = http.client.HTTPConnection(url)
    payload = "action=csf.txn&params=%7B%22ops%22%3A%5B%7B%22label%22%3A%22tsinputsrcState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%221%22%7D%2C%7B%22label%22%3A%22mpegiprcvNic%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%221%22%7D%2C%7B%22label%22%3A%22mpegiprcvStreamMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%221%22%7D%2C%7B%22label%22%3A%22mpegiprcvDestinationIp%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%22239.77.16.153%22%7D%2C%7B%22label%22%3A%22mpegiprcvPort%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A8999%7D%2C%7B%22label%22%3A%22mpegiprcvFecState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvInternalSourceFilterState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvIgmpFilterMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvNullStrippedState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvSsrcFilterState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvSsrcFilterValue%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A0%7D%2C%7B%22label%22%3A%22mpegiprcvBufferMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvBufferSize%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A400%7D%2C%7B%22label%22%3A%22mpegiprcvBufferDelayTarget%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A150%7D%2C%7B%22label%22%3A%22mpegiprcvCounterResetMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvCounterResetInterval%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A600%7D%2C%7B%22label%22%3A%22mpegipigmpRowStatus%22%2C%22inst%22%3A%22.1.2.2.1.1.4." + interface +"%22%2C%22val%22%3A%226%22%7D%5D%7D"
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8", "cookie": ready_cookie}
    conn.request("POST", "/webservice.fcgi", body=payload ,headers=headers)
    ans = conn.getresponse()
    #print(f"Solicitud aceptada: {ans.status} - {ans.reason}")

    conn = http.client.HTTPConnection(url)
    payload = "action=csf.txn&params=%7B%22ops%22%3A%5B%7B%22label%22%3A%22tsinputsrcState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%221%22%7D%2C%7B%22label%22%3A%22mpegiprcvNic%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%221%22%7D%2C%7B%22label%22%3A%22mpegiprcvStreamMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%221%22%7D%2C%7B%22label%22%3A%22mpegiprcvDestinationIp%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%22"+ multicast + "%22%7D%2C%7B%22label%22%3A%22mpegiprcvPort%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A" + port + "%7D%2C%7B%22label%22%3A%22mpegiprcvFecState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvInternalSourceFilterState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvIgmpFilterMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvNullStrippedState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvSsrcFilterState%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvSsrcFilterValue%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A0%7D%2C%7B%22label%22%3A%22mpegiprcvBufferMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvBufferSize%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A400%7D%2C%7B%22label%22%3A%22mpegiprcvBufferDelayTarget%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A150%7D%2C%7B%22label%22%3A%22mpegiprcvCounterResetMode%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A%222%22%7D%2C%7B%22label%22%3A%22mpegiprcvCounterResetInterval%22%2C%22inst%22%3A%22.1.2.2.1%22%2C%22val%22%3A600%7D%2C%7B%22label%22%3A%22mpegipigmpRowStatus%22%2C%22inst%22%3A%22.1.2.2.1.1.4." + interface +"%22%2C%22val%22%3A%224%22%7D%5D%7D"
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8", "cookie": ready_cookie}
    conn.request("POST", "/webservice.fcgi", body=payload ,headers=headers)
    ans = conn.getresponse()
    #print(f"Solicitud aceptada: {ans.status} - {ans.reason}")
    #data = ans.read()
    #print(json.loads(data))    Answer's breakpoint check
    time.sleep(20)

    conn = http.client.HTTPConnection(url)
    headers = {"Content-type": "text/html; charset=UTF-8", "cookie": ready_cookie}
    conn.request("GET", 'webservice.fcgi?action=csf.stores&_dc=1726237066472&params={"filter":["AncDecoder","AncOpt","AudioPidLock","AsiIn","AsiIo","AudioSrv","AvSsConfig","Genlock","HdAspectRatio","HdGenlock","HdSdi","Input","MpegIpCard","MpegIpRcv","MpegIpInternalFilter","MpegIpTx","MpegIpTxFec","Overlay","PidLock","SdAspectRatio","SdGenlock","SdSdi","SdiAudio","SelectedAudio","SelectedService","ServiceLock","ServiceSelection","Timecode","TsInputSrc","TsOutputSrc","Video","VideoOutput","Audio","TsSsConfig","VideoOutputGenlock","Mpe","MpeMac","VideoSync","Unit"],"revision":450896,"firstInst":"0","maxRows":0}', headers=headers)
    ans = conn.getresponse()
    #print(f"Solicitud aceptada: {ans.status} - {ans.reason}")
    data = ans.read()
    data_json = json.loads(data)
    conn.close()
    return data_json
