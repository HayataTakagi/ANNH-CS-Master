import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Times New Roman'  # 全体のフォントを設定
    fig = plt.figure(figsize=(6, 3.5), dpi=300)

    k_ne_sum_data = np.loadtxt('data/GS-CAS-SUM.csv', skiprows=1, delimiter=',')
    k_ne_sum_data_ = k_ne_sum_data / 10  # μsからmsへの変換
    ax = fig.add_subplot(121, xlabel='Grid size', ylabel='Processing time (ms)')
    ax.plot(k_ne_sum_data[:, 0], k_ne_sum_data_[:, 1], marker='o', label='Grid', color='#2AA02B')
    ax.plot(k_ne_sum_data[:, 0], k_ne_sum_data_[:, 2], marker='^', label='Quatree', color='#D62827')
    ax.set_title('(a) SUM', loc='center', y=-0.3, fontweight='bold')
    # ax.set_ylim(10, 1000000)

    k_ne_max_data = np.loadtxt('data/GS-CAS-MAX.csv', skiprows=1, delimiter=',')
    k_ne_max_data_ = k_ne_max_data / 10  # μsからmsへの変換
    ax2 = fig.add_subplot(122, xlabel='Grid size', ylabel='Processing time (ms)')
    ax2.plot(k_ne_max_data[:, 0], k_ne_max_data_[:, 1], marker='o', color='#2AA02B')
    ax2.plot(k_ne_max_data[:, 0], k_ne_max_data_[:, 2], marker='^', color='#D62827')
    ax2.set_title('(b) MAX', loc='center', y=-0.3, fontweight='bold')
    # ax2.set_ylim(10, 100000)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=2, frameon=False)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    fig.savefig('export/gridsize.pdf', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
