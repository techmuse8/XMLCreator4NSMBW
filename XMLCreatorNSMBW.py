import sys

def ask(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

xmlName=str(input("Name your xml file (.xml will be automatically added to the file name"))
f=open(xmlName+".xml", "w")

sectionName=str(input("What is your mod name? (Short name) [Section name]"))
optionName=str(input("What will be the message that will show up in Riivolution on the mod's page? [Option name]"))
choiceName=str(input("What will be shown when the mod is enabled? [Choice name]"))
folderName=str(input("What is your mod's folder name? (For example \"nsmbwtest\")"))

saveGame="Yes"
noDoubles=0
saveGameCustom=ask("Does your mod use a custom save file?")
Stage=ask("Does your mod use the Stage folder?")
USEUJP=ask("Does your mod use the US/EU/JP folder?")
Object=ask("Does your mod use the Object folder?")
Sound=ask("Does your mod use the Sound folder?")
Layout=ask("Does your mod use the Layout folder?")
WorldMap=ask("Does your mod use the WorldMap folder?")
Env=ask("Does your mod use the Env folder?")
Effect=ask("Does your mod use the Effect folder?")
Replay=ask("Does your mod use the Replay folder?")
rels=ask("Does your mod use the rels folder?")
MovieDemo=ask("Does your mod use the MovieDemo folder?")
HomeButton2=ask("Does your mod use the HomeButton2 folder?")

f.write("<!-- XML created by XMLCreator4NSMBW -->\n<wiidisc version=\"1\">\n    <id game=\"SMN\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"W\"/>\n       <region type=\"K\"/>\n    <options>\n")
f.write("       <section name=\""+sectionName+"\">\n")
f.write("           <option name=\""+optionName+"\">\n")
f.write("               <choice name=\""+choiceName+"\">\n")
f.write("                   <patch id=\""+sectionName+"\"/>\n")
f.write("               </choice>\n           </option>\n       </section>\n    </options>\n")
f.write("    <patch id=\""+sectionName+"\" root=\"/"+folderName+"\">\n")

if saveGameCustom:
    f.write("        <savegame external=\"save/{$__gameid}{$__region}\" clone=\"false\"/>\n")
if Stage:
    f.write("        <folder external=\"Stage\" disc=\"/Stage\" create=\"true\"/>\n        <folder external=\"Stage/Texture\" disc=\"/Stage/Texture\" create=\"true\" />\n") 
if USEUJP:
    f.write("        <folder external=\"US\" disc=\"/US\" create=\"true\"/>\n        <folder external=\"EU\" disc=\"/EU\" create=\"true\" />\n        <folder external=\"JP\" disc=\"/JP\" create=\"true\" />\n")
if Object:
    f.write("        <folder external=\"Object\" disc=\"/Object\" create=\"true\"/>\n")
if Sound:
    f.write("        <folder external=\"Sound\" disc=\"/Sound\" create=\"true\"/>\n        <folder external=\"Sound/stream\" disc=\"/Sound/stream\" create=\"true\" />\n")
if Layout:
    f.write("        <folder external=\"Layout\" disc=\"/Layout\" create=\"true\"/>\n")
if WorldMap:
    f.write("        <folder external=\"WorldMap\" disc=\"/WorldMap\" create=\"true\"/>\n")
if Env:
    f.write("        <folder external=\"Env\" disc=\"/Env\" create=\"true\"/>\n")
if Effect:
    f.write("        <folder external=\"Effect\" disc=\"/Effect\" create=\"true\"/>\n")
if Replay:
    f.write("        <folder external=\"Replay\" disc=\"/Replay\" create=\"true\"/>\n")
if rels:
    f.write("        <folder external=\"rels\" disc=\"/rels\" create=\"true\"/>\n")    
if MovieDemo: 
    f.write("        <folder external=\"MovieDemo\" disc=\"/MovieDemo\" create=\"true\"/>\n")
if HomeButton2:
    f.write("        <folder external=\"HomeButton2\" disc=\"/HomeButton2\" create=\"true\"/>\n")    
f.write("    </patch>\n</wiidisc>")

f.close()
