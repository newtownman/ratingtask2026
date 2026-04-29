from mutagen.mp3 import MP3
from pathlib import Path

folder = Path(r"C:\Users\강예인\Desktop\PNU\DISSERTATION\ratingtask\audio")

total = 0
bad = []
for f in sorted(folder.glob("*.mp3")):
    try:
        audio = MP3(f)
        dur = audio.info.length
        total += dur
        print(f"{f.name:<55} {dur:.1f}s")
    except Exception as e:
        bad.append(f.name)
        print(f"{f.name:<55} ⚠ 오류: {e}")

print(f"\n총 {total:.1f}초 = {total/60:.1f}분")
if bad:
    print(f"\n⚠ 문제 파일 {len(bad)}개: {bad}")