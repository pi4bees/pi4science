#!/usr/bin/env python
from subprocess import call
import numpy as np
from scipy.interpolate import RegularGridInterpolator, Rbf
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import heapq
import time


def main():
    #while(True):
        w = 12
        l = 12
        h = 24
        x = np.array([l, l, 0, l/2, 0, l/2, 0, 0])
        y = np.array([w/2, w/2, w, w/2, w, w/2, 0, 0])
        z = np.array([0, h, 0, 0, h, h*3/4, 0, h])
        vals = []
        with open("purple_triangle_data.tsv", 'rb') as fh:
            for line in fh:
                pass
        vals = line.split()[1:9]
        rbf = Rbf(x,y,z,vals)
        xi = yi = np.linspace(0, 12, 20)
        zi = np.linspace(0, 24, 50)
        Xi, Yi, Zi = np.meshgrid(xi, yi, zi, indexing='ij')
        result = rbf(Xi, Yi, Zi)
        m = np.max(result)
        mu = np.mean(result)
        s = np.std(result)
        result_filter = result.flatten()[heapq.nlargest(200, range(len(result.flatten())), result.flatten().take)]
        """for i in range(20):
            for j in range(20):
                for k in range(50):
                    if all(result[i][j][k] < result_filter) and ((i != 0 and j != 0 and k != 0) and \
                            (i != 0 and j != 0 and k != 49) and \
                            (i != 0 and j != 19 and k != 49) and \
                            (i != 19 and j != 19 and k != 49) and \
                            (i != 19 and j != 19 and k != 49) and \
                            (i != 19 and j != 0 and k != 0) and \
                            (i != 19 and j != 19 and k != 0) and \
                            (i != 0 and j != 19 and k != 0)):
                                result[i][j][k] = np.nan
                                Xi[i][j][k] = Yi[i][j][k] = Zi[i][j][k] = np.nan"""
        Xi = Xi[~np.isnan(Xi)]
        Yi = Yi[~np.isnan(Yi)]
        Zi = Zi[~np.isnan(Zi)]
        result = result[~np.isnan(result)]
        with open("purple_triangle_data2.csv", 'w') as fh:
            print("x1,y1,z1,result", file=fh)
            for i in range(len(Xi.flatten())):
                print(str(Xi.flatten()[i])+","+str(Yi.flatten()[i])+","+str(Zi.flatten()[i])+","+str(result.flatten()[i]), file=fh)

        #call('git stash', shell = True)
        #call('git pull', shell = True)
        #call('git stash pop', shell = True)
        #call('git commit -am "updating data"', shell = True)
        #call('git push', shell = True)
        #time.sleep(3600)

if __name__=="__main__":
    main()
