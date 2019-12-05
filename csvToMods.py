import datetime as dt
from io import StringIO
import time
import xml.etree.ElementTree as ET
import csv

#Convert a vendor CSV to individual MODS xml files, ready for Islandora Batch Ingest
#Author: Jim Duran
#Date: 2019-12-05
#csv columns should be in this order exactly:
#    Identifier
#    TapeNumber
#    Program Unique Identifier
#    Date
#    Title
#    Description
#    Interviewee
#    Interviewer

modsAttributes = {
    "xmlns" : "http://www.loc.gov/mods/v3", 
    "xmlns:mods" : "http://www.loc.gov/mods/v3",
    "xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance",
    "xmlns:xlink" : "http://www.w3.org/1999/xlink"}

with open('inputData.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]}')
            identifier = row[0]
            tapeNo = row[1]
            programGroup = row[2]
            date = row[3]
            title = row[4]
            desc = row[5]
            interviewer = row[6]
            interviewee = row[7]

            #Begin the transformation
            data = ET.Element('mods', modsAttributes)

            #Title
            titleInfo = ET.SubElement(data,'titleInfo')
            modsTitle = ET.SubElement(titleInfo,'title')
            modsTitle.text = title #from csv read
            modsSubT = ET.SubElement(data,'subTitle')
            
            #Interviewee
            modsName = ET.SubElement(data,'name')
            modsInterviewee = ET.SubElement(modsName,'namePart')
            modsInterviewee.text = interviewee
            modsNameRoleTermIE = ET.SubElement(modsName,'roleTerm',{"authority":"marcrelator","type":"text"})
            modsNameRoleTermIE.text = "Interviewee"
            
            #Interviewer
            modsInterviewer = ET.SubElement(modsName,'namePart')
            modsInterviewer.text = interviewer
            modsNameRoleTermIR = ET.SubElement(modsName,'roleTerm',{"authority":"marcrelator","type":"text"})
            modsNameRoleTermIR.text = "Interviewer"

            #Type of Resource
            modsResourceType = ET.SubElement(data,'typeOfResource')
            modsResourceType.text = "sound recording"
            modsToC = ET.SubElement(data,'tableOfContents')
            modsGenre = ET.SubElement(data,'genre')
            
            #Date and other publisher info non-variable
            modsOrigin = ET.SubElement(data,'originInfo')
            modsDateIssued = ET.SubElement(modsOrigin,'dateIssued')
            modsDateIssued.text = date
            modsPublisher = ET.SubElement(modsOrigin,'publisher')
            modsPlace = ET.SubElement(modsOrigin,'place')
            modsPlaceTerm = ET.SubElement(modsPlace,'placeTerm',{"type":"text"})

            #Language
            modsLanguage = ET.SubElement(data,'language')
            modsLanguageTerm = ET.SubElement(modsLanguage,'languageTerm',{"authority":"iso639-2b","type":"code"})
            modsLanguageTerm.text = "spa"

            #Description
            modsAbstract = ET.SubElement(data,'abstract')
            modsAbstract.text = desc

            #Identifier
            modsIdentifier = ET.SubElement(data,'identifier')
            modsIdentifier.text = identifier

            #PhysicalDescription
            modsPhysDisc = ET.SubElement(data,'physicalDescription')
            modsForm = ET.SubElement(modsPhysDisc,'form',{"authority":"marcform"})
            modsForm.text = "sound recording"
            modsExtent = ET.SubElement(modsPhysDisc,'extent')

            #Program Unique Identifier
            modsNote = ET.SubElement(data,'note')
            modsNote.text = programGroup

            myDoc = ET.tostring(data,encoding='utf-8')
            #myDoc = str(myDoc)
            #print(myDoc)
            myDocsName = 'out/'+identifier+".xml"
            with open(myDocsName,"wb") as file:
                file.write(myDoc)
            line_count += 1

print("Job Complete.",line_count - 1,'files converted.')
