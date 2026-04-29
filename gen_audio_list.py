import os

folder = r"C:\Users\강예인\Desktop\PNU\DISSERTATION\ratingtask\audio"

files = sorted([
    f for f in os.listdir(folder)
    if f.lower().endswith(('.mp3', '.wav', '.ogg'))
])

print(f"// 총 {len(files)}개 파일\n")
print("const AUDIO_FILES = [")
for f in files:
    print(f'  "{f}",')
print("];")
