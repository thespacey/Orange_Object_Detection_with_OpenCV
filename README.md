# Orange_Object_Detection_with_OpenCV
This is a Python code which uses OpenCV to detect Oranges in a picture and circle them !

# Requirements
- OpenCV Library

# Notes
You'll find besides the Python code, the input image I used and the corresponding result.

You can use this code to detect any other object of any color you want, you just need to change the values of the color arrays in the code:
min_ora = np.array([10, 50, 50])
max_ora = np.array([30, 255, 255])
and
min_ora2 = np.array([170, 50, 50])
max_ora2 = np.array([180, 255, 255])
to the HSV values of your desired color.

# Execution example
This is one of the sample images I used my code on for tuning, it is an orange on a white background (my input image):
![o](https://user-images.githubusercontent.com/20354107/30525222-e3c6a17c-9c02-11e7-9e86-e092162bbc19.jpg)

and this is the generated image that I got after running the code on the input image:
![o1](https://user-images.githubusercontent.com/20354107/30525245-44dc7d1a-9c03-11e7-91e7-7572efbed917.jpg)
