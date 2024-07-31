# DHM-FLUO-registration
Programme suite to rescale and align "manually" Fluorescence images on DHM images


A) Get_scaling_factor.py

Get_scaling_factor.py is a program to find the scaling factor between DHM and fluorescence images.
The program is expecting the same scaling factor for image width and height. Get_scaling_factor.py gives a mean scaling value for a pair of source and reference images (e.g. Fluo and DHM).

Open your images (one reference, one source) with imageJ and save them as .png

Start Get_scaling_factor.py, load reference and source image (png).

Get_scaling_factor.py shows the images in real size, i.e., if the image is 800x800 pixels, it will take 800x800 pixels of the screen to show it.
If you have images, which are too big for your screen, you need to crop them before with imageJ.

Double click on landmarks, which are clearly identifiable in reference and source. Double click every landmark in both, reference and source.
At least 2 landmarks per image are needed.
Try to find such landmarks as far from each other as possible and as many as possible.

Try to do this for different experiments per microscope objective to increase the reliability of the scaling factor.
