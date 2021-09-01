# LibFiles_Tst.py  Updated: 21_09_01

#import cv2 as cv
import numpy
#import statistics as st
#import os
import LibFiles as LibF
#import LibDebug as LibD

#===================================================================================================

#PathR = r'W:\Image_db\Patterns\Inc0_16x16.f32' # r' for read text without special chars
PathW = r'W:\Image_db\Patterns/'     # r' for read text without special chars
PathT = r'W:\Image_db\Convolution/'
PathK = r'K:\Tmp\cassandra/'
PathDB = r'W:\Image_db/'
PathM = r'M:/TempM/'


Rows = 16
Cols = 16
FN = 'Inc0_16x16.f32'
PathR = PathW + FN

Rows2 = 352
Cols2 = 352
FN2 = '1_Inp352x352.f32'
PathR2 = PathT + FN2

print("Test LibFiles:")
'''
ImgF = LibF.Read_File(PathR)
ImgF = ImgF.reshape(Rows,Cols)
print(f" ImgF.ndim = {ImgF.ndim},    ImgF.shape={ImgF.shape},  ImgF.size={ImgF.size},  ImgF.dtype={ImgF.dtype},  ImgF[0, 0] = { ImgF[0, 0] } \n\n")
print(f"ImgF = { ImgF }\n")
#LibD.ImgStat(ImgF)
'''

DataI = numpy.arange(10)
#print(f"DataI = {DataI}")
    #   [ 0  1  2  3  4  5  6  7  8  9]

Data = numpy.array([0,1,2,3,4,5,6,7,8,9], dtype=numpy.float32)
print(f"Data = {Data}")

FN3 = 'File.bin'
PathTmp = PathM + FN3
LibF.Write_File(PathTmp, Data) 
#LibF.Write_File1(PathTmp, Data)

DataR = LibF.Read_File(PathTmp)
print(f"DataR = {DataR}")
print(f"Compare = { DataR == Data }")



Row = 3   
Col = 4
Data2d = numpy.array([ [0,1,2,3], [4,5,6,7], [8,9,10,11]], dtype=numpy.float)
print(f"Data2d = { Data2d }")

'''
*F*
FN2d = 'File2d.bin'
PathTmp = PathM + FN3
LibF.Write_File(PathTmp, Data2d) 
#LibF.Write_File1(PathTmp, Data)

DataR2d = LibF.Read_File(PathTmp)
print(f"DataR2d = {DataR2d}")
print(f"Compare = { DataR2d == Data2d }")
'''












