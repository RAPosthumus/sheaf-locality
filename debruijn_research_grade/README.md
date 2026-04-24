
# De Bruijn Sheaf/Homology Research-Grade Bundle

Files:
- debruijn_sheaf_homology_paper.tex: LaTeX source.
- debruijn_sheaf_homology_paper.pdf: compiled paper PDF.
- debruijn_sheaf_visualizer.py: runnable Python visualization/demo tool.
- sample_figures/: generated example figures.

Run:
python debruijn_sheaf_visualizer.py --n 6 --out my_figures

Core idea:
De Bruijn cycles are global sections of a locality sheaf. Exact G_{q,q}
structure is a homological cycle condition. Near-G defects are boundaries.
Pattern quotienting by S_q creates a compressed skeleton with fiber-lifting
obstructions.
