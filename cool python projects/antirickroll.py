import re

def find_rickroll(url):
    try:
        import requests
        response = requests.get(url)
        response.raise_for_status()
        source = response.text.lower()
        for keyword in rickrolls:
            if re.search(keyword, source, re.MULTILINE):
                return True
            return False
    except Exception as e:
        print("Lỗi", str(e))
        return None
rickrolls = [
    "rickroll", "rick roll", "rick astley", "never gonna give you up", "never gonna let you down", 
    "rickrolling", "rickrolled", "astley", "termex", "stickbug", "stickbugged", "you got me", "fell for this", "fell for that", "distraction dance", "yeltsa kcir", "self defence move", "cyberpunk"
    , "rit roi", "ric roi", "astley"
]

url = input("Nhập URL Bạn muốn kiểm tra: ")

print("Đang kiểm tra...", end="\r")
check = find_rickroll(url)
if check is True:
    print("\033[0;31mPhát hiện URL có chứa RickRoll!!!\033[0;0m")
elif check is False:
    print("\033[0;32mKhông Phát hiện RickRoll, có thể yên tâm truy cập. \033[0;0m]")
