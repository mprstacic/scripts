import os
# Simple Comment 9:13PM
def generate_dict():
    folder_path = '/home/mprstacic/scripts/'
    files = os.listdir(folder_path)
    #print("Files in %s: %s" % (folder_path, files))

    for filename in files:
        if filename.endswith(".py"):
            print(filename)
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r') as f:
                content = f.readlines()
                print(content)
                dict[filename]=content

dict = {}
generate_dict()
print(dict.keys())
