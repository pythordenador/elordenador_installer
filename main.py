import os, json
from elordenador_lib import parser
from clint.textui import progress
import sys
import requests
print("Welcome to my Toolbox")
if sys.argv[1] == "install":
    print("Downloading DB...")
    r = requests.get("https://pythordenador.github.io/elordenador_installer/db.json", stream=True)
    path = 'db.json'
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
    with open(path,"rb") as f:
        f = json.load(f)
        url = parser.replace(f[sys.argv[2]]["url"], f[sys.argv[2]]["version"],"<version>")
        r = requests.get(url, stream=True)
        path = 'pkg.tar.gz'
        with open(path, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
    os.system("pip install pkg.tar.gz")
    os.system("rm db.json pkg.tar.gz")
