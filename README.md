# 📘 Projeto de Testes Unitários e Cobertura de Código

## 📌 Descrição

Este projeto foi desenvolvido com o objetivo de aplicar práticas de testes de software, utilizando testes unitários e análise de cobertura de código em um módulo simples em Python.

O sistema implementa funcionalidades relacionadas ao cálculo e análise de notas de alunos.

---

## ⚙️ Funcionalidades

* Cálculo da média de notas
* Verificação da situação do aluno (Aprovado, Recuperação ou Reprovado)
* Identificação da maior nota

---

## 🧪 Testes Unitários

Foram implementados testes unitários utilizando a biblioteca `unittest`, cobrindo:

* Casos normais (funcionamento esperado)
* Casos de erro (listas vazias)
* Casos de limite (notas nos limites de aprovação)

---

## 📊 Cobertura de Código

A cobertura de código foi analisada utilizando a ferramenta `coverage`.

Resultado obtido:

> Cobertura total: 97% (excelente cobertura de testes)
> A cobertura de 97% indica que praticamente todas as funcionalidades foram testadas, reduzindo significativamente o risco de falhas no sistema.

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <https://github.com/Gabriellatlr/Projeto-Testes.git>
```

### 2. Executar os testes

```bash
python -m unittest test_notas.py
```

---

## 📈 Como gerar cobertura de código

```bash
python -m coverage run -m unittest test_notas.py
python -m coverage report
python -m coverage html
```

---


## 🧠 Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Testes e Qualidade de Software.
