import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayuscula(self):
        palabra = 'hola'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'HOLA')

if __name__ == '__main__':
    unittest.main()