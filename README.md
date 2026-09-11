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
🛠️ Tecnologias
Python 3
Linux / Kali Linux
pathlib
XOR reversível

Não são necessárias bibliotecas externas.

▶️ Como executar
1. Entrar no projeto
cd ~/ransomware-simulado
2. Verificar os arquivos de teste
ls -la arquivos_teste
3. Executar a criptografia simulada
python3 encrypt_simulado.py

O programa cria cópias dos arquivos utilizando a extensão .simulado.

Exemplo:

dados.txt
dados.txt.simulado

O arquivo original permanece intacto.

4. Executar a descriptografia
python3 decrypt_simulado.py

Será criada uma cópia restaurada:

restaurado_dados.txt
5. Verificar o resultado
ls -la arquivos_teste

Para visualizar o conteúdo:

cat arquivos_teste/restaurado_dados.txt
🔄 Fluxo da demonstração
Arquivos de teste
       ↓
encrypt_simulado.py
       ↓
Arquivos .simulado
       ↓
decrypt_simulado.py
       ↓
Arquivos restaurados
🎯 Objetivo

O projeto demonstra conceitos básicos de:

transformação de dados;
criptografia simulada;
descriptografia;
restauração de arquivos;
comparação entre arquivo original e arquivo restaurado.
🔐 Segurança

O projeto foi desenvolvido para execução em laboratório e não possui mecanismos de:

propagação pela rede;
persistência;
exclusão de arquivos;
alteração fora de arquivos_teste/;
comunicação externa;
bloqueio do sistema;
pagamento ou extorsão.

A operação é limitada aos arquivos utilizados para demonstração.

🧪 Resultado

Durante o laboratório:

Foram criados arquivos fictícios em arquivos_teste/.
O encrypt_simulado.py criou cópias .simulado.
Os arquivos originais permaneceram intactos.
O decrypt_simulado.py processou as cópias.
Foram criados arquivos restaurado_*.txt.
O conteúdo restaurado foi verificado no terminal.

As screenshots presentes em screenshots/ registram as principais etapas da execução.

📚 O que este projeto demonstra

Este laboratório permite compreender, de forma prática, um dos conceitos envolvidos em ataques de ransomware: a transformação de arquivos e o processo de recuperação mediante uma operação reversível.

Também demonstra conhecimentos básicos de:

Python;
manipulação de arquivos;
Linux;
terminal;
automação;
conceitos de segurança;
análise de comportamento de malware.
⚠️ Observação sobre XOR

A transformação XOR utilizada neste projeto possui finalidade exclusivamente didática.

Ela não representa uma implementação de criptografia segura e não deve ser utilizada para proteger dados reais.

📌 Conclusão

O projeto demonstra, em ambiente controlado, o conceito básico de transformação e reversão de dados associado ao fluxo de um ransomware, sem implementar mecanismos de propagação, persistência ou destruição de arquivos.
├── README.md
└── screenshots/
