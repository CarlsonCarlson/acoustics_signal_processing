Acoustics Signal Processing CISC287 VIP University of Delaware

To run signal_plot.py, which is the main file (trig_plot.py was me messing around):
you'll want to create a new virtual environment based on the packages listed in the file "requirements.txt"

This is because I've installed multiple packages and if you don't want those installed to your main computer, you can delete the virtual environment later. After you're done checking out my code.

1. use whatever software you usually do for making a virtual environment to make a virtual environment.
   1. this can be miniconda (which is what I use) or anything else you find using a google search.
2. while inside the virtual environment, run the following command in terminal (if the name of the virtual env. is listed in parentheses before your system, username, and location, that means your terminal is inside of the virtual env.)
   1. "pip install -r requirements.txt"
   2. make sure you are in the main directory of this repository so your terminal can access the requirements.txt file in this repo.
   
When you're done playing around with the repo, you can just delete the virtual environment to get rid of the packages you installed to run this repo's contents. just look up "delete [your virtual environment manager name] environment" on google and follow those instructions