{"filter":false,"title":"jsonFileHandler.py","tooltip":"/jsonFileHandler.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["import json","","def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data","    ",""],"id":5}],[{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"remove","lines":["",""],"id":6},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":9,"column":15},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":9,"column":15},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1696638729547,"hash":"90c7c775e5ad173f1e75e558c64b4e27a488ccc5"}