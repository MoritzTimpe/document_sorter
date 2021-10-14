from Organizer import Organizer

paths = [
    "D:\Documents",
    "D:\Downloads"
]
for path in paths:

    i = Organizer(path)

    files = i.get_files()
    print(files)
    for f in files:
        try:
            i.get_file_type(f)
            i.create_file_paths(f)
            i.get_existance_of_folder()
            i.move_file(f)
        except:
            print("Finished!")