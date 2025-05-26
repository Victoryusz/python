from django.test import TestCase
from .models import Livro

class LivroModelTest(TestCase):
    def test_str_retorna_titulo(self):
        livro = Livro(titulo="Django na Prática", autor="Fulano")
        self.assertEqual(str(livro), "Django na Prática")

# ATIVIDADE PARA ENTENDER TESTE AUTOMATIZADO EM DJANGO