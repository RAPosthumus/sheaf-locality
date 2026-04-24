#!/usr/bin/env python3
"""
debruijn_sheaf_visualizer.py

A small research demo for the de Bruijn / sheaf / homology framework.

Features
--------
1. Build B(2,n) for small n and save a graph fragment.
2. Draw the special R_6 orbit.
3. Draw kernel basins for n=6.
4. Build a tiny DNA/RNA-style reconstruction demo from fragments.
5. Export figures as PNG files.

Usage
-----
python debruijn_sheaf_visualizer.py --out out_dir
python debruijn_sheaf_visualizer.py --n 6 --out out_dir
"""

from __future__ import annotations
import argparse
from itertools import product
from pathlib import Path
from collections import defaultdict, Counter, deque

import matplotlib.pyplot as plt


def words(n: int):
    return ["".join(bits) for bits in product("01", repeat=n)]


def K_even(s: str) -> str:
    n = len(s)
    if n % 2:
        raise ValueError("K_even requires even length")
    m = n // 2
    return s[1:m+1] + s[m-1:n-1]


def kernel_endpoint(s: str) -> str:
    seen = set()
    cur = s
    seq = []
    while cur not in seen:
        seen.add(cur)
        seq.append(cur)
        cur = K_even(cur)
    start = seq.index(cur)
    cyc = seq[start:]
    if len(cyc) == 1:
        return cyc[0]
    return "<->".join(sorted(cyc))


def R(s: str) -> str:
    return s[1:] + ("1" if s[0] == "0" else "0")


def debruijn_edges(n: int):
    return [(w, w[1:] + b) for w in words(n) for b in "01"]


def draw_r6_orbit(out: Path):
    orbit = ["001100", "011001", "110011", "100110"]
    coords = {
        orbit[0]: (0, 1),
        orbit[1]: (1, 0),
        orbit[2]: (0, -1),
        orbit[3]: (-1, 0),
    }
    fig, ax = plt.subplots(figsize=(7,7))
    for i, w in enumerate(orbit):
        x, y = coords[w]
        ax.scatter([x], [y], s=900)
        ax.text(x, y, w + "\ncp=" + w[2:4], ha="center", va="center", fontsize=10)
        w2 = orbit[(i+1)%len(orbit)]
        x2, y2 = coords[w2]
        ax.annotate("", xy=(x2,y2), xytext=(x,y), arrowprops=dict(arrowstyle="->", lw=2))
    ax.set_title("Special R6 orbit: all central-pair types")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out / "r6_orbit.png", dpi=200)
    plt.close(fig)


def draw_kernel_basin_summary(out: Path, n: int = 6):
    counts = Counter(kernel_endpoint(w) for w in words(n))
    labels = list(counts.keys())
    values = [counts[k] for k in labels]
    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(range(len(labels)), values)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.set_ylabel("number of words")
    ax.set_title(f"Kernel basin sizes for n={n}")
    fig.tight_layout()
    fig.savefig(out / f"kernel_basins_n{n}.png", dpi=200)
    plt.close(fig)


def draw_debruijn_fragment(out: Path, n: int = 6, start: str = "111111", depth: int = 2):
    edges = debruijn_edges(n)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    seen = {start}
    q = deque([(start,0)])
    subedges = []
    while q:
        u, d = q.popleft()
        if d >= depth:
            continue
        for v in adj[u]:
            subedges.append((u,v))
            if v not in seen:
                seen.add(v)
                q.append((v,d+1))
    nodes = sorted(seen)
    # circular layout
    import math
    coords = {}
    for i, node in enumerate(nodes):
        ang = 2*math.pi*i/len(nodes)
        coords[node] = (math.cos(ang), math.sin(ang))
    fig, ax = plt.subplots(figsize=(8,8))
    for u, v in subedges:
        x1,y1 = coords[u]
        x2,y2 = coords[v]
        ax.annotate("", xy=(x2,y2), xytext=(x1,y1), arrowprops=dict(arrowstyle="->", lw=1, alpha=0.6))
    for node in nodes:
        x,y = coords[node]
        ax.scatter([x],[y], s=500)
        ax.text(x,y,node, ha="center", va="center", fontsize=8)
    ax.set_title(f"Fragment of B(2,{n}) around {start}")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out / f"debruijn_fragment_n{n}.png", dpi=200)
    plt.close(fig)


def reconstruct_from_fragments(fragments):
    """Simple directed Eulerian reconstruction for equal-length fragments."""
    k = len(fragments[0]) - 1
    adj = defaultdict(list)
    indeg = Counter()
    outdeg = Counter()
    for f in fragments:
        u, v = f[:-1], f[1:]
        adj[u].append(v)
        outdeg[u] += 1
        indeg[v] += 1
    start = fragments[0][:-1]
    for node in set(indeg) | set(outdeg):
        if outdeg[node] - indeg[node] == 1:
            start = node
            break
    stack = [start]
    path = []
    local_adj = {u: vs[:] for u, vs in adj.items()}
    while stack:
        u = stack[-1]
        if local_adj.get(u):
            stack.append(local_adj[u].pop())
        else:
            path.append(stack.pop())
    path = path[::-1]
    if not path:
        return ""
    seq = path[0] + "".join(p[-1] for p in path[1:])
    return seq


def draw_dna_demo(out: Path):
    fragments = ["ATG", "TGA", "GAT"]
    seq = reconstruct_from_fragments(fragments)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.text(0.05,0.8,"Fragments: " + ", ".join(fragments), fontsize=14)
    ax.text(0.05,0.55,"Nodes: AT, TG, GA", fontsize=14)
    ax.text(0.05,0.30,"Eulerian reconstruction: " + seq, fontsize=14)
    ax.text(0.05,0.10,"Sheaf view: fragments = local sections; overlaps = restrictions; sequence = global section", fontsize=10)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(out / "dna_reconstruction_demo.png", dpi=200)
    plt.close(fig)


def write_readme(out: Path):
    (out / "README.txt").write_text(
        "debruijn_sheaf_visualizer outputs:\n"
        "- r6_orbit.png: special R6 orbit sampling all central-pair classes\n"
        "- kernel_basins_n6.png: kernel basin size summary\n"
        "- debruijn_fragment_n6.png: local graph fragment of B(2,6)\n"
        "- dna_reconstruction_demo.png: fragment-to-global-section demo\n",
        encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=6)
    parser.add_argument("--out", type=str, default="debruijn_viz_out")
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    draw_r6_orbit(out)
    draw_kernel_basin_summary(out, args.n)
    draw_debruijn_fragment(out, args.n)
    draw_dna_demo(out)
    write_readme(out)
    print(f"Wrote figures to {out}")


if __name__ == "__main__":
    main()
