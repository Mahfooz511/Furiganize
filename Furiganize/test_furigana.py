import pykakasi.kakasi as kakasi 

kakasi = kakasi() 
kakasi.setMode("H","a") # default: Hiragana no convert 
kakasi.setMode("K","a") # default: Katakana no convert 
kakasi.setMode("J","a") # default: Japanese no convert 
kakasi.setMode("E","a") # default: Symbols no convert 
kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table 
kakasi.setMode("s", True) # separate, default: no Separator 
kakasi.setMode("C", True) # capitalize default: no Capitalize 
conv = kakasi.getConverter() 
result = conv.do('澱んだ街角で僕らは出会った') 