# import matplotlib.patches as mpatches
# import matplotlib.pyplot as plt
#
# red_patch = mpatches.Patch(color='red', label='The red data')
# plt.legend(handles=[red_patch])
#
# plt.show()

# import matplotlib.lines as mlines
# import matplotlib.pyplot as plt
#
# blue_line = mlines.Line2D([], [], color='blue', marker='*',
#                           markersize=15, label='Blue stars')
# plt.legend(handles=[blue_line])
#
# plt.show()


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#多数据并列柱状图
# mpl.rcParams["font.sans-serif"]=["SimHei"]
# mpl.rcParams["axes.unicode_minus"]=False
# x = np.arange(6)
# y1 = [23,5,14,27,18,14]
# y2 = [10,27,25,18,23,16]
# tick_label = ["A","B","C","D","E","F"]
# bar_width = 0.35
# plt.bar(x,y1,bar_width,align="center",label="班级A",alpha=0.5)
# plt.bar(x+bar_width,y2,bar_width,align="center",label="班级B",alpha=0.5)
# plt.xlabel("成绩等级")
# plt.ylabel("人数")
# plt.xticks(x+bar_width/2,tick_label)
#
# plt.legend(bbox_to_anchor=(1,1),#图例边界框起始位置
#                  loc="upper right",#图例的位置
#                  ncol=1,#列数
#                  mode="None",#当值设置为“expend”时，图例会水平扩展至整个坐标轴区域
#                  borderaxespad=0,#坐标轴和图例边界之间的间距
#                  title="班级",#图例标题
#                  shadow=False,#是否为线框添加阴影
#                  fancybox=True)#线框圆角处理参数
# plt.show()


import matplotlib.pyplot as plt


plt.subplot(211)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label="test2")
# Place a legend above this subplot, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)

plt.subplot(223)
plt.plot([1,2,3], label="test1")
plt.plot([3,2,1], label="test2")
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()