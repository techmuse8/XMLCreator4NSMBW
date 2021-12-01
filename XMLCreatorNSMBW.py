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

sectionName=str(input("What is your mod name ? (Short name) [Section name]"))
optionName=str(input("What will be the message that will show up in riivolution on the mod's page ? [Option name]"))
choiceName=str(input("What will be shown when the mod is enabled ? [Choice name]"))
folderName=str(input("What is your mod's folder name ? (For example \"nsmbwtest\")"))

saveGame="Yes"
noDoubles=0
saveGameCustom=ask("Does your mod use a custom save file ?")
if saveGameCustom == False:
    saveGame=ask("Do you want the mod to use your vanilla save files ?")
Stage=ask("Does your mod use Stage ?")
USEUJP=ask("Does your mod use US/EU/JP ?")

f.write("<!-- XML created by XMLCreator4NSMBW -->\n<wiidisc version=\"1\">\n    <id game=\"SMN\"/>\n       <region type=\"E\"/>\n       <region type=\"J\"/>\n       <region type=\"P\"/>\n       <region type=\"W\"/>\n       <region type=\"K\"/>\n    <options>\n")
f.write("       <section name=\""+sectionName+"\">\n")
f.write("           <option name=\""+optionName+"\">\n")
f.write("               <choice name=\""+choiceName+"\">\n")
f.write("                   <patch id=\""+sectionName+"\"/>\n")
f.write("               </choice>\n           </option>\n       </section>\n    </options>\n")
f.write("    <patch id=\""+sectionName+"\" root=\"/"+folderName+"\">\n")

if Stage: 
    f.write("        <folder external=\"Stage\" disc=\"/Stage\" create=\"true\"/>\n"
if USEUJP:
    f.write("        <folder external=\"US\" disc=\"/US\" create=\"true\"/>\n        <folder external=\"EU\" disc=\"/EU\" create=\"true\" />\n        <folder external=\"JP\" disc=\"/JP\" create=\"true\" />\n")
f.write("    </patch>\n</wiidisc>")

f.close()
