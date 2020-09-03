import googletrans
import json
from tqdm import tqdm
import time

# print(googletrans.LANGUAGES)
# en = english
# bn = bengali

from googletrans import Translator

translator = Translator()

# result = translator.translate("I love you", src="en", dest="bn")
# print(result.text)

db_path = "./clean_db.json"

translations = {}

with open(db_path, 'r') as rp:
    data = json.load(rp)

for k_emo, v_en in tqdm(data.items()):
    print(f"Translating: {v_en}")
    bn_phrase = translator.translate(v_en, src="en", dest="bn")
    translations[k_emo] = bn_phrase.text
    time.sleep(0.5)

print(f"Writing to file..")

with open('db_bn.json', 'w') as wp:
    json.dump(translations, wp, indent=2, ensure_ascii=False)