from diaries.AbstractDiary import AbstractDiary

class AkieDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return "1日眠かった。今日は早く寝よう。"
    
    def get_author(self):
        return "Akie"