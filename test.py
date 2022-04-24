#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from chuquocngu import isVNESE

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Dùng lệnh: %s <từ vựng>' % sys.argv[0])
        sys.exit()
    word = sys.argv[1].strip()
    if not word:
        print('Dùng lệnh: %s <từ vựng>' % sys.argv[0])
        sys.exit()
    if isVNESE(word):
        print('\033[92mTừ vựng: \"%s\" hợp lệ.\033[0m' % word)
    else:
        print('\033[91mTừ vựng: \"%s\" không hợp lệ.\033[0m' % word)
    sys.exit(0)
