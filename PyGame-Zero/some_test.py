
import matplotlib.font_manager as fontman

def findFontFile(searchFont):
    fList = fontman.findSystemFonts(fontpaths=None, fontext='ttf')
    targetFont = []
    for row in fList:
        try:
            if searchFont in row:
                targetFont.append(row)
        except TypeError:
            pass
    return targetFont[0]

findFontFile("Calibri.tff")