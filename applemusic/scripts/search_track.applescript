

tell application "Music"
	activate
end tell

delay 0.5

tell application "System Events"
	-- Focus the search bar
	keystroke "f" using {command down}
	-- Select all and delete existing text
	keystroke "a" using {command down}
	key code 51 -- delete key
	-- Search for our song name
	keystroke songName
	key code 36
end tell
