#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 21:20:29 by marasolo            #+#    #+#            #
#   Updated: 2026/07/14 21:51:01 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print(" base:")
    healingBase = factory.create_base()
    print(healingBase.describe())
    print(healingBase.attack())
    print(healingBase.heal())

    print(" evolved:")
    healingEvolved = factory.create_evolved()
    print(healingEvolved.describe())
    print(healingEvolved.attack())
    print(healingEvolved.heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print(" base:")
    healingBase = factory.create_base()
    print(healingBase.describe())
    print(healingBase.attack())
    print(healingBase.transform())
    print(healingBase.attack())
    print(healingBase.revert())

    print(" evolved:")
    healingEvolved = factory.create_evolved()
    print(healingEvolved.describe())
    print(healingEvolved.attack())
    print(healingEvolved.transform())
    print(healingEvolved.attack())
    print(healingEvolved.revert())


def main() -> None:
    test_healing()
    print()
    test_transform()


if __name__ == "__main__":
    main()
