import requests

API_KEY = "ffd6c21d6ab10c9d0a66aa382b2e63b79c4eaed93ab794b59950b8330eaddfb3"
res = requests.get(
    "https://api.elevenlabs.io/v1/shared-voices",
    headers={"xi-api-key": API_KEY},
    params={"language": "en", "page_size": 100}
)

data = res.json()
# 키 이름 확인
print(list(data.keys()))

# 리스트 키 찾아서 accent 추출
for key, val in data.items():
    if isinstance(val, list) and len(val) > 0:
        accents = set(v.get("accent", "") for v in val if isinstance(v, dict))
        print(f"\n[{key}] accent 값들:")
        print(sorted(accents))