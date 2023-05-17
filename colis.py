import pandas as pd

def analyse_commandes(file_name, output_file):
    data = pd.read_csv(file_name)
    commandes = data.groupby("Name")["Lineitem quantity"].sum().reset_index(name="nombre d'articles")

    def count_and_list_commandes(condition):
        filtered = commandes[condition]
        return len(filtered), [str(x).replace("#", "") for x in filtered["Name"]]

    plus_de_9, list_plus_9 = count_and_list_commandes(commandes["nombre d'articles"] > 9)
    moins_de_10, _ = count_and_list_commandes(commandes["nombre d'articles"] < 10)
    entre_10_21, list_10_21 = count_and_list_commandes((10 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 21))
    entre_22_28, list_22_28 = count_and_list_commandes((22 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 28))
    entre_29_35, list_29_35 = count_and_list_commandes((29 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 35))
    entre_36_70, list_36_70 = count_and_list_commandes((36 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 70))
    entre_71_84, list_71_84 = count_and_list_commandes((71 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 84))
    plus_de_84, list_plus_84 = count_and_list_commandes(commandes["nombre d'articles"] > 84)

    with open(output_file, "w") as f:
        f.write(f"Enveloppes (Nombre de commandes avec moins de 10 articles): {moins_de_10}\n")
        f.write(f"Colis M (Nombre de commandes avec 10 à 21 articles): {entre_10_21} Liste des numéros de commandes concernés: {list_10_21}\n")
        f.write(f"Colis L (Nombre de commandes avec 22 à 28 articles): {entre_22_28} Liste des numéros de commandes concernés: {list_22_28}\n")
        f.write(f"Colis XL (Nombre de commandes avec 29 à 35 articles): {entre_29_35} Liste des numéros de commandes concernés: {list_29_35}\n")
        f.write(f"Colis 2L (Nombre de commandes avec 36 à 70 articles): {entre_36_70} Liste des numéros de commandes concernés: {list_36_70}\n")
        f.write(f"Colis 2XL (Nombre de commandes avec 71 à 84 articles): {entre_71_84} Liste des numéros de commandes concernés: {list_71_84}\n")
        f.write(f"Colis Custom (Nombre de commandes avec plus de 84 articles): {plus_de_84} Liste des numéros de commandes concernés: {list_plus_84}\n")
        f.write(f"Liste de tous les colis: {list_plus_9}\n")

if __name__ == "__main__":
    file_name = "cde.csv"
    output_file = "resultats.txt"
    analyse_commandes(file_name, output_file)


