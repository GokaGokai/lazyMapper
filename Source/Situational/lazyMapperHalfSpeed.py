import os

# Early Stage, command line version, I plan to do the GUI after my semester with more features
# By GokaGokai/ JohnTitorTitor/ Kanon
os.system("title " + os.path.basename(__file__)[0:-3])

rootdir = os.getcwd()
extensions = ('.osu')

osuFiles = []
i = 0

print("----------------------------------------")
print("\n   lazyMapper")
print(" By GokaGokai/ JohnTitorTitor/ Kanon\n")
print("----------------------------------------")
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext in extensions:
            osuFiles.append(file)
            print(str(i) + " - " + file)
            i = i + 1
            
# print(osuFiles)
input1 = osuFiles[int(input("\nWhich map to parse from? [0-" + str(i-1) + "]\n(Only for stats such as CS, AR, OD, HP..)\n"))]

print("\n---")
print("0 - Square")
print("1 - Circle")
print("2 - Small Square")
print("3 - Custom")
input2 = int(input("\nWhat kind of map do you want to generate? [0-3]\n"))

templateCustom = []
if input2 == 3:

    i = 0
    
    print("\n---")
    for x in osuFiles:
        print(str(i) + " - " + x)
        i = i + 1

    input3 = osuFiles[int(input("\nSelect the osu file you want to copy from. [0-" + str(i-1) + "]\n(Assuming you dragged it in the same folder already)\n"))]
    
    with open(input3, encoding='utf-8') as f:
        startReading = False

        while 1:
            if startReading and line == "":
                break

            line = f.readline().rstrip()
            # print(line)

            if startReading and line != "":
                templateCustom.append(line)

            if line == '[HitObjects]':
                startReading = True
            

            
# print(templateCustom)
title = input1[0:input1.index('[')]
start = 0
end = 0
bpm = 0.0
divisor = 4/2
output = []
diffName = ""

with open(input1, encoding='utf-8') as f:
    atTimingPoints = False
    atTimingPoints2 = False
    otherMode = False

    while(1):
        line = f.readline().rstrip()
        output.append(line+"\n")

        if line == '[TimingPoints]':
            atTimingPoints = True
        
        if line.__contains__("Version:"):
            if input2 == 0: diffName = "(Square)"
            if input2 == 1: diffName = "(Circle)"
            if input2 == 2: diffName = "(Small Square)"
            if input2 == 3: diffName = "("+input3[0:-4]+")"
            output[len(output)-1] = "Version:lazyMapper "+diffName+"\n"

        # For mania or other game modes
        if line.__contains__("Mode:") and not line.__contains__("0"):
            output[len(output)-1] = "Mode: 0\n"
            otherMode = True

        if line.__contains__("ApproachRate:") and otherMode:
            output[len(output)-1] = "ApproachRate: 9\n"
            wasAR = True

        if line.__contains__("HPDrainRate:") and otherMode:
            output[len(output)-1] = "HPDrainRate: 5\n"

        if line.__contains__("CircleSize:") and otherMode:
            output[len(output)-1] = "CircleSize: 4\n"
    
        if line.__contains__("OverallDifficulty:") and otherMode:
            output[len(output)-1] = "OverallDifficulty: 8\n"

        if line.__contains__("ApproachRate:"):
            wasAR = True

        # For mania or other game modes
        if line.__contains__("SliderMultiplier:") and not wasAR:
            output[len(output)-1] = "ApproachRate: 9\n" + output[len(output)-1]

        if atTimingPoints:
            timingLine = f.readline()
            output.append(timingLine)
            start = int(timingLine.rstrip().split(",")[0])
            bpm = float(timingLine.rstrip().split(",")[1])
            atTimingPoints = False
            atTimingPoints2 = True
            continue

        if line == "":
            atTimingPoints2 = False

        if atTimingPoints2:
            currentEndTime = int(line.split(",")[0])
            if end < currentEndTime:
                end = currentEndTime
            
        if line == '[HitObjects]':
            break

# ---
# ---   Output
# ---
with open(title+"[lazyMapper "+diffName+"].osu", "w", encoding='utf-8') as file:
    for i in output:
        file.write(i)
    

    currentTime = start - 1
    templateSquare = ["96,68,42935,5,6,0:0:0:0:", "112,68,43016,1,0,0:0:0:0:", "128,68,43097,1,0,0:0:0:0:", "144,68,43178,1,0,0:0:0:0:", "160,68,43259,1,0,0:0:0:0:", "176,68,43340,1,0,0:0:0:0:", "192,68,43421,1,0,0:0:0:0:", "208,68,43503,1,0,0:0:0:0:", "224,68,43584,1,2,0:0:0:0:", "240,68,43665,1,0,0:0:0:0:", "256,68,43746,1,0,0:0:0:0:", "272,68,43827,1,0,0:0:0:0:", "288,68,43908,1,2,0:0:0:0:", "304,68,43989,1,0,0:0:0:0:", "320,68,44070,1,0,0:0:0:0:", "336,68,44151,1,0,0:0:0:0:", "352,68,44232,5,2,0:0:0:0:", "352,84,44313,1,0,0:0:0:0:", "352,100,44394,1,0,0:0:0:0:", "352,116,44476,1,0,0:0:0:0:", "352,132,44557,1,2,0:0:0:0:", "352,148,44638,1,0,0:0:0:0:", "352,164,44719,1,0,0:0:0:0:", "352,180,44800,1,0,0:0:0:0:", "352,196,44881,1,2,0:0:0:0:", "352,212,44962,1,0,0:0:0:0:", "352,228,45043,1,0,0:0:0:0:", "352,244,45124,1,0,0:0:0:0:", "352,260,45205,1,2,0:0:0:0:", "352,276,45286,1,0,0:0:0:0:", "352,292,45367,1,0,0:0:0:0:", "352,308,45449,1,0,0:0:0:0:", "352,324,45530,5,2,0:0:0:0:", "336,324,45611,1,0,0:0:0:0:", "320,324,45692,1,0,0:0:0:0:", "304,324,45773,1,0,0:0:0:0:", "288,324,45854,1,2,0:0:0:0:", "272,324,45935,1,0,0:0:0:0:", "256,324,46016,1,0,0:0:0:0:", "240,324,46097,1,0,0:0:0:0:", "224,324,46178,1,2,0:0:0:0:", "208,324,46259,1,0,0:0:0:0:", "192,324,46340,1,0,0:0:0:0:", "176,324,46421,1,0,0:0:0:0:", "160,324,46503,1,2,0:0:0:0:", "144,324,46584,1,0,0:0:0:0:", "128,324,46665,1,0,0:0:0:0:", "112,324,46746,1,0,0:0:0:0:", "96,324,46827,5,2,0:0:0:0:", "96,308,46908,1,0,0:0:0:0:", "96,292,46989,1,0,0:0:0:0:", "96,276,47070,1,0,0:0:0:0:", "96,260,47151,1,2,0:0:0:0:", "96,244,47232,1,0,0:0:0:0:", "96,228,47313,1,0,0:0:0:0:", "96,212,47394,1,0,0:0:0:0:", "96,196,47476,1,2,0:0:0:0:", "96,180,47557,1,0,0:0:0:0:", "96,164,47638,1,0,0:0:0:0:", "96,148,47719,1,0,0:0:0:0:", "96,132,47800,1,2,0:0:0:0:", "96,116,47881,1,0,0:0:0:0:", "96,100,47962,1,0,0:0:0:0:", "96,84,48043,1,0,0:0:0:0:"]
    templateCircle = ["198,133,17022,5,6,0:0:0:0:", "204,128,17087,1,0,0:0:0:0:", "211,123,17152,1,0,0:0:0:0:", "218,119,17216,1,0,0:0:0:0:", "225,116,17281,1,8,0:0:0:0:", "233,113,17345,1,0,0:0:0:0:", "240,111,17410,1,0,0:0:0:0:", "248,110,17475,1,0,0:0:0:0:", "256,110,17539,1,2,0:0:0:0:", "264,110,17604,1,0,0:0:0:0:", "272,112,17669,1,0,0:0:0:0:", "280,114,17733,1,0,0:0:0:0:", "288,117,17798,1,8,0:0:0:0:", "295,120,17863,1,0,0:0:0:0:", "302,124,17927,1,0,0:0:0:0:", "308,129,17992,1,0,0:0:0:0:", "314,134,18057,5,6,0:0:0:0:", "319,140,18121,1,0,0:0:0:0:", "324,147,18186,1,0,0:0:0:0:", "328,154,18251,1,0,0:0:0:0:", "331,161,18315,1,8,0:0:0:0:", "334,169,18380,1,0,0:0:0:0:", "336,176,18445,1,0,0:0:0:0:", "337,184,18509,1,0,0:0:0:0:", "337,192,18574,1,2,0:0:0:0:", "337,200,18639,1,0,0:0:0:0:", "335,208,18703,1,0,0:0:0:0:", "333,216,18768,1,0,0:0:0:0:", "330,224,18833,1,8,0:0:0:0:", "327,231,18897,1,0,0:0:0:0:", "323,238,18962,1,0,0:0:0:0:", "318,244,19027,1,0,0:0:0:0:", "313,250,19091,5,6,0:0:0:0:", "307,255,19156,1,0,0:0:0:0:", "300,260,19220,1,0,0:0:0:0:", "293,264,19285,1,0,0:0:0:0:", "286,267,19350,1,8,0:0:0:0:", "278,270,19414,1,0,0:0:0:0:", "271,272,19479,1,0,0:0:0:0:", "263,273,19544,1,0,0:0:0:0:", "255,273,19608,1,2,0:0:0:0:", "247,273,19673,1,0,0:0:0:0:", "239,271,19738,1,0,0:0:0:0:", "231,269,19802,1,0,0:0:0:0:", "223,266,19867,1,8,0:0:0:0:", "216,263,19932,1,0,0:0:0:0:", "209,259,19996,1,0,0:0:0:0:", "203,254,20061,1,0,0:0:0:0:", "197,249,20126,5,6,0:0:0:0:", "192,243,20190,1,0,0:0:0:0:", "187,236,20255,1,0,0:0:0:0:", "183,229,20320,1,0,0:0:0:0:", "180,222,20384,1,8,0:0:0:0:", "177,214,20449,1,0,0:0:0:0:", "175,207,20514,1,0,0:0:0:0:", "174,199,20578,1,0,0:0:0:0:", "174,191,20643,1,2,0:0:0:0:", "174,183,20708,1,0,0:0:0:0:", "176,175,20772,1,0,0:0:0:0:", "178,167,20837,1,0,0:0:0:0:", "181,159,20902,1,8,0:0:0:0:", "184,152,20966,1,0,0:0:0:0:", "188,145,21031,1,0,0:0:0:0:", "193,139,21095,1,0,0:0:0:0:"]
    templateSmallSquare = ["224,192,483,5,0,0:0:0:0:", "224,160,561,1,0,0:0:0:0:", "256,160,640,1,0,0:0:0:0:", "288,160,719,1,0,0:0:0:0:", "288,192,797,1,0,0:0:0:0:", "288,224,876,1,0,0:0:0:0:", "256,224,955,1,0,0:0:0:0:", "224,224,1033,1,0,0:0:0:0:"]
    hitOut = []

    if input2 == 0:
        while currentTime < end:
            for line in templateSquare:
                if currentTime < end:
                    temp = line.rstrip().split(",")
                    temp[2] = int(currentTime)
                    line = ""
                    for i in range(0,len(temp)-1):
                        line = line + str(temp[i]) + ","
                    line = line + temp[len(temp)-1]
                    currentTime = currentTime + bpm/divisor
                    hitOut.append(line.rstrip()+"\n")
                else:
                    break
    if input2 == 1:
        while currentTime < end:
            for line in templateCircle:
                if currentTime < end:
                    temp = line.rstrip().split(",")
                    temp[2] = int(currentTime)
                    line = ""
                    for i in range(0,len(temp)-1):
                        line = line + str(temp[i]) + ","
                    line = line + temp[len(temp)-1]
                    currentTime = currentTime + bpm/divisor
                    hitOut.append(line.rstrip()+"\n")
                else:
                    break
    if input2 == 2:
        while currentTime < end:
            for line in templateSmallSquare:
                if currentTime < end:
                    temp = line.rstrip().split(",")
                    temp[2] = int(currentTime)
                    line = ""
                    for i in range(0,len(temp)-1):
                        line = line + str(temp[i]) + ","
                    line = line + temp[len(temp)-1]
                    currentTime = currentTime + bpm/divisor
                    hitOut.append(line.rstrip()+"\n")
                else:
                    break
    if input2 == 3:
        while currentTime < end:
            for line in templateCustom:
                if currentTime < end:
                    temp = line.rstrip().split(",")
                    temp[2] = int(currentTime)
                    line = ""
                    for i in range(0,len(temp)-1):
                        line = line + str(temp[i]) + ","
                    line = line + temp[len(temp)-1]
                    currentTime = currentTime + bpm/divisor
                    hitOut.append(line.rstrip()+"\n")
                else:
                    break

    for x in hitOut:
        file.write(x)
        
print("\nSucess:")
print(title + "[lazyMapper "+diffName+"].osu was created")