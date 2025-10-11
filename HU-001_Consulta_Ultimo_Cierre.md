# [HU-XXX] Ejemplo Historia de Usuario

## 📖 Historia de Usuario

**Como** usuario del sistema  
**Quiero** consultar los saldos consolidados del último cierre procesado  
**Para** conocer el estado financiero general de la cartera en una fecha específica.

---

## 🔁 Flujo Esperado

1. El usuario obtiene la fecha de proceso desde la interfaz.
2. El sistema consume el endpoint `/api/v1/cartera/precierre/saldos_consolidados?fecha_proceso=YYYY-MM-DD`.
3. El backend consulta la base de datos de Réplica filtrando por `pCieCarFecCie`.
4. Se realiza la suma de los valores consolidados para los campos:
   - `pCieCarSalAct` / Capital  
   - `pCieCarIntCau` / Intereses causados  
   - `pCieCarIntCon` / Intereses contingentes

---

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET con parámetro `fecha_proceso`.
- [ ] Se valida que la fecha recibida tenga registros en la tabla `preciecar`.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura JSON en caso exitoso:

```json
{
  "mensaje": "Consulta de saldos exitosa",
  "data": {
    "fecha_proceso": "2025-07-31",
    "capital_total": 8500000000,
    "intereses_causados": 2400000,
    "intereses_contingentes": 1200000
  },
  "success": true
}
```

- [ ] Si no existen datos, se retorna:

```json
{
  "mensaje": "No existen datos consolidados para la fecha indicada",
  "data": {
    "fecha_proceso": "2025-07-31",
    "capital_total": 0,
    "intereses_causados": 0,
    "intereses_contingentes": 0
  },
  "success": false
}
```

---

## 🚀 Endpoint – Consulta del Último Cierre

- **Método HTTP:** `GET`  
- **Ruta:** `/api/v1/cartera/precierre/saldos_consolidados`

---

## 🧪 Casos de Prueba Funcional

### ✅ Caso 1:
- **Precondición:** Existen registros con la fecha proporcionada.  
- **Acción:** GET `/api/v1/cartera/precierre/saldos_consolidados?fecha_proceso=2025-06-30`.  
- **Resultado esperado:** JSON con valores consolidados correctos y `success: true`.

### ✅ Caso 2:
- **Precondición:** No existen registros con la fecha.  
- **Resultado esperado:** JSON con valores en 0 y `mensaje: "No existen saldos consolidados para la fecha proporcionada"`.

### ❌ Caso 3:
- **Precondición:** Parámetro `fecha_proceso` con formato incorrecto.  
- **Resultado esperado:** Código 400 y mensaje `"Formato de fecha no válido. Debe ser YYYY-MM-DD"`.

### ❌ Caso 4:
- **Precondición:** Error en la base de datos o conexión.  
- **Resultado esperado:** Código 503 y mensaje `"No fue posible consultar los saldos consolidados"`.

---

## ✅ Definición de Hecho

- [ ] El endpoint entrega información correctamente según la fecha.  
- [ ] Los valores consolidados son exactos y numéricos.  
- [ ] La respuesta JSON cumple con el contrato definido.  
- [ ] Pruebas unitarias y funcionales ejecutadas y documentadas.  
- [ ] Endpoint documentado en Swagger / OpenAPI.  
- [ ] Manejo de errores implementado (400, 503).

---

© 2025 - Documento técnico de Historia de Usuario (HU-XXX)
