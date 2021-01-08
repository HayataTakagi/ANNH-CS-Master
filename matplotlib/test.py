import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def main():
    fig = plt.figure()
    data = pd.read_csv('data/K-NE-SUM.csv')
    df = data.iloc[0:10]
    ax = fig.add_subplot(111, title="main", xlabel=df.index.name, ylabel='Processing time (ms)')
    ax.plot(df['Point'])

    fig.savefig('export/1-1_a.png', facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())


if __name__ == '__main__':
    main()
