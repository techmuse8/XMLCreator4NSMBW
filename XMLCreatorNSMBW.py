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
with open(xmlName+".xml" , 'w') as file:

    sectionName=str(input("What is your mod name? (Short name) [Section name]"))
    optionName=str(input("What will be the message that will show up in Riivolution on the mod's page? [Option name]"))
    choiceName=str(input("What will be shown when the mod is enabled? [Choice name]"))
    folderName=str(input("What is your mod's folder name? (For example \"nsmbwtest\")"))

saveGame="Yes"
noDoubles=0
saveGameCustom=ask("Does your mod use a custom save file?")
xmlgenerate=ask("Generate the XML now?")

with open(xmlName+".xml" , 'w') as file:

    file.write("<!-- XML created by XMLCreator4NSMBW -->\n<wiidisc version=\"1\">\n    <id game=\"SMN\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <options>\n")
    file.write("       <section name=\""+sectionName+"\">\n")
    file.write("           <option name=\""+optionName+"\">\n")
    file.write("               <choice name=\""+choiceName+"\">\n")
    file.write("                   <patch id=\""+sectionName+"\"/>\n")
    file.write("               </choice>\n           </option>\n       </section>\n    </options>\n")
    file.write("    <patch id=\""+sectionName+"\">\n")

    if saveGameCustom:
            file.write("        <savegame external=\"save/{$__gameid}{$__region}\" clone=\"false\"/>\n")
    if xmlgenerate:
            file.write("    <folder external=\"/"+folderName+"\" disc=\"/\" create=\"true\" recursive=\"true\"/>\n")
    file.write("    </patch>\n</wiidisc>")

file.close()

