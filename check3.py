import requests

API_KEY = "ffd6c21d6ab10c9d0a66aa382b2e63b79c4eaed93ab794b59950b8330eaddfb3"
all_accents = set()
page = 0

while True:
    res = requests.get(
        "https://api.elevenlabs.io/v1/shared-voices",
        headers={"xi-api-key": API_KEY},
        params={"language": "en", "page_size": 100, "page": page}
    )
    data = res.json()
    voices = [v for val in data.values() if isinstance(val, list) for v in val if isinstance(v, dict)]
    
    for v in voices:
        if v.get("accent"):
            all_accents.add(v["accent"])
    
    if not data.get("has_more"):
        break
    page += 1
    print(f"page {page} 완료...")

print("\n전체 accent 종류:")
print(sorted(all_accents))