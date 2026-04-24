# 02 - Pattern-level counting and quotient-sheaf decomposition

## Core identity

The classical count

\[
N(q,n)=\frac{(q!)^{q^{n-1}}}{q^n}
\]

can be decomposed through the equality-pattern quotient:

\[
\boxed{
N(q,n)=
\sum_{\text{pattern skeletons }S}
|\operatorname{Lift}(S)|
}
\]

where \(S\) ranges over cycle skeletons in the quotient pattern graph and \(\operatorname{Lift}(S)\) is the set of compatible concrete symbol assignments.

## Equality-pattern quotient

The full alphabet permutation group \(S_q\) acts on words by relabeling symbols. The quotient

\[
A^n/S_q
\]

is represented by canonical equality patterns.

A pattern with \(r\) blocks has fiber size

\[
(q)_r=q(q-1)\cdots(q-r+1).
\]

Thus:

\[
\text{concrete word}=
\text{pattern}+
\text{injective symbol assignment}.
\]

## Quotient graph

The de Bruijn graph projects to

\[
\overline B(q,n)=B(q,n)/S_q.
\]

Nodes are equality patterns. Pattern edges are induced by shift-and-append followed by canonicalization.

The quotient graph is smaller but no longer uniformly \(G_{q,q}\), because many concrete transitions collapse to the same pattern transition.

## Counting by fibers

Every concrete de Bruijn cycle projects to a pattern skeleton. The set of concrete cycles is the disjoint union of fibers above these skeletons:

\[
\{\text{concrete cycles}\}
=
\bigsqcup_S \operatorname{Lift}(S).
\]

Therefore:

\[
N(q,n)=\sum_S |\operatorname{Lift}(S)|.
\]

## Cohomological obstruction

A pattern skeleton lifts only if symbol assignments remain consistent around the cycle. The obstruction is monodromy in the fiber assignment system.

So:

- \( |\operatorname{Lift}(S)|=0 \) if the obstruction is nontrivial;
- otherwise it counts the compatible assignments.

This is the cohomological form of pattern-level counting.

## Why this is useful

The classical formula counts globally. The quotient decomposition organizes the count by symmetry type and creates a compressed construction space.

For \(q=4,n=10\), the concrete state space has \(4^{10}=1,048,576\) words, while the equality-pattern quotient has \(43,947\) pattern nodes.
