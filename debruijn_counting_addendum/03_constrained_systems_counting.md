# 03 - Counting and construction for constrained systems

## Constrained de Bruijn problem

Let

\[
H\subseteq B(q,n)
\]

be a subgraph defined by constraints.

Examples:

- forbidden words or transitions;
- DNA/RNA read constraints;
- patient-specific contraindications;
- atmospheric disturbance or sensor constraints.

The central question becomes:

\[
N_{\mathcal C}(q,n)
=
\#\{\text{global sections satisfying constraints }\mathcal C\}.
\]

## Homological condition

For the edge chain

\[
c_H=\sum_{e\in E(H)}e,
\]

the boundary is

\[
\partial c_H.
\]

If

\[
\partial c_H=0,
\]

then \(H\) is balanced and may support global cycles.

If

\[
\partial c_H\neq0,
\]

then \(H\) has near-\(G\) defects.

The defect function is

\[
\delta_H(v)=\deg_H^+(v)-\deg_H^-(v),
\]

and

\[
(\partial c_H)(v)=-\delta_H(v).
\]

## Counting constrained cycles

If \(H\) is connected and Eulerian, BEST applies:

\[
\operatorname{ec}(H)=t_w(H)\prod_v(\deg(v)-1)!.
\]

If not, one must either repair the boundary or treat the boundary as a source/sink obstruction.

## DNA/RNA reconstruction

Fragments are local sections. Overlaps are restriction maps. The reconstructed sequence is a global section.

Errors, missing reads, or repeats create gluing ambiguity or boundary defects.

The count

\[
N_{\text{assembly}}
\]

is the number of compatible global sections satisfying read constraints.

## Evidence-based prescription

A patient state/history window is a local section. Treatment choices are transitions. Evidence, prior adverse effects, and patient constraints remove or weight transitions.

A coherent treatment plan is a path through admissible transitions. Boundary defects indicate states where safe continuation or consistent recommendation fails.

This is not an automated prescription system; it is a structural decision-support model for identifying incompatible or underdetermined treatment paths.

## Weather and atmospheric disturbance

Local measurements are sections. Overlap in time or space gives restriction maps. A reconstructed atmospheric state is a global section.

Disturbances and noise appear as gluing defects:

\[
\partial c\neq0.
\]

Counting or sampling compatible global sections gives uncertainty estimates and anomaly signals.

## General constrained formula

For any constraint family \(\mathcal C\),

\[
N_{\mathcal C}(q,n)
=
\sum_{\text{valid pattern skeletons }S}
|\operatorname{Lift}_{\mathcal C}(S)|.
\]

This extends the classical de Bruijn count from unconstrained global sections to constrained global sections.
