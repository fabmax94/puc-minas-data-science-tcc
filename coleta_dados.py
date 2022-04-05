import json
import requests
from bs4 import BeautifulSoup


def coleta_projetos():
  DATA_INICIO = "2017-01-01"
  DATA_FIM = "2022-01-01"
  header = {
      'Accept': 'text/html, application/xhtml+xml, */*',
      'User-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2',
      'Content-Type': 'application/x-www-form-urlencoded'
  }
  API = f"http://<SISTEMA_INTERNO>/projects?sd={DATA_INICIO}&ed={DATA_FIM}"

  resposta = requests.get(API).json()

  open("/home/fabio.silva/dados/projetos.json", "w").write(json.dumps(projetos))


def coleta_bug():
  DATA_INICIO = "2017/01/01"
  DATA_FIM = "2022/01/01"
  URL = f"http://<SISTEMA_INTERNO>/issueGripd/listPage?start={DATA_INICIO}&end={DATA_FIM}"

  resposta = requests.get(URL)
  resposta_parser
