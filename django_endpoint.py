def find_similarity(request):
  from joblib import load
  from sklearn.feature_extraction.text import TfidfVectorizer
  
  texto_problemas = [] # mascarado para evitar vazamento de informação
  vector_texto_problemas = TfidfVectorizer()
  vector_texto_problemas.fit([texto_problemas])
  
  data_problem = request.POST.dict().get("problem", "")
  data_problem_vectorizer = list(vectorizer_problem.transform([data_problem]).toarray()[0])
  
  birch = load("birch_9.joblib")
  group_item = int(birch.predict([data_problem_vectorizer])[0])
  
  result = clustering.labels_[group_item]
  
  return JsonResponse({"result": result})
