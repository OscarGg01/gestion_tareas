import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def agregar_tarea_de_prueba(self, titulo="Tarea 1", descripcion="Descripción de la tarea 1"):
        """Método auxiliar para agregar una tarea de prueba."""
        self.gestor.agregar_tarea(titulo, descripcion)

    def test_agregar_tarea(self):
        self.agregar_tarea_de_prueba()
        self.assertEqual(len(self.gestor.tareas), 1)
        tarea = self.gestor.tareas[0]
        self.assertEqual(tarea.titulo, "Tarea 1")
        self.assertEqual(tarea.descripcion, "Descripción de la tarea 1")

    def test_agregar_tarea_sin_titulo(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción")

    def test_marcar_completada(self):
        self.agregar_tarea_de_prueba()
        self.gestor.marcar_completada(0)
        self.assertTrue(self.gestor.tareas[0].completada)

    def test_eliminar_tarea(self):
        self.agregar_tarea_de_prueba()
        self.gestor.eliminar_tarea(0)
        self.assertEqual(len(self.gestor.tareas), 0)

if __name__ == "__main__":
    unittest.main()
