---
title: 2. What Is a Qubit?
short_title: "Ch. 2 — What Is a Qubit?"
label: ch-2
doi: 10.1007/978-3-030-61601-4_2
---

In classical computers, information is represented as the binary digits 0 or 1. These are called bits. For example, the number 1 in an 8-bit binary representation is written as 00000001. The number 2 is represented as 00000010. We place extra zeros in front to write every number with 8 bits total, which is called one byte. In fact, every classical computer translates these bits into the human readable information on your electronic device. The document you read or video you watch is encoded in the computer binary language in terms of these 1’s and 0’s. Computer hardware understands the 1-bit as an electrical current flowing through a wire (in a transistor) while the 0-bit is the absence of an electrical current in a wire. These electrical signals can be thought of as “on” (the 1-bit) or “off” (the 0-bit). Your computer then decodes the classical 1 or 0 bits into words or videos, etc.

Quantum bits or **qubits** are similar to bits in that there are two measurable states called the 0 and 1 states. However, unlike classical bits, qubits can also be in a superposition state of these 0 and 1 states, as shown in Fig. [](#fig-2-1). Certain computations that would normally need to be performed on 0 or 1 separately on a classical computer could now be completed in a single operation using a qubit on a quantum computer. Intuitively, this could make computations much faster. It is important to understand that although a single qubit is in a superposition of two classical bits, when a qubit is measured, the measurement actually only results in one classical bit of information: either 0 or 1.

```{figure} ../images/ch-02/490703_1_En_2_Fig1_HTML.png
:label: fig-2-1

:alt: A classical bit can be either 0 or 1. A qubit can be in a superposition of both 0 and 1


A classical bit can be either 0 or 1. A qubit can be in a superposition of both 0 and 1
```


(sec-2-1)=
## 2.1 Mathematical Representation of Qubits

### 2.1.1 Dirac Bra-Ket Notation

In order to work with qubits, it is useful to know how one can express quantum mechanical states with mathematical formulas. Dirac or “bra-ket” notation is commonly used in quantum mechanics and quantum computing. The state of a qubit is enclosed in the right half of an angled bracket, called the **“ket”**. A qubit, $\lvert \Psi \rangle$, could be in a $\lvert 0 \rangle$ or $\lvert 1\rangle$ state or even a superposition of both $\lvert 0\rangle$ and $\lvert 1\rangle$. This is written as

```{math}
:label: eq-2-1

\lvert \Psi \rangle = \alpha \lvert 0 \rangle + \beta \lvert 1 \rangle,
```

with *α* and *β* called the amplitudes of the states (Fig. [](#fig-2-2)). Amplitudes are generally complex numbers (a special type of number used in mathematics and physics). However, to understand the meaning of amplitudes, we can imagine the amplitudes as being ordinary (real) numbers. Amplitudes allow us to mathematically represent all of the possible superpositions.

```{figure} ../images/ch-02/490703_1_En_2_Fig2_HTML.png
:label: fig-2-2

:alt: The state of Schrödinger’s cat expressed in bra-ket notation


The state of Schrödinger’s cat expressed in bra-ket notation
```


**Amplitudes** are very important because they give us the probability of finding the particle in that specific state when performing a measurement. The probability of measuring the particle in state $\lvert 0 \rangle$ is $\lvert \alpha \rvert ^2$, and the probability of measuring the particle in state $\lvert 1 \rangle$ is $\lvert \beta \rvert ^2$. Why is it squared? The short answer is that it gives the correct experimental predictions for this choice of representation.[^1] Squaring *α* and *β* to find the probability is similar to squaring a wave’s amplitude to find the energy of the wave. Since the total probability of observing all the states of the quantum system must add up to 100%, the amplitudes must obey this rule:

```{math}
:label: eq-2-2

\lvert \alpha \rvert^2 + \lvert \beta \rvert^2 = 1.
```

This is called a **normalization** rule. The coefficients *α* and *β* can always be rescaled by some factor to normalize the quantum state.

### 2.1.2 Examples

1. The quantum state of a spinning coin can be written as a superposition of heads and tails. Using heads as $\lvert 1\rangle$ and tails as $\lvert 0 \rangle$, the quantum state of the coin is

   ```{math}
   :label: eq-2-3

   \lvert \text{coin} \rangle = \frac{1}{\sqrt{2}} \left( \lvert 1\rangle + \lvert 0 \rangle \right).
   ```

   What is the probability of getting heads?

   The amplitude of $\lvert 1\rangle$ is $\beta = 1/\sqrt {2}$, so $\lvert \beta \rvert ^2=\left ( 1/\sqrt {2}\right )^2=1/2$. So the probability is 0.5, or 50%.

2. A weighted coin has twice the probability of landing on heads vs. tails. What is the state of the coin in “ket” notation?

   ```{math}
   :label: eq-2-4

   \begin{aligned}
   P_{\text{heads}} + P_{\text{tails}} &= 1 ~~~(\text{Normalization Condition})\\
   P_{\text{heads}} &= 2P_{\text{tails}} ~~~(\text{Statement in Example})\\
   \rightarrow P_{\text{tails}} &= \frac{1}{3}= \alpha^2 \\
   \rightarrow P_{\text{heads}} &= \frac{2}{3}= \beta^2\\
   \rightarrow \alpha &= \sqrt{ \frac{1}{3}}, ~\beta = \sqrt{\frac{2}{3}}\\
   \rightarrow \lvert \text{coin} \rangle & =\sqrt{ \frac{1}{3}} \lvert 0 \rangle +\sqrt{ \frac{2}{3}} \lvert 1 \rangle.
   \end{aligned}
   ```

   One common misconception is that the measurement of a single qubit will result in a weighted average of the |0〉 and |1〉 states. It is important to note that after you perform the measurement on a single qubit, the qubit is no longer in a superposition but takes on a definite state of either |0〉 or |1〉.[^2] This means that you would not be able to find *α* or *β* from a single qubit. Instead, we need to create many qubits which are in the same quantum state, and then measure how many of the qubits collapse into |0〉 (giving *α*) and how many collapse into |1〉 (giving *β*). Therefore, multiple identical particles are needed in order to count how many collapse into |0〉 or |1〉.

(sec-2-2)=
## 2.2 Matrix Representation

When writing a single qubit in a superposition |*ψ*〉 = *α*|0〉 + *β*|1〉, it is useful to use matrix algebra. In matrix representation, a qubit is written as a two-dimensional vector where the amplitudes are the components of the vector

```{math}
:label: eq-2-5

|\psi\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}.
```

The states |0〉 and |1〉 are usually represented as

```{math}
:label: eq-2-6

|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad  |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.
```

Experimentally, a qubit’s state can be changed through some physical action such as applying an electromagnetic laser or passing it through an optical device. Changing a qubit’s state through a physical action mathematically corresponds to multiplying the qubit vector |*ψ*〉 by some **unitary matrix** *U* so that after the operation the state is now |*ψ*′〉 = *U*|*ψ*〉. Unitary is a mathematical term which expresses that *U* can only act on the qubit in such a way that the total probability |*α*|² + |*β*|² does not change. A matrix *U* is unitary if the matrix product of *U* and its conjugate transpose *U*† (called *U*-dagger) multiplies to give the identity matrix: $UU^{\dagger} = U^{\dagger}U = 1$. This is very important because, in all mathematical constructions of quantum mechanics, one fundamental assumption is that each (matrix) operator must be unitary. This ensures that after changing any state through an action, the total probability to observe all possible states will still add up to 100%. If this did not happen, then we could not interpret the results of quantum mechanics to be probabilistic, and the results would disagree with the many experiments that have been performed to date. The physical action of interacting with the state corresponds mathematically to applying a unitary operator.

### 2.2.1 Examples

1. What is the conjugate transpose of the following matrix?

   ```{math}
   :label: eq-2-7

   A = \begin{pmatrix} 1 & i \\ 1 & i \end{pmatrix}.
   ```

   The conjugate transpose of a matrix is found using the following two steps. First, we “conjugate” the complex numbers. The conjugate of a complex number is found by switching the sign of the imaginary part. The complex conjugate of 1 is just 1, while the complex conjugate of + *i* is − *i*. Second, we transpose the conjugated matrix. Transposing a matrix switches rows with columns, i.e., the first row turns into the first column, second row turns into the second column, etc. Therefore,

   ```{math}
   :label: eq-2-8

   A^{\dagger} = \begin{pmatrix} 1 & 1 \\ -i & -i \end{pmatrix}.
   ```

2. Is the above matrix *A* unitary?

   ```{math}
   :label: eq-2-9

   A A^{\dagger} = \begin{pmatrix} 1 & i \\ 1 & i \end{pmatrix} \begin{pmatrix} 1 & 1 \\ -i &-i \end{pmatrix}
   ```

   ```{math}
   :label: eq-2-10

   = 2 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \ne \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
   ```

   Multiplying *A* by its conjugate transpose does not produce the identity matrix, so *A* is not unitary.

3. What is the result of applying the unitary operator *X* onto a |0〉 state qubit?

   ```{math}
   :label: eq-2-11

   X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad  |0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.
   ```

   ```{math}
   :label: eq-2-12

   X|0\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |1\rangle.
   ```

   The *X* matrix changes the |0〉 qubit state to the |1〉 qubit state.

(sec-2-3)=
## 2.3 Bloch Sphere

A single qubit can be visualized using the Bloch sphere. The Bloch sphere is a visual representation of a qubit with similar geometric properties to the unit circle from trigonometry. Each point on the Bloch sphere corresponds to a different possible superposition of a single qubit. The top and bottom of the sphere correspond to the two measurable states of the qubit, |0〉 and |1〉. An arrow on the Bloch sphere, which can point to any of the different locations on the surface of the sphere, indicates the current state of the qubit. Figure [](#fig-2-3) shows four examples of how the Bloch sphere can be used to visualize different qubit states. When the arrow is not pointing directly to the top or bottom of the sphere, the qubit is in a superposition state. For example, everywhere around the equator the qubit has a 50/50 chance of collapsing into |0〉 or |1〉 upon measurement. The exact location on the equator corresponds to a distinct state, where the amplitudes can have different signs and be either real or imaginary numbers.

```{figure} ../images/ch-02/490703_1_En_2_Fig3_HTML.png
:label: fig-2-3

:alt: The state of a qubit is represented by an arrow on the Bloch sphere


The state of a qubit is represented by an arrow on the Bloch sphere
```


When the state of the qubit is changed, the arrow rotates to a different position on the sphere. One analogy is to think of the qubit like Schrödinger’s cat traveling the globe shown in Fig. [](#fig-2-4). When the cat is at the North Pole, it will definitely be alive. When the cat is at the South Pole, it will definitely be dead. As long as the cat’s state is not measured, it can be anywhere else on the globe in a superposition state of alive and dead. As coders of the quantum computer, it is our job to manipulate the state of the qubit which gives the cat instructions on how to move around the globe.

```{figure} ../images/ch-02/490703_1_En_2_Fig4_HTML.png
:label: fig-2-4

:alt: A cartoon of the Bloch sphere depicted as the Earth, and the state of Schrödinger’s cat represented as a location on Earth


A cartoon of the Bloch sphere depicted as the Earth, and the state of Schrödinger’s cat represented as a location on Earth
```


**Question 1** Schrödinger’s cat is determined to be alive. What location on the Earth in Fig. [](#fig-2-4) could the cat have been before the quantum measurement?

- (a) Russia
- (b) Australia
- (c) North Pole
- (d) all of the above

The cat could have been anywhere on Earth except for the South Pole. Notice that in Australia the cat has a smaller probability of being alive since it is further away from the North Pole.

The Bloch sphere is a helpful visual aid for understanding how a qubit can have an infinite number of possible quantum states. However, it only represents one qubit and does not work for systems of two or more qubits.

(sec-2-4)=
## 2.4 Physical Realization of Qubits

In a classical computer, the 0-bit and 1-bit values mathematically represent the two allowed voltages across a wire in a classical circuit. Semiconductor devices called transistors are used to control what happens to these voltages. A question frequently posed by new students is “What is a qubit made out of?” As quantum computers are based on fundamentally different concepts than classical computers, they must be built from completely different technology, i.e. it is not possible to have a classical current in a superposition of both flowing and not flowing through a wire. Quantum computers are still in their infancy, and so there are many different candidates for the technology to build them. Some technologies are based on optical systems, others use superconductors,[^3] and there are others based on molecules. It is still unclear if any of these are more beneficial than the others, and it is even more unclear if all future quantum computers will be built from the same technology or if there will be many different types of quantum computers available (in the same way there exist both XBox and PlayStation game consoles, but both have the same general purpose—interactive gaming). We will study two different experiments which illustrate the properties of the qubits, but the engineering details of building a quantum computer are well beyond the scope of this introduction.

(sec-2-5)=
## 2.5 Big Ideas

1. A qubit can be in a superposition of |0〉 and |1〉 states. The Bloch sphere can be used to visually represent a single qubit.
2. A qubit can be written in terms of amplitudes. Each squared amplitude corresponds to the probability of measuring the qubit in |0〉 or |1〉.
3. A physical change to a qubit mathematically corresponds to unitary matrices which multiply the qubit amplitudes.

(sec-2-6)=
## 2.6 Check Your Understanding

1. If a coin is a classical bit of information (heads = 1 and tails = 0), how is the number 2 represented in standard 8-bit notation using coins? (Hint: Find the 8-bit representation of the number 2, then convert to H’s and T’s.)

2. Using Table [](#tbl-2-1), can you figure out what this binary message 01000011 01000001 01010100 says? (Note: This is actually how your computer and phone decode information from bits to text.)

(tbl-2-1)=
**Table 2.1** Table for message

| Character | Binary code | Character | Binary code |
| --- | --- | --- | --- |
| A | 01000001 | N | 01001110 |
| B | 01000010 | O | 01001111 |
| C | 01000011 | P | 01010000 |
| D | 01000100 | Q | 01010001 |
| E | 01000101 | R | 01010010 |
| F | 01000110 | S | 01010011 |
| G | 01000111 | T | 01010100 |
| H | 01001000 | U | 01010101 |
| I | 01001001 | V | 01010110 |
| J | 01001010 | W | 01010111 |
| K | 01001011 | X | 01011000 |
| L | 01001100 | Y | 01011001 |
| M | 01001101 | Z | 01011010 |

3. Assume a flipped coin can be measured as either heads (H) or tails (T).

   - (a) If the coin is in a normalized state $\frac {1}{\sqrt {10}} \lvert H \rangle + \frac {3}{\sqrt {10}} \lvert T \rangle$, what is the probability that the coin will be tails?
   - (b) During a flip, the coin is in a state $\frac {1}{3} \lvert H \rangle + \frac {2}{3} \lvert T \rangle$. Is this state normalized?
   - (c) A machine is built to flip coins and put them into a state $\frac {1}{2} \lvert H \rangle + \frac {\sqrt {3}}{2} \lvert T \rangle$ when flipped. If 100 coins are flipped, how many coins should land on tails?
   - (d) A coin starts in the state $\frac {1}{\sqrt {10}} \lvert H \rangle + \frac {3}{\sqrt {10}} \lvert T \rangle$. After a measurement is made on the coin, what could be the state of the coin?

4. Your friend gives you many qubits which are in the same superposition state. How can you determine what the state is?

5. A qubit is prepared in an unknown state. It is then measured with the outcome $\lvert 0 \rangle$.

   - (a) Which of the following could be its initial state before the measurement: $\lvert 0 \rangle$, $\frac {1}{\sqrt {10}}\lvert 0 \rangle + \frac {3}{\sqrt {10}}\lvert 1 \rangle$, $\frac {1}{2}\lvert 0 \rangle + \frac {\sqrt {3}}{2}\lvert 1 \rangle$ and/or $\frac {1}{\sqrt {2}}\left ( \lvert 0 \rangle + \lvert 1 \rangle \right )$?
   - (b) If you tried to measure the same qubit a second time, can you narrow down what the initial state was?
   - (c) Another qubit is prepared in the same unknown state. It is measured in the $\lvert 1 \rangle$ state. What can you say about the initial state now?

6. What is the matrix product of the *X* matrix,

   ```{math}
   :label: eq-2-13

   X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
   ```

   and the $\lvert 0 \rangle$ state qubit?

7. What is the matrix product of the above *X* matrix and the $\lvert 1 \rangle$ state qubit?

8. What is the matrix product of the above *X* matrix and a qubit in the general state $\lvert \Psi \rangle = \alpha \lvert 0 \rangle + \beta \lvert 1 \rangle$?

9. Find the conjugate transpose of the matrix

   ```{math}
   :label: eq-2-14

   Y=\begin{pmatrix} 0 & -i\\ i & 0 \end{pmatrix}.
   ```

10. Show that the matrix

    ```{math}
    :label: eq-2-15

    U=\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1\\ 1 & -1 \end{pmatrix}
    ```

    is unitary.

11. Show by example that applying a non-unitary matrix to a qubit results in probabilities that no longer add up to 100%. (Hint: Start with any initial state, e.g., |0〉. Measure the probabilities of finding either 0 or 1. Apply a non-unitary matrix to the initial state. Then measure the probabilities of finding either a 0 or 1. Do the probabilities add up to 100%?)

12. If the qubit represented by Fig. [](#fig-2-5) is measured, what are the possible outcomes? Numerical values for the amplitudes are not needed, only conceptual statements.

    ```{figure} ../images/ch-02/490703_1_En_2_Fig5_HTML.png
    :label: fig-2-5

    :alt: A qubit’s state is shown on the Bloch sphere


    A qubit’s state is shown on the Bloch sphere
    ```


[^1]: We know that quantum physics is probabilistic from experiments. The squared coefficients are needed to make a quantity that behaves like a probability distribution, i.e., it is a real number and positive. There cannot be a negative probability by definition.

[^2]: When formulating the mathematical representation of quantum mechanics, this is one of four fundamental assumptions that need to be made. The reason for the collapse is still unknown: [https://en.wikipedia.org/wiki/Wave_function_collapse](https://en.wikipedia.org/wiki/Wave_function_collapse). Read more at this link: [https://www.quantamagazine.org/how-quantum-trajectory-theory-lets-physicists-understand-whats-going-on-during-wave-function-collapse-20190703/](https://www.quantamagazine.org/how-quantum-trajectory-theory-lets-physicists-understand-whats-going-on-during-wave-function-collapse-20190703/).

[^3]: Fermi National Accelerator Laboratory is researching how to make long-lived coherent qubits using their superconducting radio-frequency cavity expertise, i.e., [https://qis.fnal.gov/superconducting-quantum-systems/](https://qis.fnal.gov/superconducting-quantum-systems/).
