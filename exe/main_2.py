import argparse
import logging
import os

import gspread
from gspread.utils import ValueRenderOption, ValueInputOption

parser = argparse.ArgumentParser(description='Copy Google Spreadsheet')
parser.add_argument('--id', '-i', help='google spreadsheet id')

args = parser.parse_args()


def is_formula(value):
    return isinstance(value, str) and value.startswith("=")


def is_import_range(value):
    return value.startswith('=IMPORTRANGE') or value.startswith('={importrange')


if __name__ == '__main__':
    client_secret_path = os.path.join(os.getcwd(), "client_secret.json")
    if not os.path.exists(client_secret_path):
        raise Exception(f"{client_secret_path} not exist")

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 设置您的 Google Sheets API 认证信息
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    client = gspread.oauth(credentials_filename=client_secret_path)

    source_spreadsheet_id = args.id

    # 打开源 Spreadsheet
    logging.info("复制文件开始")

    source_spreadsheet = client.open_by_key(source_spreadsheet_id)

    # 创建目标 Spreadsheet
    target_spreadsheet = client.copy(source_spreadsheet_id, title='Archived_' + source_spreadsheet.title)
    target_spreadsheet_key = target_spreadsheet.id

    logging.info("复制文件结束")

    logging.info("-------------------- 开始处理  --------------------")

    # 遍历每个工作表
    for source_sheet in source_spreadsheet.worksheets():
        source_sheet_title = source_sheet.title
        logging.info("开始处理: " + source_sheet_title)

        # 在目标 Spreadsheet 中找到对应的工作表
        target_sheet = target_spreadsheet.get_worksheet(source_sheet.index)

        # 复制 importRange 公式的值
        cell_values = source_sheet.get_values()
        target_sheet.update(cell_values, value_input_option=ValueInputOption.user_entered)

        # 恢复 除去importRange之外的公式
        source_formulas = source_sheet.get_values(value_render_option=ValueRenderOption.formula)
        cell_list = []
        for row_index, row_data in enumerate(source_formulas):
            for col_index, cell_value in enumerate(row_data):
                if is_formula(cell_value) and not is_import_range(cell_value):
                    cell_list.append(gspread.Cell(row_index + 1, col_index + 1, cell_value))
                elif isinstance(cell_value, str) and cell_value.startswith("=IMPORTRANGE"):
                    logging.info("ignore " + cell_value)
                elif isinstance(cell_value, str) and cell_value.startswith("={importrange"):
                    logging.info("ignore " + cell_value)

        if len(cell_list) > 0:
            target_sheet.update_cells(cell_list, value_input_option=ValueInputOption.user_entered)

        logging.info("结束处理: " + source_sheet_title)
    logging.info("完成: " + target_spreadsheet.url)
