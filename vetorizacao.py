from sklearn.feature_extraction.text import TfidfVectorizer
import json

texto_problemas = []  # mascarado para evitar vazamento de informação
vector_texto_problemas = TfidfVectorizer()
vector_texto_problemas.fit([texto_problemas])

dataset = json.loads(open("/home/fabio.silva/dados/problemas_projetos.json", "r").read())

resultado = []
for item in dataset:
    texto = " ".join([item[key] for key in item])
    resultado.append({
        "id": item["id"],
        "vector": vector_texto_problemas.transform([texto]).toarray()[0]
    })

open("/home/fabio.silva/dados/problemas_projetos_vetorizado.json", "w").write(json.dumps(resultado))
