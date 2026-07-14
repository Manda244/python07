#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capability.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: marasolo <marasolo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/14 19:08:40 by marasolo            #+#    #+#            #
#   Updated: 2026/07/14 19:21:09 by marasolo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
