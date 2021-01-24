import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォントを設定
    fig = plt.figure(figsize=(6, 9), dpi=300)
    test_size = 100

    gs_ne_sum_data = np.loadtxt('data/GS-NE-SUM.csv', skiprows=1, delimiter=',')
    gs_ne_sum_data_ = gs_ne_sum_data / (10 * test_size)  # μsからmsへの変換
    ax = fig.add_subplot(321, xlabel='Grid size', ylabel='Processing time (ms)')
    ax.plot(gs_ne_sum_data[:, 0], gs_ne_sum_data_[:, 1], marker='o', label='Grid', color='#2AA02B')
    ax.plot(gs_ne_sum_data[:, 0], gs_ne_sum_data_[:, 2], marker='^', label='Quatree', color='#D62827')
    ax.set_title('(a) NE, SUM', loc='center', y=-0.27, fontweight='bold')
    # ax.set_ylim(10, 1000000)

    gs_ne_max_data = np.loadtxt('data/GS-NE-MAX.csv', skiprows=1, delimiter=',')
    gs_ne_max_data_ = gs_ne_max_data / (10 * test_size)  # μsからmsへの変換
    ax2 = fig.add_subplot(322, xlabel='Grid size', ylabel='Processing time (ms)')
    ax2.plot(gs_ne_max_data[:, 0], gs_ne_max_data_[:, 1], marker='o', color='#2AA02B')
    ax2.plot(gs_ne_max_data[:, 0], gs_ne_max_data_[:, 2], marker='^', color='#D62827')
    ax2.set_title('(b) NE, MAX', loc='center', y=-0.27, fontweight='bold')
    # ax2.set_ylim(10, 100000)

    gs_cas_sum_data = np.loadtxt('data/GS-CAS-SUM.csv', skiprows=1, delimiter=',')
    gs_cas_sum_data_ = gs_cas_sum_data / (10 * test_size)  # μsからmsへの変換
    ax3 = fig.add_subplot(323, xlabel='Grid size', ylabel='Processing time (ms)')
    ax3.plot(gs_cas_sum_data[:, 0], gs_cas_sum_data_[:, 1], marker='o', label='Grid', color='#2AA02B')
    ax3.plot(gs_cas_sum_data[:, 0], gs_cas_sum_data_[:, 2], marker='^', label='Quatree', color='#D62827')
    ax3.set_title('(c) CAS, SUM', loc='center', y=-0.27, fontweight='bold')
    # ax.set_ylim(10, 1000000)

    gs_cas_max_data = np.loadtxt('data/GS-CAS-MAX.csv', skiprows=1, delimiter=',')
    gs_cas_max_data_ = gs_cas_max_data / (10 * test_size)  # μsからmsへの変換
    ax4 = fig.add_subplot(324, xlabel='Grid size', ylabel='Processing time (ms)')
    ax4.plot(gs_cas_max_data[:, 0], gs_cas_max_data_[:, 1], marker='o', color='#2AA02B')
    ax4.plot(gs_cas_max_data[:, 0], gs_cas_max_data_[:, 2], marker='^', color='#D62827')
    ax4.set_title('(d) CAS, MAX', loc='center', y=-0.27, fontweight='bold')
    # ax2.set_ylim(10, 100000)

    gs_un_sum_data = np.loadtxt('data/GS-UN-SUM.csv', skiprows=1, delimiter=',')
    gs_un_sum_data_ = gs_un_sum_data / (10 * test_size)  # μsからmsへの変換
    ax5 = fig.add_subplot(325, xlabel='Grid size', ylabel='Processing time (ms)')
    ax5.plot(gs_un_sum_data[:, 0], gs_un_sum_data_[:, 1], marker='o', label='Grid', color='#2AA02B')
    ax5.plot(gs_un_sum_data[:, 0], gs_un_sum_data_[:, 2], marker='^', label='Quatree', color='#D62827')
    ax5.set_title('(e) UN, SUM', loc='center', y=-0.27, fontweight='bold')
    # ax.set_ylim(10, 1000000)

    gs_un_max_data = np.loadtxt('data/GS-UN-MAX.csv', skiprows=1, delimiter=',')
    gs_un_max_data_ = gs_un_max_data / (10 * test_size)  # μsからmsへの変換
    ax6 = fig.add_subplot(326, xlabel='Grid size', ylabel='Processing time (ms)')
    ax6.plot(gs_un_max_data[:, 0], gs_un_max_data_[:, 1], marker='o', color='#2AA02B')
    ax6.plot(gs_un_max_data[:, 0], gs_un_max_data_[:, 2], marker='^', color='#D62827')
    ax6.set_title('(f) UN, MAX', loc='center', y=-0.27, fontweight='bold')
    # ax2.set_ylim(10, 100000)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=2, frameon=False)
    plt.tight_layout()
    plt.subplots_adjust(top=0.95, hspace=0.3)

    fig.savefig('export/gridsize.pdf', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
