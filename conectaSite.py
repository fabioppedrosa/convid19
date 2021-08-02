import requests
from requests.auth import HTTPProxyAuth
import zipfile
import io
from proxy import Proxy


class ConectaSite:
    def __init__(self,url,diretorio_local):
        p=Proxy()
        s = requests.Session()
        #s.proxies = {"http": p.proxy_string , "https": p.proxy_string}
        s.auth = HTTPProxyAuth(p.user,p.password)
        self.saida=1

        try:
            print("Conectando")
#            req = (str(s.get(url,proxies=s.proxies)))[11:]
            req = (str(s.get(url)))[11:]
            if req.count("200") == 1:
                print("Conexão realizada com sucesso")
                #r = s.get(url,proxies=s.proxies)
                r = s.get(url)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(path = diretorio_local )
                print("Download finalizado com sucesso: ",url)
            else:
                print("Arquivo indisponível: ",url)
                self.saida=0
        except Exception as e:
            print("Erro..: ",e)
            self.saida=0