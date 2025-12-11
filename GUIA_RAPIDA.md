# 🎯 GUÍA RÁPIDA DE USO - API_MANAGE

## 1️⃣ Instalación y Ejecución

### Paso 1: Instalar dependencias
```bash
cd API_MANAGE
pip install -r requirements.txt
```

### Paso 2: Ejecutar la aplicación
```bash
python main.py
```

---

## 2️⃣ Menú de Autenticación

```
==================================================
SISTEMA DE AUTENTICACIÓN - API_MANAGE
==================================================
1. Registrar nuevo usuario
2. Iniciar sesión
3. Salir
==================================================
```

### Registrar un usuario
```
Seleccione opción: 1
Ingrese nombre completo: Juan Pérez
Ingrese correo electrónico: juan@example.com
Ingrese contraseña: MiContraseña123
Confirme contraseña: MiContraseña123
```

✅ **Requisitos:**
- Nombre: No vacío
- Correo: Formato válido (contiene @)
- Contraseña: Mínimo 6 caracteres

### Iniciar sesión
```
Seleccione opción: 2
Ingrese correo electrónico: juan@example.com
Ingrese contraseña: MiContraseña123
```

---

## 3️⃣ Menú Principal

Una vez autenticado:

```
==================================================
MENÚ PRINCIPAL - API_MANAGE
Usuario: Juan Pérez
==================================================

GESTIÓN DE DATOS:
1. Obtener usuarios desde API
2. Ver usuarios en BD
3. Ver usuarios en API
4. Obtener publicaciones desde API
5. Ver publicaciones
6. Obtener comentarios desde API
7. Ver comentarios

OPERACIONES CRUD EN API:
8. Crear nuevo recurso (POST)
9. Actualizar recurso (PUT)
10. Eliminar recurso (DELETE)
11. Obtener un recurso (GET)

CUENTA:
12. Cerrar sesión
0. Salir
==================================================
```

---

## 4️⃣ Ejemplos de Operaciones CRUD

### 📥 Obtener datos desde API (Opción 1)
```
Seleccione opción: 1
[Descarga usuarios de JSONPlaceholder y guarda en BD local]
[OK] Usuarios descargados y guardados.
```

### ➕ Crear un recurso (Opción 8)
```
Seleccione opción: 8
¿Qué tipo de recurso desea crear?
1. Usuario
2. Publicación
3. Comentario

Seleccione opción: 1
Nombre: Carlos López
Nombre de usuario: carloslopez
Correo electrónico: carlos@example.com
Teléfono: 555-1234
Sitio web: carlos.com

📤 Enviando solicitud POST...
[OK] Usuario creado exitosamente!
📊 Respuesta:
{
  "name": "Carlos López",
  "username": "carloslopez",
  ...
  "id": 11
}
```

### 🔍 Obtener un recurso (Opción 11)
```
Seleccione opción: 11
¿Qué tipo de recurso desea obtener?
1. Usuario
2. Publicación
3. Comentario

Seleccione opción: 1
Ingrese ID del usuario: 1

📥 Enviando solicitud GET...
[OK] Usuario obtenido exitosamente!
📊 Datos:
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  ...
}
```

### ✏️ Actualizar un recurso (Opción 9)
```
Seleccione opción: 9
¿Qué tipo de recurso desea actualizar?
1. Usuario
2. Publicación
3. Comentario

Seleccione opción: 1
Ingrese ID del usuario: 1
Nombre: Leanne Graham (actualizado)
Nombre de usuario: Bret
...

📤 Enviando solicitud PUT...
[OK] Usuario actualizado exitosamente!
```

### 🗑️ Eliminar un recurso (Opción 10)
```
Seleccione opción: 10
¿Qué tipo de recurso desea eliminar?
1. Usuario
2. Publicación
3. Comentario

Seleccione opción: 1
Ingrese ID del usuario a eliminar: 11
¿Está seguro de que desea eliminar el usuario con ID 11? (s/n): s

📤 Enviando solicitud DELETE...
[OK] Usuario eliminado exitosamente!
```

---

## 5️⃣ Códigos de Respuesta HTTP

| Código | Significado | Acción |
|--------|-------------|--------|
| **200** | OK | ✅ Operación exitosa |
| **201** | Created | ✅ Recurso creado |
| **204** | No Content | ✅ Eliminado sin contenido |
| **400** | Bad Request | ❌ Datos inválidos |
| **401** | Unauthorized | ❌ No autenticado |
| **403** | Forbidden | ❌ Permiso denegado |
| **404** | Not Found | ❌ Recurso no existe |
| **500** | Server Error | ❌ Error en servidor |
| **502** | Bad Gateway | ❌ Conexión inestable |
| **503** | Unavailable | ❌ Servicio no disponible |
| **504** | Timeout | ⏱️ El servidor tardó demasiado |

---

## 6️⃣ Solución de Problemas Comunes

### Error: "No module named 'bcrypt'"
```bash
pip install bcrypt
```

### Error: "No module named 'requests'"
```bash
pip install requests
```

### Error: "Usuario no encontrado"
- Verificar que el email esté correcto
- Asegurarse de haber registrado el usuario primero

### Error: "Contraseña incorrecta"
- Revisar que la contraseña sea correcta
- Las contraseñas son sensibles a mayúsculas/minúsculas

### Error: "No se puede conectar a la API"
- Verificar conexión a internet
- Confirmar que https://jsonplaceholder.typicode.com esté disponible

### BD vacía después de Obtener datos
- Ejecutar nuevamente "Obtener usuarios desde API"
- Esperar a que se complete la descarga

---

## 7️⃣ Características de Seguridad

✅ **Contraseñas encriptadas** con bcrypt (12 rounds)  
✅ **Base de datos local** con SQLite  
✅ **Validación de entradas** en todos los formularios  
✅ **Manejo de errores** sin exposición de datos sensibles  
✅ **Confirmación** antes de eliminar datos  

---

## 8️⃣ Estructura de la BD

### Tabla: usuarios
```
id (PK)           → ID único
nombre            → Nombre del usuario registrado
correo            → Email (único)
contrasena_hash   → Contraseña encriptada
contrasena_salt   → Salt para encriptación
```

### Tabla: users (desde API)
```
id, name, username, email, phone, website, addressId, companyId
```

### Tabla: posts
```
id, title, body, userId
```

### Tabla: comments
```
id, name, email, body, postId
```

---

## 9️⃣ Tips y Trucos

💡 **Guardar datos locales primero**
```
Opción 1 → Obtener datos desde API
Opción 2 → Ver en BD local
```

💡 **Probar CRUD sin afectar datos reales**
- JSONPlaceholder simula las operaciones
- Los cambios no se persisten en la API real

💡 **Ver todas las tablas rápidamente**
```
2 → Usuarios en BD
5 → Publicaciones
7 → Comentarios
```

---

## 🔟 Contacto y Soporte

📧 Para más información, revisar:
- `README_COMPLETO.md` - Documentación completa
- `SOLUCION_PROBLEMAS.md` - Errores y soluciones
- Código fuente con comentarios en cada módulo

---

**¡Disfruta usando API_MANAGE!** 🚀
