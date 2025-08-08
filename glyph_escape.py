Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Glyph Portal Escape Game 🌀

# Required glyph sequence to escape
required_sequence = ['Ѥ', 'Ѵ', 'Ѳ', 'Ѱ', 'Ѯ', 'Ѫ', 'Ѧ', 'Ѣ']

# Player's collected glyphs
collected_glyphs = []

print("🔒 You are trapped in symbolic Russia.")
print("🌀 To escape, collect and enter the glyphs in the correct order to activate the portal.")
print("📜 Required glyphs: " + " + ".join(required_sequence))
print("Press 'W' to collect a glyph.")
print("Press 'enter' to enter a glyph into the portal.")
print("Press 'S' to view your progress.")
print("Press 'X' to quit.\n")

while True:
...     command = input("🔹 What will you do? ").strip()
... 
...     if command.lower() == 'exit':
...         print("👋 Game ended. You remain in symbolic Russia... for now.")
...         break
... 
...     elif command.startswith('collect '):
...         glyph = command.split('collect ')[1].strip()
...         if glyph in required_sequence and glyph not in collected_glyphs:
...             collected_glyphs.append(glyph)
...             print(f"✅ Glyph {glyph} collected.")
...         elif glyph in collected_glyphs:
...             print(f"⚠️ You already have glyph {glyph}.")
...         else:
...             print(f"❌ Glyph {glyph} is not part of the escape sequence.")
... 
...     elif command.startswith('enter '):
...         glyph = command.split('enter ')[1].strip()
...         expected_index = len([g for g in collected_glyphs if g in required_sequence])
...         if glyph == required_sequence[expected_index]:
...             collected_glyphs.append(glyph)
...             print(f"🔐 Glyph {glyph} entered into the portal.")
...         else:
...             print(f"❌ Incorrect glyph. Expected: {required_sequence[expected_index]}")
... 
...         if collected_glyphs[-8:] == required_sequence:
...             print("\n🌈 Portal activated! You escape symbolic Russia and return home safely and it is not a dream.")
...             break
... 
...     elif command == 'status':
...         print(f"📦 Collected glyphs: {collected_glyphs}")
...         print(f"🔑 Progress: {len([g for g in collected_glyphs if g in required_sequence])}/8")
... 
...     else:
