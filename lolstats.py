from riotwatcher import LolWatcher, ApiError
import sys

def full_stats(champ_info):
    
    print("Enter champion name: ")
    name = str(input())
    
    try:
        champ_info = champions_list.get(name)
    except  AttributeError:
        sys.exit("Wrong Name")

    
    print('\t\t'+str(champ_info.get('id')) +' '+str(champ_info.get('title')) )
    version = champ_info.get('version')
    info = champ_info.get('info')
    
    image = champ_info.get('image')
    print("Tags: " + str(champ_info.get('tags')))
    tags = champ_info.get('tags')

    #stats to variables
    base_stats= champ_info.get('stats')
    hp = base_stats.get('hp')
    print("Base HP: " +str(hp))
    hpper_lvl = base_stats.get('hpperlevel')
    print("HP per level: " +str(hpper_lvl))
    mpperlevel=base_stats.get('mpperlevel')


    mp = base_stats.get('mp')
    print("Base MP: " +str(mp) +'\nMP per level : ' + str(mpperlevel) )
    movespeed =base_stats.get('movespeed')
    print("Base movespeed: " + str(movespeed))
    armorperlevel =base_stats.get('armorperlevel')
    print("Armor per level:" + str(armorperlevel))
    spellblock=base_stats.get('spellblock')
    spellblockperlevel=base_stats.get('spellblockperlevel')
    print("Base spell block: " + str(spellblock))
    print("Spell block per level: " + str(spellblockperlevel))
    attackrange=base_stats.get('attackrange')
    hpregen =base_stats.get('hpregen')
    hpregenperlevel = base_stats.get('hpregenperlevel')
    mpregen =base_stats.get('mpregen')
    print("Attack range: " +str(attackrange) + '\nBase HP regen: ' + str(hpregen) + '\nHP regen per level: ' + str(hpregen))
    mpregenperlevel = base_stats.get('mpregenperlevel')
    print("MP regen: " + str(mpregen)+'\nMP regen epr level: ' + str(mpregenperlevel))
    crit=base_stats.get('crit')
    critperlevel =base_stats.get('critperlevel')
    print("Critical Strike: " + str(crit) + '\nCritical Strike per level: ' + str(critperlevel))
    attackdamage = base_stats.get('attackdamage ')
    attackdamageperlevel=base_stats.get('attackdamageperlevel')
    print('Attack Damage: ' + str(attackdamage) + '\nAttack Damage per level: ' + str(attackdamageperlevel))
    attackspeedperlevel=base_stats.get('attackspeedperlevel')
    attackspeed=base_stats.get('attackspeed')
    print('Attack Speed: ' + str(attackspeed) + '\nAttack Speed per level: ' + str(attackspeedperlevel))

def champ_list(champ_info):

    count = len(champions_list.keys())
    
    for key in range(0,count-1):
        name = list(champions_list.keys())[key]
        print(name)
    
 



# golbal variables
api_key = "RGAPI-xxxxxx"
watcher = LolWatcher(api_key)
my_region = 'na1'



latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
#full champion list
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
item_list = watcher.data_dragon.items(latest,'en_US')

champions_list = static_champ_list.get('data')
#random champion for initialization of champ_info list
champ_info = champions_list.get('Draven')

print('(1)Stats for champion\n(2)Latest champion list')
user_input = int(input())
if user_input == 1:
    full_stats(champ_info)
elif user_input ==2:
    champ_list(champ_info)






