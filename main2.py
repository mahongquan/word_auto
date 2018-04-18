# -*- coding: utf-8 -*-
import reg
import installcs
import installonh
isonh=reg.ison()
if isonh:
    installonh.main()
else:
    installcs.main()
