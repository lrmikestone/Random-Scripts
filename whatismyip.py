#!/usr/bin/python3

import requests
import yaml
import socket
import urllib3

urllib3.disable_warnings()
#logging.captureWarnings(True)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)

    try:
        s.connect(("192.168.0.1", 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = "Unable to determine local IP"
    finally:
        s.close()

    return local_ip

local_ip = get_local_ip()

ip_addr = requests.get("https://icanhazip.com/4", verify=False).text.strip()
parsed_data = yaml.safe_load(requests.get("https://ipinfo.io/" + ip_addr, verify=False).text.strip())

city = parsed_data['city'].strip()
country = parsed_data['country'].strip()

print(f"\n🏡 Intranet IP: {local_ip}")
print(f"💻 Internet IP: {ip_addr}")
print(f"🌎 Location: {city}, {country}\n")
