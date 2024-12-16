#Aiming to make this a bigger indie game, hope you enjoy it :)
#Sorry if anything is a bit off in the translation. Spanish is my first language, and I used AI to help me out and make it better.

import random

knowledge = 0
instability = 0
Malice = 0

print('__________________________')
print('|  Welcome to Nexus 🧠🧪 |')
print('|                        |')
print('|        play(1)         |')
print('|       credits(2)       |')
print('|________________________|')
play=int(input('Choose: '))

while play == 1:
    print('\n')
    print('You stir, a throbbing pain pulsing behind your eyes. Your lab chair is cold against your back as you try to recall last night.Your notebook is the first thing you see; you trace your name with a trembling finger:')
    name = str(input('Your name:'))
    print('\n')
    print("You flip open the notebook, memories flooding back. When you read the last page, the word 'Nexus' jumped out at you. Nexus, your groundbreaking discovery - a compound designed to amplify the human mind. Despite the scientific community's dismissal of your research as unethical, you'd succeeded in synthesizing a stable sample last night. And your first guinea pig? Yourself.")
    print('\n')
    print(name,":'What the hell did I do last night? How much Nexus was it?'")
    print('\n')
    print('The substance has transformed you. Your concentration is superhuman, your understanding profound. But as you delve deeper, a growing sense of unease gnaws at you. Something is off.')
    print('\n')

    print(name,": 'It worked!, what shall i do now?, I could see if my theory is correct, although it seems it worked better than I expected, and I don't want others to steal my discovery'")
    print('\n')
    print('1) Read the Notebook')
    print('2) Continue experimenting')
    print('3) Destroy you notebook')
    scene1 = int(input('Choose: '))
    1
    if scene1 == 1:
        knowledge = knowledge + 2
        action = 'studying'
        print('With your newly enhanced mind, you delve into your notes and are astonished by the speed and depth of your understanding. Diagrams, formulas, and calculations that once seemed daunting now seem almost trivial. You discover that the Nexus is directly influencing your glutamate and serotonin receptors.')
    elif scene1 == 2:
        instability = instability + 2
        action = 'experimenting'
        print("Emboldened by your newfound mental prowess and convinced that the ends justify the means, you ramp up your Nexus synthesis and consumption. Yet, a nagging sense of dread begins to take hold as you notice disturbing changes, which you desperately try to dismiss")
    elif scene1 == 3:
        Malice = Malice + 2
        action = 'Destroying'
        print("The Nexus formula is etched into your mind thanks to your new abilities. Creating another would be a matter of minutes. However, fear of the repercussions and ambition to be the sole possessor of this knowledge lead you to make a radical decision: you burn all your notes with a chemical that guarantees their total destruction.")
    
    
    play = 2
