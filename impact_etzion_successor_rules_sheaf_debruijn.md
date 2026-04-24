
# Impact on Etzion-style constructions and successor-rule methods

## 1. Scope

This note connects the previous framework

\[
\text{start/end locality}
\to
\text{sheaf gluing}
\to
\text{homological cycles}
\to
\text{cohomological lifting}
\]

to two construction families:

1. Etzion-style constructions of de Bruijn cycles;
2. successor-rule methods.

I interpret “succesreels” as **successor rules**, since that is the standard term in the de Bruijn sequence literature.

---

## 2. Etzion-style constructions: what they do

Etzion’s construction of \(m\)-ary de Bruijn cycles is an algorithmic construction of de Bruijn cycles for general alphabet size. In the broader Etzion/Lempel line, constructions are often organized around cycle structure, shift-register behavior, and efficient generation of full cycles.

From our viewpoint, such constructions can be interpreted as:

\[
\text{choose local transition rules}
\quad+\quad
\text{join local cycles}
\quad+\quad
\text{obtain one global de Bruijn cycle}.
\]

In graph terms:

\[
\text{construct an Eulerian/Hamiltonian global cycle in a de Bruijn graph}.
\]

In homological terms:

\[
\text{construct a distinguished integral 1-cycle}.
\]

In sheaf terms:

\[
\text{construct a global cyclic section from compatible local sections}.
\]

---

## 3. What the sheaf viewpoint changes

The classical construction works at the level of concrete words:

\[
A^n.
\]

The sheafified approach says:

1. first quotient by the full alphabet symmetry \(S_q\);
2. work on equality-pattern types;
3. lift pattern cycles through symbol-assignment fibers.

So instead of constructing directly in

\[
B(q,n),
\]

one first works in

\[
\overline B(q,n)=B(q,n)/S_q.
\]

Then one tries to lift a pattern-level cycle to a concrete de Bruijn cycle.

This turns construction into a two-layer problem:

\[
\boxed{
\text{pattern skeleton}
+
\text{fiber lift}
=
\text{concrete de Bruijn cycle}.
}
\]

---

## 4. Impact on Etzion-style construction

Etzion-style methods can be reorganized as follows.

### Classical layer

Construct cycles using concrete words.

### Sheafified layer

Construct quotient pattern cycles first.

### Fiber layer

Lift the quotient cycles to concrete words by assigning alphabet symbols consistently.

This matters because for alphabet size \(q=4\), the quotient compression is large.

For example, at \(n=10\):

\[
4^{10}=1,048,576
\]

concrete words, but only

\[
43,947
\]

equality-pattern nodes under the \(S_4\)-quotient.

So an Etzion-style construction over a 4-letter alphabet could potentially be decomposed into:

1. generate or classify pattern cycles;
2. determine fiber monodromy;
3. lift only those pattern cycles with trivial obstruction;
4. use cycle-joining at the pattern or fiber level.

This does not replace Etzion’s construction. It refactors it.

---

## 5. Homological interpretation of Etzion-style joining

Cycle-joining constructions can be interpreted homologically.

Suppose we have several disjoint cycles

\[
c_1,c_2,\dots,c_r
\]

in the de Bruijn graph.

Each satisfies

\[
\partial c_i=0.
\]

A joining operation modifies edges so that

\[
c_1+\cdots+c_r
\]

becomes one larger cycle, while keeping the total boundary zero.

So joining is a boundary-preserving operation:

\[
\partial(c_1+\cdots+c_r)=0.
\]

The operation changes the decomposition of a homology class into connected cycle components, but it preserves the cycle condition.

In sheaf language, joining replaces several local cyclic sections by one global cyclic section.

---

## 6. What the quotient adds to cycle joining

After quotienting by \(S_q\), cycles in the concrete graph become cycles or weighted cycles in the pattern graph.

A pattern cycle may represent many concrete cycles because each pattern node has a fiber:

\[
\operatorname{Fib}(p).
\]

A joining operation in the quotient therefore has two possible obstruction points:

1. the pattern cycles must join in the quotient graph;
2. the fiber assignments must remain compatible after joining.

Thus joining has two layers:

\[
\text{homological joining in the base}
\]

and

\[
\text{cohomological compatibility in the fibers}.
\]

This is the key new interpretation.

---

## 7. Successor rules: what they do

A successor rule is a function

\[
f:A^n\to A
\]

that tells which symbol follows the current length-\(n\) word.

Thus it defines a deterministic map

\[
T_f(x_1\cdots x_n)
=
x_2\cdots x_n f(x_1\cdots x_n).
\]

A de Bruijn successor rule is one where iterating \(T_f\) visits every length-\(n\) word exactly once before returning.

So a successor rule is a choice of one outgoing edge at every vertex:

\[
x\mapsto x_2\cdots x_n f(x).
\]

Graphically, it selects a functional subgraph of \(B(q,n)\).

For it to produce a de Bruijn cycle, this functional graph must be one cycle containing all vertices.

---

## 8. Successor rules as sheaf morphisms

The de Bruijn graph has \(q\) outgoing choices from each vertex.

A successor rule chooses one of them.

So a successor rule is a section of the outgoing-edge bundle:

\[
\operatorname{Out}:V_n\to \{\text{possible extensions}\}.
\]

In sheaf terms, it is a rule for extending a local section one step to the right:

\[
x_1\cdots x_n
\mapsto
x_2\cdots x_n f(x_1\cdots x_n).
\]

Thus:

\[
\boxed{
\text{successor rule}
=
\text{local extension morphism}.
}
\]

The de Bruijn condition says this local extension morphism generates one global orbit covering all local sections.

---

## 9. Successor rules and homology

A successor rule selects the edge chain

\[
c_f=\sum_{v\in V_n} e_v,
\]

where \(e_v\) is the selected outgoing edge from \(v\).

Every vertex has selected outdegree \(1\).

For \(c_f\) to be a union of cycles, every vertex must also have selected indegree \(1\).

That is:

\[
\partial c_f=0.
\]

For \(c_f\) to be one de Bruijn cycle, the selected graph must be connected as one directed cycle.

So successor-rule correctness has two parts:

1. **homological balance**
   \[
   \partial c_f=0;
   \]

2. **cycle connectivity**
   the functional graph has one component.

The common method of joining disjoint cycles addresses the second condition after the first has created a cycle cover.

---

## 10. Successor rules and the quotient by \(S_q\)

Because the pre-arithmetic de Bruijn graph is \(S_q\)-equivariant, one can ask for successor rules that are also equivariant or pattern-controlled.

A fully \(S_q\)-equivariant successor rule cannot usually pick a specific concrete symbol by name, because names are meaningless under \(S_q\).

Instead, it must pick by pattern type:

- repeat an existing block;
- introduce a new block, if allowed;
- select according to equality-pattern features.

Thus a quotient successor rule has the form:

\[
\bar f:\overline B(q,n)\to \{\text{pattern extensions}\}.
\]

Then one must lift it to concrete symbols in the fibers.

So again:

\[
\boxed{
\text{successor rule}
=
\text{pattern rule}
+
\text{fiber lift}.
}
\]

---

## 11. Relation to PCR and CCR

Binary successor-rule constructions often use the pure cycling register (PCR) or complemented cycling register (CCR).

The PCR corresponds to ordinary rotation/cycling structure.

The CCR corresponds to the twisted shift:

\[
R_n(x_1\cdots x_n)=x_2\cdots x_n\overline{x_1}.
\]

This is closely related to the \(R_n\)-orbits we studied.

In our framework:

- PCR is a symmetry of ordinary cyclic word structure;
- CCR is a symmetry of complement-twisted cyclic word structure;
- necklaces and co-necklaces are orbit representatives under those symmetries;
- successor rules choose where to switch edges to join these orbit cycles.

Thus the earlier \(R_n\)-orbit analysis fits naturally into successor-rule constructions based on CCR/co-necklace structure.

---

## 12. Impact of \(n=6\) and \(n=10\)

The special short \(R_n\)-orbits at \(n=6\) and \(n=10\) contain all central-pair types.

That means they are small orbit witnesses of all kernel-basin types.

For successor-rule methods, this suggests:

1. these short orbits are good places to define switching rules;
2. they test all local basin cases in one small cycle;
3. they can serve as local templates for joining larger cycles;
4. in a quotient/sheaf construction, they are minimal patches detecting all local obstruction types.

So the \(n=6\) and \(n=10\) phenomena are not merely aesthetic; they identify small symmetry-controlled substructures that can guide cycle joining.

---

## 13. Impact on Etzion-style constructions over larger alphabets

For larger alphabets, the full \(S_q\)-symmetry suggests replacing binary complement-based orbit classes by equality-pattern classes.

Etzion-style constructions over \(q\)-ary alphabets could be organized around:

1. quotient pattern cycles;
2. fiber assignments;
3. monodromy/obstruction checks;
4. joining operations that preserve liftability.

The main practical benefit is compression.

Instead of handling all

\[
q^n
\]

concrete states at once, one handles pattern states first.

For \(q=4,n=10\), the quotient level has 43,947 pattern nodes instead of 1,048,576 concrete nodes.

This suggests a possible constructive pipeline:

```text
Input: alphabet A, length n

1. Build the equality-pattern quotient graph B(q,n)/S_q.
2. Decompose it into pattern cycles using a successor-style rule.
3. For each pattern cycle, compute fiber monodromy.
4. Keep or refine cycles whose monodromy lifts.
5. Join liftable cycles using switch operations.
6. Lift the resulting pattern cycle to a concrete de Bruijn cycle.
```

This is a sheafified Etzion/successor-rule pipeline.

---

## 14. Where XOR changes the story

Everything above assumes the alphabet symbols are interchangeable.

XOR breaks full \(S_q\)-symmetry because it gives the alphabet algebraic structure.

For binary XOR:

\[
P=S\oplus E.
\]

Complementing both inputs preserves \(P\):

\[
(CS)\oplus(CE)=P.
\]

Complementing one input flips \(P\):

\[
(CS)\oplus E=C(P).
\]

So after XOR is introduced, the symmetry acts on triples

\[
(S,E,P),
\]

not on a single word alone.

Thus the sheafified pattern construction is the pre-XOR layer. XOR adds an algebraic constraint sheaf on top of it.

A future extension would use a sheaf of triples:

\[
\mathcal F_{\oplus}(S,E,P)
\]

with the local constraint

\[
P=S\oplus E.
\]

Then de Bruijn construction and XOR compatibility become a coupled lifting problem.

---

## 15. Final synthesis

The impact on Etzion-style and successor-rule constructions is:

\[
\boxed{
\text{classical construction}
=
\text{cycle joining in a de Bruijn graph}
}
\]

\[
\boxed{
\text{sheafified construction}
=
\text{pattern cycle}
+
\text{fiber lift}
+
\text{obstruction cancellation}
}
\]

\[
\boxed{
\text{successor rule}
=
\text{local extension morphism}
}
\]

\[
\boxed{
\text{correctness}
=
\partial c=0
+
\text{one connected global cycle}
}
\]

\[
\boxed{
\text{Etzion-style joining}
=
\text{homology-preserving cycle surgery}
}
\]

The new contribution of our framework is to separate:

1. the pattern skeleton;
2. the symbol-fiber lift;
3. the homological cycle condition;
4. the cohomological obstruction to lifting;
5. the special role of small symmetry orbits such as those at \(n=6\) and \(n=10\).

This gives a principled route to constructing de Bruijn cycles over larger alphabets and to understanding when successor rules lift from pattern-level rules to concrete sequences.
