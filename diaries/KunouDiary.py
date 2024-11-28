from diaries.AbstractDiary import AbstractDiary

class KunouDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日はオブジェクト演習2の授業でグループワークを行ったGitHubの演習でブランチの仕様を理解するのが少し難しかった。"

    def get_author(self):
        return "バイトだから早く帰りたい。"
