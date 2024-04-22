import unittest


personas = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Fernando",
        "segundo_nombre": "Mateo",
        "primer_apellido": "Rodriguez",
        "segundo_apellido": "Martinez"
    },
    "persona3": {
        "primer_nombre": "Martina",
        "segundo_nombre": "Fernanda",
        "primer_apellido": "Cortez",
        "segundo_apellido": "Cuesta"
    },
    "persona4": {
        "primer_nombre": "Juan",
        "segundo_nombre": "Alberto",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Lopez"
    },
    "persona5": {
        "primer_nombre": "Juan",
        "segundo_nombre": "Gabriel",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Gomez"
    }
}

def buscar_personas(nombre):
    personas_encontradas = {}
    for key, value in personas.items():
        nombre_completo = " ".join(value.values())
        if nombre.lower() in nombre_completo.lower():
            personas_encontradas[key] = value
    return personas_encontradas if personas_encontradas else {"No se encontró a ninguna persona con ese nombre"}


nombre_buscar = input("Ingresa el nombre de la persona que quieres buscar: ")


resultado = buscar_personas(nombre_buscar)


if resultado != {"No se encontró a ninguna persona con ese nombre"}:
    print("La persona encontrada es:")
    for key, value in resultado.items():
        print(key, ":", value)
else:
    print("No se encontró a ninguna persona con ese nombre")



class TestBuscarPersonas(unittest.TestCase):
    def test_nombre_unico(self):
        resultado = buscar_personas("Pablo")
        self.assertEqual(len(resultado), 1)
        self.assertIn("persona1", resultado)
        self.assertEqual(resultado["persona1"]["primer_nombre"], "Pablo")

    def test_nombre_compartido(self):
        resultado = buscar_personas("Juan")
        self.assertEqual(len(resultado), 2)
        self.assertIn("persona4", resultado)
        self.assertIn("persona5", resultado)
        self.assertEqual(resultado["persona4"]["primer_nombre"], "Juan")
        self.assertEqual(resultado["persona5"]["primer_nombre"], "Juan")

    def test_nombre_no_encontrado(self):
        resultado = buscar_personas("Gabriela")
        self.assertEqual(resultado, {"No se encontró a ninguna persona con ese nombre"})

    def test_apellido_compartido(self):
        resultado = buscar_personas("Ruiz")
        self.assertEqual(len(resultado), 3)
        self.assertIn("persona1", resultado)
        self.assertIn("persona4", resultado)
        self.assertIn("persona5", resultado)
        self.assertEqual(resultado["persona1"]["primer_apellido"], "Ruiz")
        self.assertEqual(resultado["persona4"]["primer_apellido"], "Ruiz")
        self.assertEqual(resultado["persona5"]["primer_apellido"], "Ruiz")


if __name__ == '__main__':
    unittest.main()