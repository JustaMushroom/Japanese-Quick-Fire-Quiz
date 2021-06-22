from random import randint

def kanatest(type:int=None):
    kana_hiragana = {
        'a': 'あ',
        'i': 'い',
        'u': 'う',
        'e': 'え',
        'o': 'お',
        'ka': 'か',
        'ki': 'き',
        'ku': 'く',
        'ke': 'け',
        'ko': 'こ',
        'ga': 'が',
        'gi': 'ぎ',
        'gu': 'ぐ',
        'ge': 'げ',
        'go': 'ご',
        'ta': 'た',
        'chi': 'ち',
        'tsu': 'つ',
        'te': 'て',
        'to': 'と',
        'da': 'だ',
        'ji': 'ぢ',
        'dzu': 'づ',
        'de': 'で',
        'do': 'ど',
        'sa': 'さ',
        'shi': 'し',
        'su': 'す',
        'se': 'せ',
        'so': 'そ',
        'za': 'ざ',
        'ji': 'じ',
        'zu': 'ず',
        'ze': 'ぜ',
        'zo': 'ぞ',
        'ha': 'は',
        'hi': 'ひ',
        'fu': 'ふ',
        'he': 'へ',
        'ho': 'ほ',
        'ba': 'ば',
        'bi': 'び',
        'bu': 'ぶ',
        'be': 'べ',
        'bo': 'ぼ',
        'pa': 'ぱ',
        'pi': 'ぴ',
        'pu': 'ぷ',
        'pe': 'ぺ',
        'po': 'ぽ',
        'na': 'な',
        'ni': 'に',
        'nu': 'ぬ',
        'ne': 'ね',
        'no': 'の',
        'ma': 'ま',
        'mi': 'み',
        'mu': 'む',
        'me': 'め',
        'mo': 'も',
        'ya': 'や',
        'yu': 'ゆ',
        'yo': 'よ',
        'ra': 'ら',
        'ri': 'り',
        'ru': 'る',
        're': 'れ',
        'ro': 'ろ',
        'wa': 'わ',
        'wo': 'を'
        }
    kana_katakana = {
        'a': 'ア',
        'i': 'イ',
        'u': 'ウ',
        'e': 'エ',
        'o': 'オ',
        'ka': 'カ',
        'ki': 'キ',
        'ku': 'ク',
        'ke': 'ケ',
        'ko': 'コ',
        'ga': 'ガ',
        'gi': 'ギ',
        'gu': 'グ',
        'ge': 'ゲ',
        'go': 'ゴ',
        'ta': 'タ',
        'chi': 'チ',
        'tsu': 'ツ',
        'te': 'テ',
        'to': 'ト',
        'da': 'ダ',
        'ji': 'ヂ',
        'dzu': 'ヅ',
        'de': 'デ',
        'do': 'ド',
        'sa': 'サ',
        'shi': 'シ',
        'su': 'ス',
        'se': 'セ',
        'so': 'ソ',
        'za': 'ザ',
        'ji': 'ジ',
        'zu': 'ズ',
        'ze': 'ゼ',
        'zo': 'ゾ',
        'ha': 'ハ',
        'hi': 'ヒ',
        'fu': 'フ',
        'he': 'ヘ',
        'ho': 'ホ',
        'ba': 'バ',
        'bi': 'ビ',
        'bu': 'ブ',
        'be': 'ベ',
        'bo': 'ボ',
        'pa': 'パ',
        'pi': 'ピ',
        'pu': 'プ',
        'pe': 'ペ',
        'po': 'ポ',
        'na': 'ナ',
        'ni': 'ニ',
        'nu': 'ヌ',
        'ne': 'ネ',
        'no': 'ノ',
        'ma': 'マ',
        'mi': 'ミ',
        'mu': 'ム',
        'me': 'メ',
        'mo': 'モ',
        'ya': 'ヤ',
        'yu': 'ユ',
        'yo': 'ヨ',
        'ra': 'ラ',
        'ri': 'リ',
        'ru': 'ル',
        're': 'レ',
        'ro': 'ロ',
        'wa': 'ワ',
        'wo': 'ヲ'
        }

    hiragana = list(kana_hiragana)
    katakana = list(kana_katakana)
    #id = randint(0, len(hiragana)-1)
    #print(hiragana[id] + " " + kana_hiragana[hiragana[id]])
    count = 0
    if type == 0:
        while True:
            kh = randint(0,1)
            if kh == 0:
                id = randint(0, len(hiragana)-1)
            #print(hiragana[id] + " " + kana_hiragana[hiragana[id]])
                print("What is this Hiragana Character: {}".format(kana_hiragana[hiragana[id]]))
                answer = input("answer>")
                if answer == hiragana[id]:
                    print("世界！ (Correct)")
                    count += 1
                else:
                    print("違います！ (Wrong)")
                    print("The Answer was Actually {}".format(hiragana[id]))
                    print("You got {} Questions Correct".format(count))
                    break
            else:
                id = randint(0, len(katakana)-1)
            #print(hiragana[id] + " " + kana_hiragana[hiragana[id]])
                print("What is this Katakana Character: {}".format(kana_katakana[katakana[id]]))
                answer = input("answer>")
                if answer == katakana[id]:
                    print("世界！ (Correct)")
                    count += 1
                else:
                    print("違います！ (Wrong)")
                    print("The Answer was Actually {}".format(katakana[id]))
                    print("You got {} Questions Correct".format(count))
                    break
    elif type == 1:
        while True:
            id = randint(0, len(hiragana)-1)
                #print(hiragana[id] + " " + kana_hiragana[hiragana[id]])
            print("What is this Hiragana Character: {}".format(kana_hiragana[hiragana[id]]))
            answer = input("answer>")
            if answer == hiragana[id]:
                print("世界！ (Correct)")
                count += 1
            else:
                print("違います！ (Wrong)")
                print("The Answer was Actually {}".format(hiragana[id]))
                print("You got {} Questions Correct".format(count))
                break
    elif type == 2:
        while True:
            id = randint(0, len(katakana)-1)
            #print(hiragana[id] + " " + kana_hiragana[hiragana[id]])
            print("What is this Katakana Character: {}".format(kana_katakana[katakana[id]]))
            answer = input("answer>")
            if answer == katakana[id]:
                print("世界！ (Correct)")
                count += 1
            else:
                print("違います！ (Wrong)")
                print("The Answer was Actually {}".format(katakana[id]))
                print("You got {} Questions Correct".format(count))
                break
    elif type is None:
        raise Exception("No Test Type Passed")
    input("quit>")
