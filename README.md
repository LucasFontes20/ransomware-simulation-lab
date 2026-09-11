Ransomware Simulado

Projeto didático desenvolvido em Python para demonstrar o conceito de criptografia e descriptografia de arquivos em um ambiente controlado.

Aviso: este projeto é exclusivamente educacional. A ferramenta trabalha apenas com arquivos dentro da pasta arquivos_teste/ e preserva os arquivos originais.

Estrutura do projeto
ransomware-simulado/
├── encrypt_simulado.py
├── decrypt_simulado.py
├── arquivos_teste/
│   ├── documento.txt
│   ├── exemplo.txt
│   └── dados.txt
├── README.md
└── screenshots/

Requisitos
Python 3
Linux ou Kali Linux
Terminal

Não é necessário instalar bibliotecas externas.

Como usar
1. Entrar no projeto
cd ~/ransomware-simulado

2. Verificar os arquivos de teste
ls -la arquivos_teste


Os arquivos utilizados na demonstração devem estar dentro dessa pasta.

3. Executar a criptografia simulada
python3 encrypt_simulado.py


O programa criará cópias dos arquivos utilizando a extensão:

.simulado


Exemplo:

dados.txt
dados.txt.simulado


O arquivo original permanece intacto.

4. Executar a descriptografia simulada

Depois da etapa anterior, execute:

python3 decrypt_simulado.py


O programa criará uma cópia restaurada:

restaurado_dados.txt

5. Verificar o resultado
ls -la arquivos_teste


Para visualizar o conteúdo restaurado:

cat arquivos_teste/restaurado_dados.txt

Fluxo de utilização
1. Criar arquivos de teste
          ↓
2. encrypt_simulado.py
          ↓
3. Arquivos .simulado
          ↓
4. decrypt_simulado.py
          ↓
5. Arquivos restaurados

Objetivo da demonstração

A ferramenta permite visualizar, de maneira controlada, o conceito de:

transformação de dados;
criptografia simulada;
descriptografia;
restauração de arquivos;
comparação entre arquivo original e arquivo restaurado.
Segurança

O projeto foi desenvolvido para laboratório e não possui mecanismos de:

propagação pela rede;
persistência;
exclusão de arquivos;
alteração de arquivos fora de arquivos_teste/;
comunicação externa;
bloqueio do sistema;
pagamento ou extorsão.
Tecnologia
Python 3
pathlib
XOR reversível para demonstração didática

A transformação XOR utilizada neste projeto é apenas educacional e não deve ser considerada criptografia segura para aplicações reais.

Resultado da demonstração

Durante a execução do laboratório foram realizadas as seguintes etapas:

Foram utilizados arquivos fictícios dentro da pasta arquivos_teste/.
O encrypt_simulado.py criou cópias com a extensão .simulado.
Os arquivos originais permaneceram intactos.
O decrypt_simulado.py processou as cópias simuladas.
Foram criados arquivos restaurado_*.txt para demonstrar a recuperação.
O conteúdo dos arquivos restaurados foi verificado no terminal.

As screenshots presentes na pasta screenshots/ registram as principais etapas da demonstração.

Conclusão

O projeto demonstra, em ambiente controlado, o conceito básico de transformação e reversão de dados associado ao fluxo de um ransomware, sem implementar mecanismos de propagação, persistência ou destruição de arquivos.
