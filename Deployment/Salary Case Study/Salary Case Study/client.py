import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':15, 'test_score':99, 'interview_score':95})

print(r.json())