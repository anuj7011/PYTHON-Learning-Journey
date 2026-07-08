print("===== Text Analyzer =====")

text = input("Enter your text: ")

print("\nOriginal Text:")
print(text)

print("\nTotal Characters:", len(text))

print("Total Words:", len(text.split()))

print("Uppercase:")
print(text.upper())

print("Lowercase:")
print(text.lower())

old_word = input("\nEnter word to replace: ")
new_word = input("Enter new word: ")

print("\nUpdated Text:")
print(text.replace(old_word,new_word))
