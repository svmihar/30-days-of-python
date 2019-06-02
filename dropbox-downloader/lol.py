import dropbox, itertools, os
from pprint import pprint
ACCESS_TOKEN = input('ACESS TOKEN: ')

dbx = dropbox.Dropbox(ACCESS_TOKEN)
folders = dbx.files_list_folder(path='', recursive=True)

file_list = []

def process_entries(entries):
    for entry in entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            file_list.append([entry.path_display])

process_entries(folders.entries)

while folders.has_more:
    folders = dbx.files_list_folder_continue(folders.cursor)
    process_entries(folders.entries)

merged = list(itertools.chain(*file_list))

merged = list(set(merged))
print(len(merged))

for file in merged[:10]: 
    print(f"now downloading {file.split('/')[-1]}")
    os.umask(os.umask(0))
    os.makedirs(os.path.dirname(file), exist_ok=True)
    
    with open(file, 'wb') as f: 
        meta, res = dbx.files_download_zip_to_file(download_path=file, path=file)
        f.write(res.content)