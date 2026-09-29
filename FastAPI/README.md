# Servicio de Chat en FastAPI (Arquitectura en 3 Capas)

Proyecto desarrollado para prácticas profesionales. Adapta el diseño de **Spring Boot / Spring Data JPA** a **FastAPI / SQLModel** conectado a **PostgreSQL 17**.

## Mapeo Arquitectónico (Spring Boot vs FastAPI)

| Componente Spring Boot | Componente equivalente en FastAPI | Descripción |
| :--- | :--- | :--- |
| `@RestController` / `@RequestMapping` | `APIRouter` (`chat_controller.py`) | Manejo de endpoints HTTP |
| `@Service` | `ChatService` (`chat_service.py`) | Capa de lógica de negocio |
| `JpaRepository<T, ID>` | `BaseRepository[ModelType]` (`base_repository.py`) | Métodos CRUD genéricos estilo Hibernate |
| `@Entity` | `ChatMessage` (`chat_message.py`) | Modelo SQLModel / SQLAlchemy |
| DTOs / Commands | Pydantic Models (`ChatDto`, `NewChatMessageCommand`) | Transferencia de datos y validación |

## Instrucciones de Ejecución

1. Crear y activar entorno virtual:
   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1