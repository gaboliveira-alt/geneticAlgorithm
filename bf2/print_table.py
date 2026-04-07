def print_table_results(success_rate: float, average_nfe: float) -> None:
    print("\n" + "="*40)
    print("         RESULTADOS FINAIS")
    print("="*40)
    print("Problema: Bohachevsky 2 (BF2)")
    print(f"Taxa de Sucesso (SR): {success_rate:.2f}%")
    print(f"Média de NFE: {average_nfe:.2f}")
    print("="*40)
