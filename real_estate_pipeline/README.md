```markdown
# 💳 Dashboard de Pilotage Financier & Détection de la Fraude Bancaire

## 📖 Présentation du projet

Ce projet consiste à concevoir un pipeline de données complet et un tableau de bord interactif permettant de suivre l'activité bancaire, d'analyser la performance du portefeuille de prêts et de détecter les transactions suspectes (fraudes). Il s'adresse aux analystes financiers, aux gestionnaires de risques et à la direction des opérations bancaires.

Le système centralise et transforme les données brutes issues des comptes, clients, prêts et transactions afin de faciliter le suivi des indicateurs clés (KPI) et d'optimiser la prise de décision. L'objectif principal est de convertir des volumes importants de données bancaires en informations stratégiques grâce à une architecture moderne (Medallion : Bronze, Silver, Gold) et des visualisations BI interactives.

---

## 🎯 Problématique

Les institutions financières font face à des volumes massifs de données hétérogènes (transactions, profils clients, demandes de prêts), souvent stockées sous forme de fichiers bruts. Cette dispersion rend difficile :
1. La détection rapide et efficace des transactions frauduleuses.
2. Le suivi précis du taux de défaut sur les prêts accordés.
3. Le maintien de la qualité des données à travers les différentes étapes de transformation.

La solution proposée repose sur l'ingestion automatisée des données brutes vers un Data Warehouse (architecture Bronze, Silver, Gold), transformées via **dbt**, orchestrées par **Apache Airflow**, puis restituées dans un tableau de bord **Power BI**.

---

## 🚀 Fonctionnalités principales

- **Ingestion automatisée** des données brutes (`accounts.csv`, `customers.csv`, `loans.csv`, `transactions.csv`) vers la couche Bronze.
- **Nettoyage et standardisation** des données avec dbt (Silver Layer : `stg_accounts`, `stg_customers`, `stg_loans`, `stg_transactions`).
- **Tests automatisés de qualité de données** (unicité, non-nullité, contraintes métier).
- **Modélisation décisionnelle en étoile** (Gold Layer : `dim_accounts`, `dim_customers`, `dim_date`, `fct_loans`, `fct_transactions`).
- **Orchestration globale du pipeline** via Apache Airflow (`finance_bank_dag.py`).
- **Suivi et détection de la fraude bancaire** en temps réel/différé.
- **Analyse de la performance des prêts** (taux d'approbation, encours, taux de défaut).
- **Filtrage dynamique** par statut de prêt, période, type de transaction et profil client.

---

## 🛠️ Technologies utilisées

| Technologie | Utilisation |
| :--- | :--- |
| **Snowflake / SQL** | Data Warehouse cloud (Stockage des couches Bronze, Silver, Gold) |
| **dbt (Data Build Tool)** | Transformation, modélisation en étoile (`dim_`, `fct_`) et tests de qualité |
| **Apache Airflow** | Orchestration et automatisation du pipeline ETL/ELT |
| **Python** | Scripts d'ingestion (`load_to_bronze.py`, `config.py`) et analyse exploratoire (`eda.ipynb`) |
| **Power BI** | Création des tableaux de bord interactifs et restitution BI |
| **Docker / Docker Compose** | Containerisation de l'environnement de développement (`docker-compose.yml`) |
| **Git & GitHub** | Gestion de version du projet et du code |

---

## 📂 Structure du projet

```text
FINANCE-BANK/
│
├── notebooks/
│   └── eda.ipynb                   # Analyse exploratoire des données (EDA)
│
├── real_estate_pipeline/
│   └── data/raw/
│       ├── accounts.csv            # Données brutes des comptes
│       ├── customers.csv           # Données brutes des clients
│       ├── loans.csv               # Données brutes des prêts
│       └── transactions.csv        # Données brutes des transactions
│
├── dbt_project/
│   ├── macros/
│   │   └── generate_schema_name.sql
│   ├── models/
│   │   ├── bronze/
│   │   │   └── sources.yml
│   │   ├── silver/
│   │   │   ├── silver.yml
│   │   │   ├── stg_accounts.sql
│   │   │   ├── stg_customers.sql
│   │   │   ├── stg_loans.sql
│   │   │   └── stg_transactions.sql
│   │   └── gold/
│   │       ├── dim_accounts.sql
│   │       ├── dim_customers.sql
│   │       ├── dim_date.sql
│   │       ├── fct_loans.sql
│   │       ├── fct_transactions.sql
│   │       └── gold.yml
│   ├── dbt_project.yml
│   ├── packages.yml
│   └── profiles.yml
│
├── ingestion/
│   ├── config.py                   # Configuration de la connexion à la base de données
│   ├── load_to_bronze.py           # Script d'ingestion des CSV vers la couche Bronze
│   └── requirements.txt
│
├── orchestration/dags/
│   └── finance_bank_dag.py         # DAG Airflow orchestrant le pipeline complet
│
├── powerbi/                        # Fichiers et rapports Power BI
├── .env
├── .gitignore
├── docker-compose.yml              # Fichier de déploiement des conteneurs
└── README.md
```

---

## ⚙️ Installation

### Prérequis

* Docker & Docker Compose
* Power BI Desktop
* Git

### 1. Cloner le dépôt

```bash
git clone [https://github.com/Ilham-Errady/FINANCE-BANK.git](https://github.com/Ilham-Errady/FINANCE-BANK.git)
```

### 2. Accéder au dossier

```bash
cd FINANCE-BANK
```

### 3. Lancer l'environnement (Airflow & dbt)

```bash
docker-compose up -d
```

### 4. Lancer l'ingestion et les modèles dbt

```bash
# Ingestion des données brutes vers la couche Bronze
python ingestion/load_to_bronze.py

# Exécution des transformations dbt
cd dbt_project
dbt deps
dbt run
dbt test
```

### 5. Ouvrir le tableau de bord

Ouvrir les fichiers du dossier `powerbi/` dans Power BI Desktop et vérifier la connexion aux tables de la couche `GOLD`.

---

## 📊 Tableau de bord

Le rapport est composé de deux pages principales d'analyse décisionnelle.

### 🛡️ Vue Détection de la Fraude

Cette page permet de suivre :

* Nombre total de transactions et volume financier associé.
* Nombre et pourcentage de transactions suspectes/frauduleuses.
* Répartition géographique et temporelle des tentatives de fraude.
* Montant total des pertes évitées.

### 🏦 Vue Analyse des Prêts (Loans)

Cette page permet de visualiser :

* Volume total des prêts accordés et montant moyen.
* Répartition des prêts par statut (`APPROVED`, `PENDING`, `REJECTED`, `DEFAULT`).
* Taux de remboursement et taux de défaut.
* Profil des emprunteurs et encours global.

---

## 📈 KPI utilisés

* **Montant Total des Transactions**
* **Taux de Fraude (%)**
* **Volume des Prêts Accordés**
* **Taux de Défaut de Paiement**
* **Montant Moyen par Prêt**
* **Nombre de Clients Actifs**
* **Score de Risque Moyen**

---

## 📷 Captures d'écran

### Détection de la Fraude

*Cette vue présente la répartition des transactions suspectes et les indicateurs d'alerte.*

### Analyse du Portefeuille de Prêts

*Cette vue permet d'analyser le portefeuille de prêts, les statuts d'approbation et les taux de risque.*

---

## 👩‍💻 Contribution personnelle

Projet réalisé par **Rime ERRADY**.

Mes principales contributions sont :

* Conception de l'architecture Medallion (Bronze, Silver, Gold).
* Développement des scripts d'ingestion Python (`load_to_bronze.py`).
* Création et modélisation dbt :
* Couche Silver : `stg_accounts`, `stg_customers`, `stg_loans`, `stg_transactions`.
* Couche Gold : `dim_accounts`, `dim_customers`, `dim_date`, `fct_loans`, `fct_transactions`.
* Mise en place des tests de qualité de données.
* Automatisation du flux complet via le DAG Airflow (`finance_bank_dag.py`).
* Modélisation en étoile et création des tableaux de bord interactifs sur **Power BI**.

---

## ⚠️ Difficultés rencontrées

### 1. Gestion des valeurs nulles et données orphelines

* **Problème :** Certaines transactions contenaient des identifiants clients absents de la table principale, générant des lignes vides dans les visuels Power BI.
* **Solution :** Implémentation de fonctions `COALESCE` et `NULLIF` dans les modèles staging dbt (`stg_customers.sql`, `stg_transactions.sql`) pour attribuer une valeur par défaut (`'Unknown'`) et assainir la couche Silver.

### 2. Optimisation du modèle en étoile

* **Problème :** Ralentissement lors des requêtes d'agrégation entre la table de faits des prêts (`fct_loans`) et les dimensions clients/comptes.
* **Solution :** Restructuration propre des tables de dimensions (`dim_accounts`, `dim_customers`, `dim_date`) dans la couche Gold de dbt afin de garantir une modélisation en étoile fluide et rapide.
