import numpy as np

class Line():
    def __init__(self):
        #Keep Track of Good Lane Width
        self.lineWidthAppend = []
        #Keep track fo the good lane polynomial coefficients
        self.leftCoef = np.array([[1,1,1],[1,1,1]])
        self.rightCoef = np.array([[1,1,1],[1,1,1]])
        #Keep track of number of frames processed
        self.framesCounter = 0
        #radius of curvature of the line in some units
        self.radius = []

    def lineWidthAppender(self, width):
        self.lineWidthAppend.append(width)
        return None
    
    def lineCoef(self, left,right):
        self.leftCoef = np.append(self.leftCoef, left, axis=0)
        self.rightCoef = np.append(self.rightCoef, right, axis=0)
        return None