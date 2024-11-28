from diaries.DiarySample import DiarySample
from diaries.YokomoriDiary import YokomoriDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), YokomoriDiary()] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
