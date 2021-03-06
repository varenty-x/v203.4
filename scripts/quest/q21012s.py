# Created by MechAviv
# Quest ID :: 21012
# Abilities Lost

sm.setSpeakerID(1202004)
sm.sendNext("Welcome, hero! What's that? You want to know how I knew who you were? That's easy. I eavesdropped on some people talking loudly next to me. I'm sure the rumor has spread through the entire island already. Everyone knows that you've returned!")


sm.setSpeakerID(1202004)
sm.sendSay("Anyway, what's with the long face? Is something wrong? Hm? You're not sure whether you're really a hero or not? You lost your memory?! No way... It must be because you were trapped inside the ice for hundreds and hundreds of years.")


sm.setSpeakerID(1202004)
if sm.sendAskAccept("Hm, how about trying out that sword? Wouldn't that bring back some memories? How about #bfighting some monsters#k?"):
    sm.startQuest(21012)
    sm.setSpeakerID(1202004)
    sm.removeEscapeButton()
    sm.sendNext("It just so happens that there are a lot of #r#o9300383#s#k near here. How about defeating just #r3#k of them? It could help you remember a thing or two.")


    sm.setSpeakerID(1202004)
    sm.removeEscapeButton()
    sm.sendSay("Ah, you've also forgotten how to use your skills? #bPlace skills in the quick slots for easy access.#k You can also place consumable items in the slots, so use the slots to your advantage.")

    sm.tutorAutomatedMsg(17)
else:
    sm.setSpeakerID(1202004)
    sm.sendNext("Hm... You don't think that would help? Think about it. It could help, you know...")