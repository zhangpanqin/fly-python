from easyocr import easyocr

if __name__ == '__main__':

    reader = easyocr.Reader(['en'])  # 选择支持的语言
    result = reader.readtext('/Users/panqinzhang/Desktop/Snipaste_2023-08-22_16-45-22.png')

    for detection in result:
        print(detection[1])