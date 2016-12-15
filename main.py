import wcurve, random, secp256k1

curve = secp256k1.curve()

#Bob wants to buy bitcoin
b1 = random.SystemRandom().randint(1, curve.n - 1)
pk1 = b1 * curve.base_point

#B -> A : pk1

#Alices wants to sell bitcoin
b2 = random.SystemRandom().randint(1, curve.n - 1)
pk2 = b2 * pk1

#Alice transfers bitcoin to pk2
#When Bob and Alice meet, Bob scan b2 with a QR code
#and computes b = b1 * b2

b = b1 * b2
pk = b * curve.base_point

pk2x, pk2y = pk2.to_affine()
pkx, pky = pk.to_affine()

print("")
print(pk2x)
print(pkx)
print("------")
print(pk2y)
print(pky)

