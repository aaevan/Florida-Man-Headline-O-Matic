from random import choice
from random import seed
from time import sleep

def florida_man(adjectives, verbs, subjects, action):
    seed()
    adjective = choice(adjectives)
    seed()
    verb = choice(verbs)
    seed()
    subject = choice(subjects)
    seed()
    action = choice(action)
    if action != "":
        if len(adjective) > 0:
            print("%s Florida man %s %s then %s." % (adjective, verb, subject, action))
        else:
            print("Florida man %s %s then %s." % (verb, subject, action))
    else:
        if len(adjective) > 0:
            print("%s Florida man %s %s." % (adjective, verb, subject))
        else:
            print("Florida man %s %s." % (verb, subject))


def main():
    adjectives = ["Irate", "Timid", "Postmodern", "Quintessential", "Flummoxed", "Vivacious", "Bespectacled", "Leery", "Squeemish", "Hateful", "Deeply punchable", "Slutty", "Cowardly", "Enraged", "Confused", "Perplexed", "Quotidian", "Exhausted", "Drunk", "Inebriated", "Plastered", "Sky high", "Intoxicated", "Indesposed", "Foppish", "Wet", "Tyrannical", "pompous", "Inept", "Surburban", "Middle-aged", "Unemployed", "Terrified", "Unhinged", "Hungry", "Barking", "Thirsty", "Vegan", "Elderly", "Lecherous", "Constipated", "Clinically insane", "Deaf and blind", "Courteous", "Gobsmacked", "Handsome", "Filthy", "Anorexic", "Bleeding", "Dying", "Sleep walking", "One-legged", "Incomprehensible", "Racist", "Homophobic", "Vomit stained", "Bearded", "Obese", "Morbidly obese", "Bedridden", "Quadrupalegic", "Obsessive compulsive", "Shifty eyed", "Axe wielding", "Inbred", "Genius", "Hoodie wearing", "Meth making", "Triumphant", "Hooded", "Unknown", "Invisible", "Sadistic", "Masochistic", "Deeply ashamed", "Senile", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",]
    verbs = ["hits", "destroys", "maims", "forgets", "punches", "kicks", "licks", "envelopes", "screams at", "attempts to marry", "violates", "crushes", "breaks", "paints", "hides", "steals", "redecorates", "cauterizes", "burns", "weeps upon", "sideswipes", "contemplates", "devours", "swindles", "flummoxes", "reinvigorates", "arouses", "repurposes", "freezes", "kisses", "slaps", "remembers", "unleashes", "escapes", "serenades", "gazes longingly at", "shoots", "enthusiastically sniffs", "forms religion surrounding", "gets trapped by", "is impaled by", "impersonates", "dresses up as", "attempts to replace", "robs", "burgles", "murders", "steals", "loots", "defecates upon", "forcefully massages", "totals", "attempts to mesmerize", "willfilly disobeys", "disembowels", "drains blood from", "casts Tommy Wiseau as", "overturns", "razes", "seduces", "suggestively rubs", "rides", "fails to seduce", "fails to impress", "mounts", "attempts to eat", "sleeps through", "accidentally injests", "injests", "fancies", "sexually harasses", "gets fired", "performs CPR on", "pistol whips", "incapacitates", "ties up", "verbally abuses", "elopes with", "claims ownership of"]
    subjects = ["his car", "the neighbor's cat", "John Travolta", "midsize sedan", "80 year-old man", "pack of wolves", "pirate ship", "darth vader cosplayer", "darth vader", "James K Polk", "Cast of friends", "Sleeping Kangaroo", "Brefuddled Giraffe", "percolator", "1970's ford station wagon", "chocolate rabbit", "spider man street performer", "frightened rabbit", "pile of fish", "box of scraps", "Joss Whedon", "vacuum cleaner", "himself", "shopping cart", "poker table", "picnic table", "elevator shaft", "escalator", "power scooter", "segway", "hang glider", "world's best gramma", "world's largest cookie", "marionette", "ventriloquist's dummy", "priceless work of art", "tickle me elmo", "man dressed as Mr. Peanut", "the mechanical shark from Jaws", "Bruce lee", "International Pop star Katy Perry", "High school marching band", "depressed samurai", "Masquerade party", "Middle school performance of Henry VIII", "Governor Rick Scott", "Trebuchet", "Pillsbury dough boy", "Chatrolette", "stubborn grey hound", "field of dandelions", "newly formed sinkhole", "starwars themed Danceoff", "Are you Afraid of the Dark", "violent misogynist", "Nicolas Cage", "world war II era tractor", "Senator Marco Rubio", "chainmail bikini", "baywatch theme wedding", "a 6 gallon tub of butter", "personal lubricant", "Lois CK complete DVD collection", "civil war reenactors", "moonshine distillery", "cathedral", "porcelain statuette", "alligator", "Steven King", "Harry Potter fan"]
    actions = ["flees", "commits arson", "removes clothing", "claims innocence", "cries openly", "converts to mormonism", "ejaculates", "smashes television", "sings Ave Maria", "searches for purpose", "recants", "falls asleep", "vomits", "infiltrates zoo", "slashes tires", "uncovers lost civilization", "flees on horseback", "flees on cow-back", "piggy back rides police captain", "wins lottery", "wins at life", "dies from heart attack", "combusts", "dies mysteriously", "vanishes into the night", "becomes a cat", "severs own hand", "goes to McDonalds", "fakes own death", "wins eating contest", "trashes bar", "walks away bitter for it", "kills alligator", "marries alligator", "creates children's TV show", "swims to cuba", "totally rocks it", "cuts own hair", "embraces santeria", "watches simpsons reruns", "adopts child", "donates liver", "reenacts entirety of Farscape", "huffs glue", "writes novel about it", "urinates uncontrollably", "defecates uncontrollably", "forgets how to speak", "takes vow of silence", "attempts to vote twice", "attempts to vote for herman cain", "swears he isn't racist", "claims he isn't a vampire", "falls asleep amongst cold cuts", "spends night in bakery", "dies on toilet", "embarks on heroic journey", "discovers and forgets cure for cancer", "reads anarchists literature", "quietly departs", "is never seen again", "demands to see Kurt Vonnegut", "demands retrial", "photographs women covertly", "basks in subsequent fame", "aquires book deal", "goes on book tour", "joins cast of soap opera", "gets reality tv show", "signs NDA", "places 3rd on Dances With the Stars", "crashes neighborhood pools", "skinny dips", "bends reality", "delivers impromptu yet inspiring speech", "wins American Idol", "arouses public suspicion", "crashes airplane", "crashes car", "crashes forklift", "murders family dog", "changes name to Cat Stevens", "gets facial tattoo", "steals candy from child", "obviates the inscrutable", "plots sister-in-law's murder", "plots own death", "visits grandfather's grave", "cackles maniacally", "drinks gasoline", "", "", "", "", "", "", "", "", "", "",]

    while(1):
        florida_man(adjectives, verbs, subjects, actions)
        sleep(3)
if __name__ == "__main__":
    main()


