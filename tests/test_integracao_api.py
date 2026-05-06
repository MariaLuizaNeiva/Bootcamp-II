import unittest
from src.api_nutricao import buscar_dados_alimento

class TestIntegracaoAPI(unittest.TestCase):
    def test_deve_retornar_dados_ao_consultar_codigo_valido(self):
        # Usando um código de barras real (ex: Coca-Cola) para validar o fluxo
        resultado = buscar_dados_alimento("7891000053508")
        
        # Validações do teste de integração (Critério 1.3)
        self.assertIsNotNone(resultado)
        self.assertIn("nome", resultado)
        self.assertIsInstance(resultado["calorias"], (int, float))

if __name__ == "__main__":
    unittest.main()