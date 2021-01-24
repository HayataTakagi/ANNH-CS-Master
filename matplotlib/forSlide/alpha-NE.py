import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォントを設定
    fig = plt.figure(figsize=(6, 3.5), dpi=300)
    test_size = 100

    ne_sum_data = np.loadtxt('../data/A-NE-SUM.csv', skiprows=1, delimiter=',')
    ne_sum_data_ = ne_sum_data / (1000 * test_size)  # μsからmsへの変換
    ax = fig.add_subplot(121, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax.plot(ne_sum_data[0:5, 0], ne_sum_data_[0:5, 1], marker='x', label='Point')
    ax.plot(ne_sum_data[0:5, 0], ne_sum_data_[0:5, 2], marker='s', label='MBR')
    ax.plot(ne_sum_data[:, 0], ne_sum_data_[:, 3], marker='o', label='Grid')
    ax.plot(ne_sum_data[:, 0], ne_sum_data_[:, 4], marker='^', label='Quatree')
    ax.set_title('(a) NE,SUM', loc='center', y=-0.3, fontweight='bold')
    # ax.set_ylim(10, 100000)

    ne_max_data = np.loadtxt('../data/A-NE-MAX.csv', skiprows=1, delimiter=',')
    ne_max_data_ = ne_max_data / (1000 * test_size)  # μsからmsへの変換
    ax2 = fig.add_subplot(122, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax2.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax2.plot(ne_max_data[0:5, 0], ne_max_data_[0:5, 1], marker='x')
    ax2.plot(ne_max_data[0:5, 0], ne_max_data_[0:5, 2], marker='s')
    ax2.plot(ne_max_data[0:6, 0], ne_max_data_[0:6, 3], marker='o')
    ax2.plot(ne_max_data[:, 0], ne_max_data_[:, 4], marker='^')
    ax2.set_title('(b) NE,MAX', loc='center', y=-0.3, fontweight='bold')
    # ax2.set_ylim(10, 1000000)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=4, frameon=False)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    fig.savefig('export/alpha-NE.pdf', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
