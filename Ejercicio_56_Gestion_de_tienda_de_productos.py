""" 
1. Crea una clase llamada **`Producto`** con los siguientes atributos:
    - **`nombre`**: El nombre del producto.
    - **`precio`**: El precio del producto.
    - **`stock`**: La cantidad de unidades disponibles en el stock del producto.
2. La clase **`Producto`** debe tener los siguientes métodos:
    - **`__init__(self, nombre, precio, stock)`**: Método constructor que inicializa los atributos **`nombre`**, **`precio`** y **`stock`**.
    - **`mostrar_informacion(self)`**: Método que imprime la información del producto, mostrando su nombre, precio y stock.
    - **`agregar_stock(self, cantidad)`**: Método que permite aumentar el stock del producto en la cantidad especificada.
    - **`vender(self, cantidad)`**: Método que permite vender una cantidad específica del producto. Actualiza el stock y devuelve el monto total de la venta.
3. Desarrolla una clase llamada **`Tienda`** con los siguientes atributos:
    - **`productos`**: Una lista que almacena los productos disponibles en la tienda.
4. La clase **`Tienda`** debe tener los siguientes métodos:
    - **`__init__(self)`**: Método constructor que inicializa el atributo **`productos`** como una lista vacía.
    - **`agregar_producto(self, producto)`**: Método que permite agregar un producto a la lista de productos disponibles en la tienda.
    - **`mostrar_productos(self)`**: Método que muestra la información de todos los productos disponibles en la tienda.
    - **`buscar_producto(self, nombre)`**: Método que busca un producto por su nombre y devuelve su información.
    - **`vender_producto(self, nombre, cantidad)`**: Método que permite vender una cantidad específica de un producto. Actualiza el stock del producto y devuelve el monto total de la venta.
5. Desarrolla un programa principal que permita al usuario:
    - Crear instancias de la clase **`Producto`**.
    - Agregar productos a la tienda.
    - Mostrar la información de todos los productos disponibles en la tienda.
    - Buscar un producto por su nombre y mostrar su información.
    - Vender una cantidad específica de un producto y mostrar el monto total de la venta.
"""

