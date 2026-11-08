def bensiini (gallonat):
    return gallonat * 3.785


while True:
    gallonat = float(input("anna gallonamäärä:"))
    if gallonat < 0:
        break

    litrat = bensiini(gallonat)
    print(f"gallonaa on litroissa: {litrat:.2f}")


    
        


    