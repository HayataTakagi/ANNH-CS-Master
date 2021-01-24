import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォントを設定
    fig = plt.figure(figsize=(6, 9), dpi=300)
    test_size = 100

    ne_sum_data = np.loadtxt('data/A-NE-SUM.csv', skiprows=1, delimiter=',')
    ne_sum_data_ = ne_sum_data / (1000 * test_size)  # μsからmsへの変換
    ax = fig.add_subplot(321, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax.plot(ne_sum_data[0:5, 0], ne_sum_data_[0:5, 1], marker='x', label='Point')
    ax.plot(ne_sum_data[0:5, 0], ne_sum_data_[0:5, 2], marker='s', label='MBR')
    ax.plot(ne_sum_data[:, 0], ne_sum_data_[:, 3], marker='o', label='Grid')
    ax.plot(ne_sum_data[:, 0], ne_sum_data_[:, 4], marker='^', label='Quatree')
    ax.set_title('(a) NE,SUM', loc='center', y=-0.27, fontweight='bold')
    # ax.set_ylim(10, 100000)

    ne_max_data = np.loadtxt('data/A-NE-MAX.csv', skiprows=1, delimiter=',')
    ne_max_data_ = ne_max_data / (1000 * test_size)  # μsからmsへの変換
    ax2 = fig.add_subplot(322, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax2.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax2.plot(ne_max_data[0:5, 0], ne_max_data_[0:5, 1], marker='x')
    ax2.plot(ne_max_data[0:5, 0], ne_max_data_[0:5, 2], marker='s')
    ax2.plot(ne_max_data[0:6, 0], ne_max_data_[0:6, 3], marker='o')
    ax2.plot(ne_max_data[:, 0], ne_max_data_[:, 4], marker='^')
    ax2.set_title('(b) NE,MAX', loc='center', y=-0.27, fontweight='bold')
    # ax2.set_ylim(10, 1000000)

    cas_sum_data = np.loadtxt('data/A-CAS-SUM.csv', skiprows=1, delimiter=',')
    cas_sum_data_ = cas_sum_data / (1000 * test_size)  # μsからmsへの変換
    ax3 = fig.add_subplot(323, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax3.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax3.plot(cas_sum_data[0:5, 0], cas_sum_data_[0:5, 1], marker='x')
    ax3.plot(cas_sum_data[0:5, 0], cas_sum_data_[0:5, 2], marker='s')
    ax3.plot(cas_sum_data[:, 0], cas_sum_data_[:, 3], marker='o')
    ax3.plot(cas_sum_data[:, 0], cas_sum_data_[:, 4], marker='^')
    ax3.set_title('(c) CAS,SUM', loc='center', y=-0.27, fontweight='bold')
    # ax3.set_ylim(10, 100000)

    cas_max_data = np.loadtxt('data/A-CAS-MAX.csv', skiprows=1, delimiter=',')
    cas_max_data_ = cas_max_data / (1000 * test_size)  # μsからmsへの変換
    ax4 = fig.add_subplot(324, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax4.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax4.plot(cas_max_data[0:5, 0], cas_max_data_[0:5, 1], marker='x')
    ax4.plot(cas_max_data[0:5, 0], cas_max_data_[0:5, 2], marker='s')
    ax4.plot(cas_max_data[0:6, 0], cas_max_data_[0:6, 3], marker='o')
    ax4.plot(cas_max_data[:, 0], cas_max_data_[:, 4], marker='^')
    ax4.set_title('(d) CAS,MAX', loc='center', y=-0.27, fontweight='bold')
    # ax4.set_ylim(10, 100000)

    un_sum_data = np.loadtxt('data/A-UN-SUM.csv', skiprows=1, delimiter=',')
    un_sum_data_ = un_sum_data / (1000 * test_size)  # μsからmsへの変換
    ax5 = fig.add_subplot(325, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax5.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax5.plot(un_sum_data[0:5, 0], un_sum_data_[0:5, 1], marker='x')
    ax5.plot(un_sum_data[0:5, 0], un_sum_data_[0:5, 2], marker='s')
    ax5.plot(un_sum_data[:, 0], un_sum_data_[:, 3], marker='o')
    ax5.plot(un_sum_data[:, 0], un_sum_data_[:, 4], marker='^')
    ax5.set_title('(e) UN,SUM', loc='center', y=-0.27, fontweight='bold')
    # ax5.set_ylim(10, 1000000)

    un_max_data = np.loadtxt('data/A-UN-MAX.csv', skiprows=1, delimiter=',')
    un_max_data_ = un_max_data / (1000 * test_size)  # μsからmsへの変換
    ax6 = fig.add_subplot(326, xlabel='α', ylabel='Processing time (ms)', yscale='log')
    ax6.axvline(0.5, linestyle="dashed", color="black", linewidth=1, alpha=0.5)
    ax6.plot(un_max_data[0:5, 0], un_max_data_[0:5, 1], marker='x')
    ax6.plot(un_max_data[0:5, 0], un_max_data_[0:5, 2], marker='s')
    ax6.plot(un_max_data[0:6, 0], un_max_data_[0:6, 3], marker='o')
    ax6.plot(un_max_data[:, 0], un_max_data_[:, 4], marker='^')
    ax6.set_title('(f) UN,MAX', loc='center', y=-0.27, fontweight='bold')
    # ax6.set_ylim(10, 1000000)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=4, frameon=False)
    plt.tight_layout()
    plt.subplots_adjust(top=0.95, hspace=0.3)

    fig.savefig('export/alpha.pdf', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
