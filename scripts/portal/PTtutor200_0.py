GUARD1 = 9300498
GUARD2 = 9300507

if sm.hasQuest(25000):
    sm.removeEscapeButton()
    sm.flipDialoguePlayerAsSpeaker()
    sm.sendNext("This portal leads straight into Ereve. The place is going to be positively crawling with knights. Sounds like just my kind of place.")
    sm.startQuestNoCheck(25003)
    sm.removeMobByTemplateId(GUARD1)
    sm.removeMobByTemplateId(GUARD2)
    sm.warpInstanceIn(915000300, 1)
