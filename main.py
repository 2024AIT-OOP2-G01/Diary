from diaries.MiyagoshiDiary import MiyagoshiDiary
from diaries.KunouDiary import KunouDiary
from diaries.YokomoriDiary import YokomoriDiary
from diaries.AkieDiary import AkieDiary
from diaries.okuyamaDiary import okuyamaDiary
from diaries.WatanabeDiary import WatanabeDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    MiyagoshiDiary(),
    KunouDiary(),
    YokomoriDiary(),
    AkieDiary(),
    okuyamaDiary(),
    WatanabeDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
