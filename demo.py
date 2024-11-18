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