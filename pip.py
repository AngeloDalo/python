#package manager
#pip --version
#python get pip.py
#pip install camelcase

import camelcase
c = camelcase.CamelCase()
frase = "ciao sono io"
print(c.hump(frase))
#pip unistall camelcase
#pip list #vedere package installati