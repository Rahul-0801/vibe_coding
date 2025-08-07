import requests
data = {
    "files_changed": 10,
    "test_pass_rate": 0.85,
    "build_time_sec": 120
}
response = requests.post("http://localhost:8000/predict", json=data)
print("Response:", response.json())              