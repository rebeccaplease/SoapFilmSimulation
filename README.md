# SoapFilmSimulation #

## Project Description ##
My final project will simulate the draining of a vertical soap film due to gravity. With a
ferrofluid soap film, the introduction of a magnetic field in the opposite direction of gravity can cause a competing effect in film thicknesses at different locations, called “reverse draining.” These effects are described in two papers that I have cited. From the calculated film thicknesses, the color displayed would be calculated from interference equations for the visualization. I’d also like to explore the patterns that are formed over time, which the models in the papers do not currently include. I’m not sure if including gravity, magnetic fields, and nonuniform patterns would be too much, so I plan to check out two books and read more about the pattern formation (see schedule).

## Ph 235 Topics ##
* Graphics and visualizations: for displaying dynamically changing colors based on the film
thickness at different locations
* Derivatives/Differential Equations: as described in the papers to simulate the
thicknesses and patterns of the soap film over time
* Accuracy, error: using the reflection and transmission equations. Euler or RK for
numerical steps

## Deliverables ##
* Project website maintained on github with description, estimated timeline, weekly
progress updates
* Program with changeable parameters (eg soap concentrations, magnetic field strength,
size of soap film) for initial conditions
* Either have a downloadable executable program or webapp accessible on the website
* Demo: video of simulation, realtime simulation with different parameters

## Evaluation 
Compare to results from the published papers. Also compare visualization to videos of soap films.

## Low hanging fruit/challenges/contingency plans ##
* Easier: Get the simulation to work (easily compared to the paper’s results for its given
initial conditions
* Challenging: Include pattern evolution and apply the gravity/magnetic field to it. This
would have to include some sort of continuity or conditions applied to the reverse draining model. It would be more difficult to evaluate its accuracy, but the results can be seen visually.
* Contingency plans: focus solely on gravity or magnetic fields or just patterns in soap film and make a nice visualization for the simulation. This would be in case the models are too complex or if results are not as expected.

## Schedule ##
- [x] November 6, 2015: 5 minute summary/presentation in class on my project
- [x] November 13, 2015: create website and with information from this project proposal.
Get The dynamics of patterns by M.I. Rabinovich, A.B. Ezersky, P.D. Weidman and read the relevant chapter on soap film patterns. Also get and read Soap films, studies of their thinning by Karol Mysels (cited by almost all the articles I looked up about soap films.) Narrow project with gravity/magnetic field + patterns.
  - [x] Project was narrowed down to time evolution of the magnetic soap film
- [ ] November 20, 2015: Preliminary simulations and compare results to the papers.
  * Taking longer than expected to figure out paper and determine a method for solving the equations.
- [x] November 23, 2015: 1 page progress update
- [ ] November 27, 2015: Continue refining, coding, testing
  * Still in the process of doing so

- [x] December 4, 2015: in-class update
  * Class canceled but the 1 page progress update was turned in
  * Decided to use method of finite differences for determining third derivative of h with respect to x
  * Also using Adams-Bashforth method to solve for h after finding dh/dt at each gridpoint
  * Currently debugging boundary conditions and grid parameters since spikes appear after more than 2 timesteps. Perhaps the method itself won't lead to convergence.. In which case another method must be used.  
- [ ] December 11/18, 2015: in-class final presentation
- [ ] December ~~18~~ 22, 2015: upload deliverables by ~~11:30 pm~~ 12:00 pm

## Preliminary Results ##
* One Step
  * nu = 1
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/1step_100_1.png)
  * nu = 5
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/1step_100_5.png)
* Two Steps
  * nu = 1
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/2step_100_1.png)
  * nu = 5
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/2step_100_5.png)
* Three Step
  * nu = 1
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/3step_100_1.png)
  * nu = 5
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/3step_100_5.png)
* Four Steps (divergence...)
  * nu = 1
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/4step_100_1.png)
  * nu = 5
![alt tag](https://raw.github.com/rebeccaplease/SoapFilmSimulation/master/images/4step_100_5.png)


## References ##
Moulton, D. E., and J. A. Pelesko. "Reverse Draining of a Magnetic Soap Film." Physical Review E Phys. Rev. E 81.4 (2010) Web.

Moulton, D. E., and J. Lega. "Reverse Draining of a Magnetic Soap Film --- Analysis and Simulation of a Thin Film Equation with   Non-Uniform Forcing." Physica D, 28 Aug. 2009. Web. 05 Nov. 2015.
