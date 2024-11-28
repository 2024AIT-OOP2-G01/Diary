from diaries.AbstractDiary import AbstractDiary
class okuyamaDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    def get_summary(self):
        return """
        今日は1日中課題に追われていた。
        課題を処理するのはとても面倒くさい。
        眠い。
        """
    def get_author(self):
        return "okuyama"