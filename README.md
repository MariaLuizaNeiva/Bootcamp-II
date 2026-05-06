# 🍎 Nutrilog - Evolução e Entrega Contínua

> **Link do Deploy:** [https://nutrilog-marialuiza.onrender.com/] 🚀

## 📋 Sobre o Projeto
O Nutrilog é uma aplicação focada em saúde e bem-estar, desenvolvida como parte da **Etapa 2 (Entrega Intermediária)** do Bootcamp. Nesta fase, o sistema evoluiu para consumir dados do mundo real através de APIs públicas.

## 🚀 Novas Funcionalidades (Etapa 2)
- **Integração com API Pública:** Agora o sistema consulta automaticamente a base de dados do [Open Food Facts](https://world.openfoodfacts.org/) para recuperar informações nutricionais reais via código de barras.
- **Gestão de Demandas:** Desenvolvimento orientado a issues no GitHub e fluxo de ramificação (branching).
- **Testes de Integração:** Implementação de testes automatizados para validar a comunicação com serviços externos.
- **CI/CD:** Pipeline configurada via GitHub Actions para garantir a qualidade em cada commit.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.7.4+
- **Bibliotecas:** `requests` (HTTP), `unittest` (Testes)
- **Infraestrutura:** GitHub Actions, Git

## 🧪 Como rodar os testes
Para garantir que a integração com a API está funcionando, execute:
```bash
python -m unittest tests/test_integracao_api.py