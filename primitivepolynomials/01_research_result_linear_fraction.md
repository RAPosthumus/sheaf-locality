# Research result: primitive-polynomial constructions are asymptotically negligible inside the full de Bruijn space

## 1. Statement

Primitive polynomials give a classical algebraic route to maximal-length linear feedback shift register sequences. Over \(\mathrm{GF}(2)\), a primitive polynomial of degree \(n\) gives an \(m\)-sequence of period

\[
2^n-1,
\]

cycling through all nonzero \(n\)-bit states.

A full binary de Bruijn cycle of order \(n\) has length

\[
2^n
\]

and contains all \(n\)-bit states, including \(0^n\). Therefore a pure LFSR cycle is not itself a full de Bruijn cycle unless the zero state is inserted by a standard modification. We call these sequences **primitive-polynomial-derived de Bruijn cycles**.

The main quantitative result is:

\[
\boxed{
\frac{\#\{\text{primitive-polynomial-derived cycles}\}}
{\#\{\text{all binary de Bruijn cycles}\}}
\le
\frac{\varphi(2^n-1)/n}{2^{2^{n-1}-n}}
}
\]

and this fraction tends to zero extremely fast.

So primitive-polynomial constructions form a highly structured but asymptotically negligible slice of the full de Bruijn space.

---

## 2. Counts

The number of primitive polynomials of degree \(n\) over \(\mathrm{GF}(2)\) is

\[
P(n)=\frac{\varphi(2^n-1)}{n}.
\]

The number of binary de Bruijn cycles of order \(n\) is

\[
D(n)=2^{2^{n-1}-n}.
\]

Therefore the primitive-polynomial-derived fraction is bounded by

\[
F(n)\le \frac{P(n)}{D(n)}
=
\frac{\varphi(2^n-1)/n}{2^{2^{n-1}-n}}.
\]

Since

\[
\varphi(2^n-1)\le 2^n-1,
\]

we get the simpler upper bound

\[
F(n)
\le
\frac{2^n}{n\,2^{2^{n-1}-n}}
=
\frac{2^{2n-2^{n-1}}}{n}.
\]

Thus

\[
F(n)\to 0
\]

super-exponentially.

---

## 3. Interpretation in the sheaf/homology framework

The full set of de Bruijn cycles is the space of global cyclic sections of the word sheaf with full coverage.

Primitive polynomials impose an additional linear recurrence constraint. Therefore they select only linear global sections:

\[
\boxed{
\text{primitive polynomial}
\Rightarrow
\text{linear recurrence}
\Rightarrow
\text{linear global section}
}
\]

whereas the full de Bruijn space is

\[
\boxed{
\text{all global sections}
=
\text{linear}
\cup
\text{nonlinear}.
}
\]

The count above shows that almost every de Bruijn cycle is nonlinear.

---

## 4. Homological version

A de Bruijn cycle is a full-support integral 1-cycle

\[
\partial c=0.
\]

A primitive-polynomial-derived cycle is such a 1-cycle satisfying an extra linear recurrence constraint.

So:

\[
\boxed{
\text{primitive-polynomial cycles}
\subset
\text{linear constrained part of }H_1
}
\]

while

\[
\boxed{
\text{all de Bruijn cycles}
\subset
\text{full integral cycle space with coverage constraint}.
}
\]

Primitive polynomials are therefore coordinates on a small algebraic subvariety of the global-section space, not generators of the whole space.

---

## 5. Consequence

The classical primitive-polynomial method is powerful because it is algebraically compact, not because it is representative.

It gives:

- efficient generation,
- strong periodicity,
- good statistical properties,
- a linear recurrence certificate.

But it misses almost all de Bruijn cycles.

In the locality--sheaf--homology framework:

\[
\boxed{
\text{LFSR/primitive polynomial}
=
\text{linear boundary layer}
}
\]

\[
\boxed{
\text{NLFSR / successor rules / arbitrary gluing}
=
\text{nonlinear global-section regime}.
}
\]

This is the research-level classification:

\[
\boxed{
\text{Almost all de Bruijn cycles are nonlinear global sections.}
}
\]
