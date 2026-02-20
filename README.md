# Plateforme Web Conteneurisée (Docker et Cloud)

## 🎯 Objectif du projet
Déployer une application web conteneurisée
dans un contexte Cloud à l’aide de Docker
et Docker Compose.

Ce projet simule un déploiement applicatif
réel en environnement serveur, avec des
bonnes pratiques DevOps.

---

## 🧠 Compétences démontrées
- Conteneurisation avec Docker
- Création d’images Docker personnalisées
- Déploiement avec Docker Compose
- Gestion des ports et des réseaux
- Gestion des logs applicatifs
- Bonnes pratiques Cloud & DevOps
- Documentation technique structurée

---

## 🖥️ Environnement
- Système : Linux (Debian)
- Langage : Python (Flask)
- Conteneurisation : Docker
- Orchestration locale : Docker Compose

---

```md
## 📂 Structure du projet
```text
plateforme-web-conteneurisee
├── Dockerfile
├── docker-compose.yml
├── README.md
├── app
│   ├── app.py
│   └── requirements.txt
└── docs
    ├── 01-application-web.md
    └── 02-docker-and-compose.md

---

```bash
docker build -t plateforme-web:1.0 .
docker compose up -d
Accès à l’application :
http://localhost:5000

---


## 📘 Documentation
La documentation détaillée du projet est disponible
dans le dossier docs/ :
01 : Application web (Flask)
02 : Docker & Docker Compose

---

## 🧪 Tests et validation
L’application a été testée :
en local (Flask)
via Docker
via Docker Compose
Les logs applicatifs sont accessibles
via Docker et Docker Compose.

---

## 🎓 Contexte académique
Projet réalisé dans le cadre d’une montée
en compétences Cloud/DevOps

---

## 👤 Auteur
Youssouf Souleyman
GitHub : https://github.com/YOSO98
