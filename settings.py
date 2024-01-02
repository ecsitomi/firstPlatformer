FPS=60 #képfrissítés per másodperc
BG_COLOR=(255,255,255) #háttérszín
BG_IMAGE='img/BG.png' #háttérkép

level_map = [ #pálya szerkezete string listában
  '                                                        ',
  '                                                        ',
  '                                                        ',
  '          np                          np                ',
  '                                                        ',
  '     noop                        noop                   ',
  '                                                        ',
  'op           noop           op           noop           ',
  ' P                                                      ',
  'bbbbbbc    abbc   ac  abc   bbbbbbc    abbc   ac  abc   ',
  'eeeeeef   aheejc  df  dejc  eeeeeef   aheejc  df  dejc  ']

tile_size=64 #csempek szélessége/magassága pixelben

WIDTH=1200
HEIGHT=len(level_map)*tile_size #pálya magassága (sorok a listában) * a pixel számmal