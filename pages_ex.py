import pdfplumber

def lire_pages_exclues(fichier_pages):
    with open(fichier_pages, 'r') as f:
        pages_exclues = f.read().split(',')

    return [int(page) for page in pages_exclues]

def nombre_de_pages_pdf(fichier_pdf):
    with pdfplumber.open(fichier_pdf) as pdf:
        return len(pdf.pages)

def pages_non_exclues(nb_pages, pages_exclues):
    return [page for page in range(1, nb_pages + 1) if page not in pages_exclues]

def ecrire_pages_non_exclues(pages_incluses, fichier_output):
    with open(fichier_output, 'w') as f:
        f.write(','.join(str(page) for page in pages_incluses))

def main():
    fichier_pdf = "labels.pdf"
    fichier_pages = "pages.txt"

    pages_exclues = lire_pages_exclues(fichier_pages)
    nb_pages = nombre_de_pages_pdf(fichier_pdf)
    pages_incluses = pages_non_exclues(nb_pages, pages_exclues)

    fichier_output = "enveloppes.txt"
    ecrire_pages_non_exclues(pages_incluses, fichier_output)

    print(f"Nombre de pages dans le fichier PDF : {nb_pages}")
    print(f"Liste des pages non exclues sauvegardée dans le fichier {fichier_output}")

if __name__ == "__main__":
    main()
