#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategies.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 22:01:59 by marasolo            #+#    #+#            #
#   Updated: 2026/07/15 08:26:34 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capability import HealCapability, TransformCapability
from typing import cast


class InvalidStrategiesError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creat: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creat: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creat: Creature) -> bool:
        return isinstance(creat, Creature)

    def act(self, creat: Creature) -> None:
        if not self.is_valid(creat):
            raise InvalidStrategiesError(
                f"Invalid Creature {creat.name} for this normal strategy"
                )
        print(creat.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creat: Creature) -> bool:
        return isinstance(creat, TransformCapability)

    def act(self, creat: Creature) -> None:
        c = cast(TransformCapability, creat)
        if not self.is_valid(creat):
            raise InvalidStrategiesError(
                f"Invalid Creature {creat.name} for this aggressive strategy"
                )
        print(c.transform())
        print(creat.attack())
        print(c.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creat: Creature) -> bool:
        return isinstance(creat, HealCapability)

    def act(self, creat: Creature) -> None:
        c = cast(HealCapability, creat)
        if not self.is_valid(creat):
            raise InvalidStrategiesError(
                f"Invalid Creature {creat.name} for this defensive strategy"
                )
        print(creat.attack())
        print(c.heal())
