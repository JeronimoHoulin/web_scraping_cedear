# Scrape de CEDEAR's para TC MEP, y BTC tasa con contratos futuros.
Cedear Scrape incluye trés formas de tomar data de diferentes páginas de internet, 
en específico; cotizaciones de acciones de EEUU, sus respectivos CEDEARS y el TC MEP. 

Primero, utilizando la librería BeautifulSoup, ó BS4. Luego hay un ejemplar de como Pandas utiliza una estructura para encontrar tablas en diferentes páginas. 
Y por último una librería que deriva de Yahoo Finance, YFinance, como para una solución más fácil. 

Para la primera, se incluye un uso de la función "re", para limpiar y ordenar los str que hallamos y tornarlos en floats. 

Por último, una breve función con todas estas variables que nos devuelva una conclusión acerca de si el CEDEAR está barato respecto a su cotización en EEUUU, 
es decir si su TC implícito es menor al MEP. 

-- 0 --

El script de BTC muestra el estado del carry trade para los contratos futuros de BTC.
