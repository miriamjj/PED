# PED
Realización de la prueba
El resto de la prueba consiste en la implementación de una especificación de requisitos de un sistema cliente-servidor. La puntuación se asignará a diferentes entregas realizadas en el repositorio, con las siguientes condiciones:

    Implemente una abstracción (módulo, función, clase, objeto, lo que desee) que genere los mensajes y sus respuestas adecuadas, tanto de la parte cliente como de la parte servidor) definidos en la especificación de requisitos, utilizando la metodología TDD (Test-Driven Development, Desarrollo dirigido por pruebas). La puntuación se asignará a diferentes entregas realizadas en el repositorio, con las siguientes condiciones:
        Entregas etiquetadas como "Test n". Deberán contener un caso de prueba que sea el único que no funcione en dicha entrega. Es necesario que los casos de prueba de las diferentes entregas sean funcionalmente distintos. Los casos de prueba deberán tratar de cubrir todas las situaciones especificadas en los requisitos. Cada caso de prueba funcionalmente distinto y adecuado a los requisitos del enunciado que sea ejecutado correctamente por el software sumará 0,5 puntos. Puede escribir todos los casos de prueba que estime oportunos (máximo 2 puntos)
        Entregas etiquetadas como "Test n OK". Deberán hacer funcionar un caso de prueba que fallaba en la entrega anterior. Cada una de estas entregas sumará 0,5 puntos siempre que todos los casos de prueba acumulados funcionen (máximo 2 puntos)
        Entregas etiquetadas como "Refactoring N". Deberán contener una recodificación (refactoring) del código, diferenciándose de la entrega anterior solamente en dicha recodificación pero no en los casos de prueba, que deberán ser los mismos de la entrega anterior. Sumarán 0,5 puntos si todos los casos de prueba funcionan (máximo 1 punto)
    Implemente el servidor del sistema especificado en los requisitos. El servidor deberá ejecutarse de forma continua, sin detenerse, y deberá aceptar conexiones de cualquier cliente, recibiendo los mensajes indicados y generando las respuestas adecuadas. Se sugiere el uso de la abstracción desarrollada en la pregunta anterior, así como etiquetar "Servidor" a la entrega que contiene la solución (3 puntos)
    Implemente el cliente del sistema especificado en los requisitos. El cliente deberá preguntar al usuario por la dirección del servidor, realizar una conexión y enviar un mínimo de 3 mensajes al servidor. El cliente deberá imprimir en su salida standard las respuestas recibidas del servidor (o cualquier condición de error que se produzca) y terminar tras el último mensaje. Se sugiere el uso de la abstracción desarrollada hace dos preguntas, así como etiquetar "Cliente" a la entrega que contiene la solución (2 puntos)
    Anote en el fichero README cuál de los tres puntos de escucha de la especificación de requisitos ha elegido para su servidor, así como el procedimiento y las herramientas necesarias para ejecutar el código de las respuestas anteriores: sistema operativo, herramientas de programación, de construcción, scripts, etc. (0,2 puntos)

En el siguiente enlace se indica la especificación de requisitos a implementar. 

Especificación de requisitos a implementar
Se desea realizar un sistema cliente-servidor con las siguientes características:

El servidor atenderá peticiones en uno de los tres puntos siguientes (puede elegir el que desee):

    Puerto TCP número N
    Puerto UDP número N
    Socket local /tmp/servicioN

Donde N = 16000 + 10*su número de grupo de prácticas + su posición dentro del grupo tomando como criterio de ordenación el índice alfabético de los apellidos de sus componentes (ejemplo: si su grupo es el 7 y es usted el primero de su grupo, N=16071).

El servidor responderá a los siguientes mensajes de texto, enviados desde el cliente, con las respuestas que se indican a continuación; todos ellos deberán ir codificados en UTF-8:

    FECHA → el servidor responderá con la fecha actual del sistema
    HORA → el servidor responderá con la hora actual del sistema
    Cualquier otro mensaje → el servidor responderá ERROR
