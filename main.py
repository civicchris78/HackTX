import sys
import os
from subprocess import call

currentPath = os.getcwd() #Get Current Working Directory

#Import Specific lib
sys.path.insert(0, '{}/lib'.format(currentPath))
from camera import Camera

#End of Import
cam = Camera()
