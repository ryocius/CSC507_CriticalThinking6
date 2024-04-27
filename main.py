import random
import time
import os
from filesplit.split import Split
import shutil

# 1. Run the process as it is, with the larger files
def runAsIs(inFile, outName):
    start = time.time()
    with open(inFile, "r") as file:
        array = file.readlines()
        with open(outName, "w") as output:
            for i in range(len(array)):
                try:
                    output.write(str(int(array[i]) * 2) + "\n")
                except:
                    print("empty file")
    end = time.time()
    return end - start

#2. Break the input file up into 10 files and schedule the process on each one to run in real-time, then combine the resulting files into a single output file.
def breakIntoTen(inFile, outName, size):
    start = time.time()
    with open(inFile, "r") as file:
        split = Split(inFile, "C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt2").bylinecount(size/10)
    i = 1
    for filename in os.scandir("opt2"):
        if "file1" in filename.name:
            runAsIs(filename, "Opt2\\newFile_"+ str(i) + ".txt")
        i += 1
    with open(outName, "w") as output:
        for filename in os.scandir("opt2"):
            if "newFile_" in filename.name:
                with open(filename, "r") as temp:
                    array = temp.readlines()
                    for i in range(len(array)):
                        output.write(str(array[i]))
    end = time.time()
    return end - start

# 3. Break the input file up into 2 files and schedule the process on each one to run in real-time, then combine the resulting files into a single output file.
def breakIntoTwo(inFile, outName, size):
    start = time.time()
    with open(inFile, "r") as file:
        split = Split(inFile, "C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt3").bylinecount(size/2)
    i = 1
    for filename in os.scandir("Opt3"):
        if "file1" in filename.name:
            runAsIs(filename, "Opt3\\newFile_"+ str(i) + ".txt")
        i += 1
    with open(outName, "w") as output:
        for filename in os.scandir("Opt3"):
            if "newFile_" in filename.name:
                with open(filename, "r") as temp:
                    array = temp.readlines()
                    for i in range(len(array)):
                        output.write(str(array[i]))
    end = time.time()
    return end - start

# 4. Break the input file up into 5 files and schedule the process on each one to run in real-time, then combine the resulting files into a single output file.
def breakIntoFive(inFile, outName, size):
    start = time.time()
    with open(inFile, "r") as file:
        split = Split(inFile, "C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt4").bylinecount(size/5)
    i = 1
    for filename in os.scandir("Opt4"):
        if "file1" in filename.name:
            runAsIs(filename, "Opt4\\newFile_"+ str(i) + ".txt")
        i += 1
    with open(outName, "w") as output:
        for filename in os.scandir("Opt4"):
            if "newFile_" in filename.name:
                with open(filename, "r") as temp:
                    array = temp.readlines()
                    for i in range(len(array)):
                        output.write(str(array[i]))
    end = time.time()
    return end - start


# 5. Break the input file up into 20 files and schedule the process on each one to run in real-time, then combine the resulting files into a single output file.
def breakIntoTwenty(inFile, outName, size):
    start = time.time()
    with open(inFile, "r") as file:
        split = Split(inFile, "C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt5").bylinecount(size/20)
    i = 1
    for filename in os.scandir("Opt5"):
        if "file1" in filename.name:
            runAsIs(filename, "Opt5\\newFile_"+ str(i) + ".txt")
        i += 1
    with open(outName, "w") as output:
        for filename in os.scandir("Opt5"):
            if "newFile_" in filename.name:
                with open(filename, "r") as temp:
                    array = temp.readlines()
                    for i in range(len(array)):
                        output.write(str(array[i]))
    end = time.time()
    return end - start

def main():

    inFile = "file1.txt"
    size = 1000000

    try:
        os.remove("file1.txt")
        shutil.rmtree('C:/Users/ryoci/PycharmProjects/CSC507_CriticalThinking6/Results', ignore_errors=False)
        shutil.rmtree('C:/Users/ryoci/PycharmProjects/CSC507_CriticalThinking6/Opt2', ignore_errors=False)
        shutil.rmtree('C:/Users/ryoci/PycharmProjects/CSC507_CriticalThinking6/Opt3', ignore_errors=False)
        shutil.rmtree('C:/Users/ryoci/PycharmProjects/CSC507_CriticalThinking6/Opt4', ignore_errors=False)
        shutil.rmtree('C:/Users/ryoci/PycharmProjects/CSC507_CriticalThinking6/Opt5', ignore_errors=False)
    except:
        print("Nothing deleted")

    try:
        os.mkdir("C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Results")
        os.mkdir("C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt2")
        os.mkdir("C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt3")
        os.mkdir("C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt4")
        os.mkdir("C:\\Users\\ryoci\\PycharmProjects\\CSC507_CriticalThinking6\\Opt5")
    except:
        print("Folder existed")

    with open(inFile, "a") as file:
        for i in range(size):
            file.write(f"{random.randint(0,32767)}\n") # 32767 is the max value in the bash $RANDOM, a signed 15-bit int

    asIsTime = runAsIs(inFile, "Results\\out1.txt")
    opt2Time = breakIntoTen(inFile, "Results\\out2.txt", size)
    opt3Time = breakIntoTwo(inFile, "Results\\out3.txt", size)
    opt4Time = breakIntoFive(inFile, "Results\\out4.txt", size)
    opt5Time = breakIntoTwenty(inFile, "Results\\out5.txt", size)

    print(f"{asIsTime:.4f} seconds: Time to process 10,000,000 as-is")
    print(f"{opt2Time:.4f} seconds: Time to process 10,000,000 by splitting into 10 and running real-time")
    print(f"{opt3Time:.4f} seconds: Time to process 10,000,000 by splitting into 2 and running real-time")
    print(f"{opt4Time:.4f} seconds: Time to process 10,000,000 by splitting into 5 and running real-time")
    print(f"{opt5Time:.4f} seconds: Time to process 10,000,000 by splitting into 20 and running real-time")


main()

