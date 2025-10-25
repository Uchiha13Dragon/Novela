image bg hole = im.Scale("bg_hole.png", 1920, 1080)
image bg bedroom = im.Scale("bg_bedroom.png", 1920, 1080)
image bg kitchen = im.Scale("bg_kitchen.png", 1920, 1080)
image bg rest_room = im.Scale("bg_rest_room.png", 1920, 1080)
image bg toilet = im.Scale("bg_toilet.png", 1920, 1080)

# Ariel
image ariel happy = im.Scale("ariel_happy.png", 700, 1000)
image ariel alert = im.Scale("ariel_alert.png", 700, 1000)
image ariel angry = im.Scale("ariel_angry.png", 700, 1000)
image ariel confused = im.Scale("ariel_confused.png", 700, 1000)
image ariel cry = im.Scale("ariel_cry.png", 700, 1000)
image ariel neitral = im.Scale("ariel_neitral.png", 700, 1000)
image ariel omedeto = im.Scale("ariel_omedeto.png", 1000, 1000)
image ariel please = im.Scale("ariel_please.png", 700, 1000)
image ariel sad = im.Scale("ariel_sad.png", 700, 1000)
image ariel shy = im.Scale("ariel_shy.png", 700, 1000)
define Ariel = Character("Ariel", color = "#ff6200")

# Liliya
image liliya happy = im.Scale("liliya_happy.png", 700, 1000)
image liliya angry = im.Scale("liliya_angry.png", 700, 1000)
image liliya confused = im.Scale("liliya_confused.png", 700, 1000)
image liliya cry = im.Scale("liliya_cry.png", 700, 1000)
image liliya neitral = im.Scale("liliya_neitral.png", 700, 1000)
image liliya sad = im.Scale("liliya_sad.png", 700, 1000)
image liliya shy = im.Scale("liliya_shy.png", 700, 1000)
define Liliya = Character("Liliya", color = "#ffffff")

# Lilit
image lilit happy = im.Scale("lilit_happy.png", 700, 1000)
image lilit angry = im.Scale("lilit_angry.png", 700, 1000)
image lilit cry = im.Scale("lilit_cry.png", 700, 1000)
image lilit neitral = im.Scale("lilit_neitral.png", 700, 1000)
image lilit sad = im.Scale("lilit_sad.png", 700, 1000)
image lilit shy = im.Scale("lilit_shy.png", 700, 1000)
image lilit withoutMakeUp = im.Scale("lilit_withoutMakeUp.png", 700, 1000)
define Lilit = Character("Lilit", color = "#b6b6b6")

# Shaya
image shaya happy = im.Scale("shaya_happy.png", 700, 1000)
image shaya angry = im.Scale("shaya_angry.png", 700, 1000)
image shaya confused = im.Scale("shaya_confused.png", 700, 1000)
image shaya cry = im.Scale("shaya_cry.png", 700, 1000)
image shaya neitral = im.Scale("shaya_neitral.png", 700, 1000)
image shaya sad = im.Scale("shaya_sad.png", 700, 1000)
image shaya shy = im.Scale("shaya_shy.png", 700, 1000)
define Shaya = Character("Shaya", color = "#ff0000")

# Maks
image maks happy = im.Scale("maks_happy.png", 700, 1000)
image maks smile = im.Scale("maks_smile.png", 700, 1000)
image maks happySmile = im.Scale("maks_happy_smile.png", 700, 1000)
image maks confused = im.Scale("maks_confused.png", 700, 1000)
image maks cry = im.Scale("maks_cry.png", 700, 1000)
image maks neitral = im.Scale("maks_neitral.png", 700, 1000)
image maks fck = im.Scale("maks_fck.png", 700, 1000)
image maks sad = im.Scale("maks_sad.png", 700, 1000)
image maks shy = im.Scale("maks_shy.png", 700, 1000)
define Maksim = Character("Maksim", color = "#00f3aa")


label start:
    scene bg bedroom
    show ariel happy at center
    with fade
    Ariel "Добро пожаловать на альфа тест игры"
    Ariel "Знакомьтесь с нашим составом"

    show liliya happy at left
    with dissolve
    Ariel "Лилия"

    show lilit happy at right
    with dissolve
    Ariel "Лилит"

    hide liliya happy
    hide lilit happy

    show shaya happy at left
    with dissolve
    Ariel "Шая"

    show maks happy at right
    with dissolve
    Ariel "Максим"