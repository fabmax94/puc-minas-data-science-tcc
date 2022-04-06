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
  resposta_parser = BeautifulSoup(resposta.text, "html.parser")
  tabela_parser = resposta_parser.find("table", {"id": "cphMasterMain_cphMain_lblSingleID"})

  problemas = []
  for tr in tabela_parser.find_all("tr", {"class": "spec_issue"}):
      problemas.append({
          "title": tr.find("span", {"class": "title_issue"}).text,
          "device": tr.find("span", {"class": "device_issue"}).text,
          "os_version": tr.find("span", {"class": "os_version_issue"}).text,
          "problem": tr.find("span", {"class": "problem_description_issue"}).text,
          "category": tr.find("span", {"class": "category_issue"}).text,
          "register_date": tr.find("span", {"class": "register_date_issue"}).text,
          "resolved_date": tr.find("span", {"class": "resolved_date_issue"}).text,
          "resolved_by": tr.find("span", {"class": "resolved_by_issue"}).text,
          "cause": tr.find("span", {"class": "cause_issue"}).text,
          "resolution": tr.find("span", {"class": "resolution_issue"}).text,
      })

  open("/home/fabio.silva/dados/problemas.json", "w").write(json.dumps(problemas))
  
if __name__ == "__main__":
  coleta_projetos()
  coleta_bug()
