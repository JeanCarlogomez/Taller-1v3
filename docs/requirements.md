markdown-it-py==3.0.0
mdurl==0.1.2
Pygments==2.18.0
rich==13.8.1

# Sistema de Gestión de Inventario

## Registro de Entidades
- El sistema debe permitir registrar un **producto** con sus atributos: nombre, descripción, precio, stock inicial y categoría a la que pertenece.
- El sistema debe permitir registrar una **categoría** con sus atributos: nombre y descripción.
- El sistema debe permitir registrar un **proveedor** con sus atributos: nombre, dirección, teléfono y la lista de productos que suministra.
- El sistema debe permitir registrar una **bodega** con sus atributos: nombre, ubicación, capacidad máxima y la lista de productos almacenados.

## Gestión de Stock
- El sistema debe permitir **agregar stock** a un producto existente, especificando la cantidad a ingresar.
- El sistema debe permitir **retirar stock** de un producto existente, especificando la cantidad a retirar.
- El sistema debe permitir **calcular el valor total del stock**, sumando el precio de cada producto por la cantidad disponible.

## Relaciones entre Entidades
- El sistema debe permitir **agregar un producto** a una categoría existente.
- El sistema debe permitir **eliminar un producto** de una categoría existente.
- El sistema debe permitir **agregar un producto** a la lista de productos suministrados por un proveedor existente.
- El sistema debe permitir **eliminar un producto** de la lista de productos suministrados por un proveedor existente.
- El sistema debe permitir **agregar un producto** a la lista de productos almacenados en una bodega existente, verificando si hay espacio disponible en la bodega.
- El sistema debe permitir **retirar un producto** de la lista de productos almacenados en una bodega, verificando que la cantidad a retirar no exceda el stock disponible en la bodega.
- El sistema debe permitir **consultar la disponibilidad** de un producto en una bodega específica.

## Consultas y Reportes
- El sistema debe permitir **consultar la información de un producto**, incluyendo su nombre, descripción, precio, stock actual, categoría a la que pertenece y proveedor.
- El sistema debe permitir **consultar la información de una categoría**, incluyendo su nombre, descripción y la lista de productos asociados.
- El sistema debe permitir **consultar la información de un proveedor**, incluyendo su nombre, dirección, teléfono y la lista de productos que suministra.
- El sistema debe permitir **consultar la información de una bodega**, incluyendo su nombre, ubicación, capacidad máxima y la lista de productos almacenados.
- El sistema debe permitir **generar informes de stock**, mostrando el stock total, stock por categoría, stock por proveedor y stock por bodega.
