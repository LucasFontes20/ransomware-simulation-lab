from pathlib import Path

# Pasta exclusiva do laboratório
PASTA_TESTE = Path(__file__).parent / "arquivos_teste"

# Extensão usada apenas para identificar a simulação
EXTENSAO_SIMULADA = ".simulado"

# Chave fixa apenas para demonstração didática
CHAVE = 0x5A


def criptografar_simulado(dados: bytes) -> bytes:
    """
    Transformação XOR reversível para demonstração.
    NÃO é criptografia segura para uso real.
    """
    return bytes(byte ^ CHAVE for byte in dados)


def main():
    if not PASTA_TESTE.exists():
        print("[ERRO] A pasta arquivos_teste não existe.")
        return

    arquivos = [
        arquivo
        for arquivo in PASTA_TESTE.iterdir()
        if arquivo.is_file()
        and not arquivo.name.endswith(EXTENSAO_SIMULADA)
        and not arquivo.name.startswith("restaurado_")
    ]

    if not arquivos:
        print("[INFO] Nenhum arquivo de teste encontrado.")
        return

    print("=" * 40)
    print("     RANSOMWARE SIMULADO")
    print("=" * 40)
    print("[!] Ambiente didático.")
    print("[!] Os arquivos originais NÃO serão alterados.\n")

    for arquivo in arquivos:
        destino = arquivo.with_name(
            arquivo.name + EXTENSAO_SIMULADA
        )

        dados = arquivo.read_bytes()
        dados_simulados = criptografar_simulado(dados)

        destino.write_bytes(dados_simulados)

        print(f"[OK] Simulado: {arquivo.name}")
        print(f"     Cópia:    {destino.name}")

    print("\n[+] Simulação concluída.")
    print("[+] Arquivos originais permanecem intactos.")


if __name__ == "__main__":
    main()
