from codigo.jogo import brinks

def test_quando_brincadeira_receber_1_entao_deve_return_1():
    entrada = 1
    esperada = 1
    resultado = brinks(1)
    assert resultado == esperada