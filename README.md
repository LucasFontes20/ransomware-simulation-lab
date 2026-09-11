# Ransomware Simulado

Projeto educacional desenvolvido em Python para demonstrar, em ambiente
controlado, o fluxo básico de transformação e recuperação de arquivos
associado ao conceito de ransomware.

## ⚠️ Aviso

Este projeto é exclusivamente educacional.

A ferramenta:
- trabalha somente dentro da pasta `arquivos_teste/`;
- não altera os arquivos originais;
- não possui propagação pela rede;
- não possui persistência;
- não exclui arquivos;
- não possui comunicação externa;
- não bloqueia o sistema;
- não implementa pagamento ou extorsão.

## 📁 Estrutura

```text
ransomware-simulado/
├── encrypt_simulado.py
├── decrypt_simulado.py
├── arquivos_teste/
│   ├── documento.txt
│   ├── exemplo.txt
│   └── dados.txt
├── README.md
└── screenshots/
