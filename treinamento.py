from sklearn.cluster import SpectralClustering, KMeans, Birch
from joblib import dump

dataset = json.loads(open("/home/fabio.silva/dados/problemas_projetos_vetorizado.json", "r").read())

X = []
for item in dataset:
    X.append(item["vector"])
    
for k in range(4, 15):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    resultado = []
    for index, label in enumerate(kmeans.labels_):
        resultado.append({
            "id": dataset[index]["id"],
            "cluster": label
        })
    dump(kmeans, f"/home/fabio.silva/dados/kmeans_{k}.joblib")
    open(f"/home/fabio.silva/dados/resultado_kmeans_{k}.json", "w").write(json.dumps(resultado))
    
for k in range(4, 15):
    birch = Birch(n_clusters=k).fit(X)
    resultado = []
    for index, label in enumerate(birch.labels_):
        resultado.append({
            "id": dataset[index]["id"],
            "cluster": label
        })
    dump(birch, f"/home/fabio.silva/dados/birch_{k}.joblib")
    open(f"/home/fabio.silva/dados/resultado_birch_{k}.json", "w").write(json.dumps(resultado))

for k in range(4, 15):
    spectral = SpectralClustering(n_clusters=k, assign_labels='discretize', random_state=0).fit(X)
    resultado = []
    for index, label in enumerate(spectral.labels_):
        resultado.append({
            "id": dataset[index]["id"],
            "cluster": label
        })
    dump(spectral, f"/home/fabio.silva/dados/spectral_{k}.joblib")
    open(f"/home/fabio.silva/dados/resultado_spectral_{k}.json", "w").write(json.dumps(resultado))
