{"filter":false,"title":"net-charge.py","tooltip":"/net-charge.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":29},"action":"insert","lines":["# Python3.6  ","# Coding: utf-8  ","# Store the human preproinsulin sequence in a variable called preproinsulin:  ","preproInsulin = \"malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn\"  ","# Store the remaining sequence elements of human insulin in variables:  ","lsInsulin = \"malwmrllpllallalwgpdpaaa\"  ","bInsulin = \"fvnqhlcgshlvealylvcgergffytpkt\"  ","aInsulin = \"giveqcctsicslyqlenycn\"  ","cInsulin = \"rreaedlqvgqvelgggpgagslqplalegslqkr\"  ","insulin = bInsulin + aInsulin"],"id":35}],[{"start":{"row":9,"column":29},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["pKR = {}"],"id":37}],[{"start":{"row":11,"column":7},"end":{"row":11,"column":18},"action":"insert","lines":["'y': 10.07,"],"id":38}],[{"start":{"row":11,"column":19},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":75},"action":"insert","lines":["'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}"],"id":40}],[{"start":{"row":11,"column":74},"end":{"row":11,"column":75},"action":"remove","lines":["}"],"id":41}],[{"start":{"row":11,"column":75},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":42}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":43}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":18},"action":"insert","lines":["insulin.count(\"Y\")"],"id":44}],[{"start":{"row":13,"column":18},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":18},"action":"remove","lines":["insulin.count(\"Y\")"],"id":46},{"start":{"row":13,"column":0},"end":{"row":13,"column":25},"action":"insert","lines":["float(insulin.count(\"Y\"))"]}],[{"start":{"row":13,"column":25},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":48},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":80},"action":"insert","lines":["seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})"],"id":49}],[{"start":{"row":15,"column":80},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":50},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":6},"action":"insert","lines":["pH = 0"],"id":51}],[{"start":{"row":17,"column":6},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":17},"action":"insert","lines":["while (pH <= 14):"],"id":53}],[{"start":{"row":19,"column":17},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":24,"column":43},"action":"insert","lines":["netCharge = (","    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \\","    for x in ['k','h','r']}.values()))","    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \\","    for x in ['y','c','d','e']}.values())))"],"id":55}],[{"start":{"row":24,"column":43},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":56},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":57},{"start":{"row":24,"column":43},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":43},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":59}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":60}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":38},"action":"insert","lines":["print('{0:.2f}'.format(pH), netCharge)"],"id":61}],[{"start":{"row":26,"column":38},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":62},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":63},{"start":{"row":24,"column":43},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":43},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":64},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":25,"column":42},"end":{"row":26,"column":0},"action":"remove","lines":["",""],"id":65}],[{"start":{"row":25,"column":42},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":66},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":10},"action":"insert","lines":["pH +=1"],"id":67}],[{"start":{"row":26,"column":10},"end":{"row":27,"column":0},"action":"remove","lines":["",""],"id":68}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":26,"column":10},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":37,"mode":"ace/mode/python"}},"timestamp":1696557572816,"hash":"722b95c63adfecae5a1ec31491304b6efef866e3"}