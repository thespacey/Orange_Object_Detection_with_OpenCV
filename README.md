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
