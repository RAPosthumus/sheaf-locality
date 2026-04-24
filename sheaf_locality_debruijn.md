
# Start/End Locality, Sheafification, and de Bruijn Graphs

## 1. Original Idea: Start and End Locality

We start with the notion of a directed graph \(G_{n,m}\):

- \(n\): local **start condition** (incoming structure)
- \(m\): local **end condition** (outgoing structure)

This encodes how much of the past and future determine valid transitions.

---

## 2. de Bruijn Graph as a Locality Structure

In the de Bruijn graph \(B(q,n)\):

- Nodes: words \(x_1 \cdots x_n\)
- Edges: 
  \[
  x_1\cdots x_n \to x_2\cdots x_n a
  \]

This enforces an overlap:

\[
x_2\cdots x_n
\]

So:

- **Start locality** = prefix constraint
- **End locality** = suffix constraint

Thus:

\[
\text{locality} = \text{overlap consistency}
\]

---

## 3. Sheaf Interpretation

This is naturally a **sheaf structure**:

- Local sections: words of length \(n\)
- Restriction maps: overlapping \(n-1\) substrings
- Gluing: consistency of overlaps

So:

\[
\boxed{
\text{Start/end locality = restriction maps of a sheaf}
}
\]

---

## 4. De Bruijn Cycles as Global Sections

A de Bruijn cycle is:

- A sequence covering all local sections
- With consistent overlaps everywhere

So:

\[
\boxed{
\text{De Bruijn cycle = global section of the sheaf}
}
\]

---

## 5. Symmetry Reduction via Alphabet Permutations

For alphabet \(A\) with size \(q\):

- The system is invariant under permutations \(S_q\)
- Words can be reduced to **equality patterns**

Example:
```
AABC -> aabc
BBDA -> aabc
```

So:

- Base space: equality patterns
- Fiber: concrete symbol assignments

---

## 6. Pattern-Level Locality

After quotienting:

- Locality is no longer symbol equality
- It is **pattern consistency**

So:

\[
\text{locality} = \text{equality-pattern overlap}
\]

This is a coarser but structurally identical locality.

---

## 7. Sheafified Construction

Construction splits into two layers:

### Layer 1: Pattern Skeleton
- Build cycle in pattern graph
- Enforce pattern-level locality

### Layer 2: Fiber Lift
- Assign concrete symbols
- Respect equality constraints
- Preserve overlaps

---

## 8. Near-G Graphs as Gluing Failure

Earlier definition:

\[
\deg^+(v) \neq \deg^-(v)
\]

Now interpreted as:

- Failure of local consistency
- Obstruction to global section

So:

\[
\boxed{
\text{Near-G defect = failure of sheaf gluing}
}
\]

Boundary = where gluing fails.

---

## 9. Role of n = 6 and n = 10

At these levels:

- Small \(R_n\)-orbits contain all local types
- All central-pair structures appear

So they act as:

\[
\boxed{
\text{minimal generators of all local configurations}
}
\]

In sheaf terms:

- Minimal patches that already encode all gluing behavior

---

## 10. Final Synthesis

We unify all viewpoints:

\[
\boxed{
\text{Start/end locality = sheaf restriction maps}
}
\]

\[
\boxed{
\text{De Bruijn cycle = global section}
}
\]

\[
\boxed{
\text{Near-G defect = gluing obstruction}
}
\]

\[
\boxed{
\text{Symmetry reduction = pattern-level base space}
}
\]

---

## 11. Key Insight

The original locality idea becomes a full structural framework:

- Graph theory → local constraints
- Sheaf theory → consistency + gluing
- Symmetry → quotient simplification
- Construction → lift from patterns to symbols

This provides a scalable way to build de Bruijn cycles over larger alphabets.
