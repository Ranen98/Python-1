import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

newtext = []
# 打开聊天记录文件
for word in open('C:\\Users\\Ranen\\Documents\\李就是我的唯怡(2287346011).txt', 'r', encoding='utf-8'):
    tmp = word[0:4]
    # print(tmp)
    if (tmp == "2019" or tmp == "===="):  # 过滤掉聊天记录的时间和qq名称
        continue
    tmp = word[0:2]
    # print(tmp)
    if (tmp[0] == '[' or tmp[0] == '/'):  # 过滤掉图片和表情，例如[图片]，/可爱
        continue
    newtext.append(word)

# 将过滤掉图片和表情和时间信息和qq名称剩下的文字重新写入到txt
with open('C:\\Users\\Ranen\\Documents\\过滤后的聊天记录.txt', 'w', encoding='utf-8') as f:
    for i in newtext:
        f.write(i)
# 打开新生成的聊天记录文件
text = open('C:\\Users\\Ranen\\Documents\\过滤后的聊天记录.txt', 'r', encoding='utf-8').read()
word_jieba = jieba.cut(text, cut_all=True)
word_split = " ".join(word_jieba)
# 找一张图来生成配色方案
alice_coloring = np.array(Image.open('C:\\Users\\Ranen\\Pictures\\李怡\\mmexport1556980952733.jpg'))
my_wordcloud = WordCloud(background_color="white", max_words=4000, mask=alice_coloring,
                         max_font_size=60, random_state=42,
                         font_path='C:/Windows/Fonts/simhei.ttf') \
    .generate(word_split)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()