# -*- coding: utf-8 -*-
import os
from lib.recovery_code import recovery_code

if __name__ == '__main__':
	autyPath = os.path.dirname(os.path.abspath(__file__))
	#Scripts recovery.
	recovery_code(autyPath)