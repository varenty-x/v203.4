# Piece of Time (2434584)

from net.swordie.ms.constants import JobConstants

def exchangePieces(gear):
    if not sm.hasItem(parentID, 5):
        sm.sendSayOkay("You need #b5 #i" + str(parentID) + "# #z" + str(parentID) + "##k to exchange for #b#i" + str(gear) + "# #z" + str(gear) + "##k.")
    elif not sm.canHold(gear):
        sm.sendSayOkay("Please make room in your Equip inventory.")
    else:
        sm.consumeItem(parentID, 5)
        sm.giveItem(gear)

admin = 2007

masterList = [1042254, 1042255, 1042256, 1042257, 1042258]
job = chr.getJob()

recList = []

# Filter recList based on current character class (*not* mutually exclusive because Xenon)
if JobConstants.isWarriorEquipJob(job):
    recList.append(masterList[0])
if JobConstants.isMageEquipJob(job):
    recList.append(masterList[1])
if JobConstants.isArcherEquipJob(job):
    recList.append(masterList[2])
if JobConstants.isThiefEquipJob(job):
    recList.append(masterList[3])
if JobConstants.isPirateEquipJob(job):
    recList.append(masterList[4])

# To use as last option for initial recommendation
viewAll = len(recList)

sm.setSpeakerID(admin)
recString = "Equipment for your class will be recommended first. #b\r\n"
# Construct initial recommendations
for index, gear in enumerate(recList):
    recString += "#L"+ str(index) + "##i" + str(gear) + "# #z" + str(gear) +"##l\r\n"
recString += "#L"+ str(viewAll) + "#View the entire item list.#l\r\n"
recSelection = sm.sendNext(recString)

# Look at everything
if recSelection == viewAll:
    selString = "Please select the armor you'd like to receive. #b\r\n"
    for index, gear in enumerate(masterList):
        selString += "#L"+ str(index) + "##i" + str(gear) + "# #z" + str(gear) +"##l\r\n"
    selection = sm.sendNext(selString)

    selectedGear = masterList[selection]
    exchangePieces(selectedGear)
# Picked recommended gear
else:
    selectedGear = recList[recSelection]
    exchangePieces(selectedGear)