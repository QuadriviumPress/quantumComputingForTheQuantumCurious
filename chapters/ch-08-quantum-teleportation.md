---
title: 8. Quantum Teleportation
short_title: "Ch. 8 — Teleportation"
label: ch-8
doi: 10.1007/978-3-030-61601-4_8
---

One interesting application of entanglement is **quantum teleportation**, which is a technique for transferring an *unknown* quantum state from one place to another. In science fiction, teleportation generally involves a machine scanning a person and another machine reassembling the person on the other end. The original body disintegrates and no longer exists. Similarly, quantum teleportation works by “scanning” the original qubit, sending a recipe, and reconstructing the qubit elsewhere. The original qubit is not physically destroyed in the science fiction sense, but it is no longer in the same state. Otherwise, the previously mentioned **no-cloning** theorem—which states that a qubit cannot be exactly copied onto another qubit—would be violated.[^1] As we will see, the “scanning” part poses a problem which can only be solved by leveraging quantum entanglement.

(sec-8-1)=
## 8.1 Scanning a Qubit

**Question 1** Create a qubit in the |1〉 state and pass it through a Hadamard gate. From the measurement histogram, can you tell whether the qubit started as a |0〉 or |1〉 initial state?

The measurement histogram should look identical if either of the |0〉 or |1〉 states is used initially. Then how can we tell what the initial state was after performing a Hadamard operation? In the beam splitter, we determined where the photon came from by adding a second beam splitter to create interference. The way to measure and distinguish between them is to add a second Hadamard gate. As we have seen in Sect. [](#sec-2-2), all gates must be unitary to conserve probabilities. The unitary condition ensures that all gates are reversible: we can undo the action of any gate by applying its conjugate transpose. This is easily seen in matrix form as unitary matrices as defined as $UU^\dagger = 1$. As the Hadamard gate is its own conjugate transpose, applying a second Hadamard gate is equivalent to undoing the first. This is how the original state is recovered.

**Question 2** If a qubit is in the unknown state *a*|0〉 + *b*|1〉, what is the result of a single measurement?

- (A) 0
- (B) 1
- (C) 0 with probability *a*² and 1 with probability *b*²
- (D) A number between 0 and 1

**Question 3** What is the result of a second measurement after the first from Question 2?

- (A) 0 if the first measurement is 0 or 1 if the first measurement is 1
- (B) 0 if the first measurement is 1 or 1 if the first measurement is 0
- (C) 0 with probability *a*² and 1 with probability *b*²
- (D) A number between 0 and 1

Given a single qubit, it is not possible to determine how much of a superposition it is in if you only have this single qubit, i.e., you cannot determine the coefficients of |0〉 and |1〉 in a general state from one measurement! Note that if the state is known (from measuring many independent qubits that have been prepared identically), then you can just directly send the recipe to prepare this qubit. It is only when the state is unknown and when there is only one qubit that we have to think harder about how to efficiently “scan” the particle.

(sec-8-2)=
## 8.2 Teleportation Protocol

The way to get around the problem of not being able to measure the qubit (and avoid collapsing the unknown state onto a basis state) is to “scan” the qubit indirectly with the help of entangled particles. This [comic](https://www.jpl.nasa.gov/news/news.php?feature=4384)[^2] illustrates the basic idea. The protocol is as follows:

1. Alice and Bob meet up and make a qubit each (which we will call qubit #2 and #3). At this point, the two qubits are completely independent and we can think of the qubits as two different balls that do not contain any information about the other. Then, Alice and Bob decide to entangle their qubits by causing an interaction between the qubits, for example by applying a CNOT gate. Think of entanglement as Alice writing some information on Bob’s ball that only she knows how to read, and Bob writing information on Alice’s ball that only he knows how to read. For Bob to read Alice’s information on his ball, Alice needs to send him a (classical) message describing how to understand it, and vice-versa. They do not tell each other how to read the information yet. One possible entangled state (called the Bell-state) that they decide to create is

   ```{math}
   :label: eq-8-1

   \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle.
   ```

   Alice takes her qubit and walks away, and Bob takes his and walks in a different direction as shown in Fig. [](#fig-8-1).

   ```{figure} ../images/ch-08/490703_1_En_8_Fig1_HTML.png
   :name: fig-8-1

   Alice and Bob’s qubits are entangled
   ```

2. Now Alice obtains a third qubit in an unknown state (qubit #1) that she wants to transfer to Bob. She can only communicate with him classically by email or phone, and it would take too long to physically bring the qubit to Bob. The current situation is shown in Fig. [](#fig-8-2).

   ```{figure} ../images/ch-08/490703_1_En_8_Fig2_HTML.png
   :name: fig-8-2

   Alice has a qubit (*#*1) in an unknown state she wants to transfer to Bob
   ```

3. Alice interacts her two qubits using a CNOT gate (qubits #1 and #2) and measures the qubit she originally had (qubit #2). She then sends the unknown qubit to be teleported (qubit #1) through a Hadamard gate and afterwards measures the output. Recall that the Hadamard gate is used to create a superposition of states. The current situation is shown in Fig. [](#fig-8-3).

   ```{figure} ../images/ch-08/490703_1_En_8_Fig3_HTML.png
   :name: fig-8-3

   Alice passes her two qubits through a CNOT gate
   ```

   Because Alice’s original qubit (qubit #2) was entangled with Bob’s, the CNOT interaction with qubit #1 immediately changes the state of Bob’s qubit.

   When understanding quantum teleportation, it may be more insightful to see the mathematical description of this three-qubit protocol. Qubit #1 is the qubit to be teleported, and qubit #2 and #3 are the entangled pair shared by Alice and Bob. In ket notation, the three-qubit state is written in the order | #1 #2 #3 〉. In addition, the three-qubit state can be written in ket notation in different ways as long as the order of the qubits is kept unchanged. For example, if qubit #1 = |0〉, qubit #2 = |1〉, and qubit #3 = |1〉, they can be written as |0〉|1〉|1〉 = |011〉 = |0〉|11〉 = |01〉|1〉. Sometimes it is easier to split up the multi-qubit state like this to explicitly show if a gate is acting on a single qubit.

   Now, from steps (1) and (2) we have Alice and Bob’s qubits in the Bell state $\frac {1}{\sqrt {2}}(|00\rangle + |11\rangle )$. Qubit #1 is in an unknown state *a*|0〉 + *b*|1〉. At the start of step (3), the three qubits need to be written together in ket notation by multiplying the qubit to be teleported by the entangled Bell state. The product is:

   ```{math}
   :label: eq-8-2

   \left[a|0\rangle+b|1\rangle\right] \left(\frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle\right) = \frac{1}{\sqrt{2}}\Big(a|000\rangle + a|011\rangle+b|100\rangle+b|111\rangle\Big).
   ```

   Next, we apply a CNOT gate using the first qubit in Eq. ([](#eq-8-2)) as the control and the second as the target. Recall that the target (qubit #2) changes state only if the control is |1〉. After applying the CNOT gate the three-qubit state is

   ```{math}
   :label: eq-8-3

   \frac{1}{\sqrt{2}} \Big(a|000\rangle + a|011\rangle+b|110\rangle+b|101\rangle\Big).
   ```

   After this, we apply a Hadamard gate to qubit #1 in Eq. ([](#eq-8-3)). Recall that the Hadamard gate changes the state $|0\rangle \to ({1}/{\sqrt {2}})(|0\rangle + |1\rangle )$, and $|1\rangle \to ({1}/{\sqrt {2}})(|0\rangle - |1\rangle )$. The three-qubit state is

   ```{math}
   :label: eq-8-4

   \frac{1}{2}\Big( a\left(|0\rangle+|1\rangle\right)|00\rangle + a\left(|0\rangle+|1\rangle\right)|11\rangle+b\left(|0\rangle-|1\rangle\right)|10\rangle+b\left(|0\rangle-|1\rangle\right)|01\rangle \Big).
   ```

   Next, distribute the product of qubits throughout Eq. ([](#eq-8-4)) to find

   ```{math}
   :label: eq-8-5

   \frac{1}{2} \Big(a|000\rangle+a|100\rangle +a|011\rangle+a|111\rangle+b|010\rangle-b|110\rangle+b|001\rangle-b|101\rangle\Big).
   ```

   Finally, combine like-terms of Eq. ([](#eq-8-5)) based on the first two qubits to get

   ```{math}
   :label: eq-8-6

   \frac{1}{2} \Big( |00\rangle(a|0\rangle+b|1\rangle)+|10\rangle(a|0\rangle-b|1\rangle)+|01\rangle(a|1\rangle+b|0\rangle)+|11\rangle(a|1\rangle-b|0\rangle)\Big)
   ```

   Remember that qubit #1 and qubit #2 are the ones that belong to Alice. We see that the state of Bob’s qubit #3 has changed by applying the CNOT and Hadamard gates to Alice’s qubits. As can be seen in Eq. ([](#eq-8-6)), Bob’s qubit is currently in one of four possible superposition states. This is shown in Fig. [](#fig-8-4).

   ```{figure} ../images/ch-08/490703_1_En_8_Fig4_HTML.png
   :name: fig-8-4

   Four possible superposition states of Bob’s qubit
   ```

   The four possible superposition states of Bob’s qubit depend on Alice’s original qubit #2 through the initial entanglement in Step 1, as well as depending on the unknown qubit #1 to be teleported from the CNOT gate in Step 3. The reason we need to measure the state of Alice’s qubit #2 and qubit #1 is to figure out the way Bob’s qubit depends on these two. The current status is shown in Fig. [](#fig-8-4). Note that Bob has not done anything with his qubit at this stage.

4. Alice now sends the two classical bits of information from the measurements to Bob by email or phone. According to Eq. ([](#eq-8-6)), her measurements can be 00, 10, 01 or 11, each with 25% probability.

Depending on the measurement obtained by Alice, Bob can recover the original state of the teleported qubit (i.e., *a*|0〉 + *b*|1〉) by using a combination of *X* or *Z* gates. The specific combination of *X*∕*Z* gates to use will be explored as a question in Sect. [](#sec-8-4). This situation is illustrated in Fig. [](#fig-8-5). At this stage, the qubit has been successfully teleported from Alice to Bob, and thus ends the teleportation protocol.

```{figure} ../images/ch-08/490703_1_En_8_Fig5_HTML.png
:name: fig-8-5

The final result of teleportation between Bob and Alice
```

Throughout the teleportation process, the original qubit #1 that has to be teleported does not remain in its original quantum state: *a*|0〉 + *b*|1〉. This is because Alice performs a measurement on it during the teleportation protocol. As a result, there is no copy of qubit #1 existing at any time, and so teleportation does not contradict the no-cloning theorem. It is important to understand that neither Alice nor Bob know what qubit #1’s coefficients *a* or *b* are at any point in the process. All they know is that qubit #1 has been teleported from Alice to Bob. The full quantum teleportation circuit is illustrated in Fig. [](#fig-8-6).

```{figure} ../images/ch-08/490703_1_En_8_Fig6_HTML.png
:name: fig-8-6

The full quantum circuit for quantum teleportation. The dashed box entangles Alice’s and Bob’s qubits to make the Bell state. Afterwards, the quantum teleportation protocol described in the text is performed.
```

Why is this protocol interesting? To answer this, imagine Alice and Bob met a long time ago and each took one qubit of the entangled pair. Bob is now traveling around the world and can only communicate with Alice by phone or email. If Alice wanted to transfer quantum data to Bob without quantum teleportation, she would have to meet Bob and physically give Bob her qubit. Quantum teleportation allows Alice to send *quantum* information using a *classical* communications channel. All she has to do is make some measurements and email Bob the values. Bob can then apply the correct recipe to his qubit to bring it to the state of the original qubit #1. As well as sending information between two people, quantum teleportation is a useful way of causing interaction between different parts of a quantum computer (by teleporting a qubit to a different part of the quantum computer you want to interact with).[^3]

(sec-8-3)=
## 8.3 Big Ideas

1. If Alice and Bob have a single qubit each, which they entangle, it is possible for Alice to teleport the information encoded in a third unknown qubit into Bob’s qubit.

2. Quantum teleportation sends quantum information by using the entanglement and measurement properties of quantum mechanics.

3. Quantum teleportation does not destroy the qubit to be teleported (like in science fiction). It only transfers the information contained within the qubit without ever needing to know that information.

(sec-8-4)=
## 8.4 Check Your Understanding

1. Could quantum teleportation be used to teleport a physical object from one place to another? Why or why not?

2. What would lead someone to think quantum teleportation can transmit information faster than the speed of light? Explain why this is not possible.

3. By the no-cloning theorem, it is not possible to make a copy of an unknown qubit. At what point in the teleportation protocol does the unknown qubit collapse into a definite state?

4. In the original protocol, Alice applies the CNOT and then measures Bit 2 (see Fig. [](#fig-8-3)). After this, Alice then applies the Hadamard to qubit #1 and then measures Bit 1 (see Fig. [](#fig-8-3)). What happens if she decides to reverse the procedure by measuring Bit 1 first, before applying the two-qubit CNOT gate?

5. If Bob knows that his qubit is in the *b*|0〉 + *a*|1〉 state, which gate(s) would he need to use to change it back into the original needed *a*|0〉 + *b*|1〉 state?
   - (A) *X*
   - (B) *Z*
   - (C) *X* then *Z*

6. If Bob knows that his qubit is in the *a*|0〉 − *b*|1〉 state, which gate(s) would he need to use to change it back into the original needed *a*|0〉 + *b*|1〉 state?
   - (A) *X*
   - (B) *Z*
   - (C) *X* then *Z*

7. If Bob knows that his qubit is in the *a*|1〉 − *b*|0〉 state, which gate(s) would he need to use to change it back into the original needed *a*|0〉 + *b*|1〉 state?
   - (A) *X*
   - (B) *Z*
   - (C) *X* then *Z*

[^1]: The no-cloning theorem poses a big problem for correcting errors that happen on quantum computers: [https://en.wikipedia.org/wiki/Quantum_error_correction](https://en.wikipedia.org/wiki/Quantum_error_correction).

[^2]: [https://www.jpl.nasa.gov/news/news.php?feature=4384](https://www.jpl.nasa.gov/news/news.php?feature=4384).

[^3]: Fermi National Accelerator Laboratory is building a quantum teleportation experiment which will extend over large distances, helping to develop a future quantum internet, e.g., [https://qis.fnal.gov/quantum-teleportation-experiment/](https://qis.fnal.gov/quantum-teleportation-experiment/).
