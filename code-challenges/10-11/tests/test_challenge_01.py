"""Testes do desafio de encontrar duas tarefas com a soma desejada.

Implemente encontrar_par(duracoes, objetivo) em
code-challenges/10-11/challenge-01.py. Se escolher outro nome,
ajuste FUNCTION_NAME abaixo.

Execute da raiz: python3 code-challenges/10-11/tests/test_challenge_01.py
"""

import importlib.util
from pathlib import Path
import unittest


CHALLENGE_PATH = Path(__file__).resolve().parents[1] / "challenge-01.py"
FUNCTION_NAME = "encontrar_par"


class TestEncontrarPar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("challenge_01", CHALLENGE_PATH)
        if spec is None or spec.loader is None:
            raise ImportError(f"Não foi possível carregar {CHALLENGE_PATH}")

        challenge = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(challenge)
        solucao = getattr(challenge, FUNCTION_NAME, None)
        if not callable(solucao):
            raise AssertionError(
                f"Implemente {FUNCTION_NAME}(duracoes, objetivo) em {CHALLENGE_PATH}"
            )
        cls.solucao = staticmethod(solucao)

    def assert_resultado(self, duracoes, objetivo, tem_solucao):
        # Preserve a ordem original para validar os índices mesmo se a solução
        # modificar a lista recebida.
        resultado = self.solucao(duracoes.copy(), objetivo)
        self.assertIsInstance(resultado, list, "O retorno deve ser uma lista.")

        if not tem_solucao:
            self.assertEqual(resultado, [], "Sem um par válido, retorne [].")
            return

        self.assertEqual(len(resultado), 2, "Retorne exatamente dois índices.")
        self.assertTrue(
            all(type(indice) is int for indice in resultado),
            "Os índices devem ser números inteiros.",
        )
        primeiro, segundo = resultado
        self.assertTrue(
            0 <= primeiro < segundo < len(duracoes),
            "Os índices devem ser válidos, distintos e estar em ordem crescente.",
        )
        self.assertEqual(
            duracoes[primeiro] + duracoes[segundo],
            objetivo,
            "As durações das duas tarefas devem somar o objetivo.",
        )

    def test_casos_do_desafio(self):
        casos = [
            ("exemplo do enunciado", [2, 7, 11, 15], 9, True),
            ("durações fora de ordem", [3, 2, 4], 6, True),
            ("apenas duas tarefas", [1, 4], 5, True),
            ("par nas extremidades", [8, 1, 3, 6], 14, True),
            ("duas tarefas com a mesma duração", [5, 5], 10, True),
            ("duplicatas com o par no final", [2, 2, 5, 5], 10, True),
            ("duplicatas sem solução", [3, 3, 3], 7, False),
            ("múltiplos pares válidos", [1, 9, 4, 6, 5, 5], 10, True),
            ("não pode reutilizar uma tarefa", [4, 1, 6], 8, False),
            ("nenhuma combinação válida", [2, 7, 11, 15], 10, False),
            ("lista vazia", [], 10, False),
            ("apenas uma tarefa", [5], 10, False),
            ("objetivo zero", [1, 2, 3], 0, False),
            ("objetivo negativo", [1, 2, 3], -3, False),
            (
                "soma acima do limite de inteiro de 32 bits",
                [2_147_483_647, 1, 2_147_483_648],
                4_294_967_295,
                True,
            ),
        ]

        for nome, duracoes, objetivo, tem_solucao in casos:
            with self.subTest(caso=nome):
                # Qualquer par válido é aceito; não exigimos um par específico.
                self.assert_resultado(duracoes, objetivo, tem_solucao)

    def test_lista_grande_com_unico_par_no_final(self):
        duracoes = list(range(1, 10_001)) + [1_000_000, 1_000_001]
        self.assert_resultado(duracoes, 2_000_001, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
