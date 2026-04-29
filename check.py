import requests

API_KEY = "ffd6c21d6ab10c9d0a66aa382b2e63b79c4eaed93ab794b59950b8330eaddfb3"
res = requests.get(
    "https://api.elevenlabs.io/v1/shared-voices",
    headers={"xi-api-key": API_KEY},
    params={"language": "en", "page_size": 100}
)

print(res.status_code)
print(res.json())