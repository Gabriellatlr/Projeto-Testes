# 📘 Projeto de Testes Unitários, Refatoração e Cobertura de Código

## 📌 Descrição

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de testes de software, integração contínua (CI/CD), cobertura de código e refatoração orientada a testes utilizando Python.

O sistema implementa funcionalidades relacionadas ao cálculo e análise de notas de alunos, além de aplicar boas práticas de qualidade de software e automação de testes.

---

# ⚙️ Funcionalidades

- Cálculo da média de notas
- Verificação da situação do aluno:
  - Aprovado
  - Recuperação
  - Reprovado
- Identificação da maior nota
- Validação de entradas inválidas
- Tratamento de listas vazias

---

# 🧪 Testes Automatizados

O projeto utiliza a biblioteca `unittest` para execução dos testes automatizados.

Foram implementados:

## ✅ Testes Unitários
Cobrem:
- cálculo de média;
- validação de aprovação;
- identificação da maior nota;
- tratamento de exceções;
- validação de tipos inválidos.

## ✅ Testes de Integração
Validam o fluxo completo do sistema:
- cálculo da média;
- classificação do aluno;
- integração entre funções.

---

# 📊 Cobertura de Código

A cobertura de código foi analisada utilizando a ferramenta `coverage.py`.

## Resultado Obtido

| Arquivo | Cobertura |
|---|---|
| notas.py | 100% |
| test_integracao_notas.py | 94% |
| test_notas.py | 96% |
| **TOTAL** | **96%** |

A alta cobertura indica que a maior parte das funcionalidades foi validada por testes automatizados, reduzindo significativamente o risco de falhas.

---

# 🔧 Refatoração Realizada

O projeto passou por processo de refatoração orientada a testes visando melhorar:

- legibilidade;
- reutilização de código;
- robustez;
- organização estrutural;
- validação de dados.

## Melhorias implementadas

- criação da função `validar_notas()`;
- redução de duplicação de código;
- melhoria nos nomes de funções;
- validação de tipos de entrada;
- aumento da coesão das funções;
- melhoria da manutenção futura do sistema.

Todas as alterações foram realizadas mantendo os testes automatizados funcionando corretamente.

---

# 🚀 Integração Contínua (CI/CD)

O projeto utiliza GitHub Actions para execução automática dos testes a cada `push` ou `pull request`.

O pipeline realiza:
- configuração do ambiente Python;
- execução dos testes unitários;
- execução dos testes de integração;
- validação automática do sistema.

---

# ▶️ Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/Gabriellatlr/Projeto-Testes.git
