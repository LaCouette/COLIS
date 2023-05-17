import pandas as pd

def calculer_couts_expedition(file_name, output_file):
    data = pd.read_csv(file_name)
    commandes = data.groupby("Name")["Lineitem quantity"].sum().reset_index(name="nombre d'articles")
    commandes_pays = data.groupby("Name")["Shipping Country"].first().reset_index(name="pays")

    commandes = commandes.merge(commandes_pays, on="Name")

    def count_and_list_commandes(condition):
        filtered = commandes[condition]
        return len(filtered), [str(x).replace("#", "") for x in filtered["Name"]]

    conditions_pays = {
        "FR": [
            ("moins de 9 articles", commandes["nombre d'articles"] < 9, 4.4),
            ("de 9 à 17 articles", (9 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 17), 4.9),
            ("de 18 à 33 articles", (18 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 33), 6.5),
            ("de 34 à 50 articles", (34 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 50), 6.7),
        ],
        "BE": [
            ("moins de 9 articles", commandes["nombre d'articles"] < 9, 4.6),
            ("de 9 à 17 articles", (9 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 17), 5.4),
            ("de 18 à 33 articles", (18 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 33), 6.8),
            ("de 34 à 50 articles", (34 <= commandes["nombre d'articles"]) & (commandes["nombre d'articles"] <= 50), 7.1),
        ],
    }

    cout_total = 0

    with open(output_file, "w") as f:
        for pays, conditions in conditions_pays.items():
            f.write(f"\nCoûts d'expédition pour le pays : {pays}\n")

            cout_pays = 0

            for categorie, condition, cout in conditions:
                condition_pays = (commandes["pays"] == pays) & condition
                nombre, _ = count_and_list_commandes(condition_pays)
                cout_categorie = nombre * cout
                cout_pays += cout_categorie
                f.write(f"{categorie} : Nombre de commandes : {nombre} Coût: {cout_categorie}€\n")

            cout_total += cout_pays
            f.write(f"Coût total des expéditions pour le pays {pays}: {cout_pays}€\n")

        f.write(f"\nCoût total des expéditions (tous pays confondus): {cout_total}€\n")

if __name__ == "__main__":
    file_name = "cde.csv"
    output_file = "couts_expedition.txt"
    calculer_couts_expedition(file_name, output_file)
