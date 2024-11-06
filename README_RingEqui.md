This LAMMPS input scripts is for the simulating a 2D granular system arranged in a ring shaped box consist of grains/disks 
by reading a data file prepared for the configuration at a desired packing fraction. Grains only interact via Herzian force 
which depends on the overlap between two grains and grain and wall.   

The grains are placed inside a ring shaped container with interacting walls. The walls of the container interact with the grains 
with Hertzian force with parameter defined in the script.

In the loop part the radius of the ring is decreased in athermal quasi-static (AQS) manner to anneal all the forces and so the ke remains zero.

The code was written by Harish Charan in 2022
