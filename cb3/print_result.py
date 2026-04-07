from main import success_rate, average_nfe

def print_table_results() -> None:
    print("\n" + "="*40)
    print("         RESULTADOS FINAIS")
    print("="*40)
    print("Problema: Camel Back - 3 Three Hump (CB3)")
    print(f"Taxa de Sucesso (SR): {success_rate:.2f}%")
    print(f"Média de NFE: {average_nfe:.2f}")
    print("="*40)