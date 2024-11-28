from diaries.DiarySample import DiarySample
from diaries.MiyagoshiDiary import MiyagoshiDiary
from diaries.KunouDiary import KunouDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MiyagoshiDiary(),
    KunouDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
