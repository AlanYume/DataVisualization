import matplotlib.pyplot as plt

"""绘制散列点"""
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
# 设置图标标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# plt.show()
# 保存图片:参数一,保存图片名;参数二,去除图表周围多余的白边
plt.savefig('squares_plot.png', bbox_inches='tight')