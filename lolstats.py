from riotwatcher import LolWatcher, ApiError
import sys

def item_stat_print(user_input):
    item_list = static_item_list.get('data')


    items_id = ['1001', '1004', '1006', '1011', '1018', '1026', '1027', '1028', '1029', '1031', '1033', '1035', 
    '1036', '1037', '1038', '1039', '1042', '1043', '1052', '1053', '1054', '1055', '1056', '1057', '1058', '1082', 
    '1083', '2003', '2010', '2015', '2031', '2033', '2051', '2052', '2055', '2065', '2138', '2139', '2140', '2403',
    '2419', '2420', '2421', '2422', '2423', '2424', '3001', '3003', '3004', '3006', '3009', '3011', '3020', '3024', '3026', 
    '3031', '3033', '3035', '3036', '3040', '3041', '3042', '3044', '3046', '3047', '3050', '3051', '3053', '3057', '3065', '3066',
    '3067', '3068', '3070', '3071', '3072', '3074', '3075', '3076', '3077', '3078', '3082', '3083', '3085', '3086', '3089', '3091',
    '3094', '3095', '3100', '3102', '3105', '3107', '3108', '3109', '3110', '3111', '3112', '3113', '3114', '3115', '3116', '3117', 
    '3123', '3124', '3133', '3134', '3135', '3139', '3140', '3142', '3143', '3145', '3152', '3153', '3155', '3156', '3157', '3158',
    '3165', '3177', '3179', '3181', '3184', '3190', '3191', '3193', '3211', '3222', '3330', '3340', '3363', '3364', '3400', '3504', '3508',
    '3513', '3599', '3600', '3742', '3748', '3801', '3802', '3814', '3850', '3851', '3853', '3854', '3855', '3857', '3858', '3859', 
    '3860', '3862', '3863', '3864', '3916', '4005', '4401', '4403', '4628', '4629', '4630', '4632', '4633', '4635', '4636', '4637',
    '4638', '4641', '4642', '4643', '6029', '6035', '6333', '6609', '6616', '6617', '6630', '6691', '6692', '6693', '6694', '6695',
    '7000', '7001', '7002', '7003', '7004', '7005', '7006', '7007', '7008', '7009', '7010', '7011', '7012', '7013', '7014', '7015', 
    '7016', '7017', '7018', '7019', '7020', '7021', '7022']

    if user_input==4:  
            print("Enter item's name:")
            items_name = str(input())

    length = len(items_id)
    for i in range(0,length):
        item_info = item_list.get(items_id[i])
        name = item_info.get('name')
        description = item_info.get('descriptrion')
        gold = item_info.get('gold')
        gold_total = gold.get('total')
        sell_for = gold.get('sell')
        plain_text = item_info.get('plaintext')
        into = item_info.get('into')
        stats = item_info.get('stats')

        if user_input==3: 
            print(name)

        
           
        if items_name == name :
            print(name)      
            print("Total gold: " + str(gold_total))
            print("Sell for : "+str(sell_for))
            print(plain_text)
            print('\n'.join("{}: {}".format(k, v) for k, v in stats.items()))
            print('\n')



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
api_key = "RGAPI-xxxx"
watcher = LolWatcher(api_key)
my_region = 'na1'



latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
#full champion list
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')
static_item_list = watcher.data_dragon.items(latest,'en_US')


champions_list = static_champ_list.get('data')
champ_info = champions_list.get('Draven')

print('(1)Stats for champion\n(2)Latest champion list\n(3)Print latest item list\n(4)Look up items stats\nPlease enter your choise: ')
user_input = int(input())

if user_input == 1:
    full_stats(champ_info)
elif user_input ==2:
    champ_list(champ_info)
elif user_input==3 or user_input==4:
    item_stat_print(user_input)







