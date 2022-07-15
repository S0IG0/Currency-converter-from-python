import matplotlib.pyplot as plt
from datetime import date
import matplotlib.dates as mdates
from get_value_from_name import get_week_from_name


def render(name_value: str, function=get_week_from_name):

    data = function(name_value)

    y = [item[-1] for item in data]
    events = [date(*map(lambda x: int(x), item[0])) for item in data]

    days = mdates.DayLocator()
    time_norm = mdates.DateFormatter('%Y-%m-%d')

    fig, ax = plt.subplots()
    plt.plot(events, y,
             linestyle='-',
             linewidth=2,
             color='0',
             marker='o',
             markersize=3,
             )

    plt.grid(True)
    ax.xaxis.set_major_formatter(time_norm)
    ax.xaxis.set_minor_locator(days)
    plt.xticks(rotation=90)
    plt.tight_layout()
    # plt.savefig(r'Data\foo.png', dpi=80, transparent=True)
    # plt.show()

    return fig


if __name__ == '__main__':
    render('Доллар США')
