
# Formalizing Start/End Locality as a Sheaf for de Bruijn Graphs

## 1. Purpose

The original graph idea was:

\[
G_{n,m}:
\quad
\text{local start condition } n,
\quad
\text{local end condition } m.
\]

For finite exact directed graphs, exact \(G_{n,m}\) collapses to \(G_{k,k}\) when every vertex has exactly \(n\) incoming and \(m\) outgoing edges, because total indegree equals total outdegree.

But the deeper idea is not the degree count alone. The deeper idea is **local compatibility**:

- a state may be entered only if its start condition matches the previous local data;
- a state may continue only if its end condition matches the next local data.

In de Bruijn graphs, this is overlap.

This note formalizes that as a sheaf.

---

## 2. The de Bruijn graph \(B(q,n)\)

Let \(A\) be an alphabet with

\[
|A|=q.
\]

The de Bruijn graph \(B(q,n)\) has:

\[
V_n=A^n
\]

as vertices, and directed edges

\[
x_1x_2\cdots x_n
\longrightarrow
x_2x_3\cdots x_n a,
\qquad a\in A.
\]

Equivalently, an edge is an \((n+1)\)-word

\[
x_1x_2\cdots x_nx_{n+1}.
\]

Its source is the prefix:

\[
s(x_1\cdots x_{n+1})=x_1\cdots x_n,
\]

and its target is the suffix:

\[
t(x_1\cdots x_{n+1})=x_2\cdots x_{n+1}.
\]

Thus

\[
E(B(q,n))\cong A^{n+1}\cong V(B(q,n+1)).
\]

This is the edge-to-node lift:

\[
E(B(q,n)) \cong V(B(q,n+1)).
\]

---

## 3. Start and end locality as restriction maps

For a word

\[
w=x_1\cdots x_n\in A^n,
\]

define the left and right restrictions:

\[
\rho_L(w)=x_1\cdots x_{n-1},
\]

\[
\rho_R(w)=x_2\cdots x_n.
\]

The de Bruijn edge condition between two words \(u,v\in A^n\) is:

\[
u\to v
\quad\Longleftrightarrow\quad
\rho_R(u)=\rho_L(v).
\]

So the edge condition is exactly a gluing condition.

In this language:

\[
\boxed{
\text{start locality}=\rho_L
}
\]

\[
\boxed{
\text{end locality}=\rho_R
}
\]

and

\[
\boxed{
\text{transition validity}=\rho_R(u)=\rho_L(v).
}
\]

This is the sheaf-theoretic core of de Bruijn locality.

---

## 4. A small category of local intervals

Let \([i,j]\) denote a finite interval of integer positions.

For each interval \([i,j]\), assign the set

\[
\mathcal F([i,j])=A^{j-i+1}.
\]

If \([i,j]\subseteq [r,s]\), define the restriction map

\[
\operatorname{res}^{[r,s]}_{[i,j]}:
A^{s-r+1}\to A^{j-i+1}
\]

by taking the corresponding substring.

This defines a presheaf

\[
\mathcal F:\mathcal I^{op}\to \mathbf{Set},
\]

where \(\mathcal I\) is the category of finite integer intervals with inclusions.

Because compatible local words glue uniquely to a longer word, this presheaf is a sheaf for the natural interval topology.

In practical terms:

- local sections are finite words;
- restriction maps are substring maps;
- gluing is overlap consistency.

---

## 5. de Bruijn edges as sheaf gluing

A de Bruijn edge from \(u\) to \(v\) is the same as gluing two length-\(n\) local sections over an overlap of length \(n-1\).

Let

\[
u=x_1\cdots x_n,
\]

\[
v=y_1\cdots y_n.
\]

They glue into an \((n+1)\)-word iff

\[
x_2\cdots x_n=y_1\cdots y_{n-1}.
\]

The glued word is then

\[
x_1x_2\cdots x_ny_n.
\]

Thus:

\[
B(q,n)
\]

is the graph of length-\(n\) local sections with valid gluing along length-\((n-1)\) overlaps.

---

## 6. de Bruijn cycles as global sections

A de Bruijn cycle of order \(n\) over alphabet \(A\) is a cyclic word in which every length-\(n\) word appears exactly once.

In sheaf language, it is a cyclic global section whose length-\(n\) local restrictions cover every element of

\[
A^n
\]

exactly once.

So:

\[
\boxed{
\text{de Bruijn cycle}=\text{global cyclic section covering all local sections once}.
}
\]

Equivalently:

- vertices are local sections;
- edges are gluing constraints;
- an Eulerian cycle in \(B(q,n-1)\) or a Hamiltonian cycle in \(B(q,n)\) gives a de Bruijn cycle.

The sheaf perspective emphasizes the gluing condition rather than the degree condition.

---

## 7. Near-\(G\) graphs as gluing defects

For a directed graph \(H\) derived from a de Bruijn graph, define the local imbalance

\[
\delta_H(v)=\deg_H^+(v)-\deg_H^-(v).
\]

If

\[
\delta_H(v)\neq 0,
\]

then \(v\) is a boundary or defect vertex.

In the sheaf interpretation, this means:

- there are too many outgoing local continuations,
- or too many incoming local histories,
- so local sections fail to glue into a balanced global object.

Thus:

\[
\boxed{
\text{near-}G\text{ defect}=\text{local gluing obstruction}.
}
\]

The positive and negative boundary sets are:

\[
\partial^+H=\{v:\delta_H(v)>0\},
\]

\[
\partial^-H=\{v:\delta_H(v)<0\}.
\]

Since every finite directed graph has

\[
\sum_v \delta_H(v)=0,
\]

the total obstruction balances globally.

So near-\(G\) defects behave like source/sink boundaries for failed gluing.

---

## 8. Quotienting by alphabet symmetry

Before adding arithmetic such as XOR, the alphabet symbols have no intrinsic names.

For any permutation

\[
\pi\in S_q,
\]

we may relabel all symbols:

\[
x_1\cdots x_n
\mapsto
\pi(x_1)\cdots \pi(x_n).
\]

The de Bruijn edge rule is invariant under this action because it uses only equality of overlapping positions.

Therefore \(B(q,n)\) is \(S_q\)-equivariant.

This gives a quotient by equality patterns.

---

## 9. Equality-pattern quotient

Given a word, replace its first new symbol by \(a\), the next new symbol by \(b\), and so on.

Examples:

\[
AABC \mapsto aabc,
\]

\[
CCDA \mapsto aabc.
\]

These words have the same equality pattern.

The quotient set is:

\[
A^n/S_q.
\]

Its elements are set partitions of the positions \(\{1,\dots,n\}\) into at most \(q\) blocks, represented by canonical patterns.

A pattern with \(r\) blocks has fiber size

\[
(q)_r=q(q-1)(q-2)\cdots(q-r+1),
\]

because each abstract block must be assigned a distinct concrete alphabet symbol.

Thus the quotient map

\[
A^n\to A^n/S_q
\]

has fibers of variable size.

---

## 10. Pattern sheaf

Define the pattern sheaf

\[
\mathcal P_q([i,j])
=
A^{j-i+1}/S_q.
\]

A section of \(\mathcal P_q\) is not a concrete word, but an equality pattern.

Restriction maps are induced by substring restriction followed by canonicalization.

So if

\[
p=aabca,
\]

then restricting to positions \(2,3,4\) gives

\[
abc
\]

because the substring is

\[
abc
\]

after canonical relabeling.

This gives a quotient sheaf-like structure:

\[
\mathcal F \to \mathcal P_q.
\]

Strictly speaking, because quotienting and restriction can interact with stabilizers, this is best viewed as a stacky or groupoid-valued sheaf if one wants full precision.

For construction purposes, the set-valued quotient by canonical patterns is already very useful.

---

## 11. Sheaf of realizations over a pattern

For a pattern \(p\) with \(r\) blocks, define its realization fiber:

\[
\operatorname{Fib}(p)=
\{\text{injective assignments of the }r\text{ blocks of }p\text{ to symbols in }A\}.
\]

Then

\[
|\operatorname{Fib}(p)|=(q)_r.
\]

A concrete word is therefore:

\[
\text{pattern}+\text{choice of fiber assignment}.
\]

This gives the sheafified decomposition:

\[
\boxed{
\text{concrete word}=
\text{equality pattern}
+
\text{fiber label assignment}.
}
\]

---

## 12. Pattern-level de Bruijn graph

Define the quotient pattern graph

\[
\overline{B}(q,n)=B(q,n)/S_q.
\]

Its vertices are equality patterns of length \(n\) with at most \(q\) blocks.

There is a pattern edge

\[
p\to p'
\]

if some concrete representative of \(p\) has a de Bruijn edge to some concrete representative of \(p'\).

Operationally, from a pattern \(p=p_1\cdots p_n\):

1. drop \(p_1\);
2. append either:
   - an already existing block;
   - or a new block, if fewer than \(q\) blocks are present;
3. canonicalize.

This gives the pattern-level successor set.

The quotient graph is generally not \(G_{q,q}\), because many concrete transitions collapse to one pattern transition.

So:

\[
B(q,n) \text{ is regular},
\]

but

\[
\overline{B}(q,n) \text{ is pattern-regular only in a weaker sense}.
\]

---

## 13. Start/end locality after quotienting

At the concrete level:

\[
\rho_R(u)=\rho_L(v)
\]

requires exact symbol equality.

At the pattern level, the same condition becomes:

\[
\operatorname{pat}(\rho_R(u))
=
\operatorname{pat}(\rho_L(v)).
\]

So locality becomes equality-pattern locality.

Thus:

\[
\boxed{
\text{concrete locality}=\text{symbol overlap}
}
\]

whereas

\[
\boxed{
\text{quotient locality}=\text{pattern overlap}.
}
\]

This is exactly the sheafification of start/end locality.

---

## 14. Constructing de Bruijn cycles by sheafification

The construction can be split into two stages.

### Stage 1: Pattern skeleton

Construct a walk or cycle in the pattern graph

\[
\overline{B}(q,n).
\]

This determines the equality-pattern structure of the windows.

### Stage 2: Fiber lift

Choose concrete symbol assignments in the fibers so that all overlaps are compatible.

That is, if two adjacent pattern windows overlap, the concrete assignments must agree on the shared positions.

The lift is successful if the global concrete cycle covers every word in \(A^n\) exactly once.

So:

\[
\boxed{
\text{de Bruijn cycle}
=
\text{pattern skeleton}
+
\text{compatible fiber lift}.
}
\]

This is the sheafified construction principle.

---

## 15. Relation to \(G_{n,m}\)

The original \(G_{n,m}\) intuition can now be reformulated.

Instead of saying only:

\[
\deg^-(v)=n,
\qquad
\deg^+(v)=m,
\]

we distinguish:

1. **degree locality**: number of possible incoming/outgoing continuations;
2. **restriction locality**: what overlap data must match;
3. **sheaf locality**: how local sections glue globally.

For exact de Bruijn graphs:

\[
\deg^-(v)=\deg^+(v)=q.
\]

So they are exact

\[
G_{q,q}.
\]

But more importantly, the incoming and outgoing edges are controlled by the same restriction object:

\[
A^{n-1}.
\]

Thus start and end locality are dual restrictions of the same local section.

The sheaf version is:

\[
\boxed{
G_{q,q}
=
\text{balanced local degree}
+
\text{compatible sheaf restrictions}.
}
\]

A near-\(G\) object is one where this balance or compatibility is partially broken.

---

## 16. Role of \(n=6\) and \(n=10\)

In the binary case, define the twisted shift

\[
R_n(x_1\cdots x_n)=x_2\cdots x_n\overline{x_1}.
\]

At \(n=6\), the short orbit

\[
001100\to011001\to110011\to100110
\]

contains all four central-pair types:

\[
00,\quad 01,\quad 10,\quad 11.
\]

At \(n=10\), the short orbit

\[
0011001100
\to
0110011001
\to
1100110011
\to
1001100110
\]

again contains all four central-pair types.

Since the binary kernel basins are determined by central pair, these short orbits act as minimal local witnesses of all basin types.

In sheaf language:

\[
n=6,\ n=10
\]

provide small patches containing all local gluing types relevant to the basin decomposition.

So they are local generators of the basin structure.

---

## 17. What changes when XOR is introduced

Everything above is invariant under the full symbol permutation group

\[
S_q.
\]

But XOR or any arithmetic operation introduces algebraic structure on the alphabet.

For binary XOR:

\[
P=S\oplus E.
\]

Complement behaves nontrivially:

\[
(CS)\oplus(CE)=S\oplus E=P,
\]

but

\[
(CS)\oplus E=C(P).
\]

Thus the symmetry is no longer simple symbol permutation on one word. It acts on triples:

\[
(S,E,P).
\]

So the full \(S_q\)-sheaf is the pre-arithmetic object. XOR adds an algebraic layer and reduces the symmetry group to one compatible with that algebra.

---

## 18. Final synthesis

The complete picture is:

\[
\boxed{
\text{start/end locality}
=
\text{restriction maps}
}
\]

\[
\boxed{
\text{de Bruijn graph}
=
\text{graph of compatible local sections}
}
\]

\[
\boxed{
\text{de Bruijn cycle}
=
\text{global cyclic section}
}
\]

\[
\boxed{
\text{near-}G\text{ defect}
=
\text{gluing obstruction}
}
\]

\[
\boxed{
S_q\text{-quotient}
=
\text{equality-pattern sheaf}
}
\]

\[
\boxed{
\text{construction}
=
\text{pattern skeleton}
+
\text{fiber lift}
}
\]

This gives a scalable framework for constructing de Bruijn cycles over larger alphabets:

1. quotient by symbol symmetry;
2. construct a pattern-level skeleton;
3. lift through fibers using overlap restrictions;
4. check that the resulting global section covers all concrete words exactly once.
