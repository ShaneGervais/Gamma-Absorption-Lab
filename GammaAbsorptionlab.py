#GammaAbsorptionLab by @Shane Gervais
#For the curiculum of PHYS3336

#This python code is to test a certain data set
#provided by the lab. 

#Import methods that will help us for the analysis
import pandas as pd
import io
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np

ba = pd.read_excel('Ba-133.xlsx')
cs = pd.read_excel('Cs-137.xlsx')
na = pd.read_excel('Na-22.xlsx')
co = pd.read_excel('Co-60.xlsx')

#Definning instance variables
#Thickness's
thickness = ba.Thickness
thickness = np.array(thickness)


#Ba-31
intensityBa = ba.Intensity
intensityBa = np.array(intensityBa)
intensityBa2 = ba.Intensity2
intensityBa2 = np.array(intensityBa2)

#Cs-137
intensityCs = cs.Intensity
intensityCs = np.array(intensityCs)
intensityCs2 = cs.Intensity2
intensityCs2 = np.array(intensityCs2)

#Na-22
intensityNa = na.Intensity
intensityNa = np.array(intensityNa)
intensityNa2 = na.Intensity2
intensityNa2 = np.array(intensityNa2)

#Co-60
intensityCo = co.Intensity
intensityCo = np.array(intensityCo)
intensityCo2 = co.Intensity2
intensityCo2 = np.array(intensityCo2)



#Plots our data from the excel sheet
#Ba-133 @31
plt.figure(figsize = (10, 5))
plt.title("Ba 31keV", fontsize = 24)
plt.plot(thickness, intensityBa,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Ba-133 @356
plt.figure(figsize = (10, 5))
plt.title("Ba 356keV", fontsize = 24)
plt.plot(thickness, intensityBa2,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Logarithmn of the data
#Ba-31 @31
MB1, B = np.polyfit(thickness, np.log(intensityBa), 1)
plt.figure()
plt.title("lnBa 31keV", fontsize = 24)
plt.plot(thickness, np.log(intensityBa), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MB1*thickness + B, 'r')
plt.show()
#np.log(intensityBa[0])

#Ba-31 @356
MB2, B = np.polyfit(thickness, np.log(intensityBa2), 1)
plt.figure()
plt.title("lnBa 356keV", fontsize = 24)
plt.plot(thickness, np.log(intensityBa2), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MB2*thickness + B, 'r')
plt.show()
#np.log(intensityBa2[0])

#Cs-137 @32.19
plt.figure(figsize = (10, 5))
plt.title("Cs 32.19keV", fontsize = 24)
plt.plot(thickness, intensityCs,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Cs-137 @661.6
plt.figure(figsize = (10, 5))
plt.title("Cs 661.6keV", fontsize = 24)
plt.plot(thickness, intensityCs2,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Cs-137 @32.19
MC1, B = np.polyfit(thickness, np.log(intensityCs), 1)
plt.figure()
plt.title("lnCs 32.19keV", fontsize = 24)
plt.plot(thickness, np.log(intensityCs), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MC1*thickness + B , 'r')
plt.show()

#Cs-137 @ 661.6
MC2, B = np.polyfit(thickness, np.log(intensityCs2), 1)
plt.figure()
plt.title("lnCs 661.6keV", fontsize = 24)
plt.plot(thickness, np.log(intensityCs2), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MC2*thickness + B, 'r')
plt.show()

#Na-22 @511
plt.figure(figsize = (10, 5))
plt.title("Na 511keV", fontsize = 24)
plt.plot(thickness, intensityNa,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Na-22 @1274.5
plt.figure(figsize = (10, 5))
plt.title("Na 1274.5keV", fontsize = 24)
plt.plot(thickness, intensityNa2,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Na-22 @511
MN1, B = np.polyfit(thickness, np.log(intensityNa), 1)
plt.figure()
plt.title("lnNa 511keV", fontsize = 24)
plt.plot(thickness, np.log(intensityNa), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MN1*thickness + np.log(intensityNa[0]), 'r')
plt.show()

#Na-22 @1274.5
MN2, B = np.polyfit(thickness, np.log(intensityNa2), 1)
plt.figure()
plt.title("lnNa 1274.5keV", fontsize = 24)
plt.plot(thickness, np.log(intensityNa2), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MN2*thickness + np.log(intensityNa2[0]), 'r')
plt.show()

#Co-60 @1173.2
plt.figure(figsize = (10, 5))
plt.title("Co 1173.2keV", fontsize = 24)
plt.plot(thickness, intensityCo,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Co-60 @1332.5
plt.figure(figsize = (10, 5))
plt.title("Co 1332.5keV", fontsize = 24)
plt.plot(thickness, intensityCo2,'r-o')
plt.ylabel("Intensity")
plt.xlabel("Thickness (/m)")
plt.show()

#Co-60 @1173.2
MCO1, B = np.polyfit(thickness, np.log(intensityCo), 1)
plt.figure()
plt.title("lnCo 1173.2keV", fontsize = 24)
plt.plot(thickness, np.log(intensityCo), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MCO1*thickness + np.log(intensityCo[0]), 'r')
plt.show()

#Co-60 @1332.5
MCO2, B = np.polyfit(thickness, np.log(intensityCo2), 1)
plt.figure()
plt.title("lnCo 1332.5keV", fontsize = 24)
plt.plot(thickness, np.log(intensityCo2), 'b-o')
plt.xlabel("Thickness (/m)")
plt.ylabel("ln(I)")
plt.plot(thickness, MCO2*thickness + np.log(intensityCo2[0]), 'r')
plt.show()

print("The attunation constant for Ba-31 is ", MB1)
print("The attunation constant for Ba-356 is ", MB2)
print("The attunation constant for Cs-32.19 is ", MC1)
print("The attunation constant for Cs-661.6 is ", MC2)
print("The attunation constant for Na-511 is ", MN1)
print("The attunation constant for Na-1274.5 is ", MN2)
print("The attunation constant for Co-1173.2 is ", MCO1)
print("The attunation constant for Co-1332.5 is ", MCO2)