# PROYECTO FINAL INGENIERIA DE SOFTWARE 2
- JUAN DE DIOS RODRIGUEZ PEREZ - 2210004
- Este proyecto esta conectado a la api de openai.
- Reemplazar en openai_api_key="" por la key correspondiente

# 🧠 Chat Inteligente con Integración a Google Calendar

- Este proyecto implementa un sistema de chatbot conversacional con agente basado en LangChain, que permite interactuar mediante comandos por consola o interfaz web (Flask). Además, cuenta con integración a Google Calendar y envío automático de correos y mensajes de WhatsApp para gestionar citas o interacciones con usuarios.

---

## 🚀 Características principales

- 💬 Interfaz web para chatear con un agente inteligente.
- 🧠 Backend con agentes de LangChain para procesamiento de lenguaje natural.
- 📅 Integración con Google Calendar API para agendamiento de eventos.
- 📧 Envío automático de correos electrónicos.
- 📲 Notificaciones por WhatsApp (requiere configuración).
- 🗃️ Persistencia del historial de conversación en MongoDB.

---

## 📁 Estructura del proyecto

- software2/
- ├── agenda.py # Script para Google Calendar API
- ├── app.py # Servidor Flask (interfaz web)
- ├── main.py # Interfaz CLI para pruebas
- ├── agents/ # Lógica de LangChain (agente inteligente)
- ├── CapaDatos/ # Modelos y acceso a MongoDB
- ├── CapaNegocio/ # Lógica de email, WhatsApp, y ruteo
- ├── CapaPresentacion/ # Flask + HTML
- ├── templates/index.html # Interfaz web del chat
- ├── test/ # Pruebas automáticas
- └── token.json # Token de autenticación Google (autogenerado)

---

## Ejecución

- python -m poetry install
- python -m poetry run python CapaPresentacion/app.py


## TEMAS A RESALTAR DEL PROYECTO

### Patrones de Diseño Aplicados

1. **Strategy**: Se utiliza en la función `route_query` para determinar qué acción ejecutar (agente LangChain, calendario, etc.), desacoplando el análisis de intención del flujo general del programa.

2. **Facade**: La clase `GoogleCalendarManager` centraliza y oculta la complejidad de autenticación y llamadas a la API de Google Calendar, proporcionando una interfaz clara al resto del sistema.

3. **MVC**: El sistema web basado en Flask sigue el patrón Modelo-Vista-Controlador, donde `Chat` y `Message` representan el modelo, las rutas de Flask el controlador, y `index.html` la vista.

---

### Antipatrón Identificado

- **God Object**: La clase `GoogleCalendarManager` concentra múltiples responsabilidades (API, DB, email, WhatsApp), lo que viola el principio de responsabilidad única. Se recomienda dividirla en componentes más pequeños.

---

### Caso Cotidiano

**Gestión de Citas Inteligente para una Clínica o Empresa de Servicios**  
El sistema permite a los usuarios:
- Chatear con un asistente virtual.
- Agendar y recibir recordatorios automáticos de sus citas.
- Registrar interacciones en una base de datos para seguimiento.




## ✅ Requisitos del Sistema

- 📌 Requisitos Funcionales
- RF01 – Registro de mensajes: El sistema debe registrar cada mensaje enviado y recibido en un historial de conversación almacenado en MongoDB.

- RF02 – Interfaz web interactiva: El sistema debe permitir al usuario interactuar con el agente mediante una interfaz web desarrollada con Flask.

- RF03 – Interfaz de consola alternativa: El sistema debe permitir la interacción desde línea de comandos para pruebas o uso básico.

- RF04 – Interpretación de mensajes con agente inteligente: El sistema debe procesar los mensajes del usuario usando un agente basado en LangChain.

- RF05 – Consulta de disponibilidad en Google Calendar: El sistema debe consultar si hay disponibilidad para una cita en el calendario del usuario autenticado.

- RF06 – Creación de eventos en Google Calendar: El sistema debe crear eventos en el calendario del usuario cuando se solicite una cita.

- RF07 – Envío de correo electrónico de confirmación: El sistema debe enviar un correo electrónico con los detalles de la cita al paciente o usuario.

- RF08 – Envío de mensaje de WhatsApp con confirmación: El sistema debe enviar un mensaje de WhatsApp al usuario con la información de la cita.

- RF09 – Registro de datos del paciente: El sistema debe guardar en la base de datos la información del paciente (nombre, edad, motivo de la consulta, etc.).

- RF10 – Visualización de respuestas del agente: El sistema debe mostrar las respuestas del agente en tiempo real en la interfaz web.

- 📌 Requisitos No Funcionales
- RNF01 – Accesibilidad multiplataforma: La aplicación debe ser accesible desde dispositivos móviles y navegadores modernos de escritorio.

- RNF02 – Seguridad en el manejo de credenciales: Las credenciales de API (Google, MongoDB, email, WhatsApp) deben almacenarse en variables de entorno y no estar en el código fuente.

- RNF03 – Tiempo de respuesta: El sistema debe responder a una consulta del usuario en menos de 2 segundos bajo condiciones normales.

- RNF04 – Persistencia y disponibilidad de datos: Toda la información registrada debe ser persistente y estar disponible mientras el sistema esté activo.

- RNF05 – Autenticación segura a Google Calendar: El acceso al calendario debe realizarse mediante OAuth 2.0, usando tokens protegidos y renovables.

- RNF06 – Mantenibilidad del código: El sistema debe estar estructurado en capas (datos, negocio, presentación) para facilitar el mantenimiento.

- RNF07 – Escalabilidad: El sistema debe permitir agregar nuevas funcionalidades (como nuevos agentes o canales de comunicación) sin afectar el funcionamiento existente.

- RNF08 – Tolerancia a errores: El sistema debe manejar fallos (por ejemplo, red o autenticación) sin interrumpir su ejecución, mostrando mensajes de error claros.

- RNF09 – Compatibilidad con pruebas automatizadas: El código debe ser modular y permitir la ejecución de pruebas unitarias sobre componentes clave.