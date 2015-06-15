from flask import Flask, render_template, request
from datetime import date
import random
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)

smash_chars = [
        ("Pummeluff", "pum.png"), ("Duck-Hunt-Duo", "dhd.png"), ("Mr. Game & Watch", "gaw.png"), ("Finsterer Pit", "dpt.png"),
        ("Ganondorf", "gdf.png"), ("R.O.B.", "rob.png"), ("Bowser Jr.", "bjr.png"), ("Dr. Mario", "dmr.png"), ("Wario", "wro.png"),
        ("Falco", "flo.png"), ("Ness", "nes.png"), ("Mewtu", "mwt.png"), ("Mario", "mro.png"), ("Kirby", "krb.png"),
        ("Pikachu", "pkc.png"), ("Fox", "fox.png"), ("Donkey Kong", "dko.png"), ("Link", "lnk.png"), ("Samus", "sms.png"),
        ("Yoshi", "ysh.png"), ("Luigi", "lgi.png"), ("Captain Falcon", "cpf.png"), ("Peach", "pch.png"), ("Bowser", "bws.png"),
        ("Zelda", "zld.png"), ("Shiek", "shk.png"), ("Marth", "mrt.png"), ("Meta-Knight", "mtk.png"), ("Pit", "pit.png"),
        ("Zero Suit Samus", "zss.png"), ("Ike", "ike.png"), ("Glurak", "glk.png"), ("Diddy Kong", "ddk.png"),
        ("König Dedede", "ddd.png"), ("Olimar", "olm.png"), ("Lucario", "lcr.png"), ("Toon-Link", "tlk.png"),
        ("Bewohner", "bwr.png"), ("Wii Fit-Trainerin", "wft.png"), ("Rosalina & Luma", "rul.png"), ("Little Mac", "lmc.png"),
        ("Quajutsu", "qjt.png"), ("Palutena", "plt.png"), ("Daraen", "drn.png"), ("Lucina", "lcn.png"), ("Shulk", "slk.png"),
        ("Sonic", "snc.png"), ("Mega Man", "mmn.png"), ("Pac-Man", "pac.png"), ("Mii-Kämpfer", "mii.png"), ("Ryu", "ryu.png"),
	("Roy", "roy.png"), ("Lucas", "lcs.png")
]

smash_attacks = [
	"Down Air", "Forward Air", "Back Air", "Up Air", "Neutral Air", "Down Tilt", "Side Tilt", "Up Tilt", "Jab", "Side Smash",
	"Up Smash", "Down Smash", "Neutral B", "Side B", "Up B", "Down B", "Up Throw", "Forward Throw", "Back Throw", "Down Throw",
	"Pummle",
]

@app.route('/')
def index():
	smash_chars_copy = smash_chars.copy()
	random.seed(str(date.today()))
	updated_at = str(date.today()) + " " + str(random.randint(3, 9)) + ":"
	minute = random.randint(1,59)
	if minute < 10:
		minute = "0" + str(minute)
	else:
		minute = str(minute)
	updated_at += minute
	random.shuffle(smash_chars_copy)
	return render_template("index.html", smash_chars=smash_chars_copy, updated_at=updated_at)

@app.route('/u/<name>/')
def user(name):
	if name == "kondou":
		smash_chars_copy = [
			("Shana", "drn.png", False), ("♫", "pum.png", True), ("R²", "gaw.png", False), ("SNES", "rob.png", False),
			("Flummi", "krb.png", True), ("Edison", "pkc.png", True), ("Hyperlink", "lnk.png", True), ("Fanservice", "zss.png", False),
			("Lucifer", "lcr.png", True), ("Luisa", "tlk.png", True), ("Hnnng~", "bwr.png", True), ("Alice", "rul.png", True),
			("Lilie", "lcn.png", True), ("Dr. Oetker", "pac.png", True), ("Goth Chick", "pch.png", True), ("Woow ;)", "ysh.png", True),
			("Pluls", "cpf.png", True), ("Ludwig", "roy.png", False)
		]
	elif name == "seijirou":
		smash_chars_copy = [
			("Tesla", "pkc.png", True), ("Negus", "ysh.png", True), ("Rasenmäher", "lnk.png", True), ("Dixie Kong", "ddk.png", True),
			("DonCamillo", "mro.png", True), ("Uguu~", "bwr.png", True), ("Lurio", "lcr.png", True), ("eNess", "nes.png", True),
			("NEIN!", "snc.png", False), ("Darän", "drn.png", False), ("Quark", "dhd.png", False), ("Demjanow", "wft.png", True),
			("Kackfrosch", "qjt.png", False), ("LUFTIG", "bjr.png", False), ("RickAstley", "glk.png", True), ("VOLLGAS", "bjr.png", False),
			("Gildenmais", "pum.png", False), ("Para-Nurse", "zss.png", False), ("Tenshi", "plt.png", False), ("Kühlregal", "lcs.png", False),
			("Nyancat", "mwt.png", False)
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
	random_attr = random.choice(["ausgezeichneten", "guten", "schlechten", "nicht vorhandenen"]) + " " + random.choice(["Gimp-Künsten", "Spot-Dodges", "Smashes", "Würfen", "SDs"])
	reflex = random.choice(["exzellenten", "schnellen", "guten", "langsamen", "slow-motion"])
	secret_weapon = random.choice(rating) + " " + random.choice(smash_attacks)
	return render_template("amiibo_detail.html", char=character, name=name, ranged=ranged, melee=melee, random_attr=random_attr, reflex=reflex, secret_weapon=secret_weapon)

@app.route('/real/')
def real():
	req = urllib.request.Request("http://www4.eventhubs.com/tiers/ssb4/")
	html = urllib.request.urlopen(req).read().decode("utf-8")
	soup = BeautifulSoup(html)
	tier_list = []
	for a in soup.find(id="tiers1").find_all("a"):
		if "Vote" not in a:
			if a.string == "Rosalina":
				tier_list.append(search_for("Rosalina & Luma"))
				continue
			elif a.string == "Sheik":
				tier_list.append(search_for("Shiek"))
				continue
			elif a.string == "Mewtwo":
				tier_list.append(search_for("Mewtu"))
				continue
			elif a.string == "Villager":
				tier_list.append(search_for("Bewohner"))
				continue
			elif a.string == "ROB":
				tier_list.append(search_for("R.O.B."))
				continue
			elif a.string == "Robin":
				tier_list.append(search_for("Daraen"))
				continue
			elif a.string == "Jigglypuff":
				tier_list.append(search_for("Pummeluff"))
				continue
			elif a.string == "Greninja":
				tier_list.append(search_for("Quajutsu"))
				continue
			elif a.string == "Wii Fit Trainer":
				tier_list.append(search_for("Wii Fit-Trainerin"))
				continue
			elif a.string == "Dark Pit":
				tier_list.append(search_for("Finsterer Pit"))
				continue
			elif a.string == "Toon Link":
				tier_list.append(search_for("Toon-Link"))
				continue
			elif a.string == "King Dedede":
				tier_list.append(search_for("König Dedede"))
				continue
			elif a.string == "Duckhunt":
				tier_list.append(search_for("Duck-Hunt-Duo"))
				continue
			elif a.string == "Mr. Game and Watch":
				tier_list.append(search_for("Mr. Game & Watch"))
				continue
			elif a.string == "Charizard":
				tier_list.append(search_for("Glurak"))
				continue
			elif a.string == "Meta Knight":
				tier_list.append(search_for("Meta-Knight"))
				continue
			else:
				for char in smash_chars:
					if char[0] == a.string:
						tier_list.append(char)
						continue
			print(a.string)

	tier_list.append(search_for("Mii-Kämpfer"))

	updated_at = str(date.today()) + " " + str(random.randint(3, 9)) + ":"
	minute = random.randint(1,59)
	if minute < 10:
		minute = "0" + str(minute)
	else:
		minute = str(minute)
	updated_at += minute
	return render_template("index.html", smash_chars=tier_list, updated_at=updated_at)

def search_for(name):
	for char in smash_chars:
		if char[0] == name:
			return char

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
