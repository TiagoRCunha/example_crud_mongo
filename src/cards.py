# this function creates 23310 cards
def cardsDic():
    copa_names = ["Lionel Messi", "Neymar Junior", "Cristiano Ronaldo", "Neymar Junior"]
    
    pokemon_names = [ "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
    "squirtle", "wartortle", "blastoise", "caterpie", "metapod", "butterfree", "weedle" "kakuna",
    "beedrill", "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate", "spearow", "fearow", "ekans",
    "arbok", "pikachu", "raichu", "sandshrew", "sandslash", "nidoran-f", "nidorina", "nidoqueen",
    "nidoran-m", "nidorino", "nidoking", "clefairy", "clefable", "vulpix", "ninetales", "jigglypuff",
    "wigglytuff", "zubat", "golbat", "oddish", "gloom", "vileplume", "paras", "parasect", "venonat",
    "venomoth", "diglett", "dugtrio", "meowth", "persian", "psyduck", "golduck", "mankey", "primeape",
    "growlithe", "arcanine", "poliwag", "poliwhirl", "poliwrath", "abra", "kadabra", "alakazam",
    "machop", "machoke", "machamp", "bellsprout", "weepinbell", "victreebel", "tentacool", "tentacruel",
    "geodude", "graveler", "golem", "ponyta", "rapidash", "slowpoke", "slowbro", "magnemite", "magneton",
    "farfetchd", "doduo", "dodrio", "seel", "dewgong", "grimer", "muk", "shellder", "cloyster", "gastly",
    "haunter", "gengar", "onix", "drowzee", "hypno", "krabby", "kingler", "voltorb", "electrode",
    "exeggcute", "exeggutor", "cubone", "marowak", "hitmonlee", "hitmonchan", "lickitung", "koffing",
    "weezing", "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan", "horsea", "seadra", "goldeen",
    "seaking", "staryu", "starmie", "mr-mime", "scyther", "jynx", "electabuzz", "magmar", "pinsir",
    "tauros", "magikarp", "gyarados", "lapras", "ditto", "eevee", "vaporeon", "jolteon", "flareon",
    "porygon", "omanyte", "omastar", "kabuto", "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos",
    "moltres", "dratini", "dragonair", "dragonite", "mewtwo", "mew", "chikorita", "bayleef", "meganium",
    "cyndaquil", "quilava", "typhlosion", "totodile", "croconaw", "feraligatr", "sentret", "furret",
    "hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados", "crobat", "chinchou", "lanturn",
    "pichu", "cleffa", "igglybuff", "togepi", "togetic", "natu", "xatu", "mareep", "flaaffy", "ampharos",
    "bellossom", "marill", "azumarill", "sudowoodo", "politoed", "hoppip", "skiploom", "jumpluff", "aipom",
    "sunkern", "sunflora", "yanma", "wooper", "quagsire", "espeon", "umbreon", "murkrow", "slowking",
    "misdreavus", "unown", "wobbuffet", "girafarig", "pineco", "forretress", "dunsparce", "gligar", "steelix",
    "snubbull", "granbull", "qwilfish", "scizor", "shuckle", "heracross", "sneasel", "teddiursa", "ursaring",
    "slugma", "magcargo", "swinub", "piloswine", "corsola", "remoraid", "octillery", "delibird", "mantine",
    "skarmory", "houndour", "houndoom", "kingdra", "phanpy", "donphan", "porygon2", "stantler", "smeargle",
    "tyrogue", "hitmontop", "smoochum", "elekid", "magby", "miltank", "blissey", "raikou", "entei", "suicune",
    "larvitar", "pupitar", "tyranitar", "lugia", "ho-oh", "celebi", "treecko", "grovyle", "sceptile", "torchic",
    "combusken", "blaziken", "mudkip", "marshtomp", "swampert"]
    
    harry_names = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Draco Malfoy", "Minerva McGonagall",
    "Cedric Diggory", "Cho Chang", "Severus Snape", "Rubeus Hagrid", "Neville Longbottom", "Luna Lovegood", "Ginny Weasley",
    "Sirius Black", "Remus Lupin", "Arthur Weasley", "Bellatrix Lestrange", "Lord Voldemort", "Horace Slughorn",
    "Kingsley Shacklebolt", "Dolores Umbridge", "Lucius Malfoy", "Vincent Crabbe", "Gregory Goyle", "Mrs Norris",
    "Argus Filch", "Vernon Dursley", "Petunia Dursley", "Dudley Dursley", "Lily Potter", "James Potter", "Albus Dumbledore",
    "Madam Pomfrey", "Mrs Figg", "Marge Dursley", "Yvonne", "Piers Polkiss", "Dennis", "Malcolm", "Gordon",
    "Miranda Gaushawk", "Bathilda Bagshot", "Adalbert Waffling", "Emeric Switch", "Phyllida Spore", "Arsenius Jigger", "Newt Scamander",
    "Quentin Trimble", "Tom", "Doris Crockford", "Quirinus Quirrel", "Griphook", "Madam Malkin", "Vindictus Viridian", "Garrick Ollivander",
    "Hedwig", "Molly Weasley", "Percy Weasley", "Fred Weasley", "George Weasley", "Lee Jordan", "Bill Weasley", "Charlie Weasley",
    "Fat Friar", "Peeves", "Hannah Abbott", "Susan Bones", "Terry Boot", "Mandy Brocklehurst", "Lavender Brown",
    "Millicent Bulstrode", "Justin Finch-Fletchley", "Seamus Finnegan", "Morag MacDougal", "Lily Moon", "Theodore Nott", "Pansy Parkinson",
    "Parvati Patil", "Padma Patil", "Sally-Anne Perks", "Lisa Turpin", "Blaise Zabini", "Nearly Headless Nick", "Bloody Baron", "Fat Lady",
    "Pomona Sprout", "Cuthbert Binns", "Emeric the Evil", "Uric the Oddball", "Filius Flitwick", "Madam Hooch", "Oliver Wood", "Gregory the Smarmy",
    "Wizard Baruffio", "Angelina Johnson", "Marcus Flint", "Alicia Spinet", "Katie Bell", "Adrian Pucey", "Miles Bletchley",
    "Terrence Higgs", "Fluffy", "Nicolas Flamel", "Gellert Grindelwald", "Norberta", "Ronan", "Bane", "Firenze", "Elfrick the Eager", "Perenelle Flamel",
    "Bertie Bott", "Dobby", "Mr Mason", "Mrs Mason", "Perkins", "Celestina Warbeck", "Gilderoy Lockhart", "Mundungus Fletcher",
    "Mr Borgin", "Mr Granger", "Mrs Granger", "Dr Filibuster", "Colin Creevey", "Gladys Gudgeon", "Veronica Smethley",
    "Patrick Delaney-Podmore", "Z. Nettles", "D.J. Prod", "Elsie Prod", "Moaning Myrtle", "Godric Gryffindor", "Rowena Ravenclaw",
    "Helga Hufflepuff", "Salazar Slytherin", "Madame Pince", "Milicent Bullstroude", "Ernie Macmillan", "Armando Dippet", "Penelope Clearwater", "Cornelius Fudge",
    "Aragog", "Mosag", "Stanley Shunpike", "Ernest Prang", "Madam Marsh", "Florean Fortescue", "Sir Cadogan", "Sybill Trelawney", "Buckbeak",
    "Peter Pettigrew", "Madam Rosmerta", "Derek", "Septima Vector", "Cassius Warrington", "Graham Montague", "Peregrine Derrick", "Lucian Bole",
    "Walden Macnair", "Franc Bryce", "Dot", "Bertha Jorkins", "Barty Crouch", "Ludo Bagman", "Amos Diggory", "Mr Roberts",
    "Mr Payne", "Basil", "Archie Aymslowe", "Cuthbert Mockridge", "Gilbert Wimple", "Arnold Peasegood", "Broderick Bode", "Saul Croaker", "Ali Bashir", "Victor Krum",
    "Winky", "Narcissa Malfoy", "Vasily Dimitrov", "Clara Ivanova", "Lev Zograf", "Alexei Levski", "Pyotr Vulchanov",
    "Ivan Volkov", "Connolly", "Barry Ryan", "Troy", "Mullet", "Moran", "Quigley", "Aidan Lynch", "Hassan Mostafa",
    "Dennis Creevey", "Aurora Sinistra", "Stewart Ackerley", "Malcolm Baddock", "Eleanor Branstone", "Owen Cauldwell", "Emma Dobbs", "Laura Madley", "Natalie McDonald", "Graham Pritchard",
    "Orla Quirke", "Kevin Whitby", "Eloise Midgen", "Alastor Moody", "Madame Maxime", "Igor Karkaroff", "Poliakoff", "Fawcett", "Summers",
    "Fleur Delacour", "Gregorovic", "Rita Skeeter", "Stebbins", "Wilhelmina Grubbly-Plank", "Bozo", "Evan Rosier", "Wilkes", "Avery",
    "Antonin Dolohov", "Travers", "Marlene McKinnon", "Mulciber", "Augustus Rookwood", "Frank Longbottom", "Alice Longbottom", "Violet",
    "Apollyon Pringle", "Ogg", "Mafalda Hopkirk", "Nymphadora Tonks", "Elphias Doge", "Dedalus Diggle", "Sturgis Podmore", "Hestia Jones", "Ragnok", "Alphard Black", "Regulus Black",
    "Phineas Nigelus Black", "Araminta Meliflua Black", "Elladora Black", "Andromeda Tonks", "Ted Tonks", "Rodolphus Lestrange",
    "Rabastan Lestrange", "Eric Munch", "Bob", "Bengie Fenwick", "Edgar Bones", "Amelia Bones", "Caradoc Dearborn", "Gideon Prewett",
    "Fabian Prewett", "Aberforth Dumbledore", "Dorcas Meadowes", "Algie Longbottom", "Anthony Goldstein", "Stubby Boardman", "Doris Purkiss",
    "Euan Abercrombie", "Rose Zeller", "Patricia Stimpson", "Kenneth Towler", "Vicky Frobisher", "Geoffrey Hooper", "Cassandra Trelawney",
    "Michael Corner", "Zacharias Smith", "Barnabas the Barmy", "Karkus", "Golgomath", "Fridwulfa", "Andrew Kirke", "Jack Sloper", "Everard",
    "Dilys Derwent", "Hippocrates Smethwyck", "Augustus Pye", "Urquhart Rackharrow", "Willy Widdershins", "Agnes", "Miriam Strout",
    "Madam Puddifoot", "Summerby", "Marietta Edgecombe", "Madam Edgecombe", "John Dawlish", "Bradley", "Roger Davies", "Grawp", "Griselda Marchbanks",
    "Eddie Carmichael", "Daphne Greengrass", "Tofty", "Tiberius Ogden", "Pierre Bonaccord", "Stubby Boardman", "Magorian", "Emmeline Vance", "Herbert Chorley",
    "Rufus Scrimgeour", "Corban Yaxley", "Fenrir Greyback", "Dirk Cresswell", "Barnabas Cuffe", "Ambrosius Flume", "Gwenog Jones", "Arkie Philpott",
    "Verity", "Romilda Vane", "Cormac McLaggen", "Marcus Belby", "Damocles Belby", "Tiberius", "Bertie Higgs", "Proudfoot", "Savage",
    "Humphrey Belcher", "Bob Ogden", "Morfin Gaunt", "Marvolo Gaunt", "Merope Gaunt", "Cecilia", "Tom Riddle", "Demelza Robins", "Jimmy Peakes",
    "Ritchie Coote", "Melinda Bobbin", "Leanne", "Caractacus Burke", "Billy Stubbs", "Amy Benson", "Dennis Bishop", "Mrs Cole", "Eric Whalley",
    "Vaisey", "Harper", "Urquhart", "Eldred Worple", "Sangwini", "Gawain Robards", "Fergus", "Wilkie Twycross", "Cadwallader", "Galatea Merrythought", "Hepzibah Smith",
    "Hokey", "Octavius Pepper", "Bertram Aubrey", "Eileen Prince", "Amycus Carrow", "Alecto Carrow", "Gibbon", "Tobias Snape", "Pius Thicknesse",
    "Charity Burbage", "Percival Dumbledore", "Kendra Dumbledore", "Ariana Dumbledore", "Betty Braithwaite", "Apolline Delacour", "Gabrielle Delacour", "Monsieur Delacour",
    "Dragomir Gorgovitch", "Xenophilius Lovegood", "Muriel", "Bilius", "Thorfinn Rowle", "Reg Cattermole", "Albert Runcorn", "Arkie Alderton", "Mary Cattermole",
    "Maisie Cattermole", "Ellie Cattermole", "Alfred Cattermole", "Gornuk", "Bowman Wright", "Ivor Dillonsby", "Enid Smeek", "Egbert the Egregious",
    "Godelot", "Hereward", "Loxias", "Barnabas Deverill", "Arcus", "Livius", "Antioch Peverell", "Cadmus Peverell", "Ignotus Peverell",
    "Selwyn", "Scabior", "Ragnuk the First", "Ted Lupin", "Marius", "Bogrod", "The Grey Lady", "Dexter Fortescue", "Lily Potter",
    "James Potter", "Albus Severus Potter", "Rose Weasley", "Hugo Weasley", "Scorpius Malfoy", "Victoire Weasley"]
    
    border_types = ["red","write","blue","yellow","transparent"]
    
    background_types = ["red","write","blue","yellow","transparent", "green", "black"]
    
    copa_dict_vector = []
    pokemon_dict_vector = []
    harry_dict_vector = []
    count = 0
    for x in range(len(copa_names)):
        for y in range(len(border_types)):
            for z in range(len(background_types)):
                count += 1
                copa_dict_vector.append({
                    "number": count,
                    "image": copa_names[x].replace(" ", "_").lower() + ".png",
                    "name": copa_names[x],
                    "background": "background_" + background_types[z] + ".png",
                    "border": "border_" + border_types[y] + ".png",
                    "rarity": x,
                    "album": "Copa do Mundo 2022"
                    })
    count = 0
    for x in range(len(pokemon_names)):
        for y in range(len(border_types)):
            for z in range(len(background_types)):
                count += 1
                pokemon_dict_vector.append({
                    "number": count,
                    "image": pokemon_names[x].replace(" ", "_").lower() + ".png",
                    "name": pokemon_names[x],
                    "background": "background_" + background_types[z] + ".png",
                    "border": "border_" + border_types[y] + ".png",
                    "rarity": x,
                    "album": "Pokemon"
                    })
    count = 0
    for x in range(len(harry_names)):
        for y in range(len(border_types)):
            for z in range(len(background_types)):
                count += 1
                harry_dict_vector.append({
                    "number": count,
                    "image": harry_names[x].replace(" ", "_").lower() + ".png",
                    "name": harry_names[x],
                    "background": "background_" + background_types[z] + ".png",
                    "border": "border_" + border_types[y] + ".png",
                    "rarity": x,
                    "album": "Harry Potter"
                    })
    return [copa_dict_vector, pokemon_dict_vector, harry_dict_vector]