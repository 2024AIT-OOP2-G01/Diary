from diaries.DiarySample import DiarySample
from diaries.MiyagoshiDiary import MiyagoshiDiary
from diaries.KunouDiary import KunouDiary
from diaries.YokomoriDiary import YokomoriDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MiyagoshiDiary(),
    KunouDiary(),
    YokomoriDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
