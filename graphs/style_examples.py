"""Reference renders of the house style: the isoquant figure and mock exam Ex. 3."""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import econ_style as es

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples")
os.makedirs(OUT, exist_ok=True)

# --- Fig. I(a): isoquant and isocost lines (the reference picture) ---
fig, ax = es.figure("$x_1$", "$x_2$",
                    caption="Fig. I(a). The lowest isocost line that reaches the isoquant "
                            "touches it at $x^*$, where $TRS = w_1/w_2$.")
x = np.linspace(1.35, 9.8, 200)
k = 3.6 * 3.0                      # isoquant x1*x2 = k, tangent at (3.6, 3.0)
es.line(ax, x, k / x, es.NAVY, lw=2.6)
es.note(ax, 1.75, 9.4, r"isoquant $f(x_1,x_2) = y$", es.NAVY)
slope = -3.0 / 3.6                 # tangent slope at x*
for c, col, lw, lab in [(-1.6, es.TAN, 2, "$C_0$"), (0, es.RUST, 2.4, "$C^*$"),
                        (2.0, es.TAN, 2, "$C_1$")]:
    xs = np.linspace(0, 10, 50)
    ys = 3.0 + c + slope * (xs - 3.6)
    keep = (ys >= 0) & (ys <= 9.8)
    es.line(ax, xs[keep], ys[keep], col, lw=lw, label=lab, dx=-0.6, dy=0.25)
es.note(ax, 6.3, 9.4, r"isocost slope $-w_1/w_2$", es.RUST)
es.note(ax, 7.3, 8.8, r"$C_0 < C^* < C_1$", es.RUST)
es.project(ax, 3.6, 3.0, "$x_1^*$", "$x_2^*$")
es.point(ax, 3.6, 3.0)
es.note(ax, 3.9, 3.5, r"tangency: $TRS = w_1/w_2$", fontweight="bold")
es.save(fig, os.path.join(OUT, "isoquant_isocost.png"))

# --- Mock exam Ex. 3: rate cut from 0.05 to 0.01, IS-LM and money market ---
fig, (a1, a2) = es.figure(["Y", "M/P"], ["i", "i"], size=(14, 7.2), ncols=2,
                          caption="Fig. 3. The rate cut moves the economy down along IS "
                                  "and forces the central bank to supply more money.")
# map: Y 600..1000 -> 0..10, i 0..0.07 -> 0..10
X = lambda y: (y - 600) / 40
I = lambda i: i / 0.007
ys = np.linspace(700, 900, 50)
es.line(a1, X(ys), I((580 - 0.64 * ys) / 2000), es.NAVY, label="IS", at=0, dx=0.25, dy=-0.1)
es.line(a1, [0, 10], [I(0.05)] * 2, es.TAN, label="LM", dx=-0.8, dy=0.2)
es.line(a1, [0, 10], [I(0.01)] * 2, es.RUST, label="LM'", dx=-0.8, dy=0.2)
es.arrow(a1, (1.2, I(0.047)), (1.2, I(0.014)), es.RUST)
es.project(a1, X(750), I(0.05), "750", "0.05")
es.project(a1, X(875), I(0.01), "875", "0.01")
es.point(a1, X(750), I(0.05), "A")
es.point(a1, X(875), I(0.01), "B")
# money market: M/P 250..450 -> 0..10; Md/P = 0.5Y - 1000 i
M = lambda m: (m - 250) / 20
for yv, col, lab in [(750, es.NAVY, "$M^d$"), (875, es.GREEN, r"$M^{d\prime}$")]:
    iv = np.linspace(0.0, 0.068, 30)
    es.line(a2, M(0.5 * yv - 1000 * iv), I(iv), col, label=lab, at=-1, dx=-0.15, dy=0.0, ha="right")
for mv, col, lab in [(325, es.TAN, "$M^s$"), (427.5, es.RUST, r"$M^{s\prime}$")]:
    es.line(a2, [M(mv)] * 2, [0, 9.6], col, label=lab, dx=-0.15, dy=0.1)
es.arrow(a2, (M(345), 8.6), (M(405), 8.6), es.RUST)
es.project(a2, M(325), I(0.05), "325", "0.05")
es.project(a2, M(427.5), I(0.01), "427.5", "0.01")
es.point(a2, M(325), I(0.05), "A", dx=-0.5)
es.point(a2, M(427.5), I(0.01), "B")
es.save(fig, os.path.join(OUT, "mock_ex3_rate_cut.png"))
print("ok")
