import base64

KEY = "r0btcc"
SHIFT = 39 % 26 

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
        raise ValueError("")
    b64 = unshifted[:-len(KEY)]
    try:
        decoded = base64.b64decode(b64.encode('utf-8')).decode('utf-8')
    except Exception as e:
        raise ValueError("" + str(e))
    return decoded

if __name__ == "__main__":
    print("Choisissez votre choix :")
    print("- Encrypt (1)")
    print("- Decrypt (2)")
    choice = input("Entrez votre choix (1 ou 2) : ").strip()

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

    else:
        print("Choix invalide.")
