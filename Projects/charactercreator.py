full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Name Validation
    if not isinstance(name , str):
        return("The character name should be a string")
    if name == "":
        return("The character should have a name")
    if len(name) > 10:
        return("The character name is too long")
    if " " in name:
        return("The character name should not contain spaces")

    # Stats Validation 
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int): 
        return("All stats should be integers") 
    if strength < 1 or intelligence < 1 or charisma < 1: 
        return("All stats should be no less than 1") 
    if strength > 4 or intelligence > 4 or charisma > 4: 
        return("All stats should be no more than 4") 
    if strength + intelligence + charisma > 7 or strength + intelligence + charisma < 7: 
        return("The character should start with 7 points") 

    # Assemble Stats List
    STR = ""
    INT = ""
    CHA = ""
    for display_str in range(strength):
        STR += full_dot
    for display_rest in range(10-strength):
        STR += empty_dot
    for display_str in range(intelligence):
        INT += full_dot
    for display_rest in range(10-intelligence):
        INT += empty_dot
    for display_str in range(charisma):
        CHA += full_dot
    for display_rest in range(10-charisma):
        CHA += empty_dot

    # Display Stats List
    stats = name + "\n" + "STR " + STR + "\n" + "INT " + INT + "\n" +"CHA " + CHA
    return stats

    
print(create_character("f", 1, 3, 3))