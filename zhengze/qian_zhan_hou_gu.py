import re

if __name__ == '__main__':
    # 示例字符串
    text = "applebanana, bananaapple"

    # 正向前瞻示例 - 匹配前面是 "apple" 的 "banana"
    pattern = r"(?<=apple)banana"
    matches = re.findall(pattern, text)
    print("正向前瞻匹配结果:", matches)

    # 负向前瞻示例 - 匹配前面不是 "apple" 的 "banana"
    pattern = r"(?<!apple)banana"
    matches = re.findall(pattern, text)
    print("负向前瞻匹配结果:", matches)

    # 正向后顾示例 - 匹配后面是 "apple" 的 "banana"
    pattern = r"banana(?=apple)"
    matches = re.findall(pattern, text)
    print("正向后顾匹配结果:", matches)

    # 负向后顾示例 - 匹配后面不是 "apple" 的 "banana"
    pattern = r"banana(?!apple)"
    matches = re.findall(pattern, text)
    print("负向后顾匹配结果:", matches)
