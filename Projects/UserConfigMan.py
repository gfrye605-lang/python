# List of default settings
test_settings = {
    "theme" : "dark",
    "notifications" : "enabled",
    "volume" : "high"
}
# List of acceptable settings
settings = {
    "theme" : ("light, dark"),
    "volume" : ("high", "medium", "low"),
    "notifications" : ("enabled", "disabled")
}
# Used to create a new setting
def add_setting(setting, tup):
    key, value = tup
    key = str(key).lower()
    value = str(value).lower()
    if key in setting: # Checks for a preexisting setting to prevent mulitple settings with the same name
        return(f"Setting \'{key}\' already exists! Cannot add a new setting with this name.")
    if key not in setting: # If not, the new setting it approved
        setting[key] = value
        return(f"Setting \'{key}\' added with value \'{value}\' successfully!")

# This function is used to change the value of settings, i.e, theme : dark --> theme : light
def update_setting(settings, tup):
    key, value = tup
    key = str(key).lower()
    value = str(value).lower()
    if key in settings: # Check if updated setting is in the allowed list
        settings[key] = value
        return(f"Setting \'{key}\' updated to \'{value}\' successfully!")
    if key not in settings: # If not the new setting is rejected
        return(f"Setting \'{key}\' does not exist! Cannot update a non-existing setting.")

# This function is used to delete settings
def delete_setting(settings, key):
    print("key:",key)
    key = str(key).lower()
    if key in settings: # Checks if the settings you're trying to move even exists
        settings.pop(key)
        return(f"Setting \'{key}\' deleted successfully!")
    if key not in settings: # If not, the job is rejected
        return(f"Setting not found!")

# This function allows you to view currently applied settings
def view_settings(settings):
    if settings:
        display = "Current User Settings:\n"
        keys = tuple(settings.keys())
        values = tuple(settings.values())
        for key, value in settings.items(): # <--\/ These lines essientally grab the raw settings from the dictionary and beautify them
            display += f"{key.capitalize()}: {value}\n" 
        return display
    if not settings: # If the list name provided is empty, we return an error
        return("No settings available.")



print(view_settings(test_settings))





