def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Monto total
    monto1 = 150.00
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra 1: Monto = ${monto1:.2f}, Descuento = ${descuento1:.2f}, Total a pagar = ${total1:.2f}")

    # Monto total y porcentaje
    monto2 = 200.00
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total2 = monto2 - descuento2
    print(
        f"Compra 2: Monto = ${monto2:.2f}, Descuento ({porcentaje2}%) = ${descuento2:.2f}, Total a pagar = ${total2:.2f}")