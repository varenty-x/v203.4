# 21200 - [Job Adv] (Lv.30)   Aran
sm.setSpeakerID(1201001)
sm.sendNext("Voom voom voom voom...")
sm.setPlayerAsSpeaker()
sm.sendNext("#b(The #p1201001# is producing an undulating echo. But who is that boy standing over there?)")
sm.sendNext("You've never seen him before. He doesn't look human.")
sm.setSpeakerID(1201002)
sm.sendNext("Yo, Aran! Do you not hear me? I said, do you not hear me! Ugh, how frustrating!")
sm.setPlayerAsSpeaker()
sm.sendNext("#b(Hm? Who's voice was that? It sounds like an angry boy...)")
sm.setSpeakerID(1201002)
sm.sendNext("Ugh, my only master had to end up trapped in ice for hundreds of years, abandoning me completely, and is now completely ignoring me.")
sm.setPlayerAsSpeaker()
sm.sendNext("Who...are you?")
sm.setSpeakerID(1201002)
sm.sendNext("Aran? Do you hear me now? It's me! Don't you recognize me? I'm your weapon, #b#p1201002# the polearm#k!")
sm.setPlayerAsSpeaker()
sm.sendNext("#b(...#p1201002#? A #p1201001# can talk?")
sm.setSpeakerID(1201002)
sm.sendNext("What's with that suspicious look on your face? I know you've lost your memory, but did you forget about me, too? How could you?!")
sm.setPlayerAsSpeaker()
sm.sendNext("I'm so sorry, but I can't remember a thing.")
sm.setSpeakerID(1201002)
if sm.sendAskYesNo("Sorry doesn't cut it! Do you know how lonely and bored I was for hundreds of years? I don't care what it takes! Remember me! Remember me now!"):
    sm.completeQuest(parentID)
    sm.setPlayerAsSpeaker()
    sm.sendNext("#b(The voice that claims to be #p1201002#? the #p1201001# is yelling in frustration. You don't think this conversatin is going anywhere. You better go talk to #p1510009# first.)")
    sm.dispose()
else:
    sm.dispose()