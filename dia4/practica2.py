habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

if sabe_python and habla_ingles:
    print("Cumples con los requisitos para postularte")
elif not sabe_python and habla_ingles:
    print( "Para postularte, necesitas saber programar en Python")
elif sabe_python and not habla_ingles:
    print( "Para postularte, necesitas tener conocimientos de inglés")
else:
    print( "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
