# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
	installFile = os.path.join(os.getcwd(),'requirements')
	os.system('/usr/local/bin/pip install -r '+installFile)
