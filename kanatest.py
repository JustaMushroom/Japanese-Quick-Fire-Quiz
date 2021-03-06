# Import modules
from random import randint
from terminaltables import AsciiTable
from os import system, name

# Define clear function - clears the terminal display
def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

# Define new exception type
class NoTestTypeError(Exception):
    pass

# Define user input clean function
def cleanInput(text:str=None):
    if text is None:
        return Exception("No text passed to clean!")
    
    whitelist = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    countLetter = 0
    for letter in text:
        if letter in whitelist:
            output += letter
            countLetter += 1
        if countLetter == 3:
            break
    return output

def kanatest(type:int=None):
    # Define answer sheets for hiragana and katakana
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
    
    # Convert answer sheets into lists that can be chosen from
    hiragana = tuple(kana_hiragana)
    katakana = tuple(kana_katakana)
    
    # Reset count variable for scoring
    count = 0
    
    # Check which test has been selected
    if type == 0:
        # Start the main test loop (Mixed)
        while True:
            # Rnadomly choose whether the question will be a hiragana or katakana character
            kh = randint(0,1)
            if kh == 0:
                # Select random hiragana character
                id = randint(0, len(hiragana)-1)
                
                # Build the display information
                title_data = [["Mixed Test (Hiragana)"]]
                body_data = [["Character", "Answer"]]
                body_data.append([kana_hiragana[hiragana[id]], ""])
                title = AsciiTable(title_data)
                body = AsciiTable(body_data)

                # Display the randomly selected character
                print(title.table)
                print(body.table)
                
                # Request user's answer
                answer = cleanInput(input("answer>"))

                # Change and rebuild the display information to show the answers
                body_data[1][1] = answer
                body_data[0].append("Correct Answer")
                body_data[1].append(hiragana[id])
                body = AsciiTable(body_data)

                # Clear the screen
                clear()

                # Display the new display with the user's answer
                print(title.table)
                print(body.table)
                
                # Check whether the answer is correct
                if answer.upper() == hiragana[id].upper():
                    print("世界！ (Correct)")
                    count += 1
                else:
                    # Print Result (Incorrect)
                    print("違います！ (Wrong)")
                    
                    # Display score
                    print("You got {} Questions Correct".format(count))
                    
                    # End Test
                    break
            else:
                # Select a random katakana character
                id = randint(0, len(katakana)-1)
                
                # Build the display information
                title_data = [["Mixed Test (Katakana)"]]
                body_data = [["Character", "Answer"]]
                body_data.append([kana_katakana[katakana[id]], ""])
                body = AsciiTable(body_data)
                title = AsciiTable(title_data)
                
                # Clear the screen
                clear()

                # Display the random character
                print(title.table)
                print(body.table)

                # Request user's answer
                answer = cleanInput(input("answer>"))
                
                # Change the display to show user's answer and the correct answer
                body_data[1][1] = answer
                body_data[0].append("Correct Answer")
                body_data[1].append(katakana[id])
                body = AsciiTable(body_data)

                # Clear the screen
                clear()

                # Display the correct answer
                print(title.table)
                print(body.table)

                # Check if answer is correct
                if answer.upper() == katakana[id].upper():
                    # Display result (Correct)
                    print("世界！ (Correct)")
                    
                    # Increment score
                    count += 1
                else:
                    # Display result (Incorrect)
                    print("違います！ (Wrong)")
                    
                    # Display score
                    print("You got {} Questions Correct".format(count))
                    break
    elif type == 1:
        # Start the main test loop (Hiragana)
        while True:
           # Select random hiragana character
            id = randint(0, len(hiragana)-1)
            
            # Build the display information
            title_data = [["Hiragana Test"]]
            body_data = [["Character", "Answer"]]
            body_data.append([kana_hiragana[hiragana[id]], ""])
            title = AsciiTable(title_data)
            body = AsciiTable(body_data)

            # Display the randomly selected character
            print(title.table)
            print(body.table)
            
            # Ask for user's answer
            answer = cleanInput(input("answer>"))

            # Change and rebuild the display information to show the answers
            body_data[1][1] = answer
            body_data[0].append("Correct Answer")
            body_data[1].append(hiragana[id])
            body = AsciiTable(body_data)

            # Clear the screen
            clear()

            # Display the new display with the user's answer
            print(title.table)
            print(body.table)
            
            # Check if user's answer is correct
            if answer.upper() == hiragana[id].upper():
                # Display result (Correct)
                print("世界！ (Correct)")
                
                # Increment score
                count += 1
            else:
                # Display result (Incorrect)
                print("違います！ (Wrong)")
                
                # Display score
                print("You got {} Questions Correct".format(count))
                
                # End test
                break
    elif type == 2:
        # Start test loop (Katakana)
        while True:
            # Select a random katakana character
            id = randint(0, len(katakana)-1)
            
            # Build the display information
            title_data = [["Katakana Test"]]
            body_data = [["Character", "Answer"]]
            body_data.append([kana_katakana[katakana[id]], ""])
            body = AsciiTable(body_data)
            title = AsciiTable(title_data)
            
            #Ask for user's answer
            answer = cleanInput(input("answer>"))
            
            # Clear the screen
            clear()

            # Display the random character
            print(title.table)
            
            # Change the display to show user's answer and the correct answer
            body_data[1][1] = answer
            body_data[0].append("Correct Answer")
            body_data[1].append(katakana[id])
            body = AsciiTable(body_data)

            # Clear the screen
            clear()

            # Display the correct answer
            print(title.table)
            print(body.table)

            # Check if user's answer is correct
            if answer.upper() == katakana[id].upper():
                # Display Result (Correct)
                print("世界！ (Correct)")
                
                # Increment score
                count += 1
            else:
                # Display Result (Incorrect)
                print("違います！ (Wrong)")
                
                # Print score
                print("You got {} Questions Correct".format(count))
                
                # End test
                break
    # Check if a test has actually been sent to this file
    elif type is None:
        # If not, return an error
        # This error should never appear under normal operations
        raise NoTestTypeError("No Test Type Passed")
        
    # Exit The Test function
    input("quit>")
