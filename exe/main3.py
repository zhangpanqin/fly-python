import gspread

if __name__ == '__main__':
    gc = gspread.oauth(credentials_filename='/Users/panqinzhang/github/fly-python/exe/client_secret.json')
    sh = gc.open("import 2")
    print(sh.sheet1.get('A4'))
