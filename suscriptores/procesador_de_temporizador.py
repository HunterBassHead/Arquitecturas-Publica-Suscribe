#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: procesador_de_temporizador.py
# Capitulo: 3 Estilo Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0.1 Mayo 2017
# Descripción:
#
#   Esta clase define el rol de un suscriptor, es decir, es un componente que recibe mensajes.
#
#   Las características de ésta clase son las siguientes:
#
#                                   procesador_de_temperatura.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Se suscribe a los   |
#           |                       |                         |    eventos generados   |
#           |                       |  - Procesar valores     |    por el wearable     |
#           |     Procesador de     |    extremos de          |    Xiaomi My Band.     |
#           |     Temporizador      |    temporizador         |  - Define el valor ex- |
#           |                       |                         |    tremo del           |
#           |                       |                         |    temporizador.       |
#           |                       |                         |  - Notifica al monitor |
#           |                       |                         |    cuando un valor ex- |
#           |                       |                         |    tremo es detectado. |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Recibe los signos  |
#           |       consume()        |          Ninguno         |    vitales vitales    |
#           |                        |                          |    desde el distribui-|
#           |                        |                          |    dor de mensajes.   |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - ch: propio de Rabbit. |  - Procesa y detecta  |
#           |                        |  - method: propio de     |    valores extremos   |
#           |                        |     Rabbit.              |    de la temperatura. |
#           |       callback()       |  - properties: propio de |                       |
#           |                        |     Rabbit.              |                       |
#           |                        |  - body: mensaje recibi- |                       |
#           |                        |     do.                  |                       |
#           +------------------------+--------------------------+-----------------------+
#           |    string_to_json()    |  - string: texto a con-  |  - Convierte un string|
#           |                        |     vertir en JSON.      |    en un objeto JSON. |
#           +------------------------+--------------------------+-----------------------+
#           
#
#
#           Nota: "propio de Rabbit" implica que se utilizan de manera interna para realizar
#            de manera correcta la recepcion de datos, para éste ejemplo no shubo necesidad
#            de utilizarlos y para evitar la sobrecarga de información se han omitido sus
#            detalles. Para más información acerca del funcionamiento interno de RabbitMQ
#            puedes visitar: https://www.rabbitmq.com/
#
#-------------------------------------------------------------------------
import pika
import sys
import random
sys.path.append('../')
from monitor import Monitor
import time


class ProcesadorTemporizador:

    def consume(self):
        try:
           
            # Se establece la conexión con el Distribuidor de Mensajes
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            # Se solicita un canal por el cuál se enviarán los signos vitales
            channel = connection.channel()
            # Se declara una cola para leer los mensajes enviados por el
            # Publicador
            channel.queue_declare(queue='body_temporizador', durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(self.callback, queue='body_temporizador')
            channel.start_consuming()  # Se realiza la suscripción en el Distribuidor de Mensajes
        except (KeyboardInterrupt, SystemExit):
            channel.close()  # Se cierra la conexión
            sys.exit("Conexión finalizada...")
            time.sleep(1)
            sys.exit("Programa terminado...")
    

    def callback(self, ch, method, properties, body):
	try:         
		json_message = self.string_to_json(body)
		time.sleep(2)
		#este for se utiliza para simular el paso de las horas 
		for h in range(0,len(json_message['body_temporizador'])):

			if float(json_message['body_hora_medicina']) == float(1) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			

			if float(json_message['body_hora_medicina']) == float(2) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			

			if float(json_message['body_hora_medicina']) == float(3) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(4) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(5) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(6) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(7) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(8) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(9) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(10) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(11) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
					

			if float(json_message['body_hora_medicina']) == float(12) :
			    monitor = Monitor()
			    monitor.print_notification('necesita su medicamento ' + json_message['body_nombre_medicamento'],json_message['datetime'], json_message['id'])
			    ch.basic_ack(delivery_tag=method.delivery_tag)
			    break
			
				
		
	except (KeyboardInterrupt, SystemExit):
            channel.close()  # Se cierra la conexión
            sys.exit("Conexión finalizada...")
            time.sleep(1)
            sys.exit("Programa terminado...")


    def string_to_json(self, string):
        message = {}
        string = string.replace('{', '')
        string = string.replace('}', '')
        values = string.split(', ')
        for x in values:
            v = x.split(': ')
            message[v[0].replace('\'', '')] = v[1].replace('\'', '')
        return message
    
    
        

if __name__ == '__main__':
    p_temporizador = ProcesadorTemporizador()
    p_temporizador.consume()
