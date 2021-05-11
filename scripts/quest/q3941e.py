# 3941: Stealing Queen's Order of Silk

from net.swordie.ms.client.character.skills.temp import CharacterTemporaryStat

karcasa = 2101013
tigun = 2101004
silk = 4031571
isTigun = sm.hasCTS(CharacterTemporaryStat.Morph)

sm.setSpeakerID(karcasa)
if isTigun:
    sm.sendNext("Okay, here it is. Please handle this with care. This silk is very, very hard to find. "
    "If it's damaged anywhere, you'll be in jail in no time.\r\n"
    "1 #i" + str(silk) + "##z" + str(silk) + "#")
    if sm.canHold(silk):
        sm.giveItem(silk)
        sm.completeQuest(parentID)
    else:
        sm.sendSayOkay("Er, #p" + str(tigun) + "#, it looks like you can't hold the silk. Talk to me again after you make some space.")
    
else:
    sm.sendSayOkay("Okay, here it is. Please handle this with... huh? #p" + str(tigun) + "#, where did you go?")