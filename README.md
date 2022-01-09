# Correlated Photons

### Skills: experience with infrared and ultraviolet light, correlated photons, coincidence counts, polarization, real-time optimization of photon counts, collumation, laser alignment, consturction of counting module with PSoC including milling circuit board and laser cutting, software built with python for visualization, electronic testing equipment 


Research advisor: Dr. Mark Master </br>
Past researchers I worked with: Justin Smethers

I began working on this project my senior year of undergrad earning me Outstanding Physics Research of the Year at Purdue Fort Wayne. I've worked with professors, LTLs, GTAs,and undergraduates on this project for about two and a half years. This project includes three experiements all focused on the photon model of light. Tanjentally, Spencer Kelham and I worked on building cost effect Single Photon Counting Machines and we determed the window for photon counts of our PSoC counting module, which will all be discussed below.


Parts list that I countstructed and purchased to conduct experiements: 
#### [Parts list with pricing](https://github.com/jacobsc050/quantum-mechanics/blob/main/assets/parts%20list.pdf)


## Spontaneous Parametric Downconversion
### Skills: coincidence counts, BBO crystals, Single Photon Counting Machines 

Worked on with Jucoen Yeater

With the use of an ultraviolet laser I can make a source of correlated photons using a BBO crystal. These were counted by collecting the photons and guiding them to a
single photon counting machine with fiber optic cables. Then the output of the single photon counting maching can collected using a PSoC. The output of the PSoC was sent to a computer using the serial port. This output was then used to produce the following out put from the following code: 

Note: the following code was built by Justin Smethers and I made some minor adjustments to make it more user friendly.
#### [Python code](https://github.com/jacobsc050/quantum-mechanics/blob/main/coincidence-counting.py)
This is a photo of the output of the above code: <br/>
<img src=https://github.com/jacobsc050/quantum-mechanics/blob/main/assets/GetAttachmentThumbnail.png height = 300px width = 300 px>

I then used photon counts and statistical methods to show that the coincidence counts are larger than random would allow, so the counted photons must be correlated. 



## Proving the Existance of Photons 
### Skills: 2nd order coherence, polarizing beam splitting cubes, 3-fold coincidence counts

Worked on with Cully O'Meara, Logan Reidy, Will McLane and Alex Bushe

Using 3-fold coincidence counts I used 2nd order coherence calculations to show the counts could not reflect reality if light were a wave. This result supported the photon model of light.

## Single Photon Interference 
### Skills: polarizing interferometers, yttrium beam displacers, spectrographs

Worked on with Cully O'Meara, Logan Reidy, and Alex Bushe

Using two yttrium beam displace I produced a interferometer that create path length distances that are modified by the polarization of light entering the displacers.

## Window Length for Photon Counts with a PSoC
### Skills:  testing counting module, neutral gradients, white light source from incandescent light bulb

I found the window for coincidence counts to be 10 ns with uncertainty of 0.1 ns for our counter.

Worked on with William McLane

## Constructing a low-cost Single Photon Counting Machine
### Skills: reversed biased diodes, quenching avalanche currents, designing and fabricating circuit boards

Worked on with Spencer Kelham

I worked on building a low-cost circuit for an LED based single photon detector.








