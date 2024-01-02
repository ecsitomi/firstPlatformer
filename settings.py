FPS=60
BG_COLOR=(255,255,255)
BG_IMAGE='img/BG.png'

level_map = [ #pálya szerkezete string listában
  '                            ',
  '                            ',
  '                            ',
  '          np                ',
  '                            ',
  '     noop                   ',
  '                            ',
  'op           noop           ',
  '                            ',
  'bbbbbbc    abbc   ac  abc   ',
  'eeeeeef   aheejc  df  dejc  ']

tile_size=64 #csempek szélessége/magassága pixelben

WIDTH=1200
HEIGHT=len(level_map)*tile_size #pálya magassága (sorok a listában) * a pixel számmal