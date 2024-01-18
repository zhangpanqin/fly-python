import re


def replace_before_E(version):
    if version.isspace() or version == "":
        return ""

    if version == "E043.7":
        return "E043.0"

    if version == "Selinux":
        return "E038.0"

        # 处理 i3_E035.0-18.4
    result = re.sub(r'.*(?=_E)|-.*', '', version).replace("_", "")
    if '.' not in result:
        result = result + ".0"
    return result


# 示例
original_string = "E037-22.5"

modified_string = replace_before_E(original_string)

print("Original string:", original_string)
print("Modified string:", modified_string)
