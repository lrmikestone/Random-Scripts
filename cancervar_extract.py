import requests

URLVAL = "http://cancervar.wglab.org/api_new.php?queryType=position&build=hg19&chr=14&pos=105241994&ref=G&alt=A"

response = requests.get(URLVAL)

if response.status_code == 200:
    json_data = response.json()
    cancer_string = json_data.get('Cancervar')
    split_string = cancer_string.split('#')

    intpart = int(split_string[0])
    stringpart = str(split_string[1])

    print (f"Int value: {intpart}")
    print (f"The rest: {stringpart}")
else:
    print(f"Well, something got fucked up: {response.status_code}")
