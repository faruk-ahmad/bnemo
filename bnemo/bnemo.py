"""
Emoji to Bengali translation module.

Author: Faruk Ahmad
        Sagor Sarkar

Last Update: 05 September, 2020
"""

from bnemo import emo_unicode

class Data:
    def __init__(self):
        self.text = ""
        self.emo = []
        self.pos = []
        self.meaning = []


class Translator:
    def __init__(self):
        pass

    def translate(self, sentence):
        emo2text = Data()
        try:
            for emoji, translation in emo_unicode.EMOTICONS.items():
                if emoji in sentence:
                    emo2text.emo.append(emoji)
                    emo2text.meaning.append(translation)
                    start_pos = sentence.find(emoji)
                    end_pos = start_pos + len(emoji)
                    emo2text.pos.append([start_pos, end_pos])            
                    emo2text.text = sentence.replace(emoji, translation)
        except Exception as e:
            print("Something went wrong.")
            return emo2text
        else:
            return emo2text
