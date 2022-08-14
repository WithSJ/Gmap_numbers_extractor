from libs.applibs import utils

def clean_data():
    FileData= open(f"{utils.FILENAME}_Gmap.data")
    WriteData = open(f"{utils.FILENAME}_GmapNumbers.csv","a")
    OutputData = list()

    for line in FileData.readlines():
        if utils.CODE in line:
            index = line.index(utils.CODE)
            endindx = line.index("</")
            cleanLine = line[index:endindx].replace(" ","").replace("-","")
            utils.SEARCH_ITEM.add(cleanLine)
            OutputData.append(cleanLine+"\n")

    OutputData = sorted(list(set(OutputData)))
    WriteData.writelines(OutputData)
    FileData.close()
    WriteData.close()
    

def sort_data():
    FileDATA = open(f"{utils.FILENAME}_GmapNumbers.csv")
    FileData= FileDATA.readlines()
    FileData = sorted(list(set(FileData)))
    NewData = list()
    if len(utils.Filter) > 0:
        for num in FileData:
            for item in utils.Filter:
                if item in num:
                    print(num)
                    NewData.append(num)    
    else:
        NewData = FileData

    
    NEWDATA = open(f"{utils.FILENAME}_GmapNumbers.csv","w")
    NEWDATA.writelines(NewData)
    NEWDATA.close()
    FileDATA.close()

    
