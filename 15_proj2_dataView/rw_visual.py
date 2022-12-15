import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50000)
    rw.fill_walks()

    # 将所有的点都绘制出来
    plt.style.use('classic')
    # 添加参数调整窗口大小
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # 绘制突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make anthor walk?(y/n): ")
    if keep_running == 'n':
        break