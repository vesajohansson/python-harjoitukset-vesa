leiviskä = float (input("syötä leiviskät = "))


naulat = float (input("syötä naulojen lukumäärä = "))


luodit = float (input("syötä luotien lukumäärä = "))


grammat_yhteensä = leiviskä * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3


kg = grammat_yhteensä // 1000


jäljellä_grammat = grammat_yhteensä % 1000


print(f"Massa nykymittojen mukaan: {kg:.0f} kilogrammaa ja {jäljellä_grammat:.2f} grammaa.")