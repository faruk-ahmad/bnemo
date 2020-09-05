from bnemo import Translator

emoji_translator = Translator()

result = emoji_translator.translate("তুমি বড় কষ্ট দিলে 😭")
print(f"Translation: {result.text}\nEmoji: {result.emo}\nPositions: {result.pos}\nMeaning: {result.meaning}")

result = emoji_translator.translate("আমি আজকাল ভালো আছি 8-\\)")
print(f"Translation: {result.text}\nEmoji: {result.emo}\nPositions: {result.pos}\nMeaning: {result.meaning}")