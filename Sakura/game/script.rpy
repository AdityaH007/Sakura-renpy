label start:
    scene room  # Display a background image or scene.

    "Welcome to the game!"

    $ name_prompt = renpy.input("What's your name?", "Player")  # The user's input will be stored in the 'name_prompt' variable.

    $ pl = name_prompt.strip()  # Store the entered name in a variable, removing leading or trailing spaces.

    "Nice to meet you, [pl]!"

    
    menu :
        "So Are you ready to conitnue?"
        "Yes":
            jump main_story
        "No":
            jump start
        



    # Continue with the rest of your game script.
    

label main_story:
    scene room
    with fade
    # Your main story content goes here.
    " [pl]: I'm really tired ........ its almost mid night ...."
    " [pl]: Maybe i should sleep"

    menu :
        "Will you sleep?"
        "yes":
            jump scene1
        "no, i will wait a bit":
            
            jump scene1

                

    # Continue with the rest of your story.

label scene1:
    scene scene1
    with dissolve
    "[pl]: 'breathing heavily'"
    "[pl]: what is this place , where am I ? "
    "[pl]: is it a dream?"

    menu:
        "Pinch yourself?"
        "Yes":
            with vpunch
            "ouch that hurts"
            
        "You have to do it":
            "ouch that hurts"
            with vpunch 

    "Is it true? what should i do?"
    menu:
        "Should move ahead or just wait.... maybe its just a dream"
        "Move ahead":
            
            jump scene2
        "I should wait, it will be over":
            
            jump city

label scene2:
    scene scene2
    with fade 
    "Wow , It's a beautiful place "
    "I should move ahead .... I might find something intresting"
    "........."
    
    "Is that a map , should i pick it up and see?"
    menu:
        "Pick Up The map"
        "Yes":
            jump scene3
        "No explore on your own":
            jump scene4    


label city:
    scene city
    with hpunch
    "You shoudn't have done this"
    menu:
        "Do you want to go back?"
        "Yes ! take me back":
            jump scene1
        "No ! just quit it already":
            return    

label scene3:
    scene scene3
    with fade
    "It looks some kind of treasure map ..."
    menu:

        "Should i follow it?"
        "yes":
            jump scene5
        "No! explore on your own":
            jump scene4

label scene4:
    scene scene4
    with dissolve
    "This place is beautiful "
    "Maybe its really real"
    "I should keep exploring"  
    jump scene6          

label scene5:
    scene scene5
    with fade
    "This place is massive"
    "It's scary too"
    "Maybe i should just follow the map and move ahead"
    jump scene12

label scene6:
    scene scene6
    with fade
    "uh oh my god"
    "what are these creatures"
    "I should run away"
    menu:
        "Escape?"
        "Yes":
            jump scene7
        "You dont have a choice this time you can't fight":
            jump scene7

label scene7:
    scene scene7
    with fade
    "Oh no what is this place"
    "I dont feel right to go inside"

    menu:
        "I dont know what to do"
        "Move Ahead":
            jump scene8
        "Return to pick map":
            jump scene3    

label scene8:
    scene scene8
    with fade
    "I wish it's just a dream cause things are not going in a right way"
    "............."
    "I think i should move ahead now, i dont see a way back"
    menu:
        "Move ahead?"
        "yes?":
            "Before you stands a mystical door adorned with glowing glyphs. Each glyph represents a different element of nature. The inscription below reads,"
            menu:
                "Arrange the glyphs in the correct sequence based on their harmony with nature to unlock the enchanted door."
                "['Sun'] - ['Moon'] - ['Leaf'] - ['Wave']":
                    "Wrong"
                    jump scene8
                "[Leaf] - [Wave] - [Sun] - [Moon]":
                    "Correct"
                    jump scene9
                "[Moon] - [Sun] - [Wave] - [Leaf]":
                    "wrong"
                    jump scene8
                "[Wave] - [Leaf] - [Moon] - [Sun]":
                    "wrong"
                    jump scene8            
label scene9:
    scene scene9
    with fade
    "Oh No! what is this?"
    "Am i supposed to fight him?"
    "MONSTER: Kein vokun viing sahvot dovah! Nu hin sille nuziid lost pahlok.(how dare you come here human ! now you'll face your death by my hand)"  
    "You find yourself facing an imposing elemental boss, a creature of swirling winds, molten fire, crashing waves, and earthen strength. The boss stands in front of four elemental altars, each corresponding to one of its forms."

    "Boss's Weaknesses:"

    "Wind Form - Vulnerable to Fire attacks.
    Fire Form - Vulnerable to Water attacks.
    Water Form - Vulnerable to Earth attacks.
    Earth Form - Vulnerable to Wind attacks"

    menu:
        "You have a set of magical orbs in your possession, each representing one of the elemental attacks"
        "Cast a Fire Orb at the Wind Form altar.":
            "YOU Lost"
            jump scene9

        "Cast a Water Orb at the Fire Form altar.":
            "YOu defeated the monster"
            jump scene10

        "Cast an Earth Orb at the Water Form altar":
            "You Lost"
            jump scene9

        "Cast a Wind Orb at the Earth Form altar":
            "You Lost"
            jump scene9                        

label scene10:
    scene scene10
    with fade
    "You Enter a old sanctum and found and see 4 books "
    "You start to read them one by one"
    "1. The Elemental Behemoth of Sakura's Grove"
    "Centuries ago, Sakura's grove was a sanctuary of balance and tranquility,"
    "guarded by powerful elemental spirits representing wind, fire, water, and earth."
    "These benevolent spirits ensured the harmony of the grove,"
    "nurturing the cherry blossoms and safeguarding its magical essence."
    "However, a dark force known as the Shadow Enchanter sought to harness the grove's power for nefarious purposes." 
    "Using forbidden rituals, the enchanter corrupted the elemental spirits, merging them into a colossal Elemental Behemoth — 
    a creature embodying the twisted fusion of wind, fire, water, and earth"

    "2.Prophecy: The Chosen One of Sakura's Whispers"
    "When the sakura whispers fall silent, a hero shall rise, 
    wielding the power of wind, fire, water, and earth. The elements, 
    once corrupted, shall bow before the chosen one, and Sakura's grove shall bloom anew." 

    "3.The Fading Whispers"
    "As the Elemental Behemoth wreaked havoc, the sakura blossoms began to lose their vibrant glow. 
    The connection between the sakura and the elemental spirits was weakened, 
    causing the whispers of Sakura to fade, and the grove fell into disarray."

    "The once-lush grove became shrouded in an unnatural gloom, 
    and the sakura blossoms lost their enchanting brilliance. 
    It was as if the very soul of the grove was being drained by the corrupted Elemental Behemoth."   

    "The fourth book said :Kein vokun viing wahlaan qethsegol, Kein tol daar dovah"

    "Your eyes suddenly closed and everything starts to fade"
    jump scene11

label scene11:
    scene scene11
    with fade
    "You woke in your room"
    "You coudn't undertsand was it real or just a dream"


label scene12:
    scene scene12
    with fade
    "you reach a mystical place full of spirits"
    "A guardian approach you"
    "Guardian:Hello adventurer , are you looking for something? "
    "you tell all your story how you reaach here "
    "guarding said he can take you back to your world , sometimes it happned and ask you to follow him"
    "You follow  him"
    jump scene13

label scene13:
    scene scene13
    with fade
    "He takes you to a old remains of a large fort"
    "everything is destroyed and lots mystical creatured live"

    scene scene14
    with fade
    "The creatured greets you welcome and you also greets them "
    "you move ahead following the guardian"

    scene scene15
    with fade
    "You reach to a old room where he guidess you to a portal "
    "U wished him thank you and move into the portal"
    "Your eyes starts to close and everything turns black"
    jump scene11    