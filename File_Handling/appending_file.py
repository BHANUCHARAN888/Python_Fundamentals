# # Adding new content without removing old content
# with open("Data.txt", "a") as file:
#     file.write("\nTruth is..\nI am IRONMAN.")
# print("--------------------------------------")
# # Implementing read file mode to above appended file
# with open("Data.txt", "r") as file:
#     print(file.read())
# print("----------------------------------------")
# with open("skills.txt", "a") as file:
#     file.write("\nMachine Learning")
# print("Data Added")
# print("----------------------------------------")
# with open("skills.txt", "a") as file:
#     file.write("\nDeep Learning")
#     file.write("\nArtificial Intelligence")
#     file.write("\nLLM")
# print("Updated")
# print("----------------------------------------")
print("<-----Started----->")
skills = input("Enter your skill: ")
with open("Skills.txt", "a") as file:
    file.write(f"\n{skills}")
print("<-----Skill Added----->")
