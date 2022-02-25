if __name__ == '__main__':
    f = open('../../a.txt', mode='a', encoding='utf-8')
    f.write('芊芊')
    f.close()
    f = open('../../a.txt', mode='r', encoding='utf-8')
    print(f.read())
    f.close()
