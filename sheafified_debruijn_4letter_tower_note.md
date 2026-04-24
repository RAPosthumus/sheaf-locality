# Sheafified de Bruijn tower over a 4-letter alphabet

## 1. Why the full alphabet symmetry matters

Let \(A\) be an alphabet with \(|A|=q\). Before introducing XOR or any arithmetic operation, the de Bruijn graph \(B(q,n)\) is invariant under every permutation of the alphabet:

\[
\pi\in S_q.
\]

A word

\[
x_1x_2\cdots x_n
\]

is transformed by applying \(\pi\) to every symbol:

\[
\pi(x_1)\pi(x_2)\cdots\pi(x_n).
\]

The de Bruijn edge rule

\[
x_1\cdots x_n \to x_2\cdots x_n a
\]

does not depend on the names of the symbols, only on equality and overlap. Therefore the whole graph is \(S_q\)-equivariant.

This means that the natural quotient is not built from concrete words, but from **equality patterns**.

Example over a 4-letter alphabet:

\[
AABC,\quad BBDA,\quad CCDD
\]

may share the same abstract equality-pattern type after canonical relabeling.

---

## 2. Equality-pattern quotient

For a word \(w\in A^n\), define its canonical pattern by scanning left to right:

- the first new symbol becomes \(a\),
- the next new symbol becomes \(b\),
- the next new symbol becomes \(c\),
- and so on.

For example:

\[
A A C B A \mapsto a a b c a.
\]

The quotient set is

\[
A^n/S_q,
\]

which can be represented by all canonical equality patterns of length \(n\) using at most \(q\) distinct blocks.

For \(q=4\), the allowed patterns use at most four abstract symbols:

\[
a,b,c,d.
\]

---

## 3. Fibers: local symbol assignments

A pattern with \(k\) distinct blocks has fiber size

\[
(q)_k=q(q-1)(q-2)\cdots(q-k+1),
\]

because its \(k\) abstract blocks must be assigned distinct concrete alphabet symbols.

For \(q=4\):

\[
(4)_1=4,
\]

\[
(4)_2=12,
\]

\[
(4)_3=24,
\]

\[
(4)_4=24.
\]

Thus the sheaf picture is:

\[
\text{pattern node}
\quad\longmapsto\quad
\text{fiber of concrete words realizing that pattern}.
\]

---

## 4. Quotient de Bruijn graph

The quotient graph has:

- nodes: equality patterns of length \(n\),
- edges: pattern transitions induced by de Bruijn shift-and-append.

From a pattern \(p=p_1\cdots p_n\), a successor is obtained by:

1. dropping \(p_1\),
2. appending either:
   - one existing block symbol,
   - or a new block symbol, if fewer than \(q\) blocks are currently present,
3. canonicalizing again.

This gives the quotient pattern graph.

Important: this quotient graph is generally not regular in the same way as \(B(q,n)\). The concrete graph is \(G_{q,q}\), but the quotient pattern graph has variable degrees because many concrete symbol choices collapse to the same pattern transition.

---

## 5. Edge-to-node lift in the tower

The de Bruijn hierarchy has the exact relation

\[
E(B(q,n))\cong V(B(q,n+1)).
\]

An edge of \(B(q,n)\) is naturally labeled by a word of length \(n+1\):

\[
x_1\cdots x_n \to x_2\cdots x_nx_{n+1}
\quad\leftrightarrow\quad
x_1\cdots x_nx_{n+1}.
\]

After quotienting by \(S_q\), the same principle holds at the pattern level:

\[
\text{edge-label patterns at level }n
\cong
\text{node patterns at level }n+1.
\]

This is the tower mechanism.

---

## 6. Sheafified de Bruijn cycle construction

A de Bruijn cycle over \(A\) can be viewed as a global section of this tower.

The construction splits into two layers.

### Layer 1: pattern skeleton

Construct a walk or cycle in the quotient pattern graph that covers pattern types with the required multiplicities.

### Layer 2: fiber realization

Lift the pattern skeleton to concrete alphabet symbols by choosing compatible assignments in the fibers.

The gluing condition is the de Bruijn overlap:

\[
x_2\cdots x_n
\]

must agree between consecutive windows.

So the sheaf data is:

- base: quotient pattern graph,
- fiber over each pattern: all injective assignments of pattern blocks to concrete symbols,
- restriction maps: overlap restrictions between adjacent windows,
- global section: a consistent concrete de Bruijn cycle.

---

## 7. Why this helps for larger alphabets

Without quotienting, \(B(4,n)\) has

\[
4^n
\]

vertices.

The quotient by \(S_4\) has far fewer pattern nodes. These pattern nodes are equality structures rather than concrete words.

The tower \(n=6,\dots,10\) generated here gives:

- number of concrete words,
- number of quotient pattern nodes,
- distribution by number of equality blocks,
- quotient transition structure,
- edge-to-node lift counts.

This is a practical starting point for constructing de Bruijn cycles over larger alphabets by first solving a smaller pattern problem and then lifting through fibers.

---

## 8. What changes when XOR or arithmetic is introduced

The full \(S_q\)-symmetry holds only when the operations do not depend on symbol values.

Once XOR, addition, or another algebraic operation is introduced, the symmetry group shrinks to the automorphism group of that algebraic structure.

For binary XOR, the structure is compatible with bit-flip in a special way. For larger alphabets, the choice of algebra matters.

So the sheafified equality-pattern tower is the correct pre-arithmetic object. Arithmetic enriches it, but also breaks part of the full permutation symmetry.

---

## 9. Practical interpretation

For alphabet size \(4\), the quotient tower is a compressed scaffold:

\[
B(4,6)/S_4
\to
B(4,7)/S_4
\to
B(4,8)/S_4
\to
B(4,9)/S_4
\to
B(4,10)/S_4.
\]

Each level stores:

- pattern nodes,
- fiber sizes,
- quotient transitions,
- and the edge-to-node lift.

This tower is the sheafification scaffold for de Bruijn cycle construction over a 4-letter alphabet.