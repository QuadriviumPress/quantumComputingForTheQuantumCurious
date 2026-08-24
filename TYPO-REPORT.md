# Typo & Consistency Report — *Quantum Computing for the Quantum Curious*

**Scope:** `chapters/*.md` (MyST Markdown source, 10 chapters) + `index.md` — no files were edited.
**Date:** 2026-08-21 · **Method:** hunspell dictionary pass + scripted regex/cross-reference checks + per-chapter AI reading pass, all findings grep-verified against the source.
**Spelling convention detected:** US English (~45 US vs 7 UK variant hits). UK-form instances are flagged as inconsistencies below.

**Important context:** almost every defect below is inherited verbatim from the published Springer original (verified against `tmp/book.pdf` page extracts). The MyST conversion itself is faithful; fixing these items means deliberately deviating from the print book (an "errata-applied" edition — your call).

## Summary

| Chapter | Findings | High severity |
|---|---|---|
| ch-01 Introduction to Superposition | 8 | 3 |
| ch-02 What is a Qubit | 4 | 2 |
| ch-03 Beam Splitter | 9 | 6 |
| ch-04 Stern–Gerlach | 10 | 4 |
| ch-05 Quantum Cryptography | 8 | 3 |
| ch-06 Quantum Gates | 7 | 4 |
| ch-07 Entanglement | 5 | 2 |
| ch-08 Quantum Teleportation | 2 | 1 |
| ch-09 Quantum Algorithms | 13 | 5 |
| ch-10 Worksheets | 12 | 5 |
| Cross-cutting | 4 | 1 |
| **Total** | **82** | **36** |

Severity: **HIGH** = unambiguous error (changes meaning / factually wrong / obvious typo) · **MED** = clear defect, smaller impact · **LOW** = borderline or debatable.
"(orig)" = defect also present in the published Springer original.

---

## ch-01-introduction-to-superposition.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 13 | "superposition as shown [](#fig-1-1)" — missing "in"; parallel refs (ll. 21, 32, 40) all read "as shown in" (orig) | "as shown in [](#fig-1-1)" | HIGH |
| 32 | "but not any numbers inbetween" — nonstandard spelling (orig) | "in between" | HIGH |
| 56 | "(i.e in macroscopic objects)" — missing second period + comma; inconsistent with "i.e.," at ll. 32, 52 (orig) | "(i.e., in macroscopic objects)" | HIGH |
| 40 | "50∕50" uses U+2215 DIVISION SLASH, not "/" — math-extraction artifact (conversion-introduced) | plain "/" | MED |
| 90 | Citation "Nielsen, M. A. 1., & Chuang" — stray "1." garbles author name (orig) | "Nielsen, M. A., & Chuang" | MED |
| 32 | "For example the hydrogen atom" — missing comma after intro phrase; inconsistent with ll. 21, 52 (orig) | "For example, the hydrogen atom" | LOW |
| 50 | "a combination of heads or tails" — should be "and"; surrounding text says "both heads and tails" (orig) | "heads and tails" | LOW |
| 8 | "In this section, we review" — the unit is a chapter; same paragraph later says "At the end of the chapter" (orig) | "In this chapter" | LOW |

## ch-02-what-is-a-qubit.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 179 | "a helpful visual aide" — wrong word; "aide" is a person (orig, p. 27) | "visual aid" | HIGH |
| 226 | "qubits which are in same superposition state" — missing article (orig, p. 28) | "in the same superposition state" | HIGH |
| 184 | "there exists both XBox and PlayStation" — brand is "Xbox" (orig, p. 27) | "Xbox" | MED |
| 8 | "write every number with 8-bits total" — hyphen wrong in noun phrase (orig, p. 21) | "with 8 bits total" | LOW |

## ch-03-creating-superposition-the-beam-splitter.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 26 | Fig. 3.2 caption is a verbatim copy of Fig. 3.1's ("A beam splitter reflects 50%...") and does not describe Fig. 3.2, the water-wave barrier analogy (orig, p. 32) | Write a caption describing the barrier-with-holes analogy | HIGH |
| 8 | "exist in two different locations at this same time" — wrong word (orig, p. 31) | "at the same time" | HIGH |
| 69 | "at the instance it encounters" — wrong word for a moment in time (orig, p. 34) | "at the instant" | HIGH |
| 122 | "(e) Neither." — the only one of seven identical options ending with a period (orig, p. 36) | "(e) Neither" | HIGH |
| 180 | "the plus or minus signs represents" — subject-verb agreement (orig, p. 39) | "represent" | HIGH |
| 218 | "beam splitter matrix by initial photon state" — missing article (orig, p. 41) | "by the initial photon state" | HIGH |
| 100 | "The set up is very sensitive" — noun is one word (orig, p. 35) | "The setup" | MED |
| 172 | "experiment–though" — bare en dash joins clauses (orig, p. 39) | "experiment — though" | LOW |
| 182 | "(superposition/phase shift, etc)" — "etc." needs its period (orig, p. 39) | "etc.)" | LOW |

## ch-04-creating-superposition-stern-gerlach.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 143 | Math error: $\lvert 0\rangle = 1/\sqrt{2}\lvert -\rangle + 1/\sqrt{2}\lvert -\rangle$ — both kets are |−⟩; contradicts Eq. 4-3 and the preceding sentence (orig, p. 48) | first ket should be $\lvert +\rangle$ | HIGH |
| 204 | "after you measure the it!" — extra word (orig, p. 50) | "after you measure it!" | HIGH |
| 212 | "Two common basis are" — plural is "bases" (orig, p. 51) | "Two common bases are" | HIGH |
| 245 | "i.e, find α and β" — missing second period (orig) | "i.e.," | HIGH |
| 143, 145 | stray duplicated `\rangle` after the second coefficient renders a bogus "1/√2⟩" (orig) | delete stray `\rangle` | MED |
| 62 | "in the +z and −z axis" (and "+x and −x axis") — two axes named (orig) | "axes" (×2) | MED |
| 230 | "Stern Gerlach apparatus" — missing en dash; every other occurrence uses "Stern–Gerlach" (orig) | "Stern–Gerlach" | MED |
| 136 | "it is definitely not \|1⟩, therefore..." — comma splice (orig) | semicolon + ", therefore," | LOW |
| 201 | "by measuring the −x in the z-basis then the electron is in a superposition" — garbled caption sentence (orig) | rewrite, e.g. "...measuring the −x spin in the z-basis, the electron is in a superposition" | LOW |
| 153 | "0% probability being measured up" — missing "of" (orig) | "probability of being" | LOW |

## ch-05-quantum-cryptography.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 26 | "in 1995, Peter Shor proposed" — Shor's factoring algorithm was presented in 1994 (FOCS '94) (error also in printed original, p. 57) | "in 1994" | HIGH |
| 50 | "until desired level of security is achieved" — missing article (orig, p. 58) | "until the desired level" | HIGH |
| 111 | "lists of measurement basis" — plural needed (orig, p. 61) | "bases" | HIGH |
| 28 | "ensure a key is shared over a secure channel" — contradicts the chapter's own framing; QKD solves sharing over an *insecure* channel (orig) | "insecure channel" | MED |
| 96 | "share a secret key in a secure channel, that can then..." — same contradiction + comma before restrictive "that" (orig) | "over an insecure channel that..." | MED |
| 8 | "If you wanted... then you have to ensure" — mixed conditional (orig) | "then you would have to" | MED |
| 70 | Figure caption ends "the key is 01" — missing final period (orig) | add "." | LOW |
| 35 | "between spins and bit value" vs Table 5.1 caption "between spin and bit values" (l. 38) — number disagreement between the two (orig) | harmonize | LOW |

## ch-06-quantum-gates.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 63 | "running the circuit 100 times" — contradicts "We repeat this process 1024 times" in the same paragraph and the figure caption; histogram bins (505/519 of 1024) confirm 1024 (orig) | "1024 times" | HIGH |
| 13 | "how the qubit and quantum computer has been implemented" — compound subject (orig) | "have been" | HIGH |
| 243 | "causes unwanted or incorrect affects" — noun needed (orig) | "effects" | HIGH |
| 245 | "if there has been any errors" — agreement (orig) | "have been" | HIGH |
| 26 | "all qubits... start with the incoming qubits in the |0⟩ state" — garbled duplication (orig) | "start in the |0⟩ state" | MED |
| 212 | "in the Fig. [](#fig-6-7)" — extraneous "the"; all other refs omit it (orig) | "in Fig. [](#fig-6-7)" | MED |
| 112 | "the Stern–Gerlach could be rotated" — proper name used as a noun (orig) | "the Stern–Gerlach apparatus" | LOW |

## ch-07-entanglement.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 21 | "must also land of tails!" — wrong preposition; parallel clause says "land on heads" (orig, p. 72) | "land on tails" | HIGH |
| 228 | "Two-qubit gates act... and creates entanglement" — agreement (orig, p. 81) | "create" | HIGH |
| 242 | "assume that two-qubits start in the state" — hyphen wrong on plural subject (orig, p. 81) | "two qubits" | MED |
| 221 | "of a two qubit system" — missing hyphen in compound modifier; ll. 76, 87, 91 hyphenate (orig) | "two-qubit system" | LOW |
| 29 | "How does the other coin... what was measured on the other?" — "the other" twice for two different coins (orig, p. 73) | "second coin... on the first" | LOW |

## ch-08-quantum-teleportation.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 15 | "as unitary matrices as defined as $UU^\dagger = 1$" — garbled (orig, p. 86) | "as unitary matrices are defined as" | HIGH |
| 134 | "neither Alice nor Bob know" — formal agreement prefers "knows" (orig) | "knows" | LOW |

## ch-09-quantum-algorithms.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 220 | "the Deutsch-Jozua problem" — misspelling; ~15 other occurrences say "Jozsa" (orig, p. 101) | "Deutsch-Jozsa" | HIGH |
| 222 | "needs to be be cooled down" — doubled word (orig, p. 101) | "to be cooled down" | HIGH |
| 137 | "we need to setup some useful tools" — verb is two words (orig) | "set up" | HIGH |
| 253 | "superposition and interference allows" — compound subject (orig, p. 103) | "allow" | HIGH |
| 113 | "the second beamsplitter" — every other occurrence (ll. 97, 115, 117, 167, 211; Ch. 3 title) uses "beam splitter" | "beam splitter" | HIGH |
| 43 | "the bits needed for the memory is linear" — agreement (orig, p. 94) | "are linear" | MED |
| 43 | "the qubits needed for memory is logarithmic" — same (orig) | "are logarithmic" | MED |
| 105 | "modelled" (British) vs "modeled" (l. 191) in the same chapter | "modeled" | MED |
| 222 | "difficult to keep lots of qubits..., but also cause isolated interactions" — broken infinitive parallelism (orig) | "but also to cause" | MED |
| 8 | "what we have learnt" vs "learned" (ll. 10, 43) — mixed within the chapter (orig) | "learned" | LOW |
| 45 | "a quantum chip (called the Bristlecone) which has 72-qubits" — hyphen wrong after verb; l. 43 "256-bits", "64-bits" same pattern (orig) | "72 qubits" | LOW |
| 222 | "lasers you need to interact the qubits" — "interact" needs "with" (orig) | "interact with the qubits" | LOW |
| 268 | "The Titan at Oak Ridge Laboratory" — official name is Oak Ridge *National* Laboratory (orig footnote) | "Oak Ridge National Laboratory" | LOW |

## ch-10-worksheets.md

| Line | Issue | Fix | Sev |
|---|---|---|---|
| 486 | Footnote: "Using Quantum Games to teacher quantum mechanics" — actual paper title is "to Teach" (orig, p. 107) | "to teach" | HIGH |
| 63 | "developed by Alan Goff in 2004" — the inventor spells his name "Allan Goff" (orig, p. 107) | "Allan Goff" | HIGH |
| 132 | "they know for sure in which state each marker would collapse into" — doubled preposition (orig, p. 110) | "into which state each marker would collapse" | HIGH |
| 260, 261 | "passing through a SGA" — vowel sound takes "an" (orig, p. 117) | "an SGA" (×2) | HIGH |
| 335 | "a five letter message" — unhyphenated; the identical sentence for Bob (l. 403) correctly hyphenates | "five-letter message" | HIGH |
| 69 | "placed in any of the two spaces" — garbled; rule 2 (l. 77) shows intent (orig) | "in any two spaces" | MED |
| 118 | "the winner with lowest sum of the indexes" — missing article (orig, p. 109) | "with the lowest sum" | MED |
| 128 | "a spin that is in superposition of up and down" — missing article; parallel phrase later in sentence has one (orig) | "in a superposition of" | MED |
| 130 | "choosing the way of measuring quantum system" — missing article (orig) | "measuring a quantum system" | MED |
| 341 | Heading "10.7.2 One-Time Pad (Bob)" — parallel Alice heading (l. 266) and all 10.8.x headings use a colon (orig) | "One-Time Pad: Bob" | MED |
| 217 | "the *x*- and *z*- basis" — stray space after hyphen (orig) | "*z*-basis" | LOW |
| 381 | "then the cipher text = 1011. 0110 + 1101 = 1011." — dangling fragment; Alice's parallel (l. 311) reads "= 1011, as 0110 + 1101 = 1011" (orig) | "…= 1011, as 0110 + 1101 = 1011." | LOW |

## Cross-cutting

| Issue | Locations | Fix | Sev |
|---|---|---|---|
| UK spellings in a US-English book | ch-07:303 "factorise"; ch-09:8,10 "learnt" (×3); ch-09:105 "modelled"; ch-09:169 "organised"; ch-10:214 "labelled" | US forms: factorize, learned, modeled, organized, labeled | MED |
| U+2215 DIVISION SLASH (∕) instead of "/" in prose | ch-01:40; ch-06:63 (×2); ch-07:103, 307; ch-08:126; ch-10:118 — 8 occurrences (conversion artifact, not in print original) | plain ASCII "/" | MED |
| "i.e." punctuation inconsistent | ch-01:56 ("i.e"), ch-04:245 ("i.e,") vs correct "i.e.," elsewhere | "i.e.," | LOW |
| "near absolute zero (around −450° Fahrenheit)" — absolute zero is −459.67 °F | ch-09:222 (orig) | "−460 °F" or "−459.67 °F" — human review | LOW |

## Verified clean
- All MyST cross-references (`[](#...)`, `:name:` labels, footnote markers) resolve across all 11 files; no dangling references.
- All referenced image files exist; section numbering 5.1–10.8 is sequential.
- `index.md` is clean; author list correct (Hughes, Isaacson, Perry, Sun, Turner).
- The XOR arithmetic (0110 + 1101 = 1011) and the "2 + 1 + 4 = 7" tic-tac-toe caption are correct.
