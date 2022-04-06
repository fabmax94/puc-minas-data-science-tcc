import pandas as pd
import nltk
import json

STOP_WORDS_ENGLISH = nltk.corpus.stopwords.words('english')
STOP_WORDS_REQUIREMENT = ['behavior', 'reproduce', 'up', 'set', 'on', 'dut', 'starting', 'expected', 'first', 'call',
                          'same', 'as', 'carrier', 'you', 'it', 'that', 'applied', 'to', 'for', 'change', 'when',
                          'requirement', 'second', 'steps', 'be', 'must', 'is', 'according', '3.', 'after',
                          'requirements',
                          'files', 'information', 'phone', 'this', 'new', 'should', 'with', 'list', 'before', 'have',
                          'pre', 'and', 'does', '2.', 'was', 'cr', 'sample', '1.', 'are', 'display', 'check', 'select',
                          'only', 'wrong', 'sw', 'condition', 'attached', 'using', 'current', 'insert', 'the', 'start',
                          'device', 'but', 'of', 'from', 'document', 'in', 'not', 'a', 'after', 'selecting', 'whole',
                          'process', 'again', 'makes', 'hot', 'it', 'route', 'problem', 'expected', 'result',
                          'reproduction', 'does', 'not', 'show', 'when', 'using', 'sim', 'card', 'cards', 'code',
                          'version', 'build', 'id', 'sku', 'test', 'flash', 'binaries', 'category', 'setup', 'all',
                          'item', "o", "de", "do", "e", "os", "com",
                          'request', 'cited', 'complete', 'screen', '0', '1', '2', '3', 'dut.', '&', 'reproduce1',
                          'bellow2', 'u\\sel', '|'] + STOP_WORDS_ENGLISH

BAG_OF_WORDS = [] # mascarado para proteção a dados internos

problemas = json.loads(open("/home/fabio.silva/dados/problemas.json", "r").read())

for problema in problemas:
    problema["problem_train"] = " ".join([word for word in problema["problem"].lower().split() if word not in STOP_WORDS_REQUIREMENT])
    problema["resolution_train"] = " ".join([word for word in problema["resolution"].lower().split() if word not in STOP_WORDS_REQUIREMENT])
    problema["cause_train"] = " ".join([word for word in problema["cause"].lower().split() if word not in STOP_WORDS_REQUIREMENT])

for problema in problemas:
    problema["problem_train"] = " ".join([f"{word} {word} {word}" for word in problema["problem_train"].lower().split() if word in BAG_OF_WORDS])
    problema["resolution_train"] = " ".join([f"{word} {word} {word}" for word in problema["resolution_train"].lower().split() if word in BAG_OF_WORDS])
    problema["cause_train"] = " ".join([f"{word} {word} {word}" for word in problema["cause_train"].lower().split() if word in BAG_OF_WORDS])


open("/home/fabio.silva/dados/problemas.json", "w").write(json.dumps(problemas))

df_projetos = pd.read_json("/home/fabio.silva/dados/projetos.json")

df_problemas = pd.read_json("/home/fabio.silva/dados/problemas.json")

storage_media = df_projetos[["storage"]].means(axis=0)

df_projetos.storage.fillna(value=storage_media, inplace=True)

df_problemas.dropna()

TERMOS_SIMILARES = {} # mascarado para evitar vazamento de dados

for termo in TERMOS_SIMILARES:
    df_problemas.loc[df_problemas['category'] in TERMOS_SIMILARES[termo]].replace(value=termo, inplace=True)

df_problemas.drop('resolved_by', axis=1, inplace=True)

df_problemas["resolved_date"] = pd.to_datetime(df_problemas["resolved_date"], format="%Y-%m-%d")

df_problemas["register_date"] = pd.to_datetime(df_problemas["resolved_date"], format="%Y-%m-%d")

df_projetos["release_date"] = pd.to_datetime(df_projetos["release_date"], format="%Y/%m/%d")

df_problemas_projetos = pd.merge(df_problemas, df_projetos, on=["device", "os_version"])

data = df_problemas_projetos.to_json(orient='table')

open("/home/fabio.silva/dados/problemas_projetos.json", "w").write(json.dumps(data))
