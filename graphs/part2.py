"""Graphs for Part 2: problems 4.2, 4.3, 5.2 and 6.2."""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import econ_style as es

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "part2")
os.makedirs(OUT, exist_ok=True)

# ---------- Problem 4: IS-LM (r, Y) on top, PC (π − π^e, Y) below ----------
X4 = lambda y: (y - 2600) / 50          # Y 2600..3100
R4 = lambda r: r / 0.005                # r 0..0.05
P4 = lambda v: 4 + 60 * v               # π − π^e, zero axis at height 4
Ys = np.linspace(2650, 3080, 50)


def islm_pc(caption, shock):
    fig, (top, bot) = es.figure(["Y", "Y"], ["r", r"$\pi - \pi^e$"], caption=caption,
                                size=(8, 13), nrows=2, xaxis_y=[0, 4])
    es.line(top, X4(Ys), R4((3900 - Ys) / 30000), es.NAVY, label="IS", at=0, dx=0.1, dy=0.3)
    es.line(bot, X4(Ys), P4((Ys - 2850) / 3000), es.TAN if shock else es.NAVY,
            label="PC (m = 0.03)" if shock else "PC", at=-1, dx=-0.2, dy=0.35, ha="right")
    es.line(top, [0, 10], [R4(0.03)] * 2, es.TAN if shock else es.RUST,
            label="LM: r = 0.03", at=0, dx=0.3, dy=-0.6)
    es.project(top, X4(3000), R4(0.03), "3000", "0.03")
    es.point(top, X4(3000), R4(0.03), "A = A'" if shock else "A", dx=0.1, dy=0.35)
    es.project(bot, X4(3000), P4(0.05), None, "0.05", y0=4)
    es.point(bot, X4(3000), P4(0.05), "A", dx=0.25, dy=-0.6)
    bot.plot([X4(3000)] * 2, [0, 4], ls=(0, (4, 4)), color=es.MUTED, lw=1.2)
    bot.text(X4(3000), -0.35, "3000", ha="center", va="top", fontsize=13)
    bot.plot([X4(2850)] * 2, [0, 4], ls=(0, (4, 4)), color=es.MUTED, lw=1.2)
    bot.text(X4(2850), -0.35, "$Y_n$\n2850", ha="center", va="top", fontsize=13)
    bot.plot(X4(2850), 4, "o", ms=7, color=es.NAVY if not shock else es.TAN)
    if not shock:
        es.note(bot, X4(2850) + 0.3, P4(0.05) + 0.6, "output gap = 150\nπ = 0.02 + 0.05 = 0.07")
        return fig
    es.line(bot, X4(Ys), P4((Ys - 2790) / 3000), es.RUST, label="PC' (m = 0.05)",
            at=-1, dx=-0.2, dy=0.35, ha="right")
    es.arrow(bot, (X4(2930), P4(0.027) + 0.2), (X4(2880), P4(0.03) + 0.9), es.RUST)
    es.project(bot, X4(3000), P4(0.07), None, "0.07", y0=4)
    es.point(bot, X4(3000), P4(0.07), "A'", dx=0.25, dy=0.1)
    bot.plot(X4(2790), 4, "o", ms=10, color="black", zorder=6)
    bot.text(X4(2790) - 0.2, 4.5, "A''", fontsize=14, fontweight="bold", ha="right")
    bot.plot([X4(2790)] * 2, [0, 4], ls=(0, (4, 4)), color=es.MUTED, lw=1.2)
    bot.text(X4(2790), -0.35, "$Y_n'$\n2790", ha="center", va="top", fontsize=13)
    es.line(top, [0, 10], [R4(0.037)] * 2, es.RUST, label="LM': r = 0.037", at=0, dx=0.3, dy=0.25)
    es.arrow(top, (X4(2700), R4(0.0305)), (X4(2700), R4(0.0365)), es.RUST)
    es.project(top, X4(2790), R4(0.037), "2790", "0.037")
    es.point(top, X4(2790), R4(0.037), "A''", dx=-0.25, dy=0.35, ha="right")
    return fig


es.save(islm_pc("Fig. 4.2. With r = 0.03 output is 3000, above $Y_n$ = 2850: the positive output "
                "gap pushes inflation 5 points above expected inflation.", shock=False),
        os.path.join(OUT, "4_2_islm_pc.png"))
es.save(islm_pc("Fig. 4.3. The higher mark-up lowers $Y_n$ to 2790 and shifts PC up (A to A'); the "
                "central bank raises r to 0.037 and moves the economy to A''.", shock=True),
        os.path.join(OUT, "4_3_islm_pc_markup.png"))

# ---------- Problem 5: Keynesian cross, ε from 1 to 1.5 ----------
X5 = lambda y: (y - 1600) / 70          # zoomed: Y and Z from 1600 to 2300
fig, ax = es.figure("Y", "Z", size=(8, 8.4),
                    caption="Fig. 5.2. The 50% real appreciation lowers autonomous demand "
                            "(exports fall) and output drops from 2000 to 1928.6.")
yy = np.linspace(1600, 2290, 50)
ax.plot(X5(yy), X5(yy), color=es.MUTED, lw=1.2)
es.note(ax, X5(2150), X5(2250), "45°: Z = Y", es.MUTED, ha="right")
es.line(ax, X5(yy), X5(1000 + 0.5 * yy), es.TAN, label="Z (ε = 1)", at=0, dx=0.1, dy=0.3)
es.line(ax, X5(yy), X5(900 + 0.5333 * yy), es.RUST, label="Z' (ε = 1.5)", at=0, dx=0.1, dy=-0.65)
es.arrow(ax, (X5(1780), X5(1890) + 0.05), (X5(1780), X5(1849.3) - 0.1), es.RUST)
es.project(ax, X5(2000), X5(2000), "2000", "2000")
es.project(ax, X5(1928.6), X5(1928.6), "1928.6", "1928.6")
es.point(ax, X5(2000), X5(2000), "A", dx=-0.3, dy=0.3, ha="right")
es.point(ax, X5(1928.6), X5(1928.6), "B", dx=0.25, dy=-0.5)
es.save(fig, os.path.join(OUT, "5_2_keynesian_cross.png"))

# ---------- Problem 6: money market (left) and IS-LM (right) ----------
M6 = lambda m: (m - 2500) / 45          # M/P 2500..2950
I6 = lambda i: i / 0.01                 # i 0..0.1
X6 = lambda y: (y - 2700) / 80          # Y 2700..3500
fig, (mm, il) = es.figure(["M/P", "Y"], ["i", "i"], size=(14, 7.6), ncols=2,
                          caption="Fig. 6.2. G rises: IS shifts right and Y rises to 3200 at "
                                  "$i = i^f$; money demand rises and the central bank expands "
                                  "money supply to keep i at 5%.")
iv = np.linspace(0, 0.095, 30)
es.line(mm, M6(2700 - 1200 * iv), I6(iv), es.NAVY, label="$M^d$ (Y = 3000)", at=-1,
        dx=-0.15, dy=0.1, ha="right")
es.line(mm, M6(2880 - 1200 * iv), I6(iv), es.GREEN, label=r"$M^{d\prime}$ (Y = 3200)", at=0,
        dx=0.15, dy=0.3)
es.line(mm, [M6(2640)] * 2, [0, 9.7], es.TAN, label="$M^s$", dx=-0.15, dy=0.1)
es.line(mm, [M6(2820)] * 2, [0, 9.7], es.RUST, label=r"$M^{s\prime}$", dx=-0.15, dy=0.1)
es.arrow(mm, (M6(2680), 8.3), (M6(2790), 8.3), es.RUST)
es.project(mm, M6(2640), I6(0.05), "2640", "0.05")
es.project(mm, M6(2820), I6(0.05), "2820")
es.point(mm, M6(2640), I6(0.05), "A", dx=-0.25, dy=0.3, ha="right")
es.point(mm, M6(2820), I6(0.05), "B")
yv = np.linspace(2800, 3200, 30)
es.line(il, X6(yv), I6((3200 - yv) / 4000), es.TAN, label="IS (G = 780)", at=0, dx=0.2, dy=-0.1)
yv = np.linspace(3000, 3400, 30)
es.line(il, X6(yv), I6((3400 - yv) / 4000), es.RUST, label="IS' (G = 880)", at=0, dx=0.2,
        dy=-0.1)
es.line(il, [0, 10], [I6(0.05)] * 2, es.NAVY, label="LM: $i = i^f = 0.05$", at=0, dx=0.3, dy=0.3)
es.arrow(il, (X6(2930), I6(0.0725)), (X6(3130), I6(0.0725)), es.RUST)
es.project(il, X6(3000), I6(0.05), "3000", "0.05")
es.project(il, X6(3200), I6(0.05), "3200")
es.point(il, X6(3000), I6(0.05), "A", dx=-0.25, dy=0.3, ha="right")
es.point(il, X6(3200), I6(0.05), "B")
es.save(fig, os.path.join(OUT, "6_2_money_market_islm.png"))
print("ok")
