#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 15:51:38 by marasolo            #+#    #+#            #
#   Updated: 2026/07/15 06:47:44 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    player1 = factory.create_base()
    print(player1.describe())
    print(player1.attack())
    player2 = factory.create_evolved()
    print(player2.describe())
    print(player2.attack())


def test_battle(flame: FlameFactory, aqua: AquaFactory) -> None:
    print("Testing battle")
    player1 = flame.create_base()
    print(player1.describe())
    print(" vs.")
    player2 = aqua.create_base()
    print(player2.describe())
    print(" fight!")
    print(player1.attack())
    print(player2.attack())


def main() -> None:
    Flame = FlameFactory()
    Aqua = AquaFactory()
    test_factory(Flame)
    print()
    test_factory(Aqua)
    print()
    test_battle(Flame, Aqua)


if __name__ == "__main__":
    main()
