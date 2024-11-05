This LAMMPS input scripts is for the simulating a 2D granular system arranged in a ring shaped box consist of spheres by reading a restart file of a jammed system.	

The grains are placed inside a ring shaped containerwith interacting walls.

The walls of the container interact with the grains with Hertzian force with parameter defined in the script.

In this script, a restart file is being read which was jammed and equilibrated in a separate athermal quasi-static simulation (AQS).

Now we just inflate the grain which closest to the center of the our big ring shaped system made.

We again perform an AQS run to anneal all the forces and so the ke remains zero.

We then take note of the displacement field of the entire system.

Grains only interact via Herzian force which depends on the overlap between two grains and grain and wall.		

The core of the code was made by Harish Charan in 2021. I made some adaptations to the given problem.
