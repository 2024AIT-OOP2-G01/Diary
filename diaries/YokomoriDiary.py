from diaries.AbstractDiary import AbstractDiary

class YokomoriDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return """GitHubなんもわからん。
コンフリクトへの対処とか
SQLとか正規表現とかそういうの早く自動化してくれ。"""

    def get_author(self):
        return "Yokomori"
