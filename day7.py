# 1.完成包的使用（与上课一致）

# import message
#
# message.send_message.send_message()
# txt = message.receive_message.receive_message()
# print(txt)

# 2.完成文件的文本模式的读，写（与上课一致）
# def open_r():
#     file = open('file1.txt', mode='r', encoding='utf-8')
#     text = file.read()
#     print(text)
#     file.close()
#
#
# def open_rw():
#     file = open('file1.txt', mode='r+', encoding='utf-8')
#     text = file.read()
#     print(text)
#     file.write('hello world')
#     file.close()
#
#
# def open_w():
#     file = open('file2.txt', mode='w', encoding='utf-8')
#     file.write('hello world')
#     file.close()
#
#
# def oppe_a():
#     file = open('file3', mode='a', encoding='utf-8')
#     file.write('hello')
#     file.close()
#
#
# def use_readline():
#     file = open("file1.txt",  encoding='utf-8')
#     while True:
#         line = file.readline()
#         if not line:
#             break
#
#         print(line, end='')
#
# if __name__ == '__main__':
#     open_r()
#     open_rw()
#     open_w()
#     oppe_a()
#     use_readline()


# 3.完成目录的listdir，getcwd,chdir的使用（与上课一致）
# import os
#
#
# def use_name():
#     os.rename('dir1/file2', 'dir1/file1')
#     os.remove('dir1/file1.txt')
#
#
# def use_func():
#     file_list = os.listdir('.')
#     print(file_list)
#     os.mkdir('dir1')
#     os.rmdir('dir1')
#     print(os.getcwd())
#     os.chdir('dir2')
#     file = open('file1', 'w', encoding='utf8')
#     file.close()
#
#
# def change_dir():
#     print(os.getcwd())
#     os.chdir('dir2')
#     print(os.getcwd())
#
#
# def scan_dir(current_path, width):
#     file_list = os.listdir(current_path)
#     for file in file_list:
#         print(' ' * width, file)
#         new_path = current_path + '/' + file
#         if os.path.isdir(new_path):
#             scan_dir(new_path, width + 4)
#
#
# if __name__ == '__main__':
#     # use_name()
#     use_func()
#     # change_dir()
#     scan_dir('.', 0)


# 4.完成python的传参练习（与上课一致）
# import sys
#
#
# def write_file(file_path):
#     file = open(file_path, 'w+', encoding='utf-8')
#     file.write('hello world')
#     file.close()
#
#
# if __name__ == '__main__':
#     write_file(sys.argv[1])

# 5.完成普通文件文件的seek，二进制文件的seek（代码编写与上课一致即可）
# 创建并写入文件
# with open('seek.txt', 'w') as f:
#     f.write("这是一个文件\n第二行.")
# # 修改文件内容
# with open('seek.txt', 'r+') as f:
#     # 读取原始内容
#     content = f.read()
#     print("初始内容\n", content)
#     # 使用 seek 方法移动到文件开头
#     f.seek(0)
#     # 在开头写入一行新内容
#     f.write("在一个宁静的清晨，阳光透过薄薄的云层洒在山谷间，清新的空气中弥漫着花草的香气。小溪在岩石间欢快地流淌，发出悦耳的水声，仿佛在为大地谱写一首自然的乐章。远处，一位"
#             "身穿朴素衣衫的老人缓缓走来，手中提着一篮新鲜采摘的野果，脸上带着温暖的微笑。他轻声哼着一首老歌，歌声悠扬，与周围的景致相得益彰。不远处，一群孩子正在草地上嬉戏，"
#             "他们的笑声回荡在山谷间，为宁静的早晨增添了几分生机。一个小女孩停下脚步，抬头望向天空，指着一只飞过的白鹭，兴奋地喊道："
#             "“看！多漂亮的鸟儿！”其他孩子也跟着仰起头，目光中充满了好奇和欣喜。这片大自然的画卷，无需任何修饰，便已美得令人陶醉。\n")
#     # 使用 seek 方法移到特定位置
#     f.seek(10)
#     # 替换指定位置的内容
#     f.write("更新")
#     # 查看最终的文件内容
#     f.seek(0)
#     updated_content = f.read()
#     print("更新后的内容:\n", updated_content)

# 6.完成深度优先遍历目录（代码编写与上课一致即可）
import os


def get_all_dirs_deep(path):
    stack = []
    stack.append((path, 0))
    # 把文件夹路径压入栈
    while len(stack) != 0:
        # 当栈不为空的时候，要处理栈里的目录
        current_dir, level = stack.pop()
        print(level * '    ' + '目录： ' + os.path.basename(current_dir))
        # 把栈里的最后一个目录取出来处理
        fileslist = os.listdir(current_dir)
        # 获取当前正在处理的目录里的文件目录
        for filename in fileslist:
            # 针对当前处理的目录里所有的文件
            fileabspath = os.path.join(current_dir, filename)
            # 获取每个文件的绝对路径
            if os.path.isdir(fileabspath):
                stack.append((fileabspath, level + 1))
                # 如果这个文件还是目录，就打印出提示，并且压进栈，继续处理
            else:
                print((level + 1) * '    ' + '普通文件: ' + filename)


get_all_dirs_deep('F:\python2025\python')
