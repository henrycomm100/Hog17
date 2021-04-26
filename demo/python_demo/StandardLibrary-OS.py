import os


# os.mkdir("newdir")

# os.removedirs("newdir")
# print(os.listdir("./"))
# print(os.getcwd())

print(os.path.exists("b"))

if not os.path.exists("b"):
    os.mkdir("b")

if not os.path.exists("b/new.txt"):
    with open("b/new.txt", "w") as f:
        f.write("Hello, can you see this?")