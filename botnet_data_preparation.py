from __future__ import division
import os, sys
import threading
import numpy

class prepare(threading.Thread):
    def __init__(self, X, Y, XT, YT, accLabel=None):
        threading.Thread.__init__(self)
        self.X = X
        self.Y = Y
        self.XT = XT
        self.YT = YT
        self.accLabel = accLabel

    def run(self):
        X = numpy.zeros(self.X.shape)
        Y = numpy.zeros(self.Y.shape)
        XT = numpy.zeros(self.XT.shape)
        YT = numpy.zeros(self.YT.shape)
        numpy.copyto(X, self.X)
        numpy.copyto(Y, self.Y)
        numpy.copyto(XT, self.XT)
        numpy.copyto(YT, self, YT)
        for i in range(9):
            x[:, i] = (X[:, i] - X[:, i].mean()) / (X[:, i].std())
        for i in range(9):
            XT[:, i] = (XT[:, i] - XT[:, i].mean()) / (XT[:, i].std())
