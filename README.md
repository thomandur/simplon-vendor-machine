# Simplon - Distributeur de produits

## Consignes :

**Le distributeur**
* Le distributeur contient 100 cannettes.
* Le distributeur contient 100 paquets de cacahuètes.
* Le distributeur contient 11,50 €.
* Une cannette vaut 1,50 €.
* Un paquet de cacahuète vaut 1€

**Le consommateur**
* Un consommateur peut acheter une cannette ou des cacahuètes. Le stock diminue de 1. La trésorerie est également modifiée.
* Le distributeur rend la monnaie.

**Le technicien**
* Le technicien doit s’authentifier.
* Le technicien peut afficher l’état du stock et de la trésorerie.
* Le technicien peut ajouter des cannettes et des cacahuètes.
* Le technicien peut vider la caisse.

**Persister la donnée dans un `csv` par exemple, et remodifier le code déjà effectué pour gérer la mécanique de sérialisation et de deserialisation :**

---
## Programme :
**Execution**
- Dans son terminal
```
cd simplon-vendor-machine
python main.py
```


**Architecture des fichiers**
- `main.py` : Execution du code
- `vendor.py` : Gestion du distributeur
- `data.py` : Gestion des données
- `data.csv` : Base de données
