import pytest
from keyedCaesarCipher import *

@pytest.fixture
def cipher_one():
    cipher = KeyedCaesarCipher()
    cipher.createCipher('potato', 6)
    return cipher

@pytest.fixture
def testData_one():
    return [
        ['corsair', 'fuxydlx'], 
        ['playmax', 'vqdbrda'],
        ['amd ryzen', 'drg xbchs'],
        [' tie fighter ', ' zlh iljkzhx ']
        ]

@pytest.fixture
def cipher_two():
    cipher = KeyedCaesarCipher()
    cipher.createCipher('keylime', 12)
    return cipher

@pytest.fixture
def testData_two():
    return [
        ['starlight', 'imhlwtrsm'], 
        ['straight', 'imlhtrsm'],
        ['nicholas', 'ztnskwhi'],
        ['jeremiah', 'uplpxths']
        ]

@pytest.fixture
def cipher_three():
    cipher = KeyedCaesarCipher()
    cipher.createCipher('', 23)
    return cipher

@pytest.fixture
def testData_three():
    return [
        ['dragon', 'aoxdlk'],
        ['auxilary', 'xrufixov'],
        ['evangeline', 'bsxkdbifkb'],
        ['dragon!', 'aoxdlk!']
    ]

def test_encryption(testData_three, cipher_three, testData_two, cipher_two, testData_one, cipher_one):
    for i in range(0, len(testData_two) - 1):
        assert cipher_one.encrypt(testData_one[i][0]) == testData_one[i][1]
        assert cipher_two.encrypt(testData_two[i][0]) == testData_two[i][1]
        assert cipher_three.encrypt(testData_three[i][0]) == testData_three[i][1]

def test_decryption(testData_three, cipher_three, testData_two, cipher_two, testData_one, cipher_one):
    for i in range(0, len(testData_two) - 1):
        assert cipher_one.decrypt(testData_one[i][1]) == testData_one[i][0]
        assert cipher_two.decrypt(testData_two[i][1]) == testData_two[i][0]
        assert cipher_three.decrypt(testData_three[i][1]) == testData_three[i][0]
