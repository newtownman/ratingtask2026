import requests
import re
import time
from pathlib import Path

API_KEY   = "ffd6c21d6ab10c9d0a66aa382b2e63b79c4eaed93ab794b59950b8330eaddfb3"
AUDIO_DIR = Path(r"C:\Users\강예인\Desktop\PNU\DISSERTATION\ratingtask\audio")

# 1) 로컬 파일에서 voice ID 수집
files = sorted(AUDIO_DIR.glob("*.mp3"))
id_to_file = {}
for f in files:
    parts = f.stem.split("__")
    if len(parts) == 3:
        id_to_file[parts[2]] = f

print(f"찾아야 할 ID: {len(id_to_file)}개")

# 2) shared-voices 전체 긁어서 id→name 딕셔너리 구축
id_to_name = {}
page = 0
while True:
    res = requests.get(
        "https://api.elevenlabs.io/v1/shared-voices",
        headers={"xi-api-key": API_KEY},
        params={"language": "en", "page_size": 100, "page": page},
        timeout=15,
    )
    data = res.json()
    voices = next((v for v in data.values() if isinstance(v, list) and len(v) > 0), [])
    for v in voices:
        id_to_name[v["voice_id"]] = v["name"]

    # 찾던 ID 다 찾으면 조기 종료
    found = sum(1 for vid in id_to_file if vid in id_to_name)
    print(f"  page {page}: {found}/{len(id_to_file)}개 매칭됨")
    if found == len(id_to_file) or not data.get("has_more"):
        break
    page += 1
    time.sleep(0.25)

# 3) 파일명 변경
def safe_name(name):
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    return name.strip().replace(' ', '_')[:40]

renamed, failed = 0, []
for voice_id, old_path in id_to_file.items():
    accent, rank = old_path.stem.split("__")[:2]
    name = id_to_name.get(voice_id)
    if not name:
        print(f"  ⚠ 매칭 안됨: {voice_id}")
        failed.append(old_path.name)
        continue
    new_path = old_path.parent / f"{accent}__{rank}__{safe_name(name)}.mp3"
    old_path.rename(new_path)
    print(f"  ✓ {old_path.name} → {new_path.name}")
    renamed += 1

print(f"\n완료: {renamed}개, 실패: {len(failed)}개")
if failed:
    print(failed)