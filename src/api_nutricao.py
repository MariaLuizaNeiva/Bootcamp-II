import requests

def buscar_dados_alimento(codigo_barras):
    # Endpoint da API pública para buscar produtos por código
    url = f"https://world.openfoodfacts.org/api/v0/product/{codigo_barras}.json"
    
    try:
        response = requests.get(url, timeout=30)
        # Verifica se a requisição foi bem sucedida (Critério 1.2 e 1.3)
        if response.status_code == 200:
            dados = response.json()
            if dados.get("status") == 1:
                produto = dados["product"]
                return {
                    "nome": produto.get("product_name", "Desconhecido"),
                    "calorias": produto.get("nutriments", {}).get("energy-kcal_100g", 0)
                }
        return None
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return None