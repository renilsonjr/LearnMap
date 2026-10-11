"""Testes do desafio do controlador de elevador inteligente.

Implemente controlar_elevador(andar_maximo, comandos) em
code-challenges/10-11/challenge-02.py. Se escolher outro nome,
ajuste FUNCTION_NAME abaixo.

Execute da raiz: python3 code-challenges/10-11/tests/test_challenge_02.py
"""

import importlib.util
from pathlib import Path
import unittest


CHALLENGE_PATH = Path(__file__).resolve().parents[1] / "challenge-02.py"
FUNCTION_NAME = "controlar_elevador"


class TestControlarElevador(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("challenge_02", CHALLENGE_PATH)
        if spec is None or spec.loader is None:
            raise ImportError(f"Não foi possível carregar {CHALLENGE_PATH}")

        challenge = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(challenge)
        solucao = getattr(challenge, FUNCTION_NAME, None)
        if not callable(solucao):
            raise AssertionError(
                f"Implemente {FUNCTION_NAME}(andar_maximo, comandos) em {CHALLENGE_PATH}"
            )
        cls.solucao = staticmethod(solucao)

    def assert_resultado(self, andar_maximo, comandos, esperado):
        resultado = self.solucao(andar_maximo, comandos.copy())
        self.assertIsInstance(resultado, list, "O retorno deve ser uma lista.")
        self.assertEqual(
            len(resultado), 2, "Retorne [andar_final, movimentos_bloqueados]."
        )
        self.assertTrue(
            all(type(valor) is int for valor in resultado),
            "O andar final e o total de bloqueios devem ser números inteiros.",
        )
        self.assertEqual(
            resultado,
            esperado,
            "O andar final ou o total de movimentos bloqueados está incorreto.",
        )

    def test_casos_do_desafio(self):
        casos = [
            (
                "exemplo do enunciado",
                3,
                ["SUBIR", "SUBIR", "SUBIR", "SUBIR", "DESCER", "REINICIAR", "DESCER"],
                [0, 2],
            ),
            ("sem comandos", 3, [], [0, 0]),
            ("começa no térreo e sobe um andar", 3, ["SUBIR"], [1, 0]),
            ("descida bloqueada no térreo", 3, ["DESCER"], [0, 1]),
            ("chega exatamente ao último andar", 3, ["SUBIR"] * 3, [3, 0]),
            ("subida bloqueada no último andar", 2, ["SUBIR"] * 3, [2, 1]),
            ("bloqueios consecutivos no térreo", 3, ["DESCER"] * 4, [0, 4]),
            ("bloqueios consecutivos no topo", 2, ["SUBIR"] * 5, [2, 3]),
            (
                "volta exatamente ao térreo",
                3,
                ["SUBIR"] * 3 + ["DESCER"] * 3,
                [0, 0],
            ),
            ("alterna subidas e descidas", 1, ["SUBIR", "DESCER"] * 3, [0, 0]),
            ("respeita a ordem dos comandos", 1, ["DESCER", "SUBIR"], [1, 1]),
            (
                "reinicia no topo e continua os comandos",
                3,
                ["SUBIR"] * 3 + ["REINICIAR", "SUBIR"],
                [1, 0],
            ),
            (
                "reinícios no térreo não contam como bloqueios",
                3,
                ["REINICIAR", "REINICIAR", "DESCER", "REINICIAR"],
                [0, 1],
            ),
            (
                "reiniciar preserva o total de bloqueios",
                2,
                ["SUBIR", "SUBIR", "SUBIR", "REINICIAR", "DESCER", "SUBIR"],
                [1, 2],
            ),
            (
                "prédio com apenas o térreo",
                0,
                ["SUBIR", "DESCER", "REINICIAR", "SUBIR", "DESCER"],
                [0, 4],
            ),
        ]

        for nome, andar_maximo, comandos, esperado in casos:
            with self.subTest(caso=nome):
                self.assert_resultado(andar_maximo, comandos, esperado)

    def test_sequencia_longa_de_comandos(self):
        # Cada ciclo termina no térreo e tem exatamente três bloqueios.
        ciclo = ["DESCER"] + ["SUBIR"] * 4 + ["DESCER"] * 4 + ["REINICIAR"]
        self.assert_resultado(3, ciclo * 1_000, [0, 3_000])


if __name__ == "__main__":
    unittest.main(verbosity=2)
