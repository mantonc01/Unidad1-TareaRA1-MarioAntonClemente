# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero y la excepción desde el módulo padre
from lavadero import Lavadero, IllegalStateException

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        """Test : Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero.hacerLavado(True, True, True)  # Cambiado de _hacer_lavado a hacerLavado
        self.lavadero._cobrar()
        self.lavadero.terminar()        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertGreater(self.lavadero.ingresos, 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------
    """Tests básicos de la clase Lavadero."""
    def test1_estado_inicial_correcto(self):
        """Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)# El lavadero debe estar inactivo inicialmente
        self.assertEqual(self.lavadero.ingresos, 0.0)# Los ingresos iniciales deben ser 0.0
        self.assertFalse(self.lavadero.ocupado)# El lavadero no debe estar ocupado inicialmente
        self.assertFalse(self.lavadero.prelavado_a_mano)# El prelavado a mano debe estar desactivado inicialmente
        self.assertFalse(self.lavadero.secado_a_mano)# El secado a mano debe estar desactivado inicialmente
        self.assertFalse(self.lavadero.encerado)# El encerado debe estar desactivado inicialmente
   
    
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        # hacerLavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)# Debe lanzar ValueError porque no se puede encerar sin secado a mano

    
    def test3_excepcion_lavado_ocupado(self):
        """Test 3: Comprueba que intentar un lavado mientras ocupado lanza IllegalStateException."""
        # Iniciar un lavado
        self.lavadero.hacerLavado(False, False, False)
        self.assertTrue(self.lavadero.ocupado)# Verificar que el lavadero está ocupado
        # Intentar otro lavado sin terminar el primero
        with self.assertRaises(IllegalStateException):
            self.lavadero.hacerLavado(False, False, False)# Debe lanzar IllegalStateException porque el lavadero está ocupado

    def test4_ingresos_prelavado_mano(self):
        """Test 4: Si seleccionamos un lavado con prelavado a mano, los ingresos son 6,50€."""
        self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=False, encerado=False)
        self.assertAlmostEqual(self.lavadero.ingresos, 6.50, places=2)
        
    def test5_ingresos_secado_mano(self):
        """Test 5: Si seleccionamos un lavado con secado a mano, los ingresos son 6,00€."""
        self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=False)
        self.assertAlmostEqual(self.lavadero.ingresos, 6.00, places=2)
        
    def test6_ingresos_secado_mano_encerado(self):
        """Test 6: Si seleccionamos un lavado con secado a mano y encerado, los ingresos son 7,20€."""
        self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=True)
        self.assertAlmostEqual(self.lavadero.ingresos, 7.20, places=2)
        
    def test7_ingresos_prelavado_secado_mano(self):
        """Test 7: Si seleccionamos un lavado con prelavado a mano y secado a mano, los ingresos son 7,50€."""
        self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=False)
        self.assertAlmostEqual(self.lavadero.ingresos, 7.50, places=2)
        
    def test8_ingresos_todos_extras(self):
        """Test 8: Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, los ingresos son 8,70€."""
        self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=True)
        self.assertAlmostEqual(self.lavadero.ingresos, 8.70, places=2)

    # ----------------------------------------------------------------------
    # Tests de flujo de fases
    # Utilizamos la función def ejecutar_y_obtener_fases(self, prelavado, secado, encerado)
    # Estos tests dan errores ya que en el código original hay errores en las las fases esperados, en los saltos.
    # ----------------------------------------------------------------------
    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
         
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_esperadas, fases_obtenidas,
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
    
    def test10_flujo_con_prelavado_mano(self):
        """Test 10: Flujo con prelavado a mano - fases 0, 1, 2, 3, 4, 5, 6, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=False, encerado=False)
        self.assertEqual(fases_esperadas, fases_obtenidas)
    
    def test11_flujo_con_secado_mano(self):
        """Test 11: Flujo con secado a mano - fases 0, 1, 3, 4, 5, 7, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=False)
        self.assertEqual(fases_esperadas, fases_obtenidas)
        
    def test12_flujo_con_secado_mano_encerado(self):
        """Test 12: Flujo con secado a mano y encerado - fases 0, 1, 3, 4, 5, 7, 8, 0."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=True)
        self.assertEqual(fases_esperadas, fases_obtenidas)
    
    def test13_flujo_con_prelavado_secado_mano(self):
        """Test 13: Flujo con prelavado y secado a mano - fases 0, 1, 2, 3, 4, 5, 7, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=False)
        self.assertEqual(fases_esperadas, fases_obtenidas)
    
    def test14_flujo_con_todos_extras(self):
        """Test 14: Flujo con prelavado, secado a mano y encerado - fases 0, 1, 2, 3, 4, 5, 7, 8, 0."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=True)
        self.assertEqual(fases_esperadas, fases_obtenidas)
    
    def test15_reseteo_estado_con_terminar(self):
        """Test adicional: Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero.avanzarFase()  # Va a cobrar
        # self.lavadero._cobrar()
        # Avanzamos hasta terminar
        while self.lavadero.ocupado:
            self.lavadero.avanzarFase()
        self.lavadero.terminar()
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
    
 
# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()