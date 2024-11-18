# 我们用Python一步一步来做一个简单的个人博客demo吧
import os

# 创建目录
os.makedirs('docs/python', exist_ok=True)
os.makedirs('docs/tools', exist_ok=True)


# 创建文件
open('docs/python/basics.md', 'a').close()
open('docs/python/advanced.md', 'a').close() 
open('docs/tools/git.md', 'a').close()
open('docs/about.md', 'a').close()



# # 初始化Git仓库
# git init

# # 添加所有文件到暂存区
# git add .

# # 提交修改
# git commit -m "Initial commit"

# # 添加远程仓库地址（替换为你的仓库地址）
# # 地址格式：https://github.com/你的用户名/my-blog.git
# git remote add origin https://github.com/你的用户名/my-blog.git


#创建一个新的 main 分支：
# git checkout -b main

# # 推送到GitHub
# git push -u origin main


os.makedirs('.github/workflows', exist_ok=True)
