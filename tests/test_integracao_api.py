import unittest
from unittest.mock import patch
from src.api_nutricao import buscar_dados_alimento

class TestIntegracaoAPI(unittest.TestCase):
    
    @patch('src.api_nutricao.requests.get')
    def test_deve_retornar_dados_ao_consultar_codigo_valido(self, mock_get):
        # Aqui nós "fingimos" a resposta da API. 
        # Assim, o teste passa mesmo se a internet do GitHub falhar.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "status": 1,
            "product": {
                "product_name": "Alimento Teste",
                "nutriments": {"energy-kcal_100g": 100}
            }
        }

        resultado = buscar_dados_alimento("7891000053508")
        
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nome"], "Alimento Teste")
        self.assertEqual(resultado["calorias"], 100)

if __name__ == "__main__":
    unittest.main()