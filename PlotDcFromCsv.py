'''
Based on code taken from
https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
'''

import matplotlib.pyplot as plt
import csv, sys

def plotCSVfile(filename):
    x = []
    y = []

    with open(filename,'r') as csvfile:
        plots = list(csv.reader(csvfile, delimiter=','))
        headerRow = plots[0]
        degreeIndex = headerRow.index("Degree")
        distBackIndex = headerRow.index("DistanceBack")
        distAheadIndex = headerRow.index("DistanceAhead")

        cumulative_dist = 0.0
        for row in plots[2:-2]:
            cumulative_dist += float(row[distBackIndex])
            x.append(cumulative_dist)
            y.append(float(row[degreeIndex]))

        lastRow = plots[-2]
        y.append(float(lastRow[degreeIndex]))
        cumulative_dist += float(row[distBackIndex])
        x.append(cumulative_dist)

    plt.plot(x,y, 'ro-') #, label='GIS')
    plt.xlabel('Length Along Chords')
    plt.ylabel('Dc')
    plt.suptitle('Y15A Degree of Curve vs. Length Along Chords')
    plt.title('From GIS Polyline File')
    # plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    fName = r"D:\SourceModules\Python\RoadGeometryAnalysis\TestFiles\CSV\Y15A.csv"
    if len(sys.argv) > 1:
        fName = sys.argv[1]
    plotCSVfile(fName)


