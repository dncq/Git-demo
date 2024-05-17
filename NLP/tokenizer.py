'''
import re

def is_proper_name(word):
    # You can implement a logic to check if the word is a proper name
    # For simplicity, let's assume proper names start with an uppercase letter
    return word[0].isupper()

def is_number(word):
    # Check if the word is a number
    return word.isdigit()

def is_datetime(word):
    # You can implement a logic to check if the word is a datetime
    # For simplicity, let's assume datetime words end with "pm" or "am"
    return word.lower().endswith(("pm", "am"))

def tokenizer(text, dict, is_show=False):
    print('Input:', text)
    print()
    input = text.split(" ")
    words = []
    s = 0
    while True:
        e = len(input)
        while e > s:
            tmp_word = input[s:e]
            is_word = ""
            for item in tmp_word:
                is_word += item + " "
            is_word = is_word[:-1] 
            e -= 1

            # Handle proper names, numbers, and datetime
            if is_word.lower() in dict or is_proper_name(is_word) or is_number(is_word) or is_datetime(is_word):
                words.append(is_word)
                break
            if e == s:
                words.append(is_word)
                break
        if e >= len(input):
            break
        # Display the word segmentation process
        if is_show:
            print("s =", s)
            print("e =", e)
            print(words[len(words) - 1])
            print("-" * 100)
        s = e + 1
    output = ""
    for item in words:
        output += item.replace(" ","_")
        output += " "
    output = output[:-1]
    return output

if __name__ == "__main__":
    ex1 = "thời khóa biểu đang được cập nhật"
    ex2 = "môn học xử lý ngôn ngữ tự nhiên"
    ex3 = "con ngựa đá con ngựa đá"
    ex4 = "học sinh học sinh học"
    
    # Test sentences
    test1 = tokenizer("Tôi gặp An lúc 2pm.", dict, is_show=True)
    test2 = tokenizer("Học sinh học môn sinh học vào tiết 3", dict, is_show=True)

'''



def tokenizer(text, dict, is_show=False):
    print('Input:', text)
    print()
    input = text.split(" ")
    words = []
    s = 0
    while True:
        e = len(input)
        while e > s:
            tmp_word = input[s:e]
            is_word = ""
            for item in tmp_word:
                is_word += item + " "
            is_word = is_word[:-1] 
            e -= 1
            #print(is_word)
            if is_word.lower() in dict:
                words.append(is_word)
                break
            if e == s:
                words.append(is_word)
                break
        if e >= len(input):
            break
        # Display the word segmentation process
        if is_show:
            print("s =",s)
            print("e =",e)
            print(words[len(words) - 1])
            print("-" * 100)
        s = e + 1
    output = ""
    for item in words:
        output += item.replace(" ","_")
        output += " "
    output = output[:-1]
    return output

if __name__ == "__main__":
    ex1 = "thời khóa biểu đang được cập nhật"
    ex2 = "môn học xử lý ngôn ngữ tự nhiên"
    ex3 = "con ngựa đá con ngựa đá"
    ex4 = "học sinh học sinh học"

    #Từ điển
    dict = {"thời khóa biểu":0,
            "đang": 1,
            "được":2,
            "cập nhật":3,
            "môn học":4,
            "môn": 5,
            "học":6,
            "xử lý":7,
            "ngôn ngữ":8,
            "tự nhiên":9,
            "con":10,
            "con ngựa":11,
            "ngựa":12,
            "đá":13,
            "học":14,
            "học sinh":15,
            "sinh học":16,
            "dân tộc":17, "viện trưởng":18,"giáo viên":19,
            "đạo diễn":20,"xứ sở":21,"nguồn lực":22, "thủ đô":23,
            "số lượng":24, "thuần nhất":25,"môi giới":26,
            "đơn giản":27, "tiến bộ":28,"chính sách":29,
            "thường xuyên":30,"tình yêu":30,
            "ông già" : 31, "ông" : 32, "già" : 33, "đi" : 34, "nhanh" :35, "quá" : 36, "già đi" :51,
            "bún chả" : 37, "bún": 38, "chả" : 38, "ngon" : 39,
            "cột điện" : 40, "cao thế": 41, "cao" :42, "thế" : 43,
            "hổ mang":44, "hổ" :45, "mang" : 46, "bò lên": 47, "bò" :48,"lên":49,"núi" :50}
    
    test1 = tokenizer(ex2, dict)
    print("ouput", test1)
