# Scene
image bg airport = im.Scale("scene_airport.jpg", 1920, 1080)
image bg school = im.Scale("scene_school.jpg", 1920, 1080)
image bg hero_room = im.Scale("scene_hero_room.jpg", 1920, 1080)
image bg maksim_room = im.Scale("scene_maksim_room.jpg", 1920, 1080)
image bg rest_room = im.Scale("scene_rest_room.jpg", 1920, 1080)
image bg kitchen_room = im.Scale("scene_kitchen_room.jpg", 1920, 1080)
image bg bath_room = im.Scale("scene_bathroom.jpg", 1920, 1080)

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

# Sushi

# Aya

# Radeon

# Alex

# Nadejda

# audio
# play sound "audio/airport_sound.mp3"
# play sound "audio/car_alert_sound.mp3"
# play sound "audio/car_onmove_sound.mp3"
# play sound "audio/close_bagspot_sound_sound.mp3"
label start:
    play music "audio/airport_sound.mp3"
    scene bg airport with fade
    "....."
    "Где эта аболтуска..."
    "Вылетела первой из самолёта и убежала..."
    "Кто вообще так делает."
    "......."
    show maks fck with dissolve
    "И кого ты аболтуской назвал?"
    "Тебя."
    "Хм."
    show maks neitral with dissolve
    "И вообще Максим ты в чужой стране, веди себя как леди..."
    Maksim "От кого я это слышу? А, братец"
    "Вы" "В любом случае нам ждёт такси, идём."

    hide maks neitral with dissolve
    hide bg airport with fade
    stop music
    play sound "audio/car_onmove_sound.mp3"

    "Я был слишком усталым и даже непомню как мы загрузились и поехали, но этот звук езды..."
    "Как же я люблю этот звук, почему то он даёт чувство спокойствия."
    "Наверное, я могу ещё подрем..."

    stop sound
    play sound "audio/close_bagspot_sound_sound.mp3"
    play sound "audio/car_alert_sound.mp3"

    show maks confused with dissolve
    "Вставай, АЛЁ ОЛЕНЬ"
    "НУ ЖЕ ВСТАВАЙ"
    show maks smile with dissolve
    "ТЫ ПРОПУСТИШЬ КРАСИВУЮ МИЛФУ НА ВХОДЕ"
    "Вы" "Максим успокойся, меня этим не разбудить"
    Maksim "И тем неменее ты мне ответил."

    hide maks smile with dissolve
    stop sound

    "Как же хреново что родители заставили меня за двоюродной сестрой приглядывать, от баб одни проблемы."
    Maksim "Чё ты недовольный такой?"
    "Вы" "Что?"
    Maksim "Говорю, чё мина кислая то? Сосал?"
    "Вы" "Да, я уста... Ты в край охренела?"
    Maksim "Да ладно успокойся, яж любя."
    
    scene bg school with fade
    show maks neitral with dissolve
    Maksim "...."
    "Вы" "Что случилось?"
    Maksim "У нашего кампуса ворота?"
    show maks smile with dissolve
    "Вы" "А как ты хотела, изсходя из нашей работы, мы на охраняемой территории."
    Maksim "Понятненько."
    "Вы" "Идём"

    hide maks smile with dissolve
    scene bg rest_room with fade

    Maksim "А у нас красивый номер."
    "Вы" "Есть такое."
    Maksim "Я посмотрю свою комнату."
    "Вы" "Ок. Я пойду умоюсь и руки заодно помою."
    Maksim "Хорошо"

    scene bg bath_room with fade
    "..."
    "Поидее нам предстоит познакомится с пациентами"
    "Вы" "Как же зовут опекаемую.."
    "Вы" "Арина? Арианна? Ари.."
    Maksim "Твой пациент Ариель."
    "Вы" "Да, точно, спасибо."
    "Вы" "Я немного устал, пойду отдохну"
    Maksim "Давай, давай."

    scene bg hero_room with fade
    "А у меня неплохая комната"
    "Вздремну пожалуй чу-чуть"    