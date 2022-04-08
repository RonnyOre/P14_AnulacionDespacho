import sys
import requests
from datetime import datetime
from Funciones04 import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.request

# class Texto_Series(QDialog):
#     def __init__(self,item,codigo_material,cantidad_salida):
#         QDialog.__init__(self)
#         uic.loadUi("ERP_ALM_P027_RegistroSeries.ui",self)
#
#         global Item,Cod_Material,Cant_Salida
#
#         self.pbGrabar.clicked.connect(self.guardar)
#         self.pbEliminar.clicked.connect(self.eliminar)
#         self.pbSalir.clicked.connect(self.close)
#         self.leSeries_Insertadas.setReadOnly(True)
#
#         cargarIcono(self.pbGrabar, 'grabar')
#         cargarIcono(self.pbEliminar, 'darbaja')
#         cargarIcono(self.pbSalir, 'salir')
#         cargarIcono(self, 'erp')
#
#         Item=item
#         Cod_Material=codigo_material
#         Cant_Salida=cantidad_salida
#         self.mostrarDatos()
#
#     def mostrarDatos(self):
#         global listSeries
#         listSeries=[]
#         self.leSeries_Traspaso.setText(Cant_Salida)
#         try:
#             ItemSeries=dict_listSeries[Item]
#         except:
#             ItemSeries=[]
#         if ItemSeries != []:
#             flags = QtCore.Qt.ItemFlags()
#             flags = (QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
#             for dato in ItemSeries:
#                 rowPosition = self.tbwSeries.rowCount()
#                 self.tbwSeries.insertRow(rowPosition)
#                 info = QTableWidgetItem(dato)
#                 info.setFlags(flags)
#                 info.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
#                 self.tbwSeries.setItem(rowPosition, 0, info)
#                 self.leNro_Serie.clear()
#             cant_insertada = str(len(ItemSeries))
#             self.leSeries_Insertadas.setText(cant_insertada)
#             if cant_insertada == self.leSeries_Traspaso.text():
#                 self.leNro_Serie.setReadOnly(True)
#
#     def guardar(self):
#         if self.leSeries_Traspaso.text() == self.leSeries_Insertadas.text():
#             list_series = []
#             for row in range(self.tbwSeries.rowCount()):
#                 dato = self.tbwSeries.item(row,0).text()
#                 list_series.append(dato)
#             print(list_series)
#             k = Item
#             v = list_series
#             dict_temporal = {}
#             dict_temporal.setdefault(k,v)
#             dict_listSeries.update(dict_temporal)
#             print(dict_listSeries)
#             # global listSeries
#             # listSeries=[]
#             mensajeDialogo("informacion", "Información", "Salida de Series se grabó correctamente")
#             self.close()
#         else:
#             mensajeDialogo('error', "Error", "El Total de Series Insertadas debe ser igual al Total de Series a Traspasar")
#
#     def keyPressEvent(self, event):
#         flags = QtCore.Qt.ItemFlags()
#         flags = (QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
#         # try:
#         if event.key() == QtCore.Qt.Key_Return:
#             nro_serie = self.leNro_Serie.text()
#             if nro_serie != "":
#                 sqlSerie = '''SELECT Nro_Serie FROM `TAB_ALM_005 Registro de Nro. De series de la Empresa` WHERE Cod_Soc='%s' AND Cod_Planta='%s' AND Cod_Alm='%s' AND Cod_Mat='%s' AND Nro_Serie='%s' AND Tipo_Stock='%s' AND Estado_Serie='%s';''' %(Cod_Soc, Cod_Planta, Cod_Almacen, Cod_Material, nro_serie, 1, 2)
#                 dataSerie = consultarSql(sqlSerie)
#                 try:
#                     if nro_serie == dataSerie[0][0]:
#                         try:
#                             ItemSeries=dict_listSeries[Item]
#                             if nro_serie not in ItemSeries:
#                                 ItemSeries.append(nro_serie)
#                                 k = Item
#                                 v = ItemSeries
#                                 dict_temporal = {}
#                                 dict_temporal.setdefault(k,v)
#                                 dict_listSeries.update(dict_temporal)
#                                 rowPosition = self.tbwSeries.rowCount()
#                                 self.tbwSeries.insertRow(rowPosition)
#                                 info = QTableWidgetItem(nro_serie)
#                                 info.setFlags(flags)
#                                 info.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
#                                 self.tbwSeries.setItem(rowPosition, 0, info)
#                                 self.leNro_Serie.clear()
#                                 cant_insertada = str(len(dict_listSeries[Item]))
#                                 self.leSeries_Insertadas.setText(cant_insertada)
#                                 if cant_insertada == self.leSeries_Traspaso.text():
#                                     self.leNro_Serie.setReadOnly(True)
#
#                             else:
#                                 mensajeDialogo('error', "Error", "Nro de Serie Ya Ingresado")
#                         except:
#                             if nro_serie not in listSeries:
#                                 listSeries.append(nro_serie)
#                                 rowPosition = self.tbwSeries.rowCount()
#                                 self.tbwSeries.insertRow(rowPosition)
#                                 info = QTableWidgetItem(nro_serie)
#                                 info.setFlags(flags)
#                                 info.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
#                                 self.tbwSeries.setItem(rowPosition, 0, info)
#                                 self.leNro_Serie.clear()
#                                 cant_insertada = str(len(listSeries))
#                                 self.leSeries_Insertadas.setText(cant_insertada)
#                                 if cant_insertada == self.leSeries_Traspaso.text():
#                                     self.leNro_Serie.setReadOnly(True)
#                             else:
#                                 mensajeDialogo('error', "Error", "Nro de Serie Ya Ingresado")
#
#                 except:
#                         mensajeDialogo('error', "Registro", "Nro de Serie no registrado con el Tipo de Stock Seleccionado")
#             else:
#                 mensajeDialogo('error', "Error", "Ingrese un Nro de Serie")
#         # print(listSeries)
#         event.accept()
#         # except:
#         #     mensajeDialogo('error', "Error", "Contáctese con el Administrador del Sistema")
#
#     def eliminar(self):
#         try:
#             row = self.tbwSeries.currentRow()
#             texto = self.tbwSeries.item(row,0).text()
#             reply = mensajeDialogo('pregunta','Eliminar Posición',"¿Realmente desea remover la serie: " + texto + " ?")
#             if reply == 'Yes':
#                 if listSeries!=[]:
#                     listSeries.remove(texto)
#                     cant_insertada = str(len(listSeries))
#                 else:
#                     ItemSeries=dict_listSeries[Item]
#                     ItemSeries.remove(texto)
#                     k = Item
#                     v = ItemSeries
#                     dict_temporal = {}
#                     dict_temporal.setdefault(k,v)
#                     dict_listSeries.update(dict_temporal)
#                     cant_insertada = str(len(dict_listSeries[Item]))
#
#                 self.tbwSeries.removeRow(row)
#                 self.leSeries_Insertadas.setText(cant_insertada)
#                 self.leNro_Serie.setReadOnly(False)
#         except:
#             mensajeDialogo('error', "Error", "Seleccione una Fila")
#
class TextoCabecera(QDialog):
    def __init__(self,Nro_Doc):
        QDialog.__init__(self)
        uic.loadUi('ERP_ALM_P027_Texto_Cabecera.ui',self)

        global NroDoc
        NroDoc=Nro_Doc

        self.pbGrabar.clicked.connect(self.Grabar)
        self.pbModificar.clicked.connect(self.Modificar)
        self.pbSalir.clicked.connect(self.Salir)

        cargarIcono(self, 'erp')
        cargarIcono(self.pbGrabar, 'grabar')
        cargarIcono(self.pbModificar,'modificar')
        cargarIcono(self.pbSalir,'salir')

        sqlTexCab="SELECT Texto FROM TAB_SOC_019_Texto_Proceso WHERE Cod_Soc='%s' AND Año='%s' AND Tipo_Proceso='6' AND Nro_Doc='%s' AND Item_Doc='0'"%(Cod_Soc,Año,NroDoc)
        TexCab=consultarSql(sqlTexCab)

        if TexCab!=[]:
            self.teDetalle.setPlainText(TexCab[0][0])
            self.teDetalle.setEnabled(False)
            self.pbGrabar.setEnabled(False)

        else:
            try:
                self.teDetalle.setPlainText(texto_cabecera)
                self.teDetalle.setEnabled(False)
                self.pbGrabar.setEnabled(False)
            except Exception as e:
            	print(e)

    def Grabar(self):

        global texto_cabecera
        texto_cabecera = self.teDetalle.toPlainText()

        Hora=datetime.now().strftime("%H:%M:%S.%f")

        if NroDoc!="":

            sqlTexCab="SELECT Texto FROM TAB_SOC_019_Texto_Proceso WHERE Cod_Soc='%s' AND Año='%s' AND Tipo_Proceso='6' AND Nro_Doc='%s' AND Item_Doc='0'"%(Cod_Soc,Año,NroDoc)
            TexCab=convlist(sqlTexCab)

            if TexCab!=[]:
                sqlTextoCabecera="UPDATE TAB_SOC_019_Texto_Proceso SET Texto='%s',Fecha_Mod='%s',Hora_Mod='%s',Usuario_Mod='%s' WHERE Cod_Soc='%s' AND Año='%s' AND Tipo_Proceso='6' AND Nro_Doc='%s' AND Item_Doc='0'"%(texto_cabecera,Fecha,Hora,Cod_Usuario,Cod_Soc,Año,NroDoc)
                respuesta=ejecutarSql(sqlTextoCabecera)

                if respuesta['respuesta']=='correcto':
                    mensajeDialogo("informacion", "Información", "Texto de Cabecera Modificado")
                    del texto_cabecera
                    self.close()

                elif respuesta['respuesta']=='incorrecto':
                    mensajeDialogo("error","Error", "El Texto de cabecera no se pudo modificar")
            else:
                sqlTextoCabecera='''INSERT INTO TAB_SOC_019_Texto_Proceso(Cod_Soc, Año, Tipo_Proceso, Nro_Doc, Item_Doc, Texto, Fecha_Reg, Hora_Reg, Usuario_Reg) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(Cod_Soc,Año,3,NroDoc,0,texto_cabecera,Fecha,Hora,Cod_Usuario)
                respuesta=ejecutarSql(sqlTextoCabecera)

                if respuesta['respuesta']=='correcto':
                    mensajeDialogo("informacion","Excelente", "Texto de cabecera grabado correctamente")
                    del texto_cabecera
                    self.close()

                elif respuesta['respuesta']=='incorrecto':
                    mensajeDialogo("error","Error", "El Texto de cabecera no se pudo grabar")

        else:
            mensajeDialogo("informacion","Excelente", "Texto de cabecera grabado correctamente")
            self.close()

        self.teDetalle.setEnabled(False)
        self.pbGrabar.setEnabled(False)

    def Modificar(self):
        self.teDetalle.setEnabled(True)
        self.pbGrabar.setEnabled(True)

    def Salir(self):
        self.close()

class TextoPosicion(QDialog):
    def __init__(self,Nro_Doc,item_pos):
        QDialog.__init__(self)
        uic.loadUi('ERP_ALM_P027_Texto_Posicion.ui',self)

        global NroDoc,ItemDoc

        NroDoc=Nro_Doc
        ItemDoc=item_pos

        self.pbGrabar.clicked.connect(self.Grabar)
        self.pbModificar.clicked.connect(self.Modificar)
        self.pbSalir.clicked.connect(self.Salir)

        cargarIcono(self, 'erp')
        cargarIcono(self.pbGrabar,'grabar')
        cargarIcono(self.pbModificar,'modificar')
        cargarIcono(self.pbSalir,'salir')

        sqlText="SELECT Texto FROM TAB_SOC_019_Texto_Proceso WHERE Cod_Soc='%s'AND Año='%s' AND Tipo_Proceso='3' AND Nro_Doc='%s' AND Item_Doc='%s'"%(Cod_Soc,Año,NroDoc,ItemDoc)
        text= consultarSql(sqlText)

        if text!=[]:
            self.teDetalle.setText(text[0][0])
            self.teDetalle.setEnabled(False)
            self.pbGrabar.setEnabled(False)
        else:
            try:
                texto_item = dict_textoPosicion[ItemDoc]
                self.teDetalle.setPlainText(texto_item)
                self.teDetalle.setEnabled(False)
                self.pbGrabar.setEnabled(False)
            except Exception as e:
            	print(e)
#
#     def Grabar(self):
#
#         texto_pos=self.teDetalle.toPlainText()
#         k = ItemDoc
#         v = texto_pos
#         dict_temp = {}
#         dict_temp.setdefault(k,v)
#         dict_textoPosicion.update(dict_temp)
#
#         Hora=datetime.now().strftime("%H:%M:%S.%f")
#
#         if NroDoc!="":
#
#             sqlText="SELECT Texto FROM TAB_SOC_019_Texto_Proceso WHERE Cod_Soc='%s'AND Año='%s' AND Tipo_Proceso='6' AND Nro_Doc='%s' AND Item_Doc='%s'"%(Cod_Soc,Año,NroDoc,ItemDoc)
#             text= consultarSql(sqlText)
#
#             if text!=[]:
#                 sqlTextoPos="UPDATE TAB_SOC_019_Texto_Proceso SET Texto='%s',Fecha_Mod='%s',Hora_Mod='%s',Usuario_Mod='%s' WHERE Cod_Soc='%s' AND Año='%s' AND Tipo_Proceso='6' AND Nro_Doc='%s' AND Item_Doc='%s' "%(texto_pos,Fecha,Hora,Cod_Usuario,Cod_Soc,Año,NroDoc,ItemDoc)
#                 respuesta=ejecutarSql(sqlTextoPos)
#
#                 if respuesta['respuesta']=='correcto':
#                     mensajeDialogo("informacion","Excelente", "Texto de posición modificado con éxito")
#                     dict_textoPosicion.clear()
#                     self.close()
#
#                 elif respuesta['respuesta']=='incorrecto':
#                     mensajeDialogo("error","Error", "El Texto de posición no se pudo modificar")
#
#             else:
#                 sqlTextoPos = '''INSERT INTO TAB_SOC_019_Texto_Proceso (Cod_Soc, Año, Tipo_Proceso, Nro_Doc, Item_Doc, Texto, Fecha_Reg, Hora_Reg, Usuario_Reg)
#                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s') ''' % (Cod_Soc, Año, 6, NroDoc, ItemDoc, texto_pos, Fecha, Hora, Cod_Usuario)
#                 respuesta = ejecutarSql(sqlTextoPos)
#
#                 if respuesta['respuesta']=='correcto':
#                     mensajeDialogo("informacion","Excelente", "Texto de posición grabado con éxito")
#                     dict_textoPosicion.clear()
#                     self.close()
#
#                 elif respuesta['respuesta']=='incorrecto':
#                     mensajeDialogo("error","Error", "El Texto de posición no se pudo grabar")
#
#         else:
#             mensajeDialogo("informacion","Excelente", "Texto de posición grabado correctamente")
#             self.close()
#
#         self.teDetalle.setEnabled(False)
#         self.pbGrabar.setEnabled(False)
#
#     def Modificar(self):
#         self.teDetalle.setEnabled(True)
#         self.pbGrabar.setEnabled(True)
#
#     def Salir(self):
#         self.close()

now = datetime.now()
Año=str(now.year)

##################################################################################
class Seleccionar_DocSalida(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ERP_ALM_P027_Buscar_Despacho.ui",self)

        self.tbwDespachos.itemDoubleClicked.connect(self.Despacho)
        self.lePalabra.textChanged.connect(self.buscar)

        cargarIcono(self, 'erp')

        sqlMovSalida='''SELECT a.Nro_Doc_Alm,a.Fecha_Doc_Alm,a.Referencia,a.Fecha_Referencia,b.Razon_social,a.Guia_Remision
        FROM TAB_ALM_001_Mov_Almacenes a
        LEFT JOIN `TAB_COM_001_Maestro Clientes`b ON a.Cliente=b.Cod_cliente
        WHERE a.Cod_Emp='%s' AND a.Tipo_Doc_Alm='02' AND a.Tipo_Mov='601'
        ORDER BY a.Nro_Doc_Alm DESC, a.Fecha_Doc_Alm DESC;'''%(Cod_Soc)

        MovSalida=consultarSql(sqlMovSalida)

        self.tbwDespachos.clear()
        for fila in MovSalida:
            fila[1]=formatearFecha(fila[1])
            fila[3]=formatearFecha(fila[3])

            insertarFilatw(self.tbwDespachos, fila, [], [0,1,2,3,5])

        for i in range(self.tbwDespachos.columnCount()):
            self.tbwDespachos.resizeColumnToContents(i)

    def buscar(self):
        buscarTabla(self.tbwDespachos, self.lePalabra.text(), [0,2,4])

    def Despacho(self,item):

        global NroDocSalida,FechaDocSalida
        NroDocSalida=item.text(0)
        FechaDocSalida=formatearFecha(item.text(1))
        self.close()
##################################################################################

class Anulacion_Despacho(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("ERP_ALM_P027_Anulacion_Despacho.ui",self)

        # self.datos=[]
        # self.mantener=True
        global Cod_Soc,Nom_Soc,Cod_Usuario
        # Cod_Soc='1000'
        # Nom_Soc='MULTI PLAY TELECOMUNICACIONES S.A.C'
        Cod_Soc='2000'
        Nom_Soc='MULTICABLE PERU S.A.C.'
        Cod_Usuario='2021100004'

        # self.pbGrabar.clicked.connect(self.ValidarGrabar)
        # self.pbTexto_Cabecera.clicked.connect(self.TextoCabecera)
        # self.pbTexto_Posicion.clicked.connect(self.TextoPosicion)
        self.pbBuscar_DocSalida.clicked.connect(self.BuscarDocSalida)
        self.pbSalir.clicked.connect(self.Salir)
        self.chkMontacarga_Si.stateChanged.connect(self.chkMontacargaSi)
        self.chkMontacarga_No.stateChanged.connect(self.chkMontacargaNo)
        # self.chkMontacarga_Si.stateChanged.connect(self.checkMontacargaSi)
        # self.chkMontacarga_No.stateChanged.connect(self.checkMontacargaNo)

        # self.tbwDespacho_Venta.itemChanged.connect(self.CantidadSalida)
        # self.pbEmitir_Guia_Remision.setEnabled(False)

    # def datosGenerales(self, codSoc, empresa, usuario):
    #     global Cod_Soc, Nom_Soc, Cod_Usuario
    #     Cod_Soc = codSoc
    #     Nom_Soc = empresa
    #     Cod_Usuario = usuario

        Fecha=datetime.now().strftime("%Y-%m-%d")

        cargarLogo(self.lbLogo_Mp,'multiplay')
        cargarLogo(self.lbLogo_Soc, Cod_Soc)
        cargarIcono(self, 'erp')
        cargarIcono(self.pbGrabar, 'grabar')
        cargarIcono(self.pbTexto_Cabecera, 'agregar_texto')
        cargarIcono(self.pbTexto_Posicion, 'agregar_texto')
        cargarIcono(self.pbBuscar_DocAnulacion, 'buscar')
        cargarIcono(self.pbBuscar_DocSalida, 'buscar')
        cargarIcono(self.pbSalir, 'salir')

        self.Inicio()

    def Inicio(self):

        global dict_serie, dict_lote

        sqlSeries = '''SELECT Cod_Mat, Control_series, Lote FROM TAB_MAT_001_Catalogo_Materiales'''
        infoSeries = consultarSql(sqlSeries)
        dict_serie = {}
        dict_lote = {}
        for n in infoSeries:
            dict_serie[n[0]] = n[1]
            dict_lote[n[0]] = n[2]

    def BuscarDocSalida(self):
        global NroDocSalida,FechaDocSalida
        NroDocSalida=None
        FechaDocSalida=None

        Seleccionar_DocSalida().exec_()

        sqlCabecera='''SELECT a.Nro_Doc_Alm,a.Fecha_Doc_Alm,a.Tipo_Mov,a.Referencia,a.Fecha_Referencia,c.Nomb_Planta,d.Nomb_Alm, e.Razon_social, e.Direcc_cliente, e.RUC, e.Representante_Cliente, e.DNI, e.Correo, a.Nro_Contenedor, a.Hora_Inicio_Descarga,a.Hora_Fin_Descarga, a.Uso_Montacarga
        FROM TAB_ALM_001_Mov_Almacenes a
        LEFT JOIN TAB_ALM_002_Detalle_Mov_Almacenes b ON a.Cod_Emp=b.Cod_Emp AND a.Nro_Doc_Alm=b.Nro_Doc_Alm
        LEFT JOIN TAB_SOC_002_Planta c ON b.Cod_Emp=c.Cod_soc AND b.Planta=c.Cod_Planta
        LEFT JOIN TAB_SOC_003_Almacén d ON b.Cod_Emp=d.Cod_Soc AND b.Planta=d.Cod_Planta AND b.Almacen=d.Cod_Alm
        LEFT JOIN `TAB_COM_001_Maestro Clientes` e ON a.Cliente=e.Cod_cliente
        WHERE a.Cod_Emp='%s' AND a.Nro_Doc_Alm='%s' AND a.Fecha_Doc_Alm='%s' AND a.Tipo_Doc_Alm='02' AND a.Tipo_Mov='601'
        GROUP BY a.Nro_Doc_Alm;'''%(Cod_Soc,NroDocSalida,FechaDocSalida)
        Cabecera=convlist(sqlCabecera)
        print(Cabecera)

        if Cabecera!=[]:

            self.leNro_Doc.setText(Cabecera[0])
            self.leFecha_Doc.setText(formatearFecha(Cabecera[1]))
            self.leMovimiento.setText(Cabecera[2])
            self.leNro_Pedido.setText(Cabecera[3])
            self.leFecha_Pedido.setText(formatearFecha(Cabecera[4]))
            self.lePlanta.setText(Cabecera[5])
            self.leAlmacen.setText(Cabecera[6])
            self.leCliente.setText(Cabecera[7])
            self.leDireccion.setText(Cabecera[8])
            self.leRUC.setText(Cabecera[9])
            self.leRepresentante.setText(Cabecera[10])
            self.leDNI.setText(Cabecera[11])
            self.leCorreo.setText(Cabecera[12])
            self.leNro_Contenedor.setText(Cabecera[13])
            self.leHora_Inicio_Carga.setText(Cabecera[14][:-3])
            self.leHora_Salida.setText(Cabecera[15][:-3])
            if Cabecera[16]=='1':
                self.chkMontacarga_Si.setChecked(True)
                self.chkMontacarga_No.setChecked(False)
            else:
                self.chkMontacarga_Si.setChecked(False)
                self.chkMontacarga_No.setChecked(True)

            #..............Bloqueando LineEdit..............#

            self.leNro_Doc.setReadOnly(True)
            self.leFecha_Doc.setReadOnly(True)
            self.leMovimiento.setReadOnly(True)
            self.leNro_Pedido.setReadOnly(True)
            self.leFecha_Pedido.setReadOnly(True)
            self.lePlanta.setReadOnly(True)
            self.leAlmacen.setReadOnly(True)

            self.leCliente.setReadOnly(True)
            self.leDireccion.setReadOnly(True)
            self.leRUC.setReadOnly(True)
            self.leRepresentante.setReadOnly(True)
            self.leDNI.setReadOnly(True)
            self.leCorreo.setReadOnly(True)
            self.leNro_Contenedor.setReadOnly(True)
            self.leHora_Inicio_Carga.setReadOnly(True)
            self.leHora_Salida.setReadOnly(True)

            self.leNro_Anulacion.setReadOnly(True)
            self.leFecha_Anulacion.setReadOnly(True)
            self.leMov_Anulacion.setReadOnly(True)

        sqlDetalle='''SELECT a.Item_Doc_Alm,a.Cod_Mat,b.Descrip_Mat,b.Uni_Base,a.Cant_Salida
        FROM TAB_ALM_002_Detalle_Mov_Almacenes a
        LEFT JOIN TAB_MAT_001_Catalogo_Materiales b ON a.Cod_Mat=b.Cod_Mat
        WHERE a.Cod_Emp='%s' AND a.Nro_Doc_Alm='%s' AND a.Fecha_Doc_Alm='%s' AND a.Tipo_Doc_Alm='02' AND a.Tipo_Mov='601'
        ORDER BY CAST(a.Item_Doc_Alm as INT) ASC;'''%(Cod_Soc,NroDocSalida,FechaDocSalida)
        CargarDetalleAnulacion(self, self.tbwDespacho_Venta, sqlDetalle, dict_serie, dict_lote)

    def chkMontacargaSi(self):
        if self.chkMontacarga_Si.isChecked():
            self.chkMontacarga_No.setChecked(False)

    def chkMontacargaNo(self):
        if self.chkMontacarga_No.isChecked():
            self.chkMontacarga_Si.setChecked(False)

        # print(dict_serie)
        # print(dict_lote)
    #
    #     self.leFecha_Doc.setText(formatearFecha(Fecha))
    #     self.leMovimiento.setText('601 - Salida Venta al Cliente')
    #
    #     sqlCabecera='''SELECT a.Nro_Cot_Client, e.Razon_social, e.Direcc_cliente, e.RUC, e.Representante_Cliente, e.DNI, e.Correo, a.Planta, a.Almacén, d.Fecha_Doc_Cot
    #     FROM TAB_VENTA_004_Detalle_de_Reserva_de_Venta_al_Cliente a
    #     LEFT JOIN TAB_SOC_002_Planta b ON a.Cod_Emp=b.Cod_soc AND a.Planta=b.Cod_Planta
    #     LEFT JOIN TAB_SOC_003_Almacén c ON a.Cod_Emp=c.Cod_Soc AND a.Planta=c.Cod_Planta AND a.Almacén=c.Cod_Alm
    #     LEFT JOIN TAB_VENTA_003_Cabecera_de_Reserva_de_Venta_al_Cliente d ON a.Cod_Emp=d.Cod_Emp AND a.Año_Cot_Client=d.Año_Cot_Client AND a.Nro_Cot_Client=d.Nro_Cot_Client
    #     LEFT JOIN `TAB_COM_001_Maestro Clientes` e ON d.Cod_Cliente=e.Cod_cliente
    #     WHERE a.Cod_Emp='%s' AND a.Año_Cot_Client='%s' AND a.Nro_Cot_Client='%s';'''%(Cod_Soc, Año, Nro_Cot_Client)
    #     Cabecera=convlist(sqlCabecera)
    #
    #     if Cabecera!=[]:
    #
    #         self.leNro_Pedido.setText(Cabecera[0])
    #         self.leFecha_Pedido.setText(formatearFecha(Cabecera[9]))
    #         self.lePlanta.setText(dicPlanta[Cod_Planta])
    #
    #         sqlCod_Almacen= "SELECT Cod_Alm, Nomb_Alm FROM TAB_SOC_003_Almacén WHERE Cod_Soc='%s'and Cod_Planta='%s'AND Estado_Alm='1'"%(Cod_Soc,Cod_Planta)
    #         Alm=consultarSql(sqlCod_Almacen)
    #         dicAlm={}
    #         for dato in Alm:
    #             dicAlm[dato[0]]=dato[1]
    #
    #         self.leAlmacen.setText(dicAlm[Cod_Almacen])
    #
    #         self.leCliente.setText(Cabecera[1])
    #         self.leDireccion.setText(Cabecera[2])
    #         self.leRUC.setText(Cabecera[3])
    #         self.leRepresentante.setText(Cabecera[4])
    #         self.leDNI.setText(Cabecera[5])
    #         self.leCorreo.setText(Cabecera[6])
    #
    #         #..............Bloqueando LineEdit..............#
    #
    #         # self.leNro_Doc.setReadOnly(True)
    #         self.leFecha_Doc.setReadOnly(True)
    #         self.leMovimiento.setReadOnly(True)
    #         self.leNro_Pedido.setReadOnly(True)
    #         self.leFecha_Pedido.setReadOnly(True)
    #         self.lePlanta.setReadOnly(True)
    #         self.leAlmacen.setReadOnly(True)
    #
    #         self.leCliente.setReadOnly(True)
    #         self.leDireccion.setReadOnly(True)
    #         self.leRUC.setReadOnly(True)
    #         self.leRepresentante.setReadOnly(True)
    #         self.leDNI.setReadOnly(True)
    #         self.leCorreo.setReadOnly(True)
    #
    #         sqlDetalle='''SELECT a.Item_Cotiza, a.Cod_Mat, b.Descrip_Mat, a.Unidad, a.Cant_Confirmada, (a.Cant_Confirmada-a.Cant_Despachada)
    #         FROM TAB_VENTA_004_Detalle_de_Reserva_de_Venta_al_Cliente a
    #         LEFT JOIN TAB_MAT_001_Catalogo_Materiales b ON a.Cod_Mat=b.Cod_Mat
    #         WHERE a.Cod_Emp='%s' AND a.Año_Cot_Client='%s' AND a.Nro_Cot_Client='%s' AND a.Planta='%s' AND a.Almacén='%s' AND Estado_Pedido='0' AND a.Estado_Reg_Alm!='2'
    #         ORDER BY a.Item_Cotiza ASC;'''%(Cod_Soc, Año, Nro_Cot_Client, Cod_Planta, Cod_Almacen)
    #         CargarDetalle(self,self.tbwDespacho_Venta,sqlDetalle,dict_serie, dict_lote)
    #
    # # def validarHoras(self):
    # #     # reg_ex = QRegExp("^(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:[AaPp](\.?)[Mm]\1)?$") ## Formato 12 horas
    # #     reg_ex = QRegExp("^(?:0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]\s?$") ## Formato 24 horas
    # #     input_validator = QRegExpValidator(reg_ex, self.leHora_Inicio_Carga)
    # #     self.leHora_Inicio_Carga.setValidator(input_validator)
    # #     input_validator = QRegExpValidator(reg_ex, self.leHora_Salida)
    # #     self.leHora_Salida.setValidator(input_validator)
    #
    # def checkMontacargaSi(self):
    #     if self.chkMontacarga_Si.isChecked():
    #         self.chkMontacarga_No.setChecked(False)
    #
    # def checkMontacargaNo(self):
    #     if self.chkMontacarga_No.isChecked():
    #         self.chkMontacarga_Si.setChecked(False)
    #
    # def CantidadSalida(self, item):
    #     if self.mantener:
    #         row=item.row()
    #         col=item.column()
    #         if col==6:
    #             self.mantener=False
    #             nume=self.tbwDespacho_Venta.item(row,col).text()
    #             num=ValidarNumero(nume)
    #             if num!='0':
    #                 Cant_Restante=self.tbwDespacho_Venta.item(row,col-1).text().replace(",","")
    #                 num_format=formatearDecimal(num,'3')
    #                 if float(num_format.replace(",","")) <= float(Cant_Restante):
    #                     info=QTableWidgetItem(num_format)
    #                     info.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    #                     self.tbwDespacho_Venta.setItem(row,col,info)
    #                     self.mantener=True
    #                     # self.actualizarRestante(row)
    #                 else:
    #                     self.mantener=True
    #                     mensajeDialogo("error", "Error", "La Cant. a Salir no debe ser mayor a la Cant. Restante")
    #                     self.tbwDespacho_Venta.takeItem(row,col)
    #             else:
    #                 self.mantener=True
    #                 mensajeDialogo("error", "Error", "Ingrese un valor numérico")
    #                 self.tbwDespacho_Venta.takeItem(row,col)
    #
    # def SeriePosicion(self):
    #     Item=self.tbwDespacho_Venta.item(self.tbwDespacho_Venta.currentRow(),0).text()
    #     Cod_Material=self.tbwDespacho_Venta.item(self.tbwDespacho_Venta.currentRow(),1).text()
    #     try:
    #         Cant_Salida=self.tbwDespacho_Venta.item(self.tbwDespacho_Venta.currentRow(),6).text().replace(",","")
    #         Cantidad_Salida=Cant_Salida[:-4]
    #         Texto_Series(Item,Cod_Material,Cantidad_Salida).exec_()
    #     except:
    #         mensajeDialogo('error', "Error", "No se encontró la cantidad de salida")
    #
    def TextoCabecera(self):
        try:
            Nro_Doc=self.leNro_Doc.text()
            TextoCabecera(Nro_Doc).exec_()
        except Exception as e:
            mensajeDialogo('error', "Error", "Estamos Trabajando en ello")
            print(e)

    def TextoPosicion(self):
        try:
            fila=self.tbwDespacho_Venta.currentRow()
            Nro_Doc=self.leNro_Doc.text()
            item_pos=self.tbwDespacho_Venta.item(fila,0).text()
            TextoPosicion(Nro_Doc,item_pos).exec_()
        except Exception as e:
            mensajeDialogo("error", "Error", "Complete los Campos")
            print(e)

    # def ValidarGrabar(self):
    #     try:
    #         valorVerdad=[]
    #         d=self.tbwDespacho_Venta.rowCount()
    #         for row in range(d):
    #             Cod_Mat=self.tbwDespacho_Venta.item(row,1).text()
    #             if dict_serie[Cod_Mat] == '1':
    #                 Item=self.tbwDespacho_Venta.item(row,0).text()
    #                 try:
    #                     CantSal=self.tbwDespacho_Venta.item(row,6).text().replace(",","")
    #                     CantSal=CantSal[:-4]
    #
    #                     if len(dict_listSeries[Item])==int(CantSal):
    #                         valorVerdad.append('Correcto')
    #                     else:
    #                         valorVerdad.append('Incorrecto')
    #
    #                 except Exception as e:
    #                     valorVerdad.append('Correcto')
    #                     print(e)
    #
    #         if 'Incorrecto' in valorVerdad:
    #             mensajeDialogo("error", "Error", "No se ha dado Salida de Series a uno o mas materiales")
    #         else:
    #             self.Grabar()
    #
    #     except Exception as e:
    #         mensajeDialogo("error", "Error", "No se ha dado Salida de Series a uno o mas materiales")
    #         print(e)
    #
    def Grabar(self):
        resultado=mensajeDialogo("pregunta", "Anular Despacho", "¿Seguro que desea anular el despacho?\n\nUna vez anulado no se podrá revertir la acción")
        if resultado=='Yes':
            try:
                Hora = datetime.now().strftime('%H:%M:%S.%f')
                Año_Doc=Año
                Fecha_Doc=formatearFecha(self.leFecha_Doc.text())
                Tipo_Mov='602'
                Nro_Pedido=self.leNro_Pedido.text()
                Fecha_Pedido=formatearFecha(self.leFecha_Pedido.text())
                Planta=Cod_Planta
                Almacen=Cod_Almacen
                Cliente=self.leCliente.text()
                Representante=self.leRepresentante.text()
                Nro_Contenedor=self.leNro_Contenedor.text()
                Hora_Inicio_Carga=self.leHora_Inicio_Carga.text()
                Hora_Salida=self.leHora_Salida.text()

                # montacarga = self.leMontacarga.text() ## debe ser QCheckBox
                if self.chkMontacarga_Si.isChecked():
                    Montacarga = '1' ## Si Montacarga
                    print("Si Montacarga")
                else:
                    Montacarga = '2' ## No Montacarga
                    print("No Montacarga")

                try:
                    if (texto_cabecera != "") and (texto_cabecera != None):
                        print("++++++++++++++++++++++++")
                        print(texto_cabecera)
                        Texto_Cab = '1'
                    else:
                        Texto_Cab = '2'
                except:
                    Texto_Cab = '2'

                sqlCodActualDoc="SELECT Cod_Actual FROM TAB_SOC_018_Rango_de_Números_de_Documentos_de_procesos WHERE Cod_Soc='%s' AND Tipo_Rango='06' AND Año_Rango='%s'"%(Cod_Soc,Año)
                CodActualDoc=convlist(sqlCodActualDoc)
                self.leNro_Doc.setText(CodActualDoc[0])
                Nro_Doc=self.leNro_Doc.text()
                Tipo_Doc='02'
    #
    #             sqlCab='''INSERT INTO TAB_ALM_001_Mov_Almacenes(Cod_Emp, Año_Doc_Alm, Nro_Doc_Alm, Tipo_Doc_Alm, Tipo_Mov, Fecha_Doc_Alm, Referencia, Fecha_Referencia, Cliente, Representante_Cliente, Nro_Contenedor, Hora_Inicio_Descarga, Hora_Fin_Descarga, Uso_Montacarga, Texto_Cabecera, Fecha_Reg, Hora_Reg, Usuario_Reg)
    #             VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(Cod_Soc,Año_Doc,Nro_Doc,Tipo_Doc,Tipo_Mov,Fecha_Doc,Nro_Pedido,Fecha_Pedido,Cod_Cliente,Representante,Nro_Contenedor,Hora_Inicio_Carga,Hora_Salida, Montacarga,Texto_Cab,Fecha,Hora,Cod_Usuario)
    #             ejecutarSql(sqlCab)
    #
    #             try:
    #                 # Texto Cabecera para la Nota de Ingreso
    #                 if texto_cabecera != None:
    #                     sqlTextoCabecera='''INSERT INTO TAB_SOC_019_Texto_Proceso(Cod_Soc, Año, Tipo_Proceso, Nro_Doc, Item_Doc, Texto, Fecha_Reg, Hora_Reg, Usuario_Reg) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(Cod_Soc,Año,6,Nro_Doc,0,texto_cabecera,Fecha,Hora,Cod_Usuario)
    #                     info=ejecutarSql(sqlTextoCabecera)
    #             except Exception as e:
    #                 print(e)
    #
    #             d=self.tbwDespacho_Venta.rowCount()
    #             for row in range(d):
    #
    #                 Item=self.tbwDespacho_Venta.item(row,0).text()
    #                 Cod_Mat=self.tbwDespacho_Venta.item(row,1).text()
    #                 # Descripcion=self.tbwDespacho_Venta.item(row,2).text()
    #                 Unidad=self.tbwDespacho_Venta.item(row,3).text()
    #                 Cant_Vendida=self.tbwDespacho_Venta.item(row,4).text().replace(",","")
    #                 Cant_Restante=self.tbwDespacho_Venta.item(row,5).text().replace(",","")
    #                 Cant_Salida=self.tbwDespacho_Venta.item(row,6).text().replace(",","")
    #
    #                 # sqlstock="SELECT Stock_Vendido, Stock_Vendido_Calidad, Stock_Cliente FROM TAB_MAT_002_Stock_Almacen WHERE Cod_Soc='%s' AND Cod_Planta='%s' AND Cod_Alm='%s' AND Cod_Mat='%s';"%(Cod_Soc, Planta, Almacen, Cod_Mat)
    #                 # stocks=convlist(sqlstock)
    #                 sqlstock="SELECT Stock_Vendido FROM TAB_MAT_002_Stock_Almacen WHERE Cod_Soc='%s' AND Cod_Planta='%s' AND Cod_Alm='%s' AND Cod_Mat='%s';"%(Cod_Soc, Planta, Almacen, Cod_Mat)
    #                 stocks=convlist(sqlstock)
    #
    #                 if len(Cant_Salida)!=0:
    #                     if Cant_Salida==Cant_Restante:
    #                         Estado_Reg_Alm='2'
    #                         Estado_Pedido='1'
    #                     elif Cant_Salida!=Cant_Restante:
    #                         Estado_Reg_Alm='1'
    #                         Estado_Pedido='0'
    #                     self.actualizarStock(Cod_Soc, Planta, Almacen, Cod_Mat, Cant_Salida,stocks,Hora)
    #
    #                 else:
    #                     Estado_Reg_Alm='0'
    #                     Estado_Pedido='0'
    #
    #                 lote=self.tbwDespacho_Venta.item(row,7).text()
    #                 if lote == '---': ## No maneja Lote
    #                     Lote = '2'
    #                 else:
    #                     Lote = "1"
    #
    #                 if dict_serie[Cod_Mat] == '1': ## Si control de series
    #                     Serie = "1"
    #                     if dict_listSeries[Item]!=[]:
    #                         tuple_listSeries=tuple(dict_listSeries[Item])
    #                         if len(tuple_listSeries)!=1:
    #                             sqlSeries='''UPDATE `TAB_ALM_005 Registro de Nro. De series de la Empresa`
    #                             SET Tipo_Stock='%s', Nro_Pedido_Venta='%s',Estado_Serie='%s',Cod_Cliente='%s',Doc_Salida_Cliente='%s',Fecha_Salida_Cliente='%s',Fecha_Mod='%s',Hora_Mod='%s',Usuario_Mod='%s'
    #                             WHERE Cod_Soc='%s' AND Cod_Planta='%s' AND Cod_Alm='%s' AND Cod_Mat='%s' AND Nro_Serie in %s;''' %(19,Nro_Pedido,3,Cod_Cliente,Nro_Doc,Fecha,Fecha,Hora,Cod_Usuario,Cod_Soc,Planta,Almacen,Cod_Mat,tuple_listSeries)
    #                             ejecutarSql(sqlSeries)
    #                         else:
    #                             sqlSeries='''UPDATE `TAB_ALM_005 Registro de Nro. De series de la Empresa`
    #                             SET Tipo_Stock='%s', Nro_Pedido_Venta='%s',Estado_Serie='%s',Cod_Cliente='%s',Doc_Salida_Cliente='%s',Fecha_Salida_Cliente='%s',Fecha_Mod='%s',Hora_Mod='%s',Usuario_Mod='%s'
    #                             WHERE Cod_Soc='%s' AND Cod_Planta='%s' AND Cod_Alm='%s' AND Cod_Mat='%s' AND Nro_Serie='%s';''' %(19,Nro_Pedido,3,Cod_Cliente,Nro_Doc,Fecha,Fecha,Hora,Cod_Usuario,Cod_Soc,Planta,Almacen,Cod_Mat,tuple_listSeries[0])
    #                             ejecutarSql(sqlSeries)
    #                 else:
    #                     Serie = "2"
    #
    #                 Cant_Despachada=(float(Cant_Vendida) - float(Cant_Restante)) + float(Cant_Salida)
    #
    #                 ## Texto posición
    #                 try:
    #                     textoposicion = dict_textoPosicion[Item]
    #                     sqlTextoPos = '''INSERT INTO TAB_SOC_019_Texto_Proceso (Cod_Soc, Año, Tipo_Proceso, Nro_Doc, Item_Doc, Texto, Fecha_Reg, Hora_Reg, Usuario_Reg)
    #                     VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s') ''' % (Cod_Soc, Año, 6, Nro_Doc, Item, textoposicion, Fecha, Hora, Cod_Usuario)
    #                     infoTexto = ejecutarSql(sqlTextoPos)
    #                 except Exception as e:
    #                 	print(e)
    #
    #                 sqlDet='''INSERT INTO TAB_ALM_002_Detalle_Mov_Almacenes(Cod_Emp, Año_Doc_Alm, Nro_Doc_Alm, Tipo_Doc_Alm, Item_Doc_Alm, Tipo_Mov, Cod_Mat, Lote_Mat, Cliente, Cant_Salida, Unid_Base_Salida, Control_Serie, Fecha_Doc_Alm, Planta, Almacen, Referencia, Fecha_Reg, Hora_Reg, Usuario_Reg)
    #                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(Cod_Soc,Año_Doc,Nro_Doc,Tipo_Doc,Item,Tipo_Mov,Cod_Mat, Lote, Cod_Cliente, Cant_Salida,Unidad, Serie, Fecha_Doc, Planta, Almacen, Nro_Pedido, Fecha, Hora, Cod_Usuario)
    #                 respuesta=ejecutarSql(sqlDet)
    #
    #                 sqlEstado="UPDATE TAB_VENTA_004_Detalle_de_Reserva_de_Venta_al_Cliente SET Estado_Pedido='%s',Estado_Reg_Alm='%s', Cant_Despachada='%s', Fecha_Mod='%s', Hora_Mod='%s', Usuario_Mod='%s' WHERE Cod_Emp='%s' AND Año_Cot_Client='%s' AND Nro_Cot_Client='%s' AND Item_Cotiza='%s';"%(Estado_Pedido, Estado_Reg_Alm, Cant_Despachada, Fecha, Hora, Cod_Usuario, Cod_Soc, Año, Nro_Cot_Client, Item)
    #                 ejecutarSql(sqlEstado)
    #
    #             if respuesta['respuesta']=='correcto':
    #
    #                 CodActualNroDoc=int(CodActualDoc[0])+1
    #                 sqlCodActualNroDoc="UPDATE TAB_SOC_018_Rango_de_Números_de_Documentos_de_procesos SET Cod_Actual='%s', Fecha_Mod='%s', Hora_Mod='%s', Usuario_Mod='%s' WHERE Cod_Soc='%s' AND Tipo_Rango ='06' AND Año_Rango='%s'" %(CodActualNroDoc, Fecha, Hora, Cod_Usuario, Cod_Soc,Año)
    #                 ejecutarSql(sqlCodActualNroDoc)
    #
    #                 self.pbGrabar.setEnabled(False)
    #                 # self.pbEmitir_Guia_Remision.setEnabled(True)
    #                 self.actualizarEstado(Hora)
    #                 self.limpiar()
    #                 mensajeDialogo("informacion", "Excelente", "Despacho de Venta al Cliente se ha grabado")
    #
    #             elif respuesta['respuesta']=='incorrecto':
    #                 mensajeDialogo("error", "Error", "No se pudo grabar, verifique y vuelva a intentar")
    #
            except Exception as e:
                mensajeDialogo("error", "Error", "No se pudo anular, verifique y vuelva a intentar")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(fname, exc_tb.tb_lineno, exc_type, e)
    #
    # def actualizarStock(self, Cod_Soc, Planta, Almacen, Cod_Mat, Cant_Salida, stocks, Hora):
    #     try:
    #
    #         stockV=float(stocks[0])-float(Cant_Salida)
    #
    #         sqlstock="UPDATE TAB_MAT_002_Stock_Almacen SET Stock_Vendido='%s', Fecha_Mod='%s', Hora_Mod='%s', Usuario_Mod='%s' WHERE Cod_Soc='%s' AND Cod_Planta='%s' AND Cod_Alm='%s' AND Cod_Mat='%s';"%(stockV, Fecha, Hora, Cod_Usuario, Cod_Soc, Planta, Almacen, Cod_Mat)
    #         ejecutarSql(sqlstock)
    #
    #     except Exception as e:
    #         print(e)
    #
    # def actualizarEstado(self,Hora):
    #     try:
    #         sqlEstado="SELECT Estado_Reg_Alm FROM TAB_VENTA_004_Detalle_de_Reserva_de_Venta_al_Cliente WHERE  Cod_Emp='%s' AND Año_Cot_Client='%s' AND Nro_Cot_Client='%s';"%(Cod_Soc, Año, Nro_Cot_Client)
    #         estado=convlist(sqlEstado)
    #         print(estado)
    #         if '0' in estado or '1' in estado:
    #             sqlCab="UPDATE TAB_VENTA_003_Cabecera_de_Reserva_de_Venta_al_Cliente SET Estado_Ped_comer='2', Fecha_Mod='%s', Hora_Mod='%s', Usuario_Mod='%s' WHERE Cod_Emp='%s' AND Año_Cot_Client='%s' AND Nro_Cot_Client='%s';"%(Fecha,Hora,Cod_Usuario,Cod_Soc, Año, Nro_Cot_Client)
    #             ejecutarSql(sqlCab)
    #         else:
    #             sqlCab="UPDATE TAB_VENTA_003_Cabecera_de_Reserva_de_Venta_al_Cliente SET Estado_Ped_comer='3', Fecha_Mod='%s', Hora_Mod='%s', Usuario_Mod='%s' WHERE Cod_Emp='%s' AND Año_Cot_Client='%s' AND Nro_Cot_Client='%s';"%(Fecha,Hora,Cod_Usuario,Cod_Soc, Año, Nro_Cot_Client)
    #             ejecutarSql(sqlCab)
    #
    #     except Exception as e:
    #         print(e)
    #
    # def limpiar(self):
    #     global texto_cabecera, dict_textoPosicion, dict_listSeries
    #     texto_cabecera = None
    #     del texto_cabecera
    #     dict_textoPosicion = {}
    #     dict_listSeries = {}

##################################################################################

    # def SeleccionarFacturacion(self):
    #     global Serie,Nro_Facturacion
    #     Serie=None
    #     Nro_Facturacion=None
    #
    #     TipComp=self.cbTipo_Comprobante.currentText()
    #     SerieComp=self.cbSerie.currentText()
    #     if len(TipComp)!=0 and len(SerieComp)!=0:
    #         TipoComprobante=TipComprobante[TipComp]
    #         SeleccionarFacturacion(TipoComprobante,SerieComp).exec_()
    #         self.CargarFacturacion()
    #     elif len(TipComp)!=0 and len(SerieComp)==0:
    #         mensajeDialogo('informacion','Información','Seleccione Serie')
    #     else:
    #         mensajeDialogo('informacion','Información','Seleccione Tipo de Comprobante y la Serie')

##################################################################################

    # def EmitirGuia(self):
    #     try:
    #         data=[]
    #         data.append(self.leNro_Pedido.text()) # Número de Pedido - data[0]
    #         data.append(self.leCliente.text()) # Razon Social Cliente - data[1]
    #         data.append(self.leDireccion.text()) # Direccion Cliente - data[2]
    #         data.append(self.leRUC.text()) # RUC Cliente - data[3]
    #         data.append(self.leCorreo.text()) # Correo - data[4]
    #         data.append(Cod_Planta) # Código de Planta - data[5]
    #         data.append(Cod_Almacen) # Código de Almacén - data[6]
    #         data.append(self.leNro_Doc.text()) # Número Documento Movimiento - data[7]
    #
    #         self.Guia=Facturacion_Guia()
    #         self.Guia.datosCabecera(Cod_Soc,Nom_Soc,Cod_Usuario,data)
    #         self.Guia.pbEnviar_SUNAT.clicked.connect(self.Serie_Numero)
    #         self.Guia.showMaximized()
    #
    #     except Exception as e:
    #         exc_type, exc_obj, exc_tb = sys.exc_info()
    #         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #         print(fname, exc_tb.tb_lineno, exc_type, e)
    #
    # def Serie_Numero(self):
    #     try:
    #         serie=self.Guia.cbSerie.currentText()
    #         numero=self.Guia.leNumero.text()
    #         guia_remision=serie+'-'+numero
    #         self.leNro_Guia_Remision.setText(guia_remision)
    #         Nro_Doc=self.leNro_Doc.text()
    #         Tipo_Doc='02'
    #         sql="UPDATE TAB_ALM_001_Mov_Almacenes SET Guia_Remision='%s' WHERE Cod_Emp='%s' AND Año_Doc_Alm='%s' AND Nro_Doc_Alm='%s' AND Tipo_Doc_Alm='%s' AND Tipo_Mov='%s';"%(guia_remision,Cod_Soc,Año,Nro_Doc,Tipo_Doc,601)
    #         ejecutarSql(sql)
    #     except Exception as e:
    #         exc_type, exc_obj, exc_tb = sys.exc_info()
    #         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #         print(fname, exc_tb.tb_lineno, exc_type, e)

    def Salir(self):
        self.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    _main=Anulacion_Despacho()
    _main.showMaximized()
    app.exec_()
