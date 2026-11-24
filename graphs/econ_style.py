"""House style for exam graphs: textbook diagrams on a warm card, like Fig. I(a).

Blue = the curve that stays put (isoquant, IS, money demand...).
Tan = the old / other lines, rust = the new / optimal line.
Black dot = equilibrium. Dashed lines project it onto the axes.
No numeric ticks unless the exercise gives numbers: points are labelled (Y*, Y*', 0.05).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import textwrap
from matplotlib.patches import FancyBboxPatch

CARD = "#efede6"
EDGE = "#d9d6cc"
INK = "#2b2b2b"
MUTED = "#6b6b6b"
NAVY = "#3d4f9f"
RUST = "#b35a2b"
TAN = "#d6b48e"
GREEN = "#4f8a5b"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "font.size": 13,
    "text.color": INK,
    "savefig.dpi": 200,
})


def figure(xlabel, ylabel, caption=None, size=(7.5, 7.5), ncols=1, nrows=1, xaxis_y=None):
    """Card-style figure. Returns (fig, axes); axes is a flat list when there are several panels.

    xaxis_y: per panel, the height (0..10) of the horizontal axis, e.g. 5 for a Phillips-curve
    panel where π − π^e can be negative.
    """
    n = ncols * nrows
    fig, axes = plt.subplots(nrows, ncols, figsize=size, squeeze=False)
    axes = list(axes.flat)
    fig.patch.set_facecolor(CARD)
    labels = [(xlabel, ylabel)] * n if isinstance(xlabel, str) else list(zip(xlabel, ylabel))
    xaxis_y = xaxis_y or [0] * n
    for ax, (xl, yl), y0 in zip(axes, labels, xaxis_y):
        ax.set_facecolor(CARD)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlim(0, 10); ax.set_ylim(0, 10)
        ax.annotate("", xy=(10.3, y0), xytext=(0, y0), annotation_clip=False,
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=18))
        ax.annotate("", xy=(0, 10.3), xytext=(0, 0), annotation_clip=False,
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6, mutation_scale=18))
        ax.text(10.2, y0 - 0.55, xl, ha="center", va="top", fontsize=14)
        ax.text(0.25, 10.3, yl, ha="left", va="center", fontsize=14)
    lines = 0
    if caption:
        # "Fig. 3. Text..." -> bold "Fig. 3." then the text, wrapped to the card width
        head, rest = caption.split(" ", 2)[:2], caption.split(" ", 2)[2]
        bold = r"$\bf{" + r"\ ".join(head) + "}$"
        wrapped = textwrap.wrap(bold + " " + rest, width=int(size[0] * 7.6))
        lines = len(wrapped)
        fig.text(0.07, 0.035 + 0.045 * lines * 7.5 / size[1], "\n".join(wrapped),
                 fontsize=16, va="top", linespacing=1.5)
    bottom = 0.1 + (0.05 * lines + 0.03) * 7.5 / size[1] if caption else 0.08
    fig.subplots_adjust(left=0.13, right=0.93, top=0.93, bottom=bottom, wspace=0.25, hspace=0.3)
    return fig, (axes[0] if n == 1 else axes)


def line(ax, x, y, color=NAVY, lw=2.4, label=None, at=-1, dx=0.1, dy=0.15, ha="left", **kw):
    ax.plot(x, y, color=color, lw=lw, solid_capstyle="round", **kw)
    if label:
        ax.text(x[at] + dx, y[at] + dy, label, color=color, fontsize=13, ha=ha)


def point(ax, x, y, label=None, dx=0.25, dy=0.2, ha="left", bold=True):
    ax.plot(x, y, "o", ms=10, color="black", zorder=6)
    if label:
        ax.text(x + dx, y + dy, label, fontsize=14, ha=ha,
                fontweight="bold" if bold else "normal")


def project(ax, x, y, xlab=None, ylab=None, x0=0, y0=0):
    ax.plot([x, x], [y0, y], ls=(0, (4, 4)), color=MUTED, lw=1.2)
    ax.plot([x0, x], [y, y], ls=(0, (4, 4)), color=MUTED, lw=1.2)
    if xlab:
        ax.text(x, y0 - 0.35, xlab, ha="center", va="top", fontsize=13)
    if ylab:
        ax.text(x0 - 0.2, y, ylab, ha="right", va="center", fontsize=13)


def arrow(ax, start, end, color=INK, lw=2):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=18))


def note(ax, x, y, text, color=INK, **kw):
    ax.text(x, y, text, color=color, fontsize=13, **kw)


def save(fig, path):
    fig.patches.append(FancyBboxPatch((0.01, 0.01), 0.98, 0.98, transform=fig.transFigure,
                                      boxstyle="round,pad=0,rounding_size=0.03",
                                      fc="none", ec=EDGE, lw=2))
    fig.savefig(path, facecolor=CARD)
    plt.close(fig)
