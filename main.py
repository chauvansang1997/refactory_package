import os

directory_in_str = '/Users/sangchauvan/Documents/tshop_mobile/tdesk_api_client'
# directory = os.fsencode(directory_in_str)
replace_package = 'tshop_api_client'
new_package = 'tdesk_api_client'
for subdir, dirs, files in os.walk(directory_in_str):
    for file in files:
        filepath = subdir + os.sep + file
        with open(filepath, "r") as inp:
            new_file_lines = []
            for line in inp:
                if line.__contains__(replace_package):
                    line = line.replace(replace_package, new_package)
                    print(line)
                new_file_lines.append(line)

        with open(filepath, "w") as document1:
            document1.writelines(new_file_lines)
        # with open(filepath, "r") as inp:
        #     new_file_lines = []
        #     for line in inp:
        #         if line.__contains__(new_package):
        #             print(line)
        # print(filepath)
    for directory in dirs:
        print(directory)
