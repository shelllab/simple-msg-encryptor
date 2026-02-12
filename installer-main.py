import base64

KEY = "r0btcc"
cryptnumb = int(input("Entrez votre profil (2 chiffres) : "))
SHIFT = 39 % cryptnumb

def caesar(text, shift_amount):
    out = []
    for c in text:
        if 'A' <= c <= 'Z':
            out.append(chr((ord(c) - ord('A') + shift_amount) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            out.append(chr((ord(c) - ord('a') + shift_amount) % 26 + ord('a')))
        else:
            out.append(c)
    return ''.join(out)

def encrypt(plain):
    b64 = base64.b64encode(plain.encode('utf-8')).decode('utf-8')
    with_key = b64 + KEY
    final = caesar(with_key, SHIFT)
    return final

def decrypt(cipher):
    unshifted = caesar(cipher, -SHIFT)
    if not unshifted.endswith(KEY):
        raise ValueError("Clé invalide ou texte corrompu.")
    b64 = unshifted[:-len(KEY)]
    try:
        decoded = base64.b64decode(b64.encode('utf-8')).decode('utf-8')
    except Exception as e:
        raise ValueError("Erreur de décodage : " + str(e))
    return decoded

while True:
    print("\nChoisissez votre choix :")
    print("- Encrypt (1)")
    print("- Decrypt (2)")
    print("- Quitter (3)")
    choice = input("Entrez votre choix (1, 2 ou 3) : ").strip()

    if choice == '1':
        msg = input("Entrez le message à encoder : ")
        out = encrypt(msg)
        print("Message encodé :", out)
    elif choice == '2':
        cipher = input("Entrez le texte encodé : ")
        try:
            out = decrypt(cipher)
            print("Message décodé :", out)
        except ValueError as err:
            print("Erreur :", err)
    elif choice == '3':
        print("BYE")
        break
    else:
        print("Choix invalide. Réessayez.")
