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
xmlgenerate=ask("Generate the XML now?")

f.write("<!-- XML created by XMLCreator4NSMBW -->\n<wiidisc version=\"1\">\n    <id game=\"SMN\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <options>\n")
f.write("       <section name=\""+sectionName+"\">\n")
f.write("           <option name=\""+optionName+"\">\n")
f.write("               <choice name=\""+choiceName+"\">\n")
f.write("                   <patch id=\""+sectionName+"\"/>\n")
f.write("               </choice>\n           </option>\n       </section>\n    </options>\n")
f.write("    <patch id=\""+sectionName+"\" root=\"/"+folderName+"\">\n")

if saveGameCustom:
    f.write("        <savegame external=\"save/{$__gameid}{$__region}\" clone=\"false\"/>\n")
if xmlgenerate:
    f.write("    <folder external=\"/"+folderName+"\" disc=\"/\" create=\"true\" recursive=\"true\"/>\n")
f.write("    </patch>\n</wiidisc>")

f.close()

