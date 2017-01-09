# -*- coding: utf-8 -*-
from lib.execute_selection import execute_selection
from lib.recovery_code import recovery_code
import os

if __name__ == '__main__':
	#Execute scripts.
	execute_selection()
	autyPath = os.path.dirname(os.path.abspath(__file__))
	#Scripts recovery.
	recovery_code(autyPath)