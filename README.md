# Displacement fields in amorphous solids caused by distributed stress sources

This project aims to study the behavior of the displacement fields arising in the amorphous system with distributed stress sources.

The primary computations are performed using <a href="https://www.lammps.org/#gsc.tab=0">LAMMPS</a>. Key LAMMPS input files include:
<ul>
  <li>GetConfigRing - executable file to generate initial configuration.</li>
  <li>in.2D-RingEqui - LAMMPS input file for the first part of the simulation. To generate the system with 
    a single value of desired pressure or to get the equilibrated system at a range of pressure values. </li>
  <li>in.2D-Ring-Inflate - LAMMPS input file the inflation run</li>
</ul>

Supplemental computations are performd in Python and include 
<ul>
  <li>Calculating average angle displacements</li>
  <li>Fitting data to anomalous and elastic distributions</li>
  <li>Computing boundary pressure, etc.</li>
</ul>

Full description of the project here --> <a href="https://drive.google.com/file/d/1s6msOLkYqgoxFNk0Dq8K2ntTD9V-ua41/view?usp=drive_link" target="_blank">Displacement fields in amorphous solids...</a>
