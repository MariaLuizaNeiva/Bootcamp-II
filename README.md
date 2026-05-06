# NutriLog CLI 🍎💧

[![CI Pipeline](https://github.com/Maria-Luiza-Neiva/Desafio-inicial---Bootcamp-II/actions/workflows/ci.yml/badge.svg)](https://github.com/MariaLuizaNeiva/Desafio-inicial---Bootcamp-II/actions)

## 📝 Sobre o Projeto
O **NutriLog CLI** é uma aplicação de linha de comando desenvolvida para ajudar estudantes e profissionais de tecnologia a manterem hábitos saudáveis durante a jornada de trabalho e estudos.

Muitas vezes, mergulhados no código ou nas aulas, esquecemos do básico: beber água e bater a meta de nutrientes. Este software resolve essa "dor" de forma rápida e profissional, sem que o usuário precise sair do seu ambiente de desenvolvimento (terminal).

### 🎯 Definição do Problema (Dor Real)
* **Qual problema estou resolvendo?** A dificuldade de monitorar hábitos básicos de saúde (água e alimentação) durante períodos de alto foco mental.
* **Quem é afetado?** Estudantes de Ciência da Computação e desenvolvedores que passam longas horas sentados em frente ao computador.
* **Como a aplicação ajuda?** Oferece uma interface simples para registro instantâneo, gerando um feedback visual imediato sobre o que ainda falta para atingir as metas do dia.
* **Fluxo de uso:** O usuário registra a quantidade (ex: 500ml de água) e o sistema atualiza o progresso diário, persistindo os dados para consulta.

---

## 🚀 Tecnologias Utilizadas
* **Linguagem:** [Python 3.10+](https://www.python.org/)
* **Gerenciador de Dependências:** Pip (via `requirements.txt`)
* **Testes Automatizados:** [Pytest](https://docs.pytest.org/)
* **Linter / Análise Estática:** [Flake8](https://flake8.pycqa.org/)
* **CI/CD:** [GitHub Actions](https://github.com/features/actions) (Pipeline de Integração Contínua)
* **Versionamento Semântico:** [SemVer](https://semver.org/)

---

## 🛠️ Como Executar o Projeto

### 1. Pré-requisitos
* Ter o Python instalado (v3.10 ou superior).
* Ter o Git configurado.

### 2. Instalação e Configuração
```bash
# Clone o repositório
git clone https://github.com/MariaLuizaNeiva/Desafio-inicial---Bootcamp-II.git
cd Desafio-inicial---Bootcamp-II

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Windows)
.\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
``` 