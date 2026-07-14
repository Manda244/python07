#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatureFactory.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 20:12:28 by marasolo            #+#    #+#            #
#   Updated: 2026/07/14 21:16:23 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.factories import CreatureFactory
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
