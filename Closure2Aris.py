import json
import time
import os
import sys

CharacterClub = {
    "shiroko": "Foreclosure Task Force",
    "hoshino": "Foreclosure Task Force",
    "serika": "Foreclosure Task Force",
    "nonomi": "Foreclosure Task Force",
    "ayane": "Foreclosure Task Force",
    "prefect-team-member": "Prefect Team",
    "hina": "Prefect Team",
    "iori": "Prefect Team",
    "ako": "Prefect Team",
    "chinatsu": "Prefect Team",
    "mutsuki": "Problem Solver 68",
    "haruka": "Problem Solver 68",
    "kayoko": "Problem Solver 68",
    "aru": "Problem Solver 68",
    "izumi": "Gourmet Research Society",
    "junko": "Gourmet Research Society",
    "akari": "Gourmet Research Society",
    "haruna": "Gourmet Research Society",
    "makoto": "Pandemonium Society",
    "iroha": "Pandemonium Society",
    "ibuki": "Pandemonium Society",
    "satsuki": "Pandemonium Society",
    "pandemonium-member": "Pandemonium Society",
    "fuuka": "School Lunch Club",
    "juri": "School Lunch Club",
    "kasumi": "Hot Springs Department",
    "megu": "Hot Springs Department",
    "development member": "Hot Springs Department",
    "sena": "Emergency Medical Club",
    "medicine member": "Emergency Medical Club",
    "elika": "Go-Home Club",
    "kilala": "Go-Home Club",
    "arius-student": "Arius Squad",
    "akane": "Cleaning & Clearing",
    "neru": "Cleaning & Clearing",
    "asuna": "Cleaning & Clearing",
    "karin": "Cleaning & Clearing",
    "toki": "Cleaning & Clearing",
    "aris": "Game Development Department",
    "key": "Game Development Department",
    "momoi": "Game Development Department",
    "midori": "Game Development Department",
    "yuzu": "Game Development Department",
    "himari": "Veritas",
    "hare": "Veritas",
    "kotama": "Veritas",
    "chihiro": "Veritas",
    "maki": "Veritas",
    "hibiki": "Engineering Club",
    "utaha": "Engineering Club",
    "kotori": "Engineering Club",
    "utahaturret": "Engineering Club",
    "rio": "Seminar",
    "yuuka": "Seminar",
    "koyuki": "Seminar",
    "noa": "Seminar",
    "eimi": "Super Phenomenon Task Force",
    "sumire": "Athletics Training Club",
    "natsu": "After-School Sweets Club",
    "yoshimi": "After-School Sweets Club",
    "airi": "After-School Sweets Club",
    "kazusa": "After-School Sweets Club",
    "teaparty": "Tea Party",
    "mika": "Tea Party",
    "seia": "Tea Party",
    "nagisa": "Tea Party",
    "azusa": "Make-Up Work Club",
    "koharu": "Make-Up Work Club",
    "hifumi": "Make-Up Work Club",
    "hanako": "Make-Up Work Club",
    "justice-task-force-member": "Justice Task Force",
    "mashiro": "Justice Task Force",
    "tsurugi": "Justice Task Force",
    "hasumi": "Justice Task Force",
    "ichika": "Justice Task Force",
    "sisterhood": "Sisterhood",
    "hinata": "Sisterhood",
    "mari": "Sisterhood",
    "sakurako": "Sisterhood",
    "serina": "Remedial Knights",
    "hanae": "Remedial Knights",
    "mine": "Remedial Knights",
    "shimiko": "Library Committee",
    "ui": "Library Committee",
    "suzumi": "Trinity's Vigilante Crew",
    "reisa": "Trinity's Vigilante Crew",
    "pina": "Festival Operations Department",
    "shizuko": "Festival Operations Department",
    "umika": "Festival Operations Department",
    "mimori": "Inner Discipline Club",
    "tsubaki": "Inner Discipline Club",
    "kaede": "Inner Discipline Club",
    "chise": "Yin-Yang Club",
    "niya": "Yin-Yang Club",
    "kaho": "Yin-Yang Club",
    "izuna": "忍术研究部",
    "michiru": "忍术研究部",
    "tsukuyo": "忍术研究部",
    "hatsune-miku": "???",
    "kanna": "Public Peace Bureau",
    "miria": "???",
    "nao": "???",
    "rone": "???",
    "yukari": "???",
    "francis": "???",
    "anubis": "???",
    "???": "???",
    "the-nameless-priests": "???",
    "akira": "???",
    "kuzunoha": "百花缭乱纷争调停委员会",
    "nagusa": "百花缭乱纷争调停委员会",
    "kissaki": "Genryumon",
    "mina": "Genryumon",
    "genryumon-member": "Genryumon",
    "saya": "Eastern Alchemy Society",
    "rumi": "Black Tortoise Promenade",
    "reizo": "Black Tortoise Promenade",
    "genbu-shokai-employee": "Black Tortoise Promenade",
    "shun": "Plum Blossom Garden",
    "kokona": "Plum Blossom Garden",
    "cherino": "Red Winter Office",
    "tomoe": "Red Winter Office",
    "marina": "Red Winter Office",
    "member-of-the-ss": "Red Winter Office",
    "shigure": "Spec Ops No. 227",
    "nodoka": "Spec Ops No. 227",
    "meru": "Knowledge Liberation Front",
    "momiji": "Knowledge Liberation Front",
    "minori": "Labor Party",
    "construction-department-member": "Labor Party",
    "kirino": "Public Safety Bureau",
    "fubuki": "Public Safety Bureau",
    "saki": "RABBIT Squad",
    "miyako": "RABBIT Squad",
    "miyu": "RABBIT Squad",
    "moe": "RABBIT Squad",
    "yukino": "FOX Platoon",
    "niko": "FOX Platoon",
    "otogi": "FOX Platoon",
    "kurumi": "FOX Platoon",
    "saori": "Arius Squad",
    "atsuko": "Arius Squad",
    "hiyori": "Arius Squad",
    "misaki": "Arius Squad",
    "president": "General Student Council",
    "rin": "General Student Council",
    "momoka": "General Student Council",
    "ayumu": "General Student Council",
    "kaya": "General Student Council",
    "aoi": "General Student Council",
    "student-council-officer": "General Student Council",
    "mai": "Kronos School of Journalism",
    "shinon": "Kronos School of Journalism",
    "bunnygirl-guard": "Golden Fleece Cruise",
    "black-suit": "Gematria",
    "golconde": "Gematria",
    "décalcomanie": "Gematria",
    "maestro": "Gematria",
    "beatrice": "Gematria",
    "perorozilla": "无限怪谈图书馆",
    "automata": "黑龟组",
    "goro": "黑龟组",
    "thugs": "看门人",
    "hod": "十字神名",
    "chesed": "十字神名",
    "binah": "十字神名",
    "peroro-sama": "Momo Friends",
    "nyantenmaru": "百鬼夜行商店街",
    "shiro": "Slumpia",
    "kuro": "Slumpia",
    "goz": "Slumpia",
    "kivotos-citizen": "Citizen",
    "android": "Citizen",
    "shibaseki-master": "Shiba Seki",
    "sora": "Angel 24",
    "chimi-ichiza": "魑魅一座・路上流",
    "kaiser-pmc-director": "Kaiser PMC",
    "kaiser-pmc-general": "Kaiser PMC",
    "kaiser-president": "Kaiser PMC",
    "kaiser-sof": "Kaiser PMC",
    "kaiten-fx-mk.0": "凯坦泽",
    "kaitenranger": "凯坦泽",
    "helmet-gang": "Helmet Gang",
    "rabu": "Helmet Gang",
    "hieronymus": "诸圣相通",
    "frenapates": "色彩",
    "yongha": "蔚蓝档案",
    "arona": "Shittim Chest",
    "plana": "Shittim Chest",
    "sensei": "S.C.H.A.L.E."
}

CharacterName = {
    "shiroko": "Shiroko",
    "hoshino": "Hoshino",
    "serika": "Serika",
    "nonomi": "Nonomi",
    "ayane": "Ayane",
    "prefect-team-member": "Prefect Team Member",
    "hina": "Hina",
    "iori": "Iori",
    "ako": "Ako",
    "chinatsu": "Chinatsu",
    "mutsuki": "Mutsuki"
    "haruka": "Haruka",
    "kayoko": "Kayoko",
    "aru": "Aru",
    "izumi": "Izumi",
    "junko": "Junko",
    "akari": "Akari",
    "haruna": "Haruna",
    "makoto": "Makoto",
    "iroha": "Iroha",
    "ibuki": "Ibuki",
    "satsuki": "Satsuki",
    "pandemonium-member": "Pandemonium Society Member",
    "fuuka": "Fuuka",
    "juri": "Juri",
    "kasumi": "Kasumi",
    "megu": "Megu",
    "development member": "Hot Springs Development Member",
    "sena": "冰室 濑名",
    "medicine member": "Emergency Medicine Club Member",
    "elika": "Erika",
    "kilala": "Kirara",
    "gehenna-student": "Gehenna Student",
    "akane": "Akane",
    "neru": "Neru",
    "asuna": "Asuna",
    "karin": "Karin",
    "toki": "Toki",
    "aris": "Aris",
    "key": "Key",
    "momoi": "Momoi",
    "midori": "Midori",
    "yuzu": "Yuzu",
    "himari": "Himari",
    "hare": "Hare",
    "kotama": "Kotama",
    "chihiro": "Chihiro",
    "maki": "Maki",
    "hibiki": "Hibiki",
    "utaha": "Utaha",
    "kotori": "Kotori",
    "utahaturret": "Turret",
    "rio": "Rio",
    "yuuka": "Yuuka",
    "koyuki": "Koyuki",
    "noa": "Noa",
    "eimi": "Eimi",
    "sumire": "Sumire",
    "millennium-student": "Millenium Student",
    "natsu": "Natsu",
    "yoshimi": "Yoshimi",
    "airi": "Airi",
    "kazusa": "Kazusa",
    "teaparty": "Tea Party Member",
    "mika": "Mika",
    "seia": "Seia",
    "nagisa": "Nagisa",
    "azusa": "Azusa",
    "koharu": "Koharu",
    "hifumi": "Hifumi",
    "hanako": "Hanako",
    "justice-task-force-member": "Justice Task Force Member",
    "mashiro": "Mashiro",
    "tsurugi": "Tsurugi",
    "hasumi": "Hasumi",
    "ichika": "Ichika",
    "sisterhood": "Sisterhood Member",
    "hinata": "Hinata",
    "mari": "Mari",
    "sakurako": "Sakurako",
    "serina": "Serina",
    "hanae": "Hanae",
    "mine": "Mine",
    "shimiko": "Shimiko",
    "ui": "Ui",
    "suzumi": "Suzumi",
    "reisa": "Reisa",
    "trinity-student": "Trinity Student",
    "pina": "Pina",
    "shizuko": "Shizuko",
    "umika": "Umika",
    "mimori": "Mimori",
    "tsubaki": "Tsubaki",
    "kaede": "Kaede",
    "chise": "Chise",
    "niya": "Niya",
    "kaho": "Kaho",
    "izuna": "Izuna",
    "michiru": "Michiru",
    "tsukuyo": "Tsukuyo",
    "wakamo": "Wakamo",
    "kuzunoha": "Kuzunoha",
    "nagusa": "Nagusa",
    "kissaki": "Kisaki",
    "mina": "Mina",
    "genryumon-member": "Genryumon",
    "saya": "Saya",
    "rumi": "Rumi",
    "reizo": "Reijo",
    "genbu-shokai-employee": "Black Tortoise Promenade Member",
    "shun": "Shun",
    "kokona": "Kokona",
    "pei": "支付",
    "kai": "Kai",
    "cherino": "Cherino",
    "tomoe": "Tomoe",
    "marina": "Marina",
    "member-of-the-ss": "Red Winter Office Member",
    "shigure": "Shigure",
    "nodoka": "Nodoka",
    "meru": "Meru",
    "momiji": "Momiji",
    "minori": "Minori",
    "construction-department-member": "Labor Party Member",
    "kirino": "Kirino",
    "fubuki": "Fubuki",
    "kanna": "Kanna",
    "valkyrie-student": "Valkyrie Student",
    "saki": "Saki",
    "miyako": "Miyako",
    "miyu": "Miyu",
    "moe": "Moe",
    "yukino": "Yukino",
    "niko": "Niko",
    "otogi": "Otogi",
    "kurumi": "Kurumi",
    "saori": "Saori",
    "atsuko": "Atsuko",
    "hiyori": "Hiyori",
    "misaki": "Misaki",
    "arius-student": "Arius Student",
    "president": "GSC President",
    "rin": "Rin",
    "momoka": "Momoka",
    "ayumu": "Ayumu",
    "kaya": "Kaya",
    "aoi": "Aoi",
    "student-council-officer": "Student Council Member",
    "mai": "Mai",
    "shinon": "Shinon",
    "bunnygirl-guard": "Bunny Girl",
    "black-suit": "Black Suit",
    "golconde": "Golconde",
    "décalcomanie": "Decalcomanie",
    "maestro": "Maestro",
    "beatrice": "Beatrice",
    "perorozilla": "Perorodzilla",
    "automata": "Automata",
    "goro": "Kamejima Goro",
    "thugs": "看门人",
    "hod": "Hod",
    "chesed": "Chesed",
    "binah": "Binah",
    "peroro-sama": "Peroro",
    "nyantenmaru": "Nyantenmaru",
    "shiro": "Shiro",
    "kuro": "Kuro",
    "goz": "Goz",
    "kivotos-citizen": "Kivotos Citizen",
    "android": "Android",
    "shibaseki-master": "Shiba Seki Master",
    "sora": "Sora",
    "chimi-ichiza": "二流魅剧团",
    "kaiser-pmc-director": "Kaiser PMC Director",
    "kaiser-pmc-general": "Kaiser PMC General",
    "kaiser-president": "Kaiser President",
    "kaiser-sof": "Kaiser SOF",
    "kaiten-fx-mk.0": "KAITEN-FX-Mk.0",
    "kaitenranger": "Kaiten Ranger",
    "helmet-gang": "Helmet Gang",
    "rabu": "Rabu",
    "hieronymus": "Hieronymus",
    "hatsune-miku": "Hatsune Miku",
    "miria": "米莉亚",
    "nao": "纳奥",
    "rone": "罗内",
    "yukari": "Yukari",
    "francis": "Francis",
    "anubis": "阿努比斯",
    "???": "???",
    "the-nameless-priests": "Nameless Priest",
    "akira": "Akira",
    "frenapates": "Phrenapates",
    "yongha": "龙河",
    "arona": "Arona",
    "plana": "Plana",
    "sensei": "Sensei"
}

if hasattr(sys, 'frozen'):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(application_path)

txt = ""

print("在Windows系统自带终端中，把文件拖入终端会自带引号，请务必去掉。")
print("拖入终端后按回车，如果空着则直接按回车。")
InputPath = input("Input ClosureTalk.json file path >>")
OutputPath = input("Input path to txt file. Ensure that the txt file is empty. It will create a new version of this file. >>")

# Delete " symbol

if InputPath[-1] == '"':
    InputPath = InputPath.split('"')[1]

if OutputPath:
    if OutputPath[-1] == '"':
        OutputPath = OutputPath.split('"')[1]
    

with open(InputPath,'r',encoding='utf-8') as f:
    Talk = json.loads(f.read())

# Processing data

ChatList = Talk["chat"]

CharacterList = []

for Chr in Talk["chars"]:
    if Chr['img'].lower() in CharacterName:
        CharacterList.append(Chr['img'].lower())
    else:
        CharacterName[Chr['char_id']] = Chr['char_id']
        CharacterClub[Chr['char_id']] = ""
        CharacterList.append(Chr['char_id'])
        print("检测到自创角色或者不支持的角色，由于格式限制将名字转换为{}，头像为{}".format(Chr["char_id"], Chr['img']))


# Loading spring

for Chr in CharacterList:

    # If character isn't custom

    if Chr[:6] != "custom":
        txt = txt + "load spr {} {}".format(Chr, Chr+"_spr") + "\n"

txt += "load end\n"

# Adding chats
 
state = ''

ChoiceState = 0

for Chat in ChatList:

    # If type = text
    
    if Chat['yuzutalk']['type'] == "TEXT":

        if "img" in Chat:

            # If character isn't custom
            # Skip showing the spring

            if Chat['img'] != "uploaded":

                Name = Chat["img"].lower()

                if state == Name:
                    pass
                else:

                    # Let character hide then show if previous character isn't same

                    if state != '':
                        txt += "spr hide {}\n".format(state)

                    txt += "spr show {}\n".format(Name)
                state = Name

            else:
                Name = Chat["char_id"]
                
            content = Chat["content"].split("\n")
            
            for text in content:

                # Iterate by every return, cuz there's a bug on showing \n in aris studio
                # Student chat in chinese <Name> <Club>

                txt = txt + "txt '{}' '{}' '{}'\n".format(CharacterName[Name],CharacterClub[Name],text)
            
        else:

            # Use button to show sensei's chat
            # Every choice must follow a taget
            # Target <> is the event number after pressing button
            # I use self-add int

            content = Chat["content"].split("\n")

            for text in content:
                txt += "button '{}' '{}'\n".format(text,str(ChoiceState))

            txt += "target {}\n".format(str(ChoiceState))
            ChoiceState += 1

            # Not change if sensei say sth

        # Use \n for every part

        txt += '\n'

    # If type = narration

    elif Chat['yuzutalk']['type'] == "NARRATION":

        # Add chat with no name
        # Easiest one
        content = Chat["content"].split("\n")
        for text in content:
            txt += "txt '' '' '{}'".format(text)
            txt += '\n'

    # Choice
    elif Chat['yuzutalk']['type'] == "CHOICES":

        # In ClosureTalk, Choice is splited by \n
        # Iterate in content to add each choice
        # Every choice is point to one event

        content = Chat["content"].split("\n")
        txt += "button"
        for text in content:
            txt = txt + " '{}' '{}'".format(text,str(ChoiceState))
        txt += "\ntarget {}".format(str(ChoiceState))
        ChoiceState += 1
        txt += "\n"

    else:
        pass

# Save by time

if OutputPath:
    with open("{}ArisStudio-{}.txt".format(OutputPath,time.strftime("%Y-%m-%d-%H-%M",time.gmtime())),'w',encoding='utf-8') as file:
        file.write(txt)
else:
    with open("ArisStudio-{}.txt".format(time.strftime("%Y-%m-%d-%H-%M",time.gmtime())),'w',encoding='utf-8') as file:
        file.write(txt)

print("转换完毕")
time.sleep(3)

# 防止有人看不到转换结果所以加了个 sleep 3

# 因为懒所以没做函数封装(被打)
