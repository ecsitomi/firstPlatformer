FPS=60 #képfrissítés per másodperc
BG_COLOR=(255,255,255) #háttérszín
DESERT=(220,165,40)
RED=(100,30,50)
BG_IMAGE='img/BG.png' #háttérkép

tile_size=64 #csempek szélessége/magassága pixelben

#pálya szerkezete string listában
level_map = [
{'data': [
    '                                                        ',
    '                                                        ',
    '          T2                          T2                ',
    '          np                          np                ',
    '    C135EC                      C135EC                  ',
    '     noop                        noop                   ',
    '1T          CE1E45TC        1T          CE1E45TC        ',
    'np           noooop         np           noooop         ',
    '431P25T    232    2T  322T1C431E25TC   232    2T  322T1 ',
    'abbbbbc   2abbcT  ac  abbbc abbbbbc   2abbcT  ac  abbbc ',
    'deeeeef   aheejc  df  deeejcdeeeeef   aheejc  df  deeejc'
]},
{'data': [
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '                                                        ',
    '431P25T    232    2T  322T1C431E25TC   232    2T  322T1 ',
    'abbbbbc   2abbcT  ac  abbbc abbbbbc   2abbcT  ac  abbbc ',
    'deeeeef   aheejc  df  deeejcdeeeeef   aheejc  df  deeejc'
]}
]


"""
  terrain: a-p
  cactus: 1
  plant: 2
  rock: 3
  skeleton: 4
  tree: 5
  crate: T
  player: P
  enemy: E
"""

others = { #különböző pályaelemek kódjai
'1': 'cactus',
'2': 'plant',
'3': 'rock',
'4': 'skeleton',
'5': 'tree'
}  

WIDTH=1200 #képernyő szélessége
HEIGHT=len(level_map[0]['data'])*tile_size #pálya magassága (sorok a listában) * a pixel számmal