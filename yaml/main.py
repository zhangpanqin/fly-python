import yaml

if __name__ == '__main__':
    # 示例 YAML 字符串
    yaml_data = """
    text: |
        This is a
        multi-line
        text.
    """

    # 解析 YAML 数据
    parsed_data = yaml.safe_load(yaml_data)

    # 访问多行字符串块
    multi_line_text = parsed_data['text']

    # 展示多行字符串块
    print("Multi-line Text:")
    print(multi_line_text)
