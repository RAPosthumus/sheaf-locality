# 01 - Counting de Bruijn cycles via homology and the BEST theorem

## Classical counting formula

The number of cyclic de Bruijn sequences of order \(n\) over an alphabet of size \(q\) is

\[
N(q,n)=\frac{(q!)^{q^{n-1}}}{q^n}.
\]

For \(q=2\),

\[
N(2,n)=2^{2^{n-1}-n}.
\]

This formula is classically obtained from Eulerian circuits in \(B(q,n-1)\), using the de Bruijn-van Aardenne-Ehrenfest-Smith-Tutte theorem, usually called the BEST theorem.

## De Bruijn graph used for counting

The graph \(B(q,n-1)\) has

\[
|V|=q^{n-1},\qquad |E|=q^n.
\]

Each vertex has indegree and outdegree \(q\). A de Bruijn sequence of order \(n\) corresponds to an Eulerian circuit using each edge of \(B(q,n-1)\) once.

## BEST theorem proof sketch

For a connected Eulerian directed graph \(G\), the BEST theorem gives

\[
\operatorname{ec}(G)=t_w(G)\prod_{v\in V}(\deg(v)-1)!,
\]

where \(t_w(G)\) is the number of directed spanning arborescences rooted at \(w\).

For \(B(q,n-1)\),

\[
\prod_v(\deg(v)-1)! = ((q-1)!)^{q^{n-1}}.
\]

The arborescence count is

\[
t_w(B(q,n-1))=q^{q^{n-1}-n}.
\]

Therefore

\[
\operatorname{ec}(B(q,n-1))
=
q^{q^{n-1}-n}((q-1)!)^{q^{n-1}}
=
\frac{(q!)^{q^{n-1}}}{q^n}.
\]

## Homological interpretation

Let

\[
C_1=\mathbb Z[E],\qquad C_0=\mathbb Z[V],
\]

and define

\[
\partial(e:u\to v)=v-u.
\]

A de Bruijn cycle corresponds to a full-support integral 1-chain

\[
c=\sum_{e\in E} e
\]

with

\[
\partial c=0.
\]

Thus the enumeration is the number of full-support integral 1-cycles satisfying the de Bruijn coverage constraint.

## Sheaf interpretation

The word sheaf has local sections \(A^k\) on intervals of length \(k\). Edges are gluing constraints between length-\((n-1)\) sections. A de Bruijn sequence is a global cyclic section covering every length-\(n\) section once.

So

\[
N(q,n)
=
\#\{\text{global cyclic sections of the word sheaf with full coverage}\}.
\]
