import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/home/user/Macro/graphs"
os.makedirs(OUT, exist_ok=True)

INK = "#1f2328"
MUTED = "#6e7781"
GRID = "#d0d7de"
BEFORE = "#1f2328"
AFTER = "#2a6fdb"
WARN = "#d9622b"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 150,
})


def drop(ax, x, y, x0=0, y0=0):
    ax.plot([x, x], [y0, y], ls=":", color=MUTED, lw=1)
    ax.plot([x0, x], [y, y], ls=":", color=MUTED, lw=1)


def point(ax, x, y, label, color, dx=0, dy=0, ha="left"):
    ax.plot(x, y, "o", ms=8, color=color, mec="white", mew=2, zorder=5)
    ax.annotate(label, (x, y), xytext=(x + dx, y + dy), fontsize=12,
                fontweight="bold", color=INK, ha=ha)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(f"{OUT}/{name}", bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------- 1.3 Keynesian cross ----------
fig, ax = plt.subplots(figsize=(8, 6.2))
Y = np.linspace(0, 3400, 100)
ax.plot(Y, Y, color=GRID, lw=1.5)
ax.text(2950, 3250, "45°: Y = Z", color=MUTED)
ax.plot(Y, 1100 + 0.6 * Y, color=BEFORE, lw=2.2, label="Z₁ = 1100 + 0.6Y   (G = 590)")
ax.plot(Y, 1000 + 0.6 * Y, color=AFTER, lw=2.2, label="Z₂ = 1000 + 0.6Y   (G = 490)")
drop(ax, 2750, 2750)
drop(ax, 2500, 2500)
point(ax, 2750, 2750, "A", BEFORE, dx=-40, dy=110, ha="right")
point(ax, 2500, 2500, "B", AFTER, dx=60, dy=-170)
ax.annotate("", xy=(300, 1000 + 180), xytext=(300, 1100 + 180),
            arrowprops=dict(arrowstyle="->", color=AFTER, lw=1.8))
ax.text(360, 1150, "ΔG = −100", color=INK)
ax.annotate("", xy=(2500, 180), xytext=(2750, 180),
            arrowprops=dict(arrowstyle="->", color=AFTER, lw=1.8))
ax.text(2625, 240, "ΔY = −250", ha="center", color=INK)
ax.set_xticks([2500, 2750]); ax.set_yticks([1000, 1100, 2500, 2750])
ax.set_xlim(0, 3400); ax.set_ylim(0, 3400)
ax.set_xlabel("Y, output and income"); ax.set_ylabel("Z, demand")
ax.set_title("1.3  Keynesian cross: G falls by 100, output falls by 250",
             loc="left", fontweight="bold", color=INK)
ax.legend(loc="upper left", frameon=False)
save(fig, "1_3_keynesian_cross.png")

# ---------- 2.3 IS-LM ----------
fig, ax = plt.subplots(figsize=(8, 6.2))
i = np.linspace(0.0, 0.11, 100)
ax.plot(3975 - 7500 * i, i, color=INK, lw=2.2)
ax.text(3975 - 7500 * 0.105 + 20, 0.105, "IS:  Y = 3975 − 7500i", color=INK)
ax.axhline(0.03, color=BEFORE, lw=2.2, xmin=0.02)
ax.axhline(0.07, color=AFTER, lw=2.2, xmin=0.02)
ax.text(3990, 0.032, "LM  (i = 0.03)", color=INK)
ax.text(3990, 0.072, "LM′ (i = 0.07)", color=AFTER)
drop(ax, 3750, 0.03, x0=3100)
drop(ax, 3450, 0.07, x0=3100)
point(ax, 3750, 0.03, "A", BEFORE, dx=30, dy=-0.009)
point(ax, 3450, 0.07, "B", AFTER, dx=30, dy=0.004)
ax.annotate("", xy=(3200, 0.068), xytext=(3200, 0.032),
            arrowprops=dict(arrowstyle="->", color=AFTER, lw=1.8))
ax.text(3215, 0.05, "central bank\nraises i", color=INK)
ax.set_xlim(3100, 4150); ax.set_ylim(0, 0.11)
ax.set_xticks([3450, 3750]); ax.set_yticks([0.03, 0.07])
ax.set_xlabel("Y, output"); ax.set_ylabel("i, interest rate")
ax.set_title("2.3  IS-LM: flat LM moves up, economy slides along IS (A → B)",
             loc="left", fontweight="bold", color=INK)
ax.text(3800, 0.092, "A: Y = 3750, I = 180, C = 2640\nB: Y = 3450, I = 60,  C = 2460",
        color=MUTED, fontsize=10)
save(fig, "2_3_IS_LM.png")

# ---------- 2.3 Money market ----------
fig, ax = plt.subplots(figsize=(8, 6.2))
m = np.linspace(2950, 3420, 100)
ax.plot(m, (0.9 * 3750 - m) / 1000, color=BEFORE, lw=2.2)
ax.plot(m, (0.9 * 3450 - m) / 1000, color=AFTER, lw=2.2)
ax.text(3240, 0.105, "Mᵈ/P (Y = 3750)", color=INK, ha="right")
ax.text(3085, 0.04, "Mᵈ/P (Y = 3450)", color=AFTER)
ax.axvline(3345, color=BEFORE, lw=1.6, ls="--")
ax.axvline(3035, color=AFTER, lw=1.6, ls="--")
ax.text(3350, 0.09, "Mˢ/P = 3345\n(Mˢ = 6690)", color=INK, fontsize=10)
ax.text(3040, 0.09, "Mˢ/P = 3035\n(Mˢ = 6070)", color=AFTER, fontsize=10)
ax.plot([2950, 3345], [0.03, 0.03], ls=":", color=MUTED, lw=1)
ax.plot([2950, 3035], [0.07, 0.07], ls=":", color=MUTED, lw=1)
point(ax, 3345, 0.03, "A", BEFORE, dx=12, dy=0.004)
point(ax, 3035, 0.07, "B", AFTER, dx=12, dy=0.004)
ax.annotate("", xy=(3060, 0.02), xytext=(3320, 0.02),
            arrowprops=dict(arrowstyle="->", color=AFTER, lw=1.8))
ax.text(3190, 0.008, "CB sells bonds: real money −310", ha="center", color=INK)
ax.set_xlim(2950, 3440); ax.set_ylim(0, 0.125)
ax.set_xticks([3035, 3345]); ax.set_yticks([0.03, 0.07])
ax.set_xlabel("M/P, real money"); ax.set_ylabel("i, interest rate")
ax.set_title("2.3  Money market: Y falls → demand shifts left, supply cut to hold i = 7%",
             loc="left", fontweight="bold", color=INK, fontsize=11.5)
save(fig, "2_3_money_market.png")


# ---------- 3.3 Debt dynamics ----------
def staircase(ax, slope, d, b0, n, color):
    b = b0
    ax.plot([b, b], [0, slope * b + d], color=color, lw=1.2)
    for _ in range(n):
        nb = slope * b + d
        ax.plot([b, b], [b if _ else 0, nb], color=color, lw=1.2)
        ax.plot([b, nb], [nb, nb], color=color, lw=1.2)
        b = nb
    return b


fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13, 6))
slope, d = 1.10 / 1.15, 0.05
bstar = d / (1 - slope)
x = np.linspace(0, 2, 100)
ax.plot(x, x, color=GRID, lw=1.5); ax.text(1.53, 1.585, "45°", color=MUTED)
ax.plot(x, slope * x + d, color=AFTER, lw=2.2)
ax.text(1.02, 1.45, "b_t = 0.957·b_(t−1) + 0.05\nslope < 1  (i = 10% < g = 15%)\n(zoomed around b*; intercept d = 0.05)", color=INK, fontsize=10)
bb = 1.5
for k in range(12):
    nb = slope * bb + d
    ax.plot([bb, bb], [bb if k else 1.0, nb], color=WARN, lw=1.4)
    ax.plot([bb, nb], [nb, nb], color=WARN, lw=1.4)
    bb = nb
drop(ax, bstar, bstar, x0=1.0, y0=1.0)
point(ax, bstar, bstar, "b* = 1.15", INK, dx=0.01, dy=-0.04)
ax.plot(1.5, 1.0, "o", ms=8, color=WARN, mec="white", mew=2, clip_on=False, zorder=5)
ax.text(1.5, 1.015, "b₀ = 1.5 ", ha="right", color=INK)
ax.set_xlim(1.0, 1.6); ax.set_ylim(1.0, 1.6)
ax.set_xticks([1.0, 1.15, 1.3, 1.5]); ax.set_yticks([1.0, 1.15, 1.3, 1.5])
ax.set_xlabel("b last year  (b_(t−1))"); ax.set_ylabel("b this year  (b_t)")
ax.set_title("Phase diagram: steps go down to b*", loc="left", fontweight="bold", color=INK)

T = np.arange(0, 61)
b = [1.5]
for _ in T[1:]:
    b.append(slope * b[-1] + d)
ax2.plot(T, b, color=AFTER, lw=2.2)
ax2.axhline(bstar, color=INK, ls="--", lw=1.2); ax2.text(45, 1.11, "b* = 115%", color=INK)
ax2.axhline(0.6, color=WARN, ls=":", lw=1.4); ax2.text(45, 0.62, "Maastricht 60%", color=WARN)
ax2.plot(0, 1.5, "o", ms=8, color=AFTER, mec="white", mew=2)
ax2.text(1.5, 1.505, "150% → 148.5% → 147.1% → …", color=INK)
ax2.set_ylim(0.4, 1.7); ax2.set_xlim(0, 60)
ax2.set_xlabel("years"); ax2.set_ylabel("debt / GDP")
ax2.set_title("Time path: converges to 115%, not to 60%", loc="left", fontweight="bold", color=INK)
fig.suptitle("3.3  Debt-to-GDP with i = 10%, g = 15%, d = 0.05", x=0.01, ha="left",
             fontweight="bold", color=INK, fontsize=13)
save(fig, "3_3_debt_stable.png")

# ---------- 3.3 Contractionary monetary policy ----------
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13, 6))
s2 = 1.20 / 1.15
x = np.linspace(0, 3, 100)
ax.plot(x, x, color=GRID, lw=1.5); ax.text(2.85, 2.6, "45°", color=MUTED)
ax.plot(x, slope * x + d, color=AFTER, lw=2, label="i = 10%: slope 0.957 (stable)")
ax.plot(x, s2 * x + d, color=WARN, lw=2.2, label="i = 20%: slope 1.043 (explodes)")
staircase(ax, s2, d, 1.5, 12, WARN)
ax.plot(1.5, 0, "o", ms=8, color=WARN, mec="white", mew=2, clip_on=False, zorder=5)
ax.text(1.5, 0.07, "b₀ = 1.5", ha="center", color=INK)
ax.set_xlim(0, 3); ax.set_ylim(0, 3)
ax.set_xlabel("b last year  (b_(t−1))"); ax.set_ylabel("b this year  (b_t)")
ax.legend(loc="upper left", frameon=False)
ax.set_title("Line above 45°: no crossing, steps climb away", loc="left",
             fontweight="bold", color=INK)

T = np.arange(0, 31)
for rate, col, lab in [(0.10, AFTER, "i = 10% < g  → converges"),
                       (0.15, MUTED, "i = 15% = g  → rises by d each year"),
                       (0.20, WARN, "i = 20% > g  → explodes")]:
    s = (1 + rate) / 1.15
    b = [1.5]
    for _ in T[1:]:
        b.append(s * b[-1] + d)
    ax2.plot(T, b, color=col, lw=2.2, label=lab)
ax2.set_xlim(0, 30); ax2.set_ylim(1, 6)
ax2.set_xlabel("years"); ax2.set_ylabel("debt / GDP")
ax2.legend(loc="upper left", frameon=False)
ax2.set_title("Raising i above g turns convergence into explosion", loc="left",
              fontweight="bold", color=INK)
fig.suptitle("3.3  Contractionary monetary policy: i ↑ raises the slope (1+i)/(1+g)",
             x=0.01, ha="left", fontweight="bold", color=INK, fontsize=13)
save(fig, "3_3_debt_contractionary.png")
print("ok")
