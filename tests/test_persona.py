import unittest
from Comunidad.persona import Persona

class PersonaTestCase(unittest.TestCase):

    def setUp(self):
        self.persona1 = Persona(nombre='Alejandra', edad=25)
        self.persona2 = Persona(nombre='Diego', edad=22)
        self.persona3 = Persona(nombre='Alejandra', edad=25)
        self.persona4 = Persona(nombre='Diana', edad=25)
        self.grupo = [self.persona1, self.persona2, self.persona3]

    def test_constructor(self):
        self.assertEqual(self.persona1.dar_nombre(), 'Alejandra')
        self.assertEqual(self.persona1.dar_edad(), 40)
