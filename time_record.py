import datetime

# 读取Markdown文件
with open('mkdocs.yml', 'r', encoding='utf-8') as file:
    content = file.read()

# 获取当前日期
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
print(current_date)
# 替换占位符
content = content.replace('{{date}}', current_date)

# 写回Markdown文件
with open('mkdocs.yml', 'w', encoding='utf-8') as file:
    file.write(content)

# # 我的博客文章

# 最后编辑日期：{{date}}

# 内容开始...