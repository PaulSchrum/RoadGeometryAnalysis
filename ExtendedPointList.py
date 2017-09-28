import sys, csv, os
from ExtendedPoint import ExtendedPoint as EP
import ExtendedPoint

__author__ = ['Paul Schrum']

class ExtendedPointList(list):
    def __init__(self):
        pass

    def computeAllPointInformation(self):
        """
        For each triplet of points in the list of points, compute the
        attribute data for the arc (circular curve segment) that starts
        at point 1, passes through point 2, and ends at point 3.  Then
        assign the curve data to point 2 for safe keeping.
        :param self: This list of points to be analyzed. These must be ordered spatially or the results are meaningless.
        :return: None
        """
        for pt1, pt2, pt3 in zip(self[:-2],
                                 self[1:-1],
                                 self[2:]):
            ExtendedPoint.compute_arc_parameters(pt1, pt2, pt3)

    def writeToCSV(self, fileName):
        """
        Write all points in the point list to the indicated file, expecting
        the points to be of type ExtendedPoint.
        :param self:
        :return: None
        """
        with open(fileName, 'w') as f:
            headerStr = EP.header_list()
            f.write(headerStr + '\n')
            for i, point in enumerate(self):
                writeStr = str(point)
                f.write(writeStr + '\n')


def CreateExtendedPointList(csvFileName):
    '''
    Factory method. Use this instead of variable = ExtendedPointList().
    Args:
        csvFileName: The path and filename of the csv file to be read.

    Returns: New instance of an ExtendedPointList.
    '''
    newEPL = ExtendedPointList()
    with open(csvFileName, mode='r') as f:
        rdr = csv.reader(f)
        count = 0
        for aRow in rdr:
            if count == 0:
                header = aRow
                count += 1
                xIndex = header.index('X')
                yIndex = header.index('Y')
            else:
                x = float(aRow[xIndex])
                y = float(aRow[yIndex])
                newEPL.append(EP(x, y))
    return newEPL

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Running tests."
        inFileName = r"D:\SourceModules\Python\RoadGeometryAnalysis\TestFiles\CSV\Y15A_Computed.csv"
        outFileName = r"D:\SourceModules\Python\RoadGeometryAnalysis\TestFiles\CSV\Y15A_Computed_temp.csv"
    else:
        inFileName = sys.argv[1]
        outFileName = sys.argv[2]

    aPointList = CreateExtendedPointList(inFileName)
    aPointList.computeAllPointInformation()
    aPointList.writeToCSV(outFileName)
    i = 0
