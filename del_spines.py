import matplotlib as mpl


def del_spines(ax):
    """This function deletes the x, y axes and all the four spines in the
    plot. It also disable the utility of showing the coordinates at the
    toolbar."""
    mpl.rcParams['toolbar'] = 'None'
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return ax