#   Configuración de MariaDB en NAS Synology.
---------------------------------------------------------------------------------

[Guía Instalación](https://mysqlya.com.ar/bases-de-datos/acceder-a-base-de-datos-maria-db-synology/)

---------------------------------------------------------------------------------

### Pasos

- Instalación MariaDB desde el Centro de Paquetes.
- Solicitará que establezcas una contraseña para el usuario administrativo 'root'.
    NasMariaDB4+
- Cambiamos el puerto por defecto 3306 por seguridad al 7954.

---------------------------------------------------------------------------------

#### Configuración Inicial: Acceso Remoto con phpMyAdmin

- Instalar phpMyAdmin desde el Centro de Paquetes, pedirá por dependencia el paquete PHP y Web Station.
- En phpMyAdmin  > Cuentas de usuarios. Buscar la cuenta por defecto, 'root' y editar los privilegios. Cambiar el Nombre de host a %, poniendo “Cualquier servidor”, y te pide poner nueva password (he puesto la anterior). 

 - Damos de alta el usuario:  usuario (Mcjavier9+)

 - Cadena conexión a la base de datos:
    
    mariadb_path = "mysql+mysqldb://usuario:Mcjavier9+@javicu.synology.me:7954/pruebacrud"
    conn = st.connection("sql", url=db_path)
