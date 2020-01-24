#! python3
import re

neighborhoodsAst = ["Astoria","Long-Island-City","Upper-East-Side"]
neighborhoodsSunny = ["Sunnyside-Gardens","Sunnyside","Blissville","Laurel-Hill"]
neighborhoodsJack = ["Woodside","Jackson-Heights","East-Elmhurst","Corona","Elmhurst","Maspeth","LeFrak-City",
    "Middle-Village","Rego-Park","Forest-Hills","Forest-Hills-Gardens","Kew-Gardens","Flushing",
    "College-Point"]
neighborhoodsOzone = ["Woodhaven","Ozone-Park","Lindenwood","Glendale"]
neighborhoodsRich = ["South-Richmond-Hill","Richmond-Hill","South-Ozone-Park"]
neighborhoodsSut = ["Briarwood","Kew-Gardens-Hills","Pomonok","Utopia","Hillcrest","Jamaica-Hills","Fresh-Meadows",
   "Jamaica-Estates","Jamaica","South-Jamaica","Sutphin"]
neighborhoodsJam = ["Hollis","Queens-Village","Saint-Albans","Cambria-Heights","Locust-Manor","Laurelton","Springfield-Gardens",
   "Rochdale","Rosedale","Jamaica"]
neighborhoodsFlo = ["Floral-Park","Glen-Oaks","Douglaston-Little-Neck","Oakland-Gardens","Bellaire","Bellerose"]
neighborhoodsPCCH = ["Parkchester","Castle-Hill","Bronxdale","Morris-Park","Van-Nest","Pelham-Bay","Westchester-Square",
    "Fairmont-Claremont-Village","Soundview","Unionport","Bronx"]
neighborhoodsBrook = ["Borough-Park","Park-Slope","Greenwood","Windsor-Terrace","Sunset-Park","Mapleton","Prospect-Park-South",
     "Flatbush","Prospect-Lefferts-Gardens","Brooklyn"]

def writeTo(fileName,fileContent):
    with open(fileName,"w+") as outfile:
        outfile.write(fileContent)
    return

# Regex Cannot handle special characters : '?' be careful
# escape the ? by \?
def findAll(lookup,refContent,tag):
    startIndices = [m.start() for m in re.finditer(lookup, refContent)]
    indexPairs = []
    lookLength = len(lookup)
    for elem in startIndices:
        indexPairs.append((elem,elem+lookLength,tag))
    return indexPairs

def orderIndices(arr,arrLen):
    key = None
    for i in range(1,arrLen):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# input ex. : "Astoria", "Floral-Park"
# output: index.html with replaced titleString
def makeFile(nbrhood):
    # bannerString and first indexLink are too close so characters in between must be paid special attention
    titleString = "id=\"Neighborhood Title\">SHSAT - Khan's Tutorial</title>"
    bannerString = "id=\"Neighborhood 1\">SHSAT Tutoring</h1>"
    featureString = "Why do families choose Khan's"
    newTString = titleString.replace("SHSAT - Khan's Tutorial</title>",nbrhood.replace('-',' ')+" SHSAT - Khan's Tutorial</title>")
    newBString = bannerString.replace("SHSAT Tutoring</h1>",nbrhood.replace('-',' ')+" SHSAT Tutoring</h1>")
    newFString = featureString.replace("Why do families choose Khan's","Why do "+nbrhood.replace('-',' ')+" families choose Khan's")

    insertDict = {
        't' : newTString,
        'b' : newBString,
        'f' : newFString
    }

    template = "./index.html"
    if(nbrhood in neighborhoodsAst): template = "./indexAST.html"
    if(nbrhood in neighborhoodsFlo): template = "./indexFP.html"
    if(nbrhood in neighborhoodsSunny): template = "./indexSS.html"
    if(nbrhood in neighborhoodsJack): template = "./indexJH.html"
    if(nbrhood in neighborhoodsOzone): template = "./indexOP.html"
    if(nbrhood in neighborhoodsRich): template = "./indexRH.html"
    if(nbrhood in neighborhoodsSut): template = "./indexSUT.html"
    if(nbrhood in neighborhoodsJam): template = "./indexJA.html"
    if(nbrhood in neighborhoodsPCCH): template = "./indexPCCH.html"
    if(nbrhood in neighborhoodsBrook): template = "./indexBK.html"

    with open(template,"r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        tIndices = findAll(titleString,refContent,'t')
        bIndices = findAll(bannerString,refContent,'b')
        fIndices = findAll(featureString,refContent,'f')
        allIndices = tIndices+bIndices+fIndices
        #print(allIndices)
        allLength = len(allIndices)
        orderIndices(allIndices,allLength)
        endContent = ""
        # loop only works for allLength > 2
        for i in range(allLength):
            insertStr = insertDict[allIndices[i][2]]
            if(i==0):
                endContent += refContent[:allIndices[i][0]]+insertStr
            elif(i==allLength-1):
                endContent += insertStr+refContent[allIndices[i][1]:]
                break
            else:
                endContent += refContent[allIndices[i-1][1]:allIndices[i][0]]+insertStr+refContent[allIndices[i][1]:allIndices[i+1][0]]
                #refContent[allIndices[i-1][1]:allIndices[i][0]]+
        return endContent
    return endContent

def generateIndex(nbrhood):
    fileName = nbrhood+".html"
    writeTo(fileName,makeFile(nbrhood))
    return

# generates html pages for all neighborhoods on file
def cityGeneration():
    neighborhoods = ["Astoria","Auburndale","Bay-Terrace","Bayside","Beechhurst","Bellaire",
                     "Bellerose","Blissville","Borough-Park","Briarwood","Bronxdale","Cambria-Heights",
                     "Castle-Hill","Clearview","College-Point","Corona","Ditmas-Park","Douglaston-Little-Neck",
                     "East-Elmhurst","Elmhurst","Fairmont-Claremont-Village","Flatbush","Floral-Park",
                     "Flushing","Forest-Hills-Gardens","Forest-Hills","Fresh-Meadows","Glen-Oaks","Glendale","Greenwood",
                     "Hillcrest","Hollis","Jackson-Heights","Jamaica-Estates","Jamaica-Hills","Jamaica",
                     "Kew-Gardens-Hills","Kew-Gardens","Laurel-Hill","Laurelton","LeFrak-City","Lindenwood",
                     "Locust-Manor","Long-Island-City","Malba","Mapleton","Maspeth","Middle-Village",
                     "Morris-Park","Murray-Hill","Oakland-Gardens","Ozone-Park","Park-Slope","Parkchester",
                     "Pelham-Bay","Pomonok","Prospect-Lefferts-Gardens","Prospect-Park-South","Queens-Village",
                     "Rego-Park","Richmond-Hill","Rochdale","Rosedale","Saint-Albans","Soundview","South-Jamaica",
                     "South-Ozone-Park","South-Richmond-Hill","Springfield-Gardens","Sunnyside-Gardens","Sunnyside",
                     "Sunset-Park","Unionport","Upper-East-Side","Utopia","Van-Nest","West-Farms","Westchester-Square",
                     "Whitestone","Windsor-Terrace","Woodhaven","Woodside","Sutphin","Jamaica","Bronx","Brooklyn"]
    for x in neighborhoods:
        generateIndex(x)
    return

def test():
    generateIndex("Floral-Park")
    return

#test()
cityGeneration()
