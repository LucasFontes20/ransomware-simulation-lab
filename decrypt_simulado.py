from pathlib import Path

# Pasta exclusiva do laboratório
PASTA_TESTE = Path(__file__).parent / "arquivos_teste"

# Extensão utilizada pelo simulador
EXTENSAO_SIMULADA = ".simulado"

# Mesma chave utilizada na simulação de criptografia
CHAVE = 0x5A


def descriptografar_simulado(dados: bytes) -> bytes:
    """
    Reverte a transformação XOR utilizada
    pelo encrypt_simulado.py.
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
        and arquivo.name.endswith(EXTENSAO_SIMULADA)
    ]

    if not arquivos:
        print("[INFO] Nenhum arquivo .simulado encontrado.")
        return

    print("=" * 40)
    print("     DESCRIPTOGRAFIA SIMULADA")
    print("=" * 40)
    print("[!] Ambiente didático.")
    print("[!] Os arquivos .simulado NÃO serão removidos.\n")

    for arquivo in arquivos:
        nome_original = arquivo.name[:-len(EXTENSAO_SIMULADA)]

        destino = PASTA_TESTE / f"restaurado_{nome_original}"

        dados = arquivo.read_bytes()
        dados_restaurados = descriptografar_simulado(dados)

        destino.write_bytes(dados_restaurados)

        print(f"[OK] Simulado:   {arquivo.name}")
        print(f"     Restaurado: {destino.name}")

    print("\n[+] Descriptografia simulada concluída.")
    print("[+] Os arquivos .simulado permanecem intactos.")


if __name__ == "__main__":
    main()
