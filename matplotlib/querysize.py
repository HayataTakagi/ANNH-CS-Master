import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォントを設定
    fig = plt.figure(figsize=(6, 9), dpi=300)
    sum_test_size = 70
    max_test_size = 100

    q_ne_sum_data = np.loadtxt('data/Q-NE-SUM.csv', skiprows=2, delimiter=',')
    q_ne_sum_data_ = q_ne_sum_data / (1000 * sum_test_size)  # μsからmsへの変換
    ax = fig.add_subplot(321, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 1], marker='x', label='Point')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 2], marker='s', label='MBR')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 3], marker='o', label='Grid')
    ax.plot(q_ne_sum_data[:, 0], q_ne_sum_data_[:, 4], marker='^', label='Quatree')
    ax.set_title('(a)NE,SUM', loc='center', y=-0.28, fontweight='bold')
    # ax.set_ylim(10, 1000000)

    q_ne_max_data = np.loadtxt('data/Q-NE-MAX.csv', skiprows=2, delimiter=',')
    q_ne_max_data_ = q_ne_max_data / (1000 * max_test_size)  # μsからmsへの変換
    ax2 = fig.add_subplot(322, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 1], marker='x')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 2], marker='s')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 3], marker='o')
    ax2.plot(q_ne_max_data[:, 0], q_ne_max_data_[:, 4], marker='^')
    ax2.set_title('(b)NE,MAX', loc='center', y=-0.28, fontweight='bold')
    # ax2.set_ylim(10, 100000)

    q_cas_sum_data = np.loadtxt('data/Q-CAS-SUM.csv', skiprows=2, delimiter=',')
    q_cas_sum_data_ = q_cas_sum_data / (1000 * sum_test_size)  # μsからmsへの変換
    ax3 = fig.add_subplot(323, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax3.plot(q_cas_sum_data[:, 0], q_cas_sum_data_[:, 1], marker='x')
    ax3.plot(q_cas_sum_data[:, 0], q_cas_sum_data_[:, 2], marker='s')
    ax3.plot(q_cas_sum_data[:, 0], q_cas_sum_data_[:, 3], marker='o')
    ax3.plot(q_cas_sum_data[:, 0], q_cas_sum_data_[:, 4], marker='^')
    ax3.set_title('(c)CAS,SUM', loc='center', y=-0.28, fontweight='bold')
    # ax3.set_ylim(10, 1000000)

    q_cas_max_data = np.loadtxt('data/Q-CAS-MAX.csv', skiprows=2, delimiter=',')
    q_cas_max_data_ = q_cas_max_data / (1000 * max_test_size)  # μsからmsへの変換
    ax4 = fig.add_subplot(324, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax4.plot(q_cas_max_data[:, 0], q_cas_max_data_[:, 1], marker='x')
    ax4.plot(q_cas_max_data[:, 0], q_cas_max_data_[:, 2], marker='s')
    ax4.plot(q_cas_max_data[:, 0], q_cas_max_data_[:, 3], marker='o')
    ax4.plot(q_cas_max_data[:, 0], q_cas_max_data_[:, 4], marker='^')
    ax4.set_title('(d)CAS,MAX', loc='center', y=-0.28, fontweight='bold')
    # ax4.set_ylim(10, 100000)

    q_un_sum_data = np.loadtxt('data/Q-UN-SUM.csv', skiprows=2, delimiter=',')
    q_un_sum_data_ = q_un_sum_data / (1000 * sum_test_size)  # μsからmsへの変換
    ax5 = fig.add_subplot(325, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax5.plot(q_un_sum_data[:, 0], q_un_sum_data_[:, 1], marker='x')
    ax5.plot(q_un_sum_data[:, 0], q_un_sum_data_[:, 2], marker='s')
    ax5.plot(q_un_sum_data[:, 0], q_un_sum_data_[:, 3], marker='o')
    ax5.plot(q_un_sum_data[:, 0], q_un_sum_data_[:, 4], marker='^')
    ax5.set_title('(e) UN,SUM', loc='center', y=-0.28, fontweight='bold')
    # ax5.set_ylim(10, 10000000)

    q_un_max_data = np.loadtxt('data/Q-UN-MAX.csv', skiprows=2, delimiter=',')
    q_un_max_data_ = q_un_max_data / (1000 * max_test_size)  # μsからmsへの変換
    ax6 = fig.add_subplot(326, xlabel='Query size', ylabel='Processing time (ms)', yscale='log')
    ax6.plot(q_un_max_data[:, 0], q_un_max_data_[:, 1], marker='x')
    ax6.plot(q_un_max_data[:, 0], q_un_max_data_[:, 2], marker='s')
    ax6.plot(q_un_max_data[:, 0], q_un_max_data_[:, 3], marker='o')
    ax6.plot(q_un_max_data[:, 0], q_un_max_data_[:, 4], marker='^')
    ax6.set_title('(f) UN,MAX', loc='center', y=-0.28, fontweight='bold')
    # ax6.set_ylim(10, 100000)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=4, frameon=False)
    plt.tight_layout()
    plt.subplots_adjust(top=0.95, hspace=0.3)

    fig.savefig('export/querysize.pdf', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
