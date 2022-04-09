# coding=utf8
s = r"""
类别识别正确率定义为：类别识别正确的目标数量除以实际检测出的目标数量。定义图像帧x_i的识别正确目标数量为n_i^{zq}，实检目标数量为n_i^{sj}，图像帧总数为M=326,则识别率定义为：
"""

def is_chinese(c):
    return '\u4e00' <= c <= '\u9fa5' or c in "，。；：、（）"

ans = []
for i in range(len(s)):
    ans.append(s[i])
    if is_chinese(s[i]) and i+1 < len(s) and not is_chinese(s[i+1]) and s[i+1] != '\n':
        ans.append('$')
    elif not is_chinese(s[i]) and s[i] != '\n' and (i+1 >= len(s) or is_chinese(s[i+1])):
        ans.append('$')
    elif s[i] == '\n' and i+1 < len(s) and not is_chinese(s[i+1]):
        if s[i+1] == '\n': continue
        ans.append(r'\begin{equation}')
        ans.append('\n')
    elif i+1 < len(s) and s[i+1] == '\n' and not is_chinese(s[i]):
        ans.append('\n')
        ans.append(r'\end{equation}')
print(''.join(ans))

