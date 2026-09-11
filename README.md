# Ransomware Simulado

Projeto educacional desenvolvido em Python para demonstrar, em ambiente controlado, o fluxo básico de transformação e recuperação de arquivos associado ao conceito de ransomware.

## ⚠️ Aviso

Este projeto é **exclusivamente educacional** e foi desenvolvido para execução em laboratório controlado.

A ferramenta:

* trabalha somente dentro da pasta `arquivos_teste/`;
* não altera os arquivos originais;
* não possui propagação pela rede;
* não possui mecanismos de persistência;
* não exclui arquivos;
* não possui comunicação externa;
* não bloqueia o sistema;
* não implementa pagamento ou extorsão.

## 📁 Estrutura do projeto

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
```

## 🛠️ Tecnologias

* Python 3
* Linux / Kali Linux
* `pathlib`
* XOR reversível

Não são necessárias bibliotecas externas.

## ▶️ Como executar

### 1. Entrar no projeto

```bash
cd ~/ransomware-simulado
```

### 2. Verificar os arquivos de teste

```bash
ls -la arquivos_teste
```

Os arquivos utilizados na demonstração devem estar dentro da pasta `arquivos_teste/`.

### 3. Executar a transformação simulada

```bash
python3 encrypt_simulado.py
```

O programa cria cópias dos arquivos utilizando a extensão `.simulado`.

Exemplo:

```text
dados.txt
dados.txt.simulado
```

O arquivo original permanece intacto.

### 4. Executar a recuperação simulada

Depois da etapa anterior, execute:

```bash
python3 decrypt_simulado.py
```

O programa processará os arquivos `.simulado` e criará uma cópia restaurada.

Exemplo:

```text
restaurado_dados.txt
```

### 5. Verificar o resultado

```bash
ls -la arquivos_teste
```

Para visualizar o conteúdo do arquivo restaurado:

```bash
cat arquivos_teste/restaurado_dados.txt
```

## 🔄 Fluxo da demonstração

```text
Arquivos de teste
       ↓
encrypt_simulado.py
       ↓
Arquivos .simulado
       ↓
decrypt_simulado.py
       ↓
Arquivos restaurados
```

## 🎯 Objetivo

O projeto demonstra conceitos básicos de:

* transformação reversível de dados;
* criptografia simulada;
* descriptografia;
* restauração de arquivos;
* manipulação de arquivos;
* comparação entre arquivo original e arquivo restaurado.

## 🔐 Segurança

O projeto foi desenvolvido exclusivamente para laboratório e não possui mecanismos de:

* propagação pela rede;
* persistência;
* exclusão de arquivos;
* alteração de arquivos fora de `arquivos_teste/`;
* comunicação externa;
* bloqueio do sistema;
* pagamento ou extorsão.

A operação é limitada aos arquivos utilizados na demonstração.

## 🧪 Resultado da demonstração

Durante a execução do laboratório:

1. Foram utilizados arquivos fictícios dentro da pasta `arquivos_teste/`.
2. O `encrypt_simulado.py` criou cópias com a extensão `.simulado`.
3. Os arquivos originais permaneceram intactos.
4. O `decrypt_simulado.py` processou as cópias simuladas.
5. Foram criados arquivos `restaurado_*.txt`.
6. O conteúdo dos arquivos restaurados foi verificado no terminal.

As screenshots presentes na pasta `screenshots/` registram as principais etapas da demonstração.

## 📚 O que este projeto demonstra

Este laboratório permite compreender, de forma prática, um dos conceitos envolvidos em ataques de ransomware: a transformação de arquivos e o processo de recuperação mediante uma operação reversível.

Também demonstra conhecimentos básicos de:

* Python;
* manipulação de arquivos;
* Linux;
* terminal;
* automação;
* conceitos de segurança;
* análise de comportamento de malware.

## ⚠️ Observação sobre XOR

A transformação XOR utilizada neste projeto possui finalidade exclusivamente didática.

Ela **não representa uma implementação de criptografia segura** e não deve ser utilizada para proteger dados reais.

O objetivo é apenas demonstrar, de maneira simples, o conceito de transformação e reversão de dados.

## 📸 Screenshots

As evidências da execução do laboratório estão disponíveis na pasta:

```text
screenshots/
```

Elas registram as principais etapas da demonstração, incluindo a execução dos scripts e a verificação dos arquivos.

## 📌 Conclusão

O projeto demonstra, em ambiente controlado, o conceito básico de transformação e reversão de dados associado ao fluxo de um ransomware, sem implementar mecanismos de propagação, persistência ou destruição de arquivos.

O laboratório foi desenvolvido com foco educacional, permitindo compreender alguns conceitos relacionados ao comportamento de ransomware enquanto mantém a execução limitada a arquivos de teste.
