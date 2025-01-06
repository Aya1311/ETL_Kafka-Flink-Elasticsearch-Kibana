# ETL Kafka-Flink-Elasticsearch-Kibana

## Description
Ce projet met en œuvre une architecture ETL (Extraction, Transformation, Chargement) en streaming temps réel en utilisant des outils modernes tels que Kafka, Flink, Elasticsearch, et Kibana. Le but est de collecter, traiter et visualiser des données provenant de flux d'informations en temps réel.

## Architecture

### Diagramme de l'architecture
```plaintext
API NewsAPI --> Kafka Producer --> Kafka Topic
             --> Flink (Streaming & Transformation)
             --> Elasticsearch (Indexation)
             --> Kibana (Visualisation)
```

### Pipeline de traitement :
1. **Extraction** : Les nouvelles sont collectées depuis l'API NewsAPI par un producteur Kafka.
2. **Transformation** : Flink traite les données en streaming, en appliquant des transformations et nettoyages.
3. **Chargement** : Les données traitées sont indexées dans Elasticsearch.
4. **Visualisation** : Kibana permet d'explorer les données via des dashboards.

## Contenu du projet
Le projet est organisé comme suit :
```
C:\......\Etl_Kafka_Flink_Elasticsearch_Kibana
|
├── kafka_api_producer.py             # Producteur Kafka pour NewsAPI
├── kafka_api_consumer.py             # Consommateur Kafka pour lire les messages
├── kafka_flink_streaming.py          # Streaming Flink de Kafka vers Flink
├── kafka_flink_elasticsearch_streaming.py # Flink vers Elasticsearch
├── hdfs_consumer.py                  # Consommateur Kafka avec stockage HDFS
├── word count/pyflink_word_count.py             # Exemple de traitement Flink Word Count
└── README.md                         # Fichier README
```

## Prérequis
- **Système** : Linux
- **Langages et outils** :
  - Python 3.7+
  - Apache Kafka (v2.x)
  - Apache Flink (v1.17+)
  - Elasticsearch (v7.x)
  - Kibana (v7.x)
  - Bibliothèques Python : `kafka-python`, `pyflink`, `newsapi-python`, `requests`, `json`

## Installation

### Cloner le projet
```bash
git clone https://github.com/Aya1311/Etl_Kafka_Flink_Elasticsearch_Kibana.git
cd Etl_Kafka_Flink_Elasticsearch_Kibana
```

### Installer les dépendances
```bash
pip install -r requirements.txt
```

### Configuration
- Modifier les scripts pour refléter vos adresses IP et ports pour Kafka, Elasticsearch, et Flink si nécessaire.

## Exécution

### 1. Lancer Kafka
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

### 2. Créer un topic Kafka
```bash
bin/kafka-topics.sh --create --topic topic_aya --bootstrap-server localhost:9092
```

### 3. Exécution des scripts
- **Producteur Kafka** :
  ```bash
  python kafka_api_producer.py
  ```
- **Streaming Flink vers Elasticsearch** :
  ```bash
  python kafka_flink_elasticsearch_streaming.py
  ```

### 4. Visualisation dans Kibana
- Ajouter un index dans Kibana (nom de l'index : `demo_kafka_flink_streaming`).

## Fonctionnalités
- Streaming en temps réel avec Kafka.
- Traitement des données par Flink.
- Indexation et recherche via Elasticsearch.
- Visualisation dynamique avec Kibana.

### Auteur
Projet réalisé par Aya Laadaili dans le cadre d'une architecture ETL pour traitement de flux temps réel.
