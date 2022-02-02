import minigame as mg

class User:
    def __init__(self):
        self.name = ""
        self.job = ""
    def define(self):
        self.name = input("Now, what is your name? \n")
        print("\nWhich path will you choose? \n    1: Astronaut \n    2: Farmer \n    3: Superhero \n")
        self.choice = input("    ").lower()
        if self.choice == "1" or self.choice == "astronaut":
            self.job_id = "astro"
        if self.choice == "2" or self.choice == "farmer":
            self.job_id = "farm"
        elif self.choice == "3" or self.choice == "superhero":
            self.job_id = "super"
        self.job = Occupation(self.job_id, self.name, "") #defines all but the personalization
        clear() #clears screen
        self.personalize()
    def personalize(self):
        self.options = []
        self.options.append(self.job.opening_info["option1"])
        self.options.append(self.job.opening_info["option2"])
        self.options.append(self.job.opening_info["option3"])
        print(self.job.opening_info["prompt"])
        for i in range(len(self.options)):
            print("    ",i+1,":",self.options[i])
        print(space(2))
        choice = int((input("What option do you choose? (1, 2, or 3) "+space(3))))
        if choice in [1, 2, 3]:
            self.job.personalization = self.options[choice-1]
        else:
            print("please enter either 1,2 or 3.")
            self.personalize()
        print(space(1))

        self.job = Occupation(self.job_id, self.name, self.job.personalization)

class Occupation:
    def __init__(self, id="", name="", personalization=""):
        self.id = id
        self.name = name
        self.personalization = personalization
        if self.id == "astro":
            self.astronaut()
        elif self.id == "farm":
            self.farmer()
        elif self.id == "super":
            self.superhero()
    def astronaut(self):
        self.title = "astronaut"

        self.opening_info = { # Stage 1
            "prompt": "Welcome to the National Aeronautics and Space Administration (NASA). You will   begin your training shortly. To which planet are you planning on journeying?",
            "option1": "Mars",
            "option2": "Neptune",
            "option3": "Saturn"
        }

        self.quit_info = { # Stage 2
            "prompt": "You have begun to your training to be an astronaut. However, as you learn more  about space, you realize how dangerous it is. You are beginning to have cold    feet.",
            "option1": ["This has been your dream all of your life. Progress can't be made without taking risks.", "You fight through the fear. The training cadets witnessing your bravery and perseverence, are deeply inspired."],
            "option2": ["There are better paths in life than this one. You would rather be a superhero!","You resign, and start your supernatural crime-fighting journey. However, it is a unfortunately short journey. You come to the frightening realization that you have no super powers when confronting a group of armed robbers."]
        }

        self.urgency_info = { # Stage 3
            "prompt": "During a zero-gravity training session, you are alerted that a member of your team has made an error in their calculations. It turns out that the possible window for your take off is three months sooner than you expected. Your trainers strongly suggest that you wait until the next window in 9 months, but you think that you can do it sooner.",
            "option1": ["Be patient. Better late then never.", "You choose to be patient, and spend your extra months doing extra training, spending time with your family, and learning more about space."],
            "option2": ["Be ambitious. Space travel is all about taking risks.", "Upon your premature takeoff, you come to the conclusion that space travel is not all about taking risks. You drop the flashcards that you had to made reminding you how to initiate the takeoff sequence, and spend you last moments awkwardly sitting as the millions of veiwers witness your anticlimatic end."]
        }

        self.mg_info = { # Stage 4
            "prompt": "Oh no! Looks like you have entered into an asteroid feild! Navigate through the asteroids the best you can!",
            "obstacle": "asteroids",
            "crash": "crashed!",
            "lose": "A meteor smashes into the hull of your ship. Although you will never get to touch it, you finally get to see"+self.personalization+" with your own eyes as your oxegen tank slowly empties. Better luck next time.",
            "win": "Nice job! You have cleared the asteroid feild and may now continue with your journey!"
        }

        self.win_info = { # Stage 5
            "prompt": "You have navigated through an asteroid feild and cemented yourself in history as one of the most throughly trained and skilled pilots. Your long awaited journey has been complete and you gaze off into the cosmos peacefully.",
        }

        self.try_again_info = { # Stage 6
            "prompt": "You have been back home for a week. You have been surrounded by family and friends since the moment you stepped out of your ship. It is beginning to feel overwhelming, especially when compared to the solitude of space. Even though you just got back, your boss offers your second space mission. Will you go?",
            "option1": ["Stay, it may be difficult for a little while but it is an adjustment you have to make.", "You decide to stay, and instead, carefully explain to your family what you are going through. They are apologetic and give you as much space as you would like. After a year, your brother's wife becomes pregnant, and their kids grow up listening to your incredible stories, and wanting to be just like you as they grow up. Your niece and nephew eventually become rocket engineers. They name their first rocket, 'The "+self.name+" Expeditioner. You never feel the need to go to space again."],
            "option2": ["Go. It is a difficult adjustment to make, so why not just make it once after you are done with your space travel.", "You decide to accept the mission. Your family and friends beg you to stay or at least delay your take off, but you explain that is no longer an option. Your friends and family are understandibly hurt but you carry out the mission anyway. Up on boarding you are shaken by seeing one of your crewmates hug their family goodbye. You become torn between the obligation you have to your crew, and your regret for leaving your family so soon. Your distraction leads you to butcher the take off sequence, and as a result butcher yourself."]
        }

        self.retire_info={ # Stage 7
            "prompt": "Congradulations your restraint and thoughtfullness has led you to a peacefull and rewarding life. Good job, "+self.name+"."
        }



    def farmer(self):
        self.title = "farmer"


        self.opening_info = { #Stage 1
            "prompt": "Welcome to the simple life. Your parents are glad to see that you will joining  them on your family's ____ farm.",
            "option1": "pig",
            "option2": "cow",
            "option3": "chicken"
        }

        self.quit_info = { # Stage 2
            "prompt": "You have begun your agricultural journey on your family's "+self.personalization+" farm. Unfortunately, you are already feeling unsatisfied. Your father promises that the work will get more and more rewarding as you continue, and says that you should just wait a few months. You are not sure if you want to wait that long.",
            "option1": ["Trust your father and keep farming. Without any education you probably won't make it far anyway.", "You decide to trust you father and keep farming. As time passes, you begin to form a close connection to a "+self.personalization+" who you name "+self.name+" Jr. You recognize the gratification that your father spoke of and are content with your decision to keep farming."],
            "option2": ["Venture the world. Bill gates dropped out of Harvard, so you can be rich without a proper education too!", "Determined to make a name for yourself, you burn you bridges with your family. You have no car and no money. As you begin the 1,847 mile journey to LA, you starve and pass away."]
        }

        self.urgency_info = { # Stage 3
            "prompt": "A bursted pipe flooded a quarter of your crops and left another quarter to dry out. Half of your total crop yeild has been lost. Luckily your father has drawn up a plan on how you can cut down your spending to the bare minimum and spend a few months repairing the damaged feilds. While he explains his long plan, you overhear the radio announce that there is a dog show open to the public in three weeks and that first place gets $20,000. $20,000 would put a significant dent into this years deficit, but you wouldn't have enough time to prep the feilds for winter, and risk losing all of next spring's crops.",
            "option1": ["Go with your father's plan. Farming is the life you chose. This little hicup is the kind of thing you signed up for.", "You set out with your father and his plan and begin the long process of preparing the crops. As you work beside him you notice your father has been pleased with the dedication you have shown to the family farm."],
            "option2": ["Enter the dog show. Desperate times call for desperate measures, and you have been working with animals all your life.","After a week you have yet to find a dog and decide to dress up one of your cutest sheep instead. You arrive at the competition to confused looks, laughter and a security gaurd excorting you out. While you were trying to teach a sheep fetch, your dad carried out his plan and was able to save half of the crops. However, upon your arrival, he announces that you are 'out of the family' and should pack up your things. "]
        }

        self.mg_info ={ # Stage 4
            "prompt": "Oh no! Looks like one of the "+self.personalization+"s chewed through the ropes holding the logs for the fire! They are tumbling down towards you fast! Get to the top of the hill and retie the remaining logs before someone gets hurt!",
            "obstacle": "logs",
            "crash": "been hit!",
            "lose": "A rolling log sweeps your feet, taking you to the bottom of the hill with it. More logs continue to pile on leaving you eternally resting in a log coffin. Better luck next time!",
            "win": "Wow! Nice work! You have conquered the hill and retied the logs before someone could get hurt!."
        }

        self.win_info = { # Stage 5
            "prompt": "You and your father repaired all of the damages done. The patience and effort you put into the work not only led to a massive crop yeild in the spring, but impressed your father so much that he decided he could retire and leave the farm in your hands."
        }


        self.try_again_info = { # Stage 6
            "prompt": "Everything is going well. You have almost everything you could want in life until you meet Sam, your soon to be partner, and eventually have three children. Your oldest child is 9 years old and named Taylor. Taylor hears about a dog show in school asks you if you could enter it together.",
            "option1": ["Enter the show. You remeber how much you wanted to do the same when you were her age.","You enter the show. You are unsure if your family is ready for a dog so you borrow a puppy from a shelter. You get to spend a lot of time with the puppy and Taylor, and even though you didn't win the competition, you have added another little member to your family."],
            "option2": ["Say no. Don't make be tempted by the same thing that almost lost you and your father the farm.","Taylor is suprised and angry. They begin to resent both you, for your authoritative parenting, and the farm, thinking of it as more and more of a destiny they can't escape. When Taylor gets older, they decide to move away and your other children follow suit. After you and Sam pass away, the farm and your "+self.personalization+
            "s are left to the bank, after being declined by your children."]
        }



        self.retire_info={ # Stage 7
            "prompt": "Congradulations your dedication to your farm and to your family has lead to a peaceful and rewarding life for you, Sam, and your children. Good work, "+self.name+"."
        }


    def superhero(self):
        self.title = "superhero"
        self.opening_info = { # Stage 1
            "prompt": "Welcome to the world of supernatural crime fighting. We have reports of a new up and coming villian who goes by the name _____. Who knows? One day you might be the one who has to take them down.",
            "option1": "Team Rocket Grunt", #Pokemon Gen 1 reference
            "option2": "Johnny Lawrence", #Karate Kid reference
            "option3": "Yoko Ono" #beatles reference
        }

        self.quit_info = { # Stage 2
            "prompt": "Your training is getting harder and harder. You are considering stopping your training and living out your days as the average citizen.",
            "option1": ["Continue training. With power comes responsibilty. You have an obligation to use you gift to help the world.", "You begin to work even harder with your trainer and are suprised to see that you are quickly improving."],
            "option2": ["Stop training. You didn't choose to be giving this power, and it shouldn't decide your destiny.", "You decide to quit training. For the next three years, you impatiently live out a life of mediocrity until your nemisis, "+self.personalization+", finds, and ends you."]
            }

        self.urgency_info = { # Stage 3
            "prompt": self.personalization+" has made their plans to attack the capital with a mob, public. Your trainer tells you that you are not yet ready to fight them yet and that the police will handle it. However, you are eager to prove yourself.",
            "option1": ["Trust your trainer. This is about saving as many lives as possible, which you won't be able to do if you rush into battle prematurely.", "You decide not to rush into battle. Instead, you wait anxiously, watching your trainer's promise fall shockingly short, as the police, seeming put under a spell by "+self.personalization+", allow the mob to go inside of the building. One person is critically injured. However, you know that there was nothing that you could do and you become even more motivated to battle"+self.personalization+", as the time of your battle quickly approaches."],
            "option2": ["Defend the capital. If you don't attack the public will lose faith in you and "+self.personalization+" could go unpunished.","You sneak out and fly to the capital. Upon arrival you are shocked to see that the police seem to be letting "+self.personalization+"'s mob into the building. You assume that they have been put under a spell by "+self.personalization+" and go and try to rescue them. You land in front of a cop to try to free him with no sucess. He attacks you and pushes you into the mob. You have failed."]
        }

        self.mg_info = { # Stage 4
            "prompt": "It is time for your battle. As you fly towards the buildings "+self.personalization+" plans to attack, you see thousands of birds flying towards you. The frequency of emitting from "+self.personalization+"'s bomb must have scared them. You are going to have to weave through to get to "+self.personalization+".",
            "obstacle": "birds",
            "crash": "crashed into a bird!",
            "lose": "One of the birds hits your left arm, disrumpting your flight. You spin down towards the town below you, smashing into the road. The frightened people around your crater yell as the birds come back for revenge. Better luck next time!",
            "win": "Nice job! You have skillfully weaved through the birds. Now, nothing stands between you and "+self.personalization+"."
        }

        self.win_info = { # Stage 5
            "prompt": "You soar towards,"+self.personalization+". All of your training has lead to this moment. The anger, the pain, and the helplessness you felt as you watched"+self.personalization+" attack the capitol, manifests in your out-stretched fist as it plunges into"+self.personalization+"'s face. You have won."
        }

        self.try_again_info = { # Stage 6
            "prompt": "You are celebrated as a hero every year during "+self.name+" appreciation day. After 10 years of peace, you begin to hear whispers of a new super villian. You are determined to reignite your crime-fighting career. You begin training immediately to get back in fighting shape and are suprised at how the years have changed your abilities. As you train, you hear a knock on the door. Standing outside is a little girl, about 15 years old by your estimate. She reveals that she has been given powers greater than you could imagine. She asks you to train her.",
            "option1": ["Train her. You had your time and she has the potential to be greater than you ever were. It does feel early but maybe it is time for you to turn in the towel.","You retire from crime-fighting and spend all of your time training your new apprentice. She is a fast learner, and is able to take down the new super villian before a single civilian is hurt. You take a liking to training and throughout your life train many super heros. You are given the name 'Mangum Magister' - the great teacher. Your name is held above all others every year on HERO appreciation day."],
            "option2": ["Reject her. You are the protecter of this city and that's the way it's gonna stay. Tell her that her powers are a disease and she should never use them again.","You reject her and resume your training. The battle is upon you and give it everything you got. As you stand over this new 'super' villian ready to deliver the final blow, you are grabbed by hidden figure and are thrown in handcuffs that weaken your powers. You watch as the girl you turned away helps up her new master and they tourment the city."]
        }

        self.retire_info={ # Stage 7
            "prompt": "Congradulations your selflessness and patience has lead to peace in the city, and peace within yourself. Good work, "+ self.name+"."
        }

class Engine:
    def __init__(self, user, stages={}):
        self.user = user
        self.current_stage = stages["opening"]
        self.stages = stages
        self.running = True
    def run(self):
        while self.running == True:
            self.next_stage = self.current_stage.play()
            self.current_stage = self.stages[self.next_stage]
            a = input("\n(press enter to continue your journey)\n") # buffer between stages
            clear() # clears the screen
            if self.next_stage == "end":
                self.running = False #stops the engine
        else:
            self.stages["end"].play()


class Text_Parser:
    def __init__(self):
        pass
    def define(self, stage_info, user_input):
        self.info = stage_info
        self.option1_text = self.info["option1"][0].lower()
        self.option2_text = self.info["option2"][0].lower()
        self.input = user_input.lower()
    def parse(self):
        if self.input == "1" or self.input == "2":
            return(self.input)
        else:
            self.option1_words = self.breakdown(self.option1_text)
            self.option2_words = self.breakdown(self.option2_text)
            self.input_words = self.breakdown(self.input)
            self.op1_tally = self.compare(self.option1_words, self.input_words)
            self.op2_tally = self.compare(self.option2_words, self.input_words)
            if self.op2_tally > self.op1_tally:
                return("2")
            elif self.op1_tally >self. op2_tally:
                return("1")
            else:
                return("0")
    def breakdown(self, text):
        self.words = text.split()
        return(self.words)
    def compare(self, words, inputwords):
        self.tally = 0
        for word in words:
            for inputword in inputwords:
                if word == inputword:
                    self.tally += 1
        return(int(self.tally))



class Stage: #Parent class for a typical stage
    def __init__(self, user, parser):
        self.user = user
        self.job = user.job
        self.parser = parser
    def play(self):
        self.info = self.define()
        self.prompt = self.info["prompt"]
        self.options = []
        self.options.append(self.info["option1"])
        self.options.append(self.info["option2"])
        choice = self.prompt_senario()
        self.parser.define(self.info, choice)
        parsed_choice = self.parser.parse()
        clear()
        if parsed_choice == "1":
            print(self.options[0][1]+space(5))
            return(self.next())
        elif parsed_choice == "2":
            print(self.options[1][1]+space(5))
            return('end')
        else:
            print("Please enter either keywords of the option that you would like to choose or the number to the left of it.")
            self.play()
    def prompt_senario(self):
        print(self.prompt+space(1))
        for i in range(len(self.options)):
            print("    ",i+1,":",self.options[i][0])
        print(space(1))
        choice = str(input("What option do you choose?"+space(3)+"   "))
        return(choice)
    def define(self):
        pass #returns info in dictionary
    def next(self):
        pass # directs to the new stage

class Opening(Stage):
    def play(self):

        return("quit")

class Quit(Stage):
    def define(self):
        return(self.job.quit_info)
    def next(self):
        return("urgency")

class Urgency(Stage):
    def define(self):
        return(self.job.urgency_info)
    def next(self):
        return("minigame")

class Minigame_Stage(Stage):
    def play (self):
        self.minigame = mg.Game(self.job)
        self.mg_result = self.minigame.run()
        if self.mg_result == True:
            return("win")
        else:
            return("end")

class Win(Stage):
    def play(self):
        self.info = self.define()
        self.prompt = self.info["prompt"]
        print(self.prompt)
        return(self.next())
    def define(self):
        return(self.job.win_info)
    def next(self):
        return("try_again")

class Try_Again(Stage):
    def define(self):
        return(self.job.try_again_info)
    def next(self):
        return("retire")


class Retire(Stage):
    def play(self):
        print(self.job.retire_info["prompt"])
        return(self.next())
    def next(self):
        return("end")

class End(Stage):
    def play(self):
        print("                                 GAME OVER")
        print(space(2))
        print("              Thank you for playing my Interactive Fiction Game."+space(2))
        choice = input("                 Would you like to play again? (yes or no)"+space(4)).lower()
        if choice == "yes":
            print("Good luck!")
            main()
        elif choice == "no":
            print("Ok! Bye Bye!")
        else:
            print('Please enter "yes" or "no"')
            self.play()


def space(number):
    string =""
    for i in range(number):
        string+="\n "
    return(string)
    
def clear():
    print(space(20))

def intro(user):
    clear()
    print("                  Welcome to My Interactive Fiction Project"+space(3))
    a = input("Please adjust your window dimensions so that this sentence all fits on one line."+space(3))
    print("Throughout this game you will embark on a journey. There are three paths that   you can take: an astronaut, a farmer, or a superhero. Regardless of the path youchoose, your adventure will be perilous. Good luck.\n")
    user.define()

def main():
    user = User()
    parser = Text_Parser()
    intro(user)
    stages={"opening":Opening(user, parser),"quit":Quit(user, parser),"urgency":Urgency(user, parser), "minigame":Minigame_Stage(user, parser), "win":Win(user, parser), "try_again":Try_Again(user, parser), "retire":Retire(user, parser), "end":End(user, parser)}
    engine = Engine(user, stages)
    engine.run()


main()
