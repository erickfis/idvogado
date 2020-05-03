"""
Project iAdvogado

Description:
create app folder and files structure

Usage:
cmd: python create_infra.py dir1,dir2,dir3 Author Name

Author:
Erick Medeiros Anastácio
2020/05/03
"""

import os
import sys
import datetime


def create_infra(args):
    """
    Create folders and files for the project.

    Usage:
    cmd: python create_infra.py dir1,dir2,dir3 Author Name

    """
    subfolders = args[1].split(',')
    subfolders.append('') # add the . folder
    author = ' '.join(args[2:])
    # create main folder
    os.makedirs('app', exist_ok=True)

    # create subfolders
    for folder in subfolders:
        path = os.path.join('app', folder)
        os.makedirs(path, exist_ok=True)
        print(f'{folder} created')

    # create inits
    create_inits(subfolders, author)


def create_inits(subfolders, author):
    """Create init files for each folder."""
    date = datetime.datetime.today().strftime('%Y/%m/%d')
    # creat a init file for each folder
    with open('default_doc.txt') as file:
        init_doc = file.read()

    for folder in subfolders:
        path = os.path.join('app', folder, '__init__.py')
        vars = {'author': author, 'date': date, 'folder': folder}
        doc = init_doc.format(**vars)

        # write only if not exists:
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf8') as file:
                file.write(doc)
            print(f'{path} created.')
        else:
            print(f'{path} already exists.')


if __name__ == '__main__':
    args = sys.argv
    create_infra(args)
