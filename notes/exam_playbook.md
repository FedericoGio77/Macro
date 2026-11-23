# Macro midterm playbook

How to solve the exercises the way the course expects, built from the mock exam
(`Mock_exam_midterm_.pdf`), the weeks 1–4 notes and the Module 4–5 lectures.

## How the mock exam answers are written

Every numeric part follows the same three moves, and the official solutions show all of them:

1. **Write the equilibrium condition with the numbers plugged in.**
   `Y = C + I + G = 80 + 0.5(Y − 0.25Y + 10) + 120 + 80`
2. **Collect Y and divide by the multiplier denominator.**
   `Y = 1/(1 − 0.5(1 − 0.25)) · 285 = 1/0.625 · 285 = 456`
3. **Back out the rest in order:** `Y_D = Y − tY + TR`, `C = c0 + c1·Y_D`,
   `I = I0 − d·i`, `M^s = P·(M^d/P)`.

Discussion parts ("discuss the meaning and logic", "economic intuition") want 2–4 sentences:
definition of each curve, then the causal chain, then what the central bank does on the money market.

The graph parts want the standard picture with the points labelled by the numbers from the exercise.

## Answer format the user wants (exactly like the mock exam solutions)

Go exercise by exercise, part by part, in the order of the paper: Exercise 1 a), b), c), then Exercise 2 a), b), …
For each part:

1. Copy the question line (e.g. **b) Assume that G diminishes to 60. Find equilibrium values of …**).
2. If it asks to "discuss the meaning/logic", start with the definitions in words
   (e.g. "The IS equation represents all the combinations of Y and i for which the goods market is in equilibrium.").
3. Show the full calculation: the equation with numbers, the step collecting Y, the multiplier fraction, the result,
   then every other variable the question asks for, each on its own line (`Y_D = … = 352`, `C = … = 256`).
   Say what you substitute ("Substitute the LM into the IS:", "To find Ms set Ms/P = Md/P with P = 1:").
4. Answer only what the question asks, but answer all of it (if it asks for money supply, give M^s).
5. Graph parts: draw the graph right there in that part, in the house style, then the comment paragraph
   (adjustment / economic intuition: causal chain + money market + what the central bank does).
6. Theory extras the solutions add when relevant (e.g. the IS solved for i with its slope and intercept when t changes).

Write the solutions in English (exam language); talk to the user in Bulgarian.

## Mock exam: the four exercise types

| Ex. | Type | What to compute | Graph |
|---|---|---|---|
| 1 | Keynesian cross, proportional tax and TR | Y, Y_D, C before and after ΔG | 45° line, Z shifts down, Y*' < Y* |
| 2 | IS-LM with i fixed by the central bank | IS equation, Y, Y_D, C, I, M^s; then a change in t | Money market (Md shifts, Ms follows) + IS-LM (IS **rotates**: t changes the slope) |
| 3 | Same economy, central bank cuts i | Y, Y_D, C, I, M^s at the new i | IS-LM (flat LM moves down) + money market (Ms moves right) |
| 4 | Nominal/real GDP, growth, inflation | nominal GDP each year, real GDP at base-year prices, growth, fixed-basket inflation | none |

Mock exam numbers to check against:
- Ex. 1: Y = 456 → 424, Y_D = 352 → 328, C = 256 → 244.
- Ex. 2: IS `Y = (580 − 2000i)/0.64`, Y = 750, Y_D = 460, C = 300, I = 50, M^s = 325.
  With t = 0.2: Y = 923.08, Y_D = 748.46, C = 473.08, I = 50, M^s = 416.04.
- Ex. 3: i = 0.01: Y = 875, Y_D = 535, C = 345, I = 130, M^s = 427.5.
- Ex. 4: nominal 1000 and 1390, real 2011 = 1100, growth 10%, inflation 28%.

Key facts the solutions use:
- The **IS solved for i**: `i = (c0 + c1·TR + I0 + G)/d − [1 − c1(1 − t)]/d · Y`.
  The slope is `−[1 − c1(1 − t)]/d` and the intercept is `(c0 + c1·TR + I0 + G)/d`.
  A change in t **changes the slope** (lower t → flatter IS, it rotates out); a change in G, TR or c0 shifts it in parallel.
- **LM = i fixed by the central bank** → horizontal line. M^s is endogenous: set `M^s/P = M^d/P` at the equilibrium Y and i.
- Money market intuition: higher Y (or lower i) raises money demand; to keep i at its target the central bank must raise M^s.
- Inflation with a fixed basket: `Σ q_old·p_new / Σ q_old·p_old − 1`.

## Module 4: open economy (Mundell-Fleming)

**Lecture 1: real and financial markets in open economies**
- Nominal rate "uncertain for certain": `E_{$,€} = 1.41` means 1.41 USD per euro. E ↑ = appreciation, E ↓ = depreciation; `%ΔE = (E_{t+1} − E_t)/E_t`.
- **Real exchange rate** `ε = E·P/P^F`. ε = 1 is PPP. Example: flash drive 0.48 €, 0.42 $, E = 0.875 → ε = 0.48·0.875/0.42 = 1.
  Price in Europe 0.50 € → ε = 1.041 (real appreciation: X ↓, IM ↑, CA worsens). E falls to 0.8 → ε = 0.914 (real depreciation: X ↑, IM ↓, CA improves).
- NEER/REER: trade-weighted effective rates (a competitiveness indicator).
- `IM = IM(Y, ε)` (+, +), linear `IM = im1·Y + im2·ε`; `X = X(Y^F, ε)` (+, −), linear `X = x1·Y^F − x2·ε`.
- Demand: `Z = C + I + G + X − IM/ε`. Imports are divided by ε to express them in domestic goods (`P^F·IM/(E·P)`).
- Equilibrium: `Y = 1/(1 − c1(1 − t) − d1 + im1/ε) · [c0 + G + I0 − d2·i + x1·Y^F − x2·ε − im2]`.
  The multiplier is smaller (part of each round leaks abroad). Y^F ↑ shifts Z up and IS right; ε changes both the intercept and the slope.
- In the 45° diagram: slope of Z = `c1(1 − t) + d1 − im1/ε`, intercept = autonomous spending.
- **NX = X − IM/ε = x1·Y^F − x2·ε − (im1·Y + im2·ε)/ε**, decreasing in Y (the NX line in Y slopes down).
  G ↑: Y ↑, NX ↓ (move along the NX line). Y^F ↑: Y ↑ and NX ↑ (NX line shifts up by x1·ΔY^F).
- `∂NX/∂ε = ∂X/∂ε − (1/ε)·∂IM/∂ε + IM/ε²`: two negative quantity effects, one positive price effect.
  With rigid X and IM an appreciation can improve NX. **Marshall-Lerner**: if X and IM are elastic enough, a depreciation raises NX and shifts IS right (Y ↑ and NX ↑).
- Why depreciation can hurt: purchasing-power effect, foreign-currency debt effect (Argentina 2001: foreign debt tripled).
- **Balance of payments**: CA = goods + services + investment income + unilateral transfers; KA = capital inflows − outflows; `BP = CA + KA − ΔRes = 0`. A CA deficit is financed by KA > 0 or ΔRes < 0.
- Standard two-panel graph: IS-LM on top (i, Y), NX line below (NX, Y) with A and B aligned vertically.

**Lectures 2–3 and the case studies**
- **Open-economy IS**: `Y = 1/(1 − c1(1 − t) − d1 + im1/ε) · h[A, i, ε, Y^F]`, LM: `i = ī`.
- **Fixed exchange rate**: the central bank covers excess demand/supply of its currency with reserves.
  NX > 0 → reserves ↑ and money ↑; NX < 0 → reserves ↓ and money ↓. **Sterilization** offsets this with open-market operations (limited by reserves / domestic assets held).
- Fiscal policy under fixed rates: **effective** (G ↑ → Y ↑, imports ↑, CB sells reserves and supplies money to keep i = i^F).
- Monetary policy under fixed rates with free capital: **ineffective** (i < i^F → capital outflow → CB sells reserves, money falls, back to A).
- Devaluation: X ↑, IM ↓ → IS shifts right (if Marshall-Lerner holds). Costs: dearer imports, inflation, foreign-currency debt grows.
- Strategic games: with spillovers each country prefers the other to spend; coordination (ECOFIN) helps. Payoff matrices: benefit = ΔY + weighted ΔBudget + weighted ΔNX.
- **UIP**: `i_EUR = i_US − (E^e_{t+1} − E_t)/E_t`, i.e. `E_t = E^e_{t+1}·(1 + i)/(1 + i^F)`. With risk premia: `+ φ_t` (exchange risk) `+ ψ_t` (default risk).
  Example: i_EUR = 3%, i_US = 1% → the euro must depreciate 2% over time, so it appreciates now.
- **Flexible rates**: i ↓ → capital outflow → depreciation → NX ↑, so monetary policy is effective and IS is flatter.
  G ↑ at fixed i: Y ↑, E unchanged, NX worsens. CB raising i after G ↑: appreciation, Y back down, NX improves through lower imports.
- **J curve**: right after a depreciation NX worsens, then improves as quantities adjust.
- **PPP**: law of one price `E·P_i = P_i^F`; absolute PPP `E·P/P^F = const`; relative PPP: `%ΔE = π^F − π`.
- **Crises**: expected devaluation raises the required rate. Example: 20% devaluation with p = 50% → `E^e = 0.9E` → `i_A = i_B + 0.1`. Argentina 2001-02 (Brazil devaluation, IS left, market-imposed rate i^F + 0.15, devaluation); South Korea 1997 (ψ then φ, then devaluation, point D).

## Module 5: labour market, Phillips curve, IS-LM-PC

**Labour market definitions**
- `P = LF + I`, `LF = L + U`, `u = U/LF`, participation `LF/P`, inactivity `1 − LF/P`, employment rate `L/P`.
- Labour demand: `p·f'(K̄, N) = w` → `f'(N) = w/p` (downward sloping). Supply upward sloping (substitution effect dominates). Real wage above equilibrium → unemployment (segment BA); below → excess demand.
- Natural unemployment u* > 0: frictional, structural, efficiency wages, unions, protection, minimum wage. Cyclical = u − u*. NAIRU.

**WS-PS (medium-run wages)**
- WS: `W = P^e·A·F(u, z)`; with P^e = P: `W/P = A·F(u, z)` (down in u, up in z).
- PS: `P = (1 + m)·W/A` → `W/P = A/(1 + m)` (flat line).
- Natural rate where `A/(1 + m) = A·F(u_n, z)`; A does not matter.
- z ↑ (benefits) → WS up → u_n ↑. m ↑ (antitrust, oil shock) → PS down → u_n ↑.
- `N_n = L(1 − u_n)`, `Y_n = A·L(1 − u_n)`.

**Phillips curve**
- `π_t = π^e_t + m + z − α·u_t`, `u_n = (m + z)/α`, so `π_t = π^e_t − α(u_t − u_n)`.
- Anchored expectations `π^e = π̄`: trade-off between π and u.
- Static expectations `π^e_t = π_{t−1}`: `π_t − π_{t−1} = −α(u_t − u_n)`; u < u_n → inflation accelerates.
- Adaptive: `π^e_t = π_{t−1} + ν(π^e_{t−1} − π_{t−1})`. Example: 6%, 4%, ν = 0.5 → 5%.
- Indexation share λ: `π_t = π_{t−1} − α/(1 − λ)·(u_t − u_n)`.
- Deflation: nominal wage cuts are resisted, so the curve flattens (Great Depression, Portugal 2012).

**IS-LM-PC**
- `Y_t = Y_n + A·L(u_n − u_t)`; PC in output: `π_t − π_{t−1} = (α/AL)(Y − Y_n)`.
- Okun: `u_t − u_{t−1} = −(g_y − ḡ_y)`.
- Real rate `1 + r = (1 + i)/(1 + π^e)`, `r ≈ i − π^e`. IS uses r; CB sets r (LM: r = r̄).
- System: `Y = (c0 + I0 + G − d2·r)/(1 − c1(1 − t) − d1)`, `r = r̄`, `π_t = π_{t−1} + (α/AL)(Y − Y_n)`.
- Graph: IS-LM on top (r, Y), PC below (π_t − π_{t−1}, Y) crossing zero at Y_n.
- Y > Y_n → inflation rises → CB raises r to r_n (medium-run point A′, natural rate r_n).
- Anchored: inflation returns to π̄ after the CB acts. Not anchored: it stays at the higher level.
- Fiscal consolidation: IS left, Y < Y_n, inflation falls; CB cuts to r_n′ → Y back to Y_n with more I, less G (needs room above the ZLB).
- Oil shock = m ↑ → u_n ↑, Y_n ↓, PC shifts up → stagflation; CB raises r → Y falls to Y_n′.
- ZLB: `r = 0 − π^e`; with π^e ≤ 0 the needed negative r is unreachable → deflationary spiral (unless expectations anchored or fiscal expansion).

## Graph style (what the user asked for)

Use `graphs/econ_style.py`; `graphs/style_examples.py` shows two finished examples.
The reference picture is the isoquant/isocost figure (`graphs/examples/isoquant_isocost.png`):

- warm card background with a rounded border, black arrow axes, axis names at the arrow tips
- **navy** = the curve that stays put (isoquant, IS, original money demand)
- **tan** = old / other lines, **rust** = new or optimal line, **green** = a second shifted curve
- black dot at each equilibrium, dashed grey projections to the axes, values or starred labels at the axes (Y*, Y*', 0.05)
- short labels at the ends of the lines, in the line's colour
- an arrow showing the shift
- a caption under the plot: **Fig. N.** in bold, then one sentence saying what the figure shows
- two panels side by side when the exercise has a money market and an IS-LM part

Render every graph, look at it, and fix overlapping labels before sending it.
