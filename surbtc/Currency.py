# -*- coding: utf-8 -*-

"""
Cliente para servicios web de SURBTC
Copyright (C) SASCO SpA (https://sasco.cl)

Este programa es software libre: usted puede redistribuirlo y/o modificarlo
bajo los términos de la GNU Lesser General Public License (LGPL) publicada
por la Fundación para el Software Libre, ya sea la versión 3 de la Licencia,
o (a su elección) cualquier versión posterior de la misma.

Este programa se distribuye con la esperanza de que sea útil, pero SIN
GARANTÍA ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD
PARA UN PROPÓSITO DETERMINADO. Consulte los detalles de la GNU Lesser General
Public License (LGPL) para obtener una información más detallada.

Debería haber recibido una copia de la GNU Lesser General Public License
(LGPL) junto a este programa. En caso contrario, consulte
<http://www.gnu.org/licenses/lgpl.html>.
"""

"""
Clase que representa una moneda (fiat o cripto) genérica de SURBTC
@author Esteban De La Fuente Rubio, DeLaF (esteban[at]sasco.cl)
@version 2017-11-26
"""
class Currency :

    _currency = None # moneda para la cual se instanció el objeto
    client = None # Objeto que representa el cliente de la conexión a SURBTC

    def __init__ (self, currency, Client = None) :
        self._currency = currency
        if Client != None :
            self.client = Client

    def getBalance (self) :
        return self.client.getBalance(self._currency)

    def getAddresses (self) :
        return self.client.getAddresses(self._currency)

    def createAddress (self) :
        return self.client.createAddress(self._currency)

    def getAddress (self, id) :
        return self.client.getAddress(self._currency, id)

    def getDeposits (self) :
        return self.client.getHistory(self._currency, 'deposits')

    def getWithdrawals (self) :
        return self.client.getHistory(self._currency, 'withdrawals')

    def deposit (self, amount) :
        return self.client.deposit(self._currency, amount)

    def withdrawal (self, target_address, amount = None) :
        return self.client.withdrawal(self._currency, target_address, amount)
