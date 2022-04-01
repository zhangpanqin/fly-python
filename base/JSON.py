import json

dash_board_str = """
{
    "aa": 11
}
"""
dash_board_json = json.loads(dash_board_str)

dash_board_json['bb'] = 33
dash_board_json['aa'] = 22

if __name__ == '__main__':
    print(dash_board_json)
