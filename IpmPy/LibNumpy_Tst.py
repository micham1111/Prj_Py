# LibNumpy_Tst.py Updated: 21_09_01

import numpy
#import statistics as st
#import os
import LibNumpy as LibNP

print("Test LibNumpy:")


DataI = numpy.arange(10)
#print(f"DataI = {DataI}")
    #   [ 0  1  2  3  4  5  6  7  8  9]

Row = 3   
Col = 4
Data = numpy.array([ [0,1,2,3], [4,5,6,7], [8,9,10,11]], dtype=numpy.float)
print(f"Data = { Data }")

Row2B = Row   
Col2B = 2 * Col
Data2B = numpy.empty([Row2B, Col2B], dtype=numpy.float)


RoiY = 0
RoiX = 0
RoiH = Row
RoiW = Col

OffsetY_Out = 0
OffsetX_Out = 0
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = 0
OffsetX_Out = Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B,  OffsetY_Out, OffsetX_Out)    
print(f"Data2B = { Data2B }")

Row3B = Row   
Col3B = 3 * Col
Data3B = numpy.empty([Row3B, Col3B], dtype=numpy.float)

OffsetY_Out = 0
OffsetX_Out = 0
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data3B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = 0
OffsetX_Out = Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data3B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = 0
OffsetX_Out = 2 * Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data3B,  OffsetY_Out, OffsetX_Out)    
print(f"Data3B = { Data3B }")


#####
Row2B_3B = 2 * Row   
Col2B_3B = 3 * Col
Data2B_3B = numpy.empty([Row2B_3B, Col2B_3B], dtype=numpy.float)

OffsetY_Out = 0
OffsetX_Out = 0
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B_3B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = 0
OffsetX_Out = Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B_3B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = 0
OffsetX_Out = 2 * Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B_3B,  OffsetY_Out, OffsetX_Out)    


OffsetY_Out = Row
OffsetX_Out = 0
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B_3B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = Row
OffsetX_Out = Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B_3B,  OffsetY_Out, OffsetX_Out)    

OffsetY_Out = Row
OffsetX_Out = 2 * Col
LibNP.CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  Data2B_3B,  OffsetY_Out, OffsetX_Out)    
print(f"Data2B_3B = { Data2B_3B }")











