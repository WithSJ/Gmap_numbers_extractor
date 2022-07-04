from libs.applibs import utils

def clean_data():
    FileData= open(f"{utils.FILENAME}_Gmap.csv").readlines()
    WriteData = open(f"{utils.FILENAME}_CleanGmap.csv","a")
    OutputData = list()

    for line in FileData:
        if utils.CODE in line:
            index = line.index(utils.CODE)
            endindx = line.index("</")
            cleanLine = line[index:endindx].replace(" ","").replace("-","")
            print(cleanLine)
            utils.SEARCH_ITEM.add(cleanLine)
            OutputData.append(cleanLine+"\n")

    OutputData = sorted(list(set(OutputData)))
    WriteData.writelines(OutputData)

def sort_data():
    FileData= open(f"{utils.FILENAME}_CleanGmap.csv").readlines()
    FileData = sorted(list(set(FileData)))
    open(f"{utils.FILENAME}_CleanGmap.csv","w").writelines(FileData)

    
