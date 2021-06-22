import sys
import getopt
import fontforge


def exitsusage():
    sys.exit(f"usage: {argv[0]} -p <patchfile> -i <infile> -o <ofile>")

patchedchars = "+-*/\|^=;:',.~_[]{}()"
argv = sys.argv
opts,args = getopt.getopt(argv[1:], "hp:i:o:", [])

pfile = ""
infile = ""
outfile = ""
for opt,arg in opts:
    if opt == "-h":
        exitsusage();
    elif opt == "-p":
        pfile = arg
    elif opt == "-i":
        infile = arg
    elif opt == "-o":
        outfile = arg

if pfile == "" or infile == "" or outfile == "":
    exitsusage()
pfont = fontforge.open(pfile)
infont = fontforge.open(infile)

for c in patchedchars:
    pfont.selection.select(("more",None), c)
    infont.selection.select(("more",None), c)

pfont.copy()
infont.paste()
infont.fontname = "azukifont"
infont.generate(outfile, "ttf")
