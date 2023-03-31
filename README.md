# simulador-cryptos

Simulador de inversiones en cryptos

## Cómo lanzar el programa para usarlo

1. Crear un entorno virtual 
    
    ```
    # Windows
    python -m venv env

    # Mac/Linux
    python3 - venv env

    ```

2. Activar el entorno virtual

    ```
    # Windows
    env\Scripts\activate

    # Mac/Linux
    source ./env/bin/activate

    ´´´

3. Instalar las dependencias

    ```
    pip install -r requirements.txt

    ```


4. Hacer una copia del archivo '.env template' como '.env'

    ```
    # Windows
    copy .env_template .env

    # Mac/Linux
    cp .env_template .env
    
    ```

5. Editar el archivo '.env' y cambiar los valores de entorno necesarios. Por motivos de seguridad dejar la variable 'DEBUG' con el valor 'False'

6. Con el entorno virtual activo, lanzar la aplicación

    ```
    flask run
    ```



## Cómo lanzar el programa en desarrollo

1. Crear un entorno virtual 
    
    ```
    # Windows
    python -m venv env

    # Mac/Linux
    python3 - venv env

    ```

2. Activar el entorno virtual

    ```
    # Windows
    env\Scripts\activate

    # Mac/Linux
    source ./env/bin/activate

    ´´´

3. Instalar las dependencias

    ```
    pip install -r requirements.dev.txt

    ```


4. Hacer una copia del archivo '.env template' como '.env'

    ```
    # Windows
    copy .env_template .env

    # Mac/Linux
    cp .env_template .env
    
    ```

5. Editar el archivo '.env' y cambiar (o no) el valor 
'DEBUG' ('True'/'False') y pon tu 'SECRET KEY'

