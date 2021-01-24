import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォントを設定
    fig = plt.figure(figsize=(6, 3.5), dpi=300)
    test_size = 10

    q_ne_sum_data = np.loadtxt('../data/Q-NE-SUM.csv', skiprows=2, delimiter=',')
    q_ne_sum_data_ = q_ne_sum_data / (1000 * test_size)  # μsからmsへの変換
    ax = fig.add_subplot(121, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 1], marker='x', label='Point')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 2], marker='s', label='MBR')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 3], marker='o', label='Grid')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 4], marker='^', label='Quatree')
    ax.set_title('(a)NE,SUM', loc='center', y=-0.3, fontweight='bold')
    # ax.set_ylim(10, 1000000)

    q_ne_max_data = np.loadtxt('../data/Q-NE-MAX.csv', skiprows=2, delimiter=',')
    q_ne_max_data_ = q_ne_max_data / (1000 * test_size)  # μsからmsへの変換
    ax2 = fig.add_subplot(122, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 1], marker='x')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 2], marker='s')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 3], marker='o')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 4], marker='^')
    ax2.set_title('(b)NE,MAX', loc='center', y=-0.3, fontweight='bold')
    # ax2.set_ylim(10, 100000)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=4, frameon=False)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    fig.savefig('export/querysize-NE2.pdf', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
