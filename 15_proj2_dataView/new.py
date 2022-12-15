import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(5000)
    rw.fill_walks()

    # 将所有的点都绘制出来
    plt.style.use('classic')
    # 添加参数调整窗口大小
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    plt.show()

    keep_running = input("Make anthor walk?(y/n): ")
    if keep_running == 'n':
        break