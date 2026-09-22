---
title: "3. Creating Superposition: The Beam Splitter"
short_title: "Ch. 3 — Beam Splitter"
label: ch-3
doi: 10.1007/978-3-030-61601-4_3
---

Now that we have explored qubits and the phenomenon of superposition, we can ask the question: how do we know that superposition actually happens? What is the evidence that shows that a quantum particle really does exist in two different locations at the same time while in a quantum superposition? The nature of science means that experiments are constantly updating previous results, so are there other interpretations of the experimental results that can explain the data without the need for superposition? In this chapter we’ll explore the experimental evidence that debunks interpretations other than quantum superposition. Further, while a flipping coin is a simple model of a qubit, it is not very useful for building a quantum computer because it does not exhibit all of the properties of a true quantum superposition. For example, we cannot manipulate the superposition amplitudes. In this chapter, we will study some real physical examples of quantum particles in a superposition containing two states. These examples include a photon in a beam splitter and the Mach–Zehnder interferometer.

(sec-3-1)=
## 3.1 Beam Splitter

In classical optics, a **beam splitter** acts like a partially reflective mirror that splits a beam of light into two. In a 50/50 beam splitter, 50% of the light intensity is transmitted and 50% is reflected, as shown in Fig. [](#fig-3-1).

```{figure} ../images/ch-03/490703_1_En_3_Fig1_HTML.png
:label: fig-3-1

:alt: A beam splitter reflects 50% of the incident light and transmits 50% of the incident light


A beam splitter reflects 50% of the incident light and transmits 50% of the incident light.
```


One way to visualize the beam splitter is to imagine a barrier with holes randomly cut out like Swiss cheese, as shown in Fig. [](#fig-3-2). Imagine this barrier is placed in a pond, and a water wave moves toward the barrier. After the wave hits the barrier, we would observe a smaller wave going through the barrier and another would be reflected off the barrier.

```{figure} ../images/ch-03/490703_1_En_3_Fig2_HTML.png
:label: fig-3-2

:alt: A beam splitter reflects 50% of the incident light and transmits 50% of the incident light


A beam splitter reflects 50% of the incident light and transmits 50% of the incident light.
```


**Question 1** What would happen if a classical particle such as a soccer ball were randomly kicked at the barrier? Assume the ball can fit through the holes.

Experiments demonstrate that light behaves both like a wave (Young’s double-slit experiment) and a particle (photoelectric effect, Compton effect). Classically, light is thought of as a wave consisting of continually oscillating electric and magnetic fields. However, light can also be thought of as a stream of particles called **photons**. Photons have no mass but carry the light’s energy from one point to another at the speed of light. A laser beam is comprised of photons. If you turn down the intensity of your laser, you can even send one photon at a time, as shown in Fig. [](#fig-3-3). As setting up a single photon source and detector requires specialized equipment, we will instead run a simulator to explore the quantum effects of photons.

```{figure} ../images/ch-03/490703_1_En_3_Fig3_HTML.png
:label: fig-3-3

:alt: Low-intensity light is a stream of single photons


Low-intensity light is a stream of single photons.
```


**Question 2** Open the beam splitter simulator,[^1] go to the Controls screen, and fire a single photon. The setup before the photon hits a beam splitter is shown in Fig. [](#fig-3-4). Which detectors are triggered when the photon passes through the 50/50 beam splitter?

```{figure} ../images/ch-03/490703_1_En_3_Fig4_HTML.png
:label: fig-3-4

:alt: A single photon is sent at a beam splitter and the outcome is measured with detectors to see whether the beam splitter transmits or reflects


A single photon is sent at a beam splitter and the outcome is measured with detectors to see whether the beam splitter transmits or reflects.
```


- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither

**Question 3** Which detector(s) would trigger if a classical **wave** is sent through the beam splitter?

- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither

**Question 4** Which detector(s) would trigger if a classical **particle** is sent through the beam splitter?

- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither

**Question 5** What does the photon do at the instant it encounters the 50/50 beam splitter?

- (a) Splits in half. Half the photon is transmitted and half is reflected
- (b) The whole photon goes through with 50% probability and reflects with 50% probability
- (c) The whole photon is both transmitted and reflected, essentially in two places at once

If the photon was split in half, both detectors in the beam splitter experiment would be triggered at the same time. As only one detector goes off at a time, the photon could not have split up. In this case, we see that light behaves more like the soccer ball than the water wave.

At this point you may be thinking that the photon was either transmitted or reflected at the beam splitter, and we simply didn’t have that information until it hit Detector 1 or 2. Unfortunately, this would be the incorrect interpretation formed by our classical animal brain. This would be like saying the coin was Heads all along, and all we had to do was look at it to determine its state. Similarly to how a spinning coin will land on heads 50% of the time and tails 50% of the time, the single photon is in a superposition of both states all the way until the point when it reaches the detectors. This distinction might seem like a matter of semantics, but this is important as the distinction describes two different ways that the universe operates at the smallest possible distances. Also, it will be important once the system becomes more complicated. The experimental setup after the photon hits a beam splitter is shown in Fig. [](#fig-3-5).

```{figure} ../images/ch-03/490703_1_En_3_Fig5_HTML.png
:label: fig-3-5

:alt: The beam splitter puts the photon into a superposition state


The beam splitter puts the photon into a superposition state.
```


If we let the transmitted path be |0〉 (detector 1), and the reflected path be |1〉 (detector 2), then the photon’s state after the beam splitter is

```{math}
:label: eq-3-1

\lvert \text{photon}\rangle = \frac{1}{\sqrt{2}} \lvert 0\rangle + \frac{1}{\sqrt{2}} \lvert 1\rangle.
```

Upon measurement, will the superposition collapse into either |0〉 or |1〉? Unfortunately, it is not possible to predict which detector will be activated at any given time as quantum mechanics is inherently probabilistic.

The phenomenon of superposition allows quantum computers to perform operations on two bits of information at once with a single qubit. In fact, it is possible to create a general purpose (also called universal) quantum computer using photons as qubits, beam splitters to create superposition, and pieces of glass that slow down the photons along selected paths (phase shifters).[^2]

(sec-3-2)=
## 3.2 Mach–Zehnder Interferometer

To convince ourselves that the photon really did take two paths at once, let’s see what happens when a second beam splitter is added. This experimental setup is shown in Fig. [](#fig-3-6). The mirrors redirect the photons towards the second beam splitter. This device configuration is known as a **Mach–Zehnder interferometer**. The set up is very sensitive to the distances between the mirrors and detectors, which have to be the same or differ by an integer number of the photon’s wavelength.

```{figure} ../images/ch-03/490703_1_En_3_Fig6_HTML.png
:label: fig-3-6

:alt: Schematic of the Mach–Zehnder interferometer from...


Schematic of the Mach–Zehnder interferometer from [https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/Mach-Zehnder-Interferometer/Mach_Zehnder_Interferometer.html](https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/Mach-Zehnder-Interferometer/Mach_Zehnder_Interferometer.html)
```


**Question 6** If we assume that the photon was reflected by the first beam splitter, which detectors would be triggered?

- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither

**Question 7** If we assume that the photon was transmitted by the first beam splitter, which detectors would be triggered?

- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither.

**Question 8** Construct the Mach–Zehnder interferometer in the beam splitter simulator[^3] and fire a single photon. Which detectors are triggered?

- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither

If the photon was either transmitted or reflected by the first beam splitter, it would have a 50/50 chance of transmission or reflection by the second beam splitter. Thus, both detectors should trigger with equal probability. However, strangely the experimental results do not agree with this hypothesis, as only one detector is triggered with 100% probability. This weird phenomenon is more intuitively understood from the wave perspective of light.

To understand the operation of the interferometer, it is important to note that the beam splitters have a polarity. The beam splitter consists of a piece of glass coated with a dielectric on one side. When light enters the beam splitter from the dielectric side, the reflected light is **phase shifted** by *π*. Light entering from the glass side will not experience any phase shift. The phase shift only occurs when the light travels from a low to high index of refraction ($n_{\text{air}} < n_{\text{dielectric}} < n_{\text{glass}}$).

What does it mean for a photon to be phase shifted? In this case, it is more intuitive to think about the wave nature of light. The phase shift would invert the electric and magnetic field oscillations relative to the incoming wave. If a *π*-shifted wave overlaps with the original wave, destructive interference occurs as is shown in Fig. [](#fig-3-7).

```{figure} ../images/ch-03/490703_1_En_3_Fig7_HTML.png
:label: fig-3-7

:alt: The light through a beam splitter is phase shifted if it is reflected from the dielectric side but not phase shifted if it is reflected from the glass side


The light through a beam splitter is phase shifted if it is reflected from the dielectric side but not phase shifted if it is reflected from the glass side.
```


**Question 9** If we assume that light is a classical wave exhibiting interference, can you work out which detectors would be triggered? Note that the first beam splitter has the dielectric side on top, while the second has the dielectric on the bottom, as shown in Fig. [](#fig-3-6).

- (a) Always detector 1
- (b) Always detector 2
- (c) Detector 1 OR detector 2
- (d) Both detector 1 AND detector 2
- (e) Neither

### 3.2.1 Particle Explanation

The behavior of the interferometer can also be viewed from the particle perspective, though it may be less intuitive. Recall from the single beam splitter experiment that the photon did not split up or clone itself. It was in a superposition state, essentially taking both paths. The second beam splitter treats the photon as if it came in from both top and bottom simultaneously. As shown in Fig. [](#fig-3-8), the top path enters the second beam splitter from the glass side and experiences no phase shift, whereas the bottom path enters from the dielectric side and is phase shifted upon reflection. The +0 and +*π* states at Detector 2 interfere destructively, while the +0 and +0 states at Detector 1 interfere constructively. Therefore, Detector 1 triggers with 100% probability.

```{figure} ../images/ch-03/490703_1_En_3_Fig8_HTML.png
:label: fig-3-8

:alt: The blue path shows the photon’s path if it is reflected by Beam Splitter 1. The red path shows the path if the photon is transmitted. Because Beam Splitter 2 has the dielectric facing downwards,...


The blue path shows the photon’s path if it is reflected by Beam Splitter 1. The red path shows the path if the photon is transmitted. Because Beam Splitter 2 has the dielectric facing downwards, blue is phase shifted upon reflection.
```


**Question 10** If the photon is sent into the Mach–Zehnder interferometer from the upper left instead of the bottom left, which detector(s) would be triggered and with what probability?

Even though the output of the first beam splitter is 50/50, the second beam splitter can distinguish whether the laser was fired from the top or the bottom. The first beam splitter creates a superposition state, but adding a second one undoes the superposition and recovers the original state. This is a non-classical operation. It would be like starting with the coin heads up, flipping it, flipping it again while it is still in the air, and then always getting heads when it lands! This is highlighted in Fig. [](#fig-3-9).

```{figure} ../images/ch-03/490703_1_En_3_Fig9_HTML.png
:label: fig-3-9

:alt: Coin analogy for the interferometer. Sending a photon through one beam splitter puts it in superposition, but adding a second beam splitter undoes the superposition and recovers the original state


Coin analogy for the interferometer. Sending a photon through one beam splitter puts it in superposition, but adding a second beam splitter undoes the superposition and recovers the original state.
```


There is hidden information in the superposition state. In the Mach–Zehnder photon qubit, the information is encoded in the form of the phase shift. In the experiment shown in Fig. [](#fig-3-8), we chose the phase shift to have a value of *π*. However, we could have just as easily chosen the phase shift to have any value between 0 and 2*π* (the angles of a circle). Each separate choice of phase shift would produce a different type of superposition state that would still produce the same measurable 50/50 outcome. This is represented on the Bloch sphere by different locations along the equator.[^4] This phase shift information is present in the amplitudes but not the square of the amplitudes (and hence hidden from us in the Mach–Zehnder experiment–though we could make another experiment to try to determine this information). Here are two simple examples of distinct states that can be created in two different experimental arrangements of the Mach–Zehnder experiment which still have the same 50/50 probability:

```{math}
:label: eq-3-2

\frac{1}{\sqrt{2}} \lvert 0\rangle + \frac{1}{\sqrt{2}} \lvert 1\rangle \quad \text{or} \quad \frac{1}{\sqrt{2}} \lvert 0\rangle - \frac{1}{\sqrt{2}} \lvert 1\rangle.
```

In these two states the plus or minus signs represent two of the many different phase shifts that are possible. Each different choice of the phase shift depends on how the experimental arrangement is chosen. As you can see, quantum superposition is inextricably linked to wave-particle duality.

Furthermore, in the Mach–Zehnder experiment we created a superposition, performed a phase shift and then observed wave interference. These experimental operations are equivalent to mathematically applying matrix/gate operations on a qubit, as we shall see later. As such, the Mach–Zehnder is an example of how we can technologically implement qubits (the photon) and operations (superposition/phase shift, etc.) to build a quantum computer.[^5] In quantum computing, people talk about the superposition of states rather than the wave behavior. Yet, as we have seen, both frameworks lead to the same understanding of the Mach–Zehnder interferometer. Later we will use the interferometer to implement a quantum algorithm.

(sec-3-3)=
## 3.3 Big Ideas

1. A photon can be put into a superposition using a beam splitter. After passing through the beam splitter, a photon takes both paths simultaneously.
2. The Mach–Zehnder interferometer shows how the photon really does take two paths at once. This is conclusive experimental evidence of superposition of photons.

(sec-3-4)=
## 3.4 Check Your Understanding

1. Your friend who is explaining superposition to you says that:

   “A particle in the state $(1/\sqrt {2})\lvert 0\rangle + (1/\sqrt {2})\lvert 1\rangle$ represents a lack of knowledge of the system. Over time, the particle is changing back and forth between the state |0〉 and |1〉. The superposition state says that overall, the particle is in each of the two states for half of the time.”

   What parts of this statement do you agree with and what do you not agree with?

2. Only one detector is triggered if a single photon is sent through the beam splitter experiment shown in Fig. [](#fig-3-5). If the laser outputs two photons at the same time, what is the probability that both detectors will be triggered simultaneously? Now how about three photons? Ten photons? Note that this is why a higher power beam of light appears to reach both detectors simultaneously.

3. In practice, it is difficult to place the detectors the exact same distance from the beam splitter. The difference in distance is measured using the time delay Δ*t* between photons. The experiment is shown in Fig. [](#fig-3-10) and the data in Fig. [](#fig-3-11).

   ```{figure} ../images/ch-03/490703_1_En_3_Fig10_HTML.png
   :label: fig-3-10

   :alt: The experiment varies the position of Detector 2 and records the number of coincidences, i.e., the number of times both detectors are triggered simultaneously


   The experiment varies the position of Detector 2 and records the number of coincidences, i.e., the number of times both detectors are triggered simultaneously.
   ```


   ```{figure} ../images/ch-03/490703_1_En_3_Fig11_HTML.png
   :label: fig-3-11

   :alt: Data is shown above for light bursts sent from the laser every 0.4 μs. Figure reproduced with permission of Martin Laforest and the Communications and Strategic Initiatives Team at the Institute...


   Data is shown above for light bursts sent from the laser every 0.4 μs. Figure reproduced with permission of Martin Laforest and the Communications and Strategic Initiatives Team at the Institute for Quantum Computing, University of Waterloo Outreach department.
   ```


   - (a) Does the data shown in Fig. [](#fig-3-11) at Δ*t* = 0 support that light is a particle or a wave?
   - (b) Why are there large coincidence counts when Δ*t* ≠ 0? (Hint: Look at the spacing between the peaks.)

4. Using the matrices given in Fig. [](#fig-3-12), show how the superposition state is created by multiplying the beam splitter matrix by the initial photon state.

   ```{figure} ../images/ch-03/490703_1_En_3_Fig12_HTML.png
   :label: fig-3-12

   :alt: Matrix formulation of the Mach–Zehnder apparatus


   Matrix formulation of the Mach–Zehnder apparatus.
   ```


5. Construct the matrix representation for a 30/70 beam splitter.

6. Unsettled by the Mach–Zehnder interferometer, you decide to determine once and for all which path the photon takes after the first beam splitter. You place another detector (indicated by the eyeball) on the upper path as shown in Fig. [](#fig-3-13). If the eyeball sees a photon, what would be seen at Detectors 1 and 2?

   ```{figure} ../images/ch-03/490703_1_En_3_Fig13_HTML.png
   :label: fig-3-13

   :alt: A third detector (your eye) is added to the Mach–Zehnder apparatus


   A third detector (your eye) is added to the Mach–Zehnder apparatus.
   ```


[^1]: [https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/photons-particles-waves/photons-particles-waves.html](https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/photons-particles-waves/photons-particles-waves.html).

[^2]: Knill, E.; Laflamme, R.; Milburn, G. J. (2001). “A scheme for efficient quantum computation with linear optics”. Nature. Nature Publishing Group. 409 (6816): 46–52.

[^3]: [https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/Mach-Zehnder-Interferometer/Mach_Zehnder_Interferometer.html](https://www.st-andrews.ac.uk/physics/quvis/simulations_html5/sims/Mach-Zehnder-Interferometer/Mach_Zehnder_Interferometer.html).

[^4]: A complex amplitude $e^{i\phi}$ with infinite possible phase angles $\phi$ does not affect the probability since $\lvert e^{i\phi}\rvert ^2 = 1$.

[^5]: It should be noted that the technology has progressed so that most qubits are at present implemented using superconducting transmons and not using a Mach–Zehnder.
