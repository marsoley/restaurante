# Actividad 2 — Diseñando un Web Service

**Objetivo:**  
Diseñar una propuesta básica de un Web Service que solucione un problema específico.

---

## 🧭 Instrucciones
En grupo, seleccionen una de las situaciones identificadas en la Actividad 1 y diseñen un Web Service que dé solución al problema.  
El diseño debe incluir:
- Nombre del servicio.
- Descripción general.
- Recursos o datos que manejará.
- Tipo de operaciones (GET, POST, PUT, DELETE).
- Formato de respuesta (JSON o XML).

---

## ⚙️ Propuesta de diseño

**Situación elegida:** Pedido en una app de comida a domicilio.  

### Nombre del servicio:
`ServicioPedidosRestaurante`

### Descripción:
Permite gestionar pedidos en línea entre los clientes, los restaurantes y el sistema de reparto.  

### Recursos principales:
- **/usuarios** → manejo de clientes y repartidores.  
- **/restaurantes** → consulta del menú y precios.  
- **/pedidos** → creación, actualización y estado de los pedidos.  
- **/pagos** → validación de pagos electrónicos.

### Operaciones principales:
- **GET /pedidos/{id}** → obtener el estado de un pedido.  
- **POST /pedidos** → crear un nuevo pedido.  
- **PUT /pedidos/{id}** → actualizar información del pedido.  
- **DELETE /pedidos/{id}** → cancelar un pedido.

### Formato de respuesta:
```json
{
  "id_pedido": 105,
  "estado": "en preparación",
  "restaurante": "El Sabor Criollo",
  "total": 25000
}
