from diaries.AbstractDiary import AbstractDiary

class WatanabeDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "明日になっても今日の授業内容を覚えていられるかな"

    def get_author(self):
        return "Sample"
