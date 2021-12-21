from flask import Flask, render_template
from datetime import date
import random

app = Flask(__name__)

smash_chars = [
    ("Pummeluff", "pum.webp"), ("Duck-Hunt-Duo", "dhd.webp"), ("Mr. Game & Watch", "gaw.webp"),
    ("Finsterer Pit", "dpt.webp"), ("Ganondorf", "gdf.webp"), ("R.O.B.", "rob.webp"), ("Bowser Jr.", "bjr.webp"),
    ("Dr. Mario", "dmr.webp"), ("Wario", "wro.webp"), ("Falco", "flo.webp"), ("Ness", "nes.webp"), ("Mewtu", "mwt.webp"),
    ("Mario", "mro.webp"), ("Kirby", "krb.webp"), ("Pikachu", "pkc.webp"), ("Fox", "fox.webp"), ("Donkey Kong", "dko.webp"),
    ("Link", "lnk.webp"), ("Samus", "sms.webp"), ("Yoshi", "ysh.webp"), ("Luigi", "lgi.webp"),
    ("Captain Falcon", "cpf.webp"), ("Peach", "pch.webp"), ("Bowser", "bws.webp"), ("Zelda", "zld.webp"),
    ("Shiek", "shk.webp"), ("Marth", "mrt.webp"), ("Meta-Knight", "mtk.webp"), ("Pit", "pit.webp"),
    ("Zero Suit Samus", "zss.webp"), ("Ike", "ike.webp"), ("Diddy Kong", "ddk.webp"), ("König Dedede", "ddd.webp"),
    ("Olimar", "olm.webp"), ("Lucario", "lcr.webp"), ("Toon-Link", "tlk.webp"), ("Bewohner", "bwr.webp"),
    ("Wii Fit-Trainerin", "wft.webp"), ("Rosalina & Luma", "rul.webp"), ("Little Mac", "lmc.webp"),
    ("Quajutsu", "qjt.webp"), ("Palutena", "plt.webp"), ("Daraen", "drn.webp"), ("Lucina", "lcn.webp"),
    ("Shulk", "slk.webp"), ("Sonic", "snc.webp"), ("Mega Man", "mmn.webp"), ("Pac-Man", "pac.webp"),
    ("Mii-Kämpfer", "mii.webp"), ("Ryu", "ryu.webp"), ("Roy", "roy.webp"), ("Lucas", "lcs.webp"), ("Corrin", "crr.webp"),
    ("Cloud", "cld.webp"), ("Bayonetta", "byn.webp"), ("Junger Link", "ylk.webp"), ("Pokémon Trainer", "pkm.webp"),
    ("Ice Climbers", "icl.webp"), ("Snake", "snk.webp"), ("Daisy", "dsy.webp"), ("Piranha Pflanze", "ppl.webp"),
    ("King K. Rool", "kkr.webp"), ("Ridley", "rdl.webp"), ("Dunkle Samus", "dsm.webp"), ("Fuegro", "icr.webp"),
    ("Chrom", "chr.webp"), ("Melinda", "isb.webp"), ("Wolf", "wlf.webp"), ("Inkling", "ikl.webp"), ("Ken", "ken.webp"),
    ("Simon", "smn.webp"), ("Richter", "rch.webp"), ("Pichu", "pcu.webp"), ("Joker", "jok.webp"), ("Held", "her.webp"),
    ("Banjo & Kazooie", "bak.webp"), ("Terry", "ter.webp"), ("Byleth", "byl.webp"), ("Sephiroth", "sph.webp"),
    ("Min Min", "min.webp"), ("Steve", "stv.webp"), ("Pyra", "pyr.webp"),
]
smash_attacks = [
    "Down Air", "Forward Air", "Back Air", "Up Air", "Neutral Air", "Down Tilt", "Side Tilt", "Up Tilt", "Jab",
    "Side Smash", "Up Smash", "Down Smash", "Neutral B", "Side B", "Up B", "Down B", "Up Throw", "Forward Throw",
    "Back Throw", "Down Throw", "Pummle",
]


@app.route('/')
def index():
    smash_chars_copy = smash_chars.copy()
    random.seed(str(date.today()))
    updated_at = str(date.today()) + " " + str(random.randint(3, 9)) + ":"
    minute = random.randint(1, 59)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    updated_at += minute
    random.shuffle(smash_chars_copy)
    return render_template("index.html", smash_chars=smash_chars_copy, updated_at=updated_at)


@app.route('/u/<name>/')
def user(name):
    if name == "niduroki":
        smash_chars_copy = [
            ("Shana", "drn.webp", True), ("♫", "pum.webp", True), ("R² c R³", "gaw.webp", True),
            ("Flummi", "krb.webp", True), ("Edison", "pkc.webp", True), ("Hyperlink", "lnk.webp", True),
            ("Hawkeye", "zss.webp", True), ("Lucifer", "lcr.webp", True), ("Luisa", "tlk.webp", True),
            ("Hnnng~", "bwr.webp", True), ("Alice", "rul.webp", True),
            ("Lilie", "lcn.webp", True), ("Dr. Oetker", "pac.webp", True), ("Goth Chick", "pch.webp", True),
            ("Woow ;)", "ysh.webp", True), ("Pluls", "cpf.webp", True), ("Mah Boy", "roy.webp", True),
            ("SmokeWeed", "ikl.webp", True), ("Mercer", "chr.webp", True), ("Fuffi", "isb.webp", True),
            ("Kaktus", "ppl.webp", True), ("HammerBros", "icl.webp", True), ("Hayter", "snk.webp", True),
        ]
    elif name == "seijirou":
        smash_chars_copy = [
            ("Tesla", "pkc.webp", True), ("Negus", "ysh.webp", True), ("Rasenmäher", "lnk.webp", True),
            ("Dixie Kong", "ddk.webp", True), ("DonCamillo", "mro.webp", True), ("Uguu~", "bwr.webp", True),
            ("Lurio", "lcr.webp", True), ("eNess", "nes.webp", True), ("NEIN!", "snc.webp", False),
            ("Darän", "drn.webp", False), ("Quark", "dhd.webp", False), ("Demjanow", "wft.webp", True),
            ("Kackfrosch", "qjt.webp", False), ("LUFTIG", "bjr.webp", False), ("RickAstley", "glk.webp", True),
            ("VOLLGAS", "bjr.webp", False), ("Gildenmais", "pum.webp", False), ("Para-Nurse", "zss.webp", False),
            ("Tenshi", "plt.webp", False), ("Kühlregal", "lcs.webp", False), ("Nyancat", "mwt.webp", False)
        ]
    else:
        return
    random.seed(str(date.today()))
    random.shuffle(smash_chars_copy)
    return render_template("user.html", smash_chars=smash_chars_copy)


@app.route('/<shortcut>/')
def detail(shortcut):
    character = None
    for char in smash_chars:
        if char[1][0:3] == shortcut:
            character = char
    if character is None:
        return 404

    random.seed(str(date.today())+character[0])
    smash_attacks_copy = smash_attacks.copy()
    random.shuffle(smash_attacks_copy)
    good_attacks = smash_attacks_copy[0:2]
    bad_attacks = smash_attacks_copy[2:4]
    taunt = random.choice(["Up Taunt", "Side Taunt", "Down Taunt"])
    return render_template("detail.html", char=character, good=good_attacks, bad=bad_attacks, taunt=taunt)


@app.route('/<shortcut>/<name>/')
def amiibo_detail(shortcut, name):
    character = None
    for char in smash_chars:
        if char[1][0:3] == shortcut:
            character = char
    if character is None:
        return 404

    random.seed(str(date.today())+shortcut+name)
    rating = ["unbesiegbarer", "starker", "guter", "mittelmäßiger", "schlechter", "mieser"]
    ranged = random.choice(rating)
    melee = random.choice(rating)
    random_attr = random.choice(["ausgezeichneten", "guten", "schlechten", "nicht vorhandenen"]) + " " + \
        random.choice(["Gimp-Künsten", "Spot-Dodges", "Smashes", "Würfen", "SDs", "Taunts"])
    reflex = random.choice(["exzellenten", "schnellen", "guten", "langsamen", "slow-motion"])
    secret_weapon = random.choice(rating) + " " + random.choice(smash_attacks)
    return render_template(
        "amiibo_detail.html", char=character, name=name, ranged=ranged, melee=melee, random_attr=random_attr,
        reflex=reflex, secret_weapon=secret_weapon
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
