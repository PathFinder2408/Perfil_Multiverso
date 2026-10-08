# Perfil Multiverso 🚀

Plataforma integral desarrollada en Django para la gestión y exposición de portafolios profesionales. El sistema consolida proyectos de Obras Civiles y Arquitectura TI, proporcionando un panel administrativo transaccional y una API RESTful segura.

## 📌 Problemática Abordada
La organización necesitaba centralizar la información de sus profesionales y transacciones (como la asignación de ingenieros a obras) y exponer esta información a otras plataformas de manera segura. El desafío principal era garantizar que los datos sensibles (RUT, teléfonos, sueldos) no quedaran expuestos al público, implementando estrictos controles de acceso.

## 🛠️ Stack Tecnológico
*   **Backend:** Python 3.14 / Django 6.1
*   **API:** Django REST Framework (DRF)
*   **Base de Datos:** MySQL 8.0 (vía XAMPP en local y Nativo en AWS)
*   **Frontend:** HTML5, Bootstrap 5, Crispy Forms
*   **Seguridad:** JSON Web Tokens (SimpleJWT), Autenticación por Grupos (RBAC)
*   **Despliegue:** Nginx, Gunicorn, AWS EC2, Ubuntu Server

## ⚙️ Características Principales
*   **Operaciones CRUD completas** desde la interfaz web.
*   **Carga de archivos multimedia** (`ImageField` / `FileField`).
*   **Seguridad y Roles:** Perfiles de Administrador, Operador y Consulta.
*   **Transacciones Seguras:** Uso de `@transaction.atomic` para prevenir corrupción de datos en escrituras simultáneas.
*   **API RESTful:** Endpoints autogenerados y protegidos por token JWT.
*   **Serializador Dinámico:** La API oculta automáticamente los campos confidenciales dependiendo de si el token pertenece a un rol administrativo o de consulta.

## 📖 Documentación de API
El proyecto cuenta con documentación autogenerada mediante **Swagger (OpenAPI 3.0)**.
Para acceder a la documentación interactiva, visita el endpoint:
`/api/docs/`

## 🚀 Despliegue en AWS EC2
Este proyecto está optimizado para su ejecución continua en un servidor Linux (Ubuntu) utilizando Gunicorn como servidor de aplicaciones y Nginx como proxy inverso. Las configuraciones sensibles de la base de datos se manejan mediante variables de entorno (`.env`).
