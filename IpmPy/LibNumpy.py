# LibNumpy.py   Updated: 21_09_01


import numpy

# Copy num
def CopyRoi(Data, RoiX, RoiY, RoiW, RoiH, OffsetX_Dst = 0, OffsetY_Dst=0, dtype=numpy.float32, FillValue = 0):    
    OutH = OffsetY_Dst + RoiH
    OutW = OffsetX_Dst + RoiW
    DataOut = numpy.empty([OutH, OutW], dtype)
    DataOut.fill(FillValue)
    DataOut[OffsetY_Dst:OutH, OffsetX_Dst:OutW] = Data[RoiY: RoiY+RoiH, RoiX: RoiX+RoiW]    
    return DataOut

def CopyRoi(Data, RoiY, RoiX, RoiH, RoiW,  DataOut, OffsetY_Out = 0, OffsetX_Out=0):    
    SrcY_End = RoiY + RoiH
    SrcX_End = RoiX + RoiW  
    OutY_End = OffsetY_Out + RoiH
    OutX_End = OffsetX_Out + RoiW
    DataOut[OffsetY_Out:OutY_End, OffsetX_Out:OutX_End] = Data[RoiY:SrcY_End, RoiX:SrcX_End]    
    return DataOut

