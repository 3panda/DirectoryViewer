#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import glob


def main(path: str, layer: int = 0, is_root: bool = False):
    """
    :param path: ツリー状で表示させる対象のPath
    :param layer: 取得するディレクトリの階層
    :param is_root: root(最上層)であるか
    """
    tab = u" "
    if is_root is True:
        file_path = glob.glob(path)
        root_name = ','.join(file_path)
        print(root_name)

    files = glob.glob(path + '/*')

    for file in files:
        # get dir or file path
        file_paths = file.split('/')
        # get dir or file name
        print(tab * (layer + 1) + "|-" + file_paths.pop())
        if os.path.isdir(file):
            # case dir (recall)
            main(file, layer + 1)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        main(path=sys.argv[1], is_root=True)
    else:
        print("usage.")
        print("{filename} <path(ex:/root)>>"
              .format(filename=sys.argv[0]))
