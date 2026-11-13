# Proyecto de Web Scraping con Automatización DevOps (EA2)

## Descripción del Proyecto
Este proyecto forma parte de la **Evidencia de Aprendizaje 2**, enfocado en la aplicación de control de versiones con Git/GitHub y la implementación de un pipeline de integración continua (**CI/CD**) mediante **GitHub Actions**. El objetivo principal es extraer información automatizada de un producto de comercio electrónico de Amazon (ASIN: `B0HFMCH32K`) utilizando Python, asegurando que cada cambio en el código pase pruebas automáticas antes de integrarse al entorno de producción (`main`).

---

## Tecnologías y Librerías Utilizadas
* **Lenguaje:** Python 3.10 / 3.15
* **Librerías de Scraping:** `BeautifulSoup` (análisis HTML), `Requests` (peticiones HTTP), `Pandas` (procesamiento de datos tabulares).
* **Control de Versiones:** Git y GitHub (Gestión de ramas y flujos colaborativos).
* **CI/CD / DevOps:** GitHub Actions (Automatización de pruebas en entornos virtuales Linux).

---

## Estructura del Repositorio
```text
Proyecto-Scraping-DevOps/
│
├── .github/
│   └── workflows/
│       └── ci.yml          # Configuración del pipeline de CI/CD (GitHub Actions)
├── .gitignore              # Archivos excluidos del control de versiones (.venv/)
├── main.py                 # Script principal de Web Scraping
├── requirements.txt        # Dependencias del proyecto (pandas, beautifulsoup4, requests)
└── README.md               # Documentación oficial del proyecto