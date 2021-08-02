class Proxy:
    def __init__(self):
        self.proxy={
            "http"  : "192.168.100.178:80",
            "https" : "192.168.100.178:80"
        }
        self.user="fabio.pedrosa"
        self.password="Fab%403lau"
        self.proxy_string = 'http://fabio.pedrosa:Fab%403lau@192.168.100.178:80'
