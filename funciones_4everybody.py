import mysql.connector

produccion = True
# produccion = False #Activar para pruebas

if produccion:
    ############################################# BASE DE DATOS LIMPIA #############################################
    # ENLACE ANTIGUO
    url = 'https://www.multiplay.com.pe/consultas/consulta-erp-productivo.php' # BD para pruebas de integración
    db = mysql.connector.connect(host="67.23.254.35",user="multipla_admin",passwd="multiplay123",database="multipla_erp_productivo")
    RUTA_WEB = '''https://www.multiplay.com.pe/productivo'''
    FTP_HOST = "ftp.multiplay.com.pe"
    FTP_USER = 'productivo@multiplay.com.pe'
    FTP_PASS = 'UGAGUXqiq5tA'
    print('BASE DE DATOS DEL PRODUCTIVO..')

    # ENLACE NUEVO
    # url = 'https://www.multiplayperu.com/consultas/consulta-erp-productivo.php' # BD para pruebas de integración
    # db = mysql.connector.connect(host="67.23.254.35",user="multipla_admin",passwd="multiplay123",database="multipla_erp_productivo")
    # RUTA_WEB = '''https://www.multiplayperu.com/productivo'''
    # FTP_HOST = "ftp.multiplayperu.com"
    # FTP_USER = 'productivo@multiplayperu.com'
    # FTP_PASS = 'UGAGUXqiq5tA'
    # print('BASE DE DATOS DEL PRODUCTIVO.. NUEVA RUTA..')

    rutaFacturacion="https://api.nubefact.com/api/v1/77a35fe6-d184-446e-9c0f-7f461959e71b"
    tokenFacturacion="b43d98af03c64c8191c84eacde631b79671b8cf51d8f45cf8ec0b706db619cec"
    tokenFacturacionT002="055fc3e198f648a4902fa4e12d59b988014a10f343c340bc9def7c95e96860ee"
else:
    ############################################## BASE DE DATOS DE PRUEBA #############################################
    url = 'https://www.multiplay.com.pe/consultas/consulta-prueba.php' # BD para pruebas de desarrollo
    db = mysql.connector.connect(host="67.23.254.35",user="multipla_admin",passwd="multiplay123",database="multipla_pruebas")
    RUTA_WEB = '''https://www.multiplay.com.pe/pruebas'''
    FTP_HOST = "ftp.multiplay.com.pe"
    FTP_USER = "pruebas@multiplay.com.pe"
    FTP_PASS = "multiplay123"
    print('BASE DE DATOS DE PRUEBA..')

    rutaFacturacion="https://api.nubefact.com/api/v1/2131942b-3fc3-459d-87bc-ba1dbb2b1ec5"
    tokenFacturacion="511ed830bdb14a098fa44bcf2535f14ae0a71ee9ff0b4e8fae4239593e551de4"


############################################## BASE DE DATOS DE PRUEBA v2 #############################################

# url = 'https://www.multiplay.com.pe/consultas/consulta-prueba-v2.php' # BD para datos reales
# db = mysql.connector.connect(host="67.23.254.35",user="multipla_admin",passwd="multiplay123",database="multipla_pruebas_v2")
# RUTA_WEB = '''https://www.multiplay.com.pe/productivo'''
# FTP_HOST = "ftp.multiplay.com.pe"
# FTP_USER = 'productivo@multiplay.com.pe'
# FTP_PASS = 'UGAGUXqiq5tA'
# print('BASE DE DATOS DE PRUEBAS V2..')

############################################## BASE DE DATOS LOCAL #############################################

# url = ''
# db = mysql.connector.connect(host="192.168.30.198",user="root",passwd="",database="multipla_pruebas")
# RUTA_WEB = '''https://www.multiplay.com.pe/productivo'''
# FTP_HOST = "ftp.multiplay.com.pe"
# FTP_USER = 'productivo@multiplay.com.pe'
# FTP_PASS = 'UGAGUXqiq5tA'
# print('BASE DE DATOS LOCAL..')
