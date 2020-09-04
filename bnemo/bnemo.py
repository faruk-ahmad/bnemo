
from bnemo import emo_unicode

def translate(sentence):
    emo = []
    mean = []
    pos = []
    results = {}
    for k, v in emo_unicode.EMOTICONS.items():
        if k in sentence:
            emo.append(k)
            mean.append(v)
            start_pos = sentence.find(k)
            pos.append([start_pos,start_pos])            
            sentence = sentence.replace(k, v)

    if len(emo)<1:
        print("No emo found in the text")

    results = {
        'sentence': sentence,
        'emo': emo,
        'mean': mean,
        'pos': pos
    }  

    return results
