import gspread

if __name__ == '__main__':
    id = gspread.utils.extract_id_from_url(
        "https://docs.google.com/spreadsheets/d/1tem9qKYMbx5VwV0PPwSGrmjKWPQzxorldEGwFUKto48/edit#gid=2130644358")
    print(id)
