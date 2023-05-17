import sys
import re
import pdfplumber

def chercher_commandes(fichier_pdf, commandes):
    resultats = {commande: [] for commande in commandes}

    with pdfplumber.open(fichier_pdf) as pdf:
        num_pages = len(pdf.pages)

        for commande in commandes:
            for i in range(num_pages):
                page = pdf.pages[i]
                texte_page = page.extract_text()
                if re.search(rf'\b{commande}\b', texte_page):
                    resultats[commande].append(i + 1)

    return resultats

def separer_resultats(resultats):
    commandes_avec_doublons = {cmd: pages for cmd, pages in resultats.items() if len(pages) > 1}
    commandes_sans_doublon = [page for pages in resultats.values() for page in pages if len(pages) == 1]
    commandes_introuvables = [cmd for cmd, pages in resultats.items() if len(pages) == 0]

    return commandes_avec_doublons, commandes_sans_doublon, commandes_introuvables

def ecrire_resultats_dans_fichier(commandes_avec_doublons, commandes_sans_doublon, commandes_introuvables, nom_fichier):
    with open(nom_fichier, 'w') as f:
        f.write("Commandes sans doublon: ")
        f.write(','.join(str(page) for page in commandes_sans_doublon))
        f.write("\n\nCommandes avec doublons:\n")
        for commande, pages in commandes_avec_doublons.items():
            f.write(f"Commande {commande}: {','.join(str(page) for page in pages)}\n")
        f.write("\nCommandes introuvables: ")
        f.write(','.join(str(cmd) for cmd in commandes_introuvables))

if __name__ == "__main__":
    fichier_pdf = "labels.pdf"
    commandes = ['1680', '1683', '1686', '1687', '1689', '1707', '1713', '1715', '1722', '1736', '1738', '1748', '1755', '1762', '1767', '1777', '1778', '1781', '1789', '1794', '1795', '1797', '1800', '1846', '1872', '1875', '1887', '1895', '1896', '1906', '1910', '1940', '1966', '1968']

    resultats = chercher_commandes(fichier_pdf, commandes)
    commandes_avec_doublons, commandes_sans_doublon, commandes_introuvables = separer_resultats(resultats)
    nom_fichier_output = "pages_commandes.txt"
    ecrire_resultats_dans_fichier(commandes_avec_doublons, commandes_sans_doublon, commandes_introuvables, nom_fichier_output)

    print(f"Résultats sauvegardés dans le fichier {nom_fichier_output}.")
